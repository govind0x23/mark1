from django.shortcuts import redirect, render, HttpResponse
from .models import employees, technologies, projects
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# # Create your views here.

def blank(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username or password is empty
        if not username or not password:
            messages.error(request, "Please provide both username and password.")
            return render(request, 'login.html')

        # Check if username exists in the database
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist. Please enter a valid username.")
            return render(request, 'login.html')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        # If user exists and credentials are correct
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            # Provide feedback to the user about invalid credentials
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')
    
def user_logout(request):
    logout(request)
    return render(request, 'login.html')

@login_required(redirect_field_name="next", login_url="login")
def home(request):
    return render(request, 'index.html')
   

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'profile.html')


def team(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'team.html')

def get_project(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'projects.html')

def create_user(request):
    
    if request.method == 'POST':
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
        # Check if username already exists
        if employees.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('fetchusers')
        
        if employees.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('fetchusers')
        
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        past_experience = request.POST['experience']
        skills_score = request.POST['skills_score']
        
        user = employees(username=username, first_name=first_name, last_name=last_name, email=email, past_experience=past_experience, skills_score=skills_score)
        user.save()
        messages.success(request, "User Created Successfully!")
        return redirect('fetchusers')

    else:
        return render(request, '404.html')

@login_required(redirect_field_name="next", login_url="login")
def show_employees(request):
    
    users = employees.objects.all()
        
    fields = technologies._meta.get_fields() 
    field_names = [field.name for field in fields if field.name != 'id' and field.name != 'username'] 
    top_10_fields = field_names[:10]
    last10_fields = field_names[10:] 
    
    return render(request, 'users.html', {'users': users, 'top_10_fields': top_10_fields, 'last10_fields': last10_fields})


def easy(request):
    if not request.user.is_authenticated:
        return redirect('login')
    users = employees.objects.filter(employee_level='Junior')
    return render(request, 'users.html', {'users': users})

def intermediate(request):
    if not request.user.is_authenticated:  
        return redirect('login')
    users = employees.objects.filter(employee_level='Intermediate')
    return render(request, 'users.html', {'users': users})

def advance(request):
    if not request.user.is_authenticated:  
        return redirect('login')
   
    users = employees.objects.filter(employee_level='Senior')
    return render(request, 'users.html', {'users': users})


def user_technologies(request):
    if not request.user.is_authenticated:
        return redirect('login')
    fields = technologies._meta.get_fields() 
    field_names = [field.name for field in fields if field.name != 'id' and field.name != 'username'] 
    top_10_fields = field_names[:10]
    last10_fields = field_names[10:] 
    return render(request, 'users.html', {'top_10_fields': top_10_fields, 'last10_fields': last10_fields})

@login_required(redirect_field_name="next", login_url="login")
def save_data(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        backend_tech = request.POST.getlist('backend_tech')

        if not employees.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist. Please enter a valid username.")
            # return render(request, 'profile.html')
            return redirect('fetchusers')

        # Check if user has already been updated
        if technologies.objects.filter(username=username).exists():
            messages.warning(request, "User has already been updated.")
            return redirect('fetchusers')

        # Create or get the technologies object
        technologies_obj, created = technologies.objects.get_or_create(username=username)

        # Update backend technologies
        for tech in backend_tech:
            setattr(technologies_obj, tech, True)
        technologies_obj.save()

        # Calculate total technologies known
        total_technologies = sum(getattr(technologies_obj, field.name) for field in technologies._meta.get_fields() if field.name != 'id' and field.name != 'username')

        # Update employee instance
        employee_instance = employees.objects.get(username=username)
        employee_instance.technology_known = total_technologies
        employee_instance.save()

        messages.success(request, "User Update Successful!")
        # return render(request, 'profile.html')
        return redirect('fetchusers')

    return render(request, 'profile.html')

def display_projects(request):
    if not request.user.is_authenticated:
        return redirect('login')
    all_projects = projects.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})


@login_required(redirect_field_name="next", login_url="login")
def filter_employees(request):
      
    if request.method == 'POST':
        project_name = request.POST.get('project_name')

        # Retrieve project complexity based on project name
        try:
            project = projects.objects.get(name=project_name)
            project_complexity = project.project_complexity
        except projects.DoesNotExist:
            
            messages.error(request, "Project not found! Enter Valid Project Name.")
            return render(request, 'team.html')
            

        # Retrieve suitable employees based on project complexity
        if project_complexity == 'Easy':
            suitable_employees = employees.objects.filter(employee_level='Junior')
        elif project_complexity == 'Intermediate':
            suitable_employees = employees.objects.filter(employee_level= 'Intermediate')
        else:
            suitable_employees = employees.objects.filter(employee_level='Senior')

        return render(request, 'team.html', {'project_name': project_name,'employees': suitable_employees})

   
    return render(request, '404.html')



@login_required(redirect_field_name="next", login_url="login")
def save_data(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        backend_tech = request.POST.getlist('backend_tech')

        if not employees.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist. Please enter a valid username.")
            return redirect('fetchusers')

        if employees.objects.filter(username=username, technology_known__isnull=False).exists():
            messages.warning(request, "User has already been updated.")
            return redirect('fetchusers')

        technologies_obj, created = technologies.objects.get_or_create(username=username)

        for tech in backend_tech:
            setattr(technologies_obj, tech, True)
        technologies_obj.save()

        total_technologies = sum(getattr(technologies_obj, field.name) for field in technologies._meta.get_fields() if field.name != 'id' and field.name != 'username')

        employee_instance = employees.objects.get(username=username)
        employee_instance.technology_known = total_technologies
        employee_instance.save()

        messages.success(request, "User Update Successful!")
        
        # Call employee_level function after saving data
        employee_level(request)
        
        return redirect('fetchusers')

    return render(request, 'profile.html')

@login_required(redirect_field_name="next", login_url="login")
def employee_level(request):
    all_employees = employees.objects.all()

    for employee in all_employees:
        if employee.technology_known is None:
            messages.warning(request, f" Please Update User-Skills! For {employee.username}.")
            return redirect('fetchusers')
        
        level_score = (
            employee.past_experience + employee.skills_score + (employee.technology_known or 0)
        ) // 3
        
        if level_score <= 2:
            employee.employee_level = "Junior"
        elif level_score <= 6:
            employee.employee_level = "Intermediate"
        else:
            employee.employee_level = "Senior"
        
        employee.save()
    
    messages.success(request, "Employee Role Update Successfully!")  
    return redirect('fetchusers')


@login_required(redirect_field_name="next", login_url="login")
def create_project(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        scope = int(request.POST['scope'])
        complexity = int(request.POST['complexity'])
        knowledge = int(request.POST['knowledge'])
        time_effort = int(request.POST['time_effort'])
        resources = int(request.POST['resources'])
        risk = int(request.POST['risk'])

        # Check if project with the same name already exists
        if projects.objects.filter(name=name).exists():
            messages.error(request, "A project with the same name already exists!")
            return redirect('project')  # Redirect to the project page or wherever appropriate

        # If no project with the same name exists, create and save the new project
        project = projects(name=name, description=description, scope=scope, complexity=complexity, knowledge=knowledge, time_effort=time_effort, resources=resources, risk=risk)
        project.save()

        # Call function to calculate project complexity
        project_complexity(project)

        messages.success(request, "Project Created Successfully!")
        return redirect('project')  
    else:
        return render(request, '404.html')
    

def project_complexity(project):
    average_value = (
        project.scope + project.complexity + project.knowledge + project.time_effort + project.resources + project.risk ) // 6  
    # Taking average of all fields
    
    # Assign project complexity category based on average value
    if average_value <= 3:
        project.project_complexity = "Easy"
    elif average_value <= 7:
        project.project_complexity = "Intermediate"
    else:
        project.project_complexity = "Advanced"
    
    # Save the updated project
    project.save()



@login_required(redirect_field_name="next", login_url="login")
def delete(request):
    users = employees.objects.all()  # Fetch all users
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        
        # Check if username is provided
        if not username:
            messages.error(request, "Please enter a username.")
            return render(request, 'delete.html', {'users': users})

        try:
            # Check if the user exists in the employees table
            user = employees.objects.get(username=username)
            # Check for null values
            if not all([user.username, user.first_name, user.last_name, user.email, user.past_experience, user.skills_score]):
                messages.error(request, "User data has null values. Please contact the administrator.")
                return render(request, 'delete.html', {'users': users})

            # If the user exists, delete them
            user.delete()

            # Check if the user exists in the technologies table
            if technologies.objects.filter(username=username).exists():
                # If the user's technologies exist
                tech_user = technologies.objects.get(username=username)
                tech_user.delete()

            messages.success(request, "User Deleted Successfully!")
        except employees.DoesNotExist:
            # If the user does not exist in the employees table
            messages.error(request, "Username not found.")

    # Render the form to input the username
    return render(request, 'delete.html', {'users': users})