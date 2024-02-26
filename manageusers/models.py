from django.db import models

class employees(models.Model):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    past_experience = models.IntegerField()
    skills_score = models.IntegerField()
    technology_known = models.PositiveIntegerField(null=True)
    employee_level = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = "employees"    

    class Meta:
        verbose_name_plural = "employees"  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class technologies(models.Model):
    username = models.CharField(max_length=100, unique=True)
    python = models.BooleanField(default=False)
    c = models.BooleanField(default=False)
    java = models.BooleanField(default=False)
    javascript = models.BooleanField(default=False)
    nodejs = models.BooleanField(default=False)
    git_github = models.BooleanField(default=False)
    php = models.BooleanField(default=False)
    react = models.BooleanField(default=False)
    bootstrap = models.BooleanField(default=False)
    nginx = models.BooleanField(default=False)
    typescript = models.BooleanField(default=False)
    angularjs = models.BooleanField(default=False)
    frontend = models.BooleanField(default=False)
    backend = models.BooleanField(default=False)
    mongodb = models.BooleanField(default=False)
    mysql = models.BooleanField(default=False)
    docker = models.BooleanField(default=False)
    azure = models.BooleanField(default=False)
    django = models.BooleanField(default=False)
    postgresql = models.BooleanField(default=False)

    class Meta:
        db_table = "technologies"    

    class Meta:
        verbose_name_plural = "technologies"  

    def __str__(self):
        return self.username
    
    
class projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    scope = models.IntegerField(default=1, help_text="Scope of the project (1-10)")
    complexity = models.IntegerField(default=1, help_text="Technical complexity of the project (1-10)")
    knowledge = models.IntegerField(default=1, help_text="Domain knowledge required for the project (1-10)")
    time_effort = models.IntegerField(default=1, help_text="Time and effort required for the project (1-10)")
    resources = models.IntegerField(default=1, help_text="Resource requirements for the project (1-10)")
    risk = models.IntegerField(default=1, help_text="Risk and uncertainty associated with the project (1-10)")
    project_complexity = models.CharField(max_length=20, null=True, blank=True, help_text="Project complexity (Easy, Intermediate, Advanced)")

    class Meta:
        db_table = "projects"    

    class Meta:
        verbose_name_plural = "projects"  

    def __str__(self):
        return self.name