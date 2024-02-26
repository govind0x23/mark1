from django.contrib import admin
from django.urls import include, path
from . import views
# from .models import employee
urlpatterns = [
   path('home', views.home,name='home'),
   path('', views.blank,name='blank'),
 
   path('login', views.user_login,name='login'),
   path('logout', views.user_logout,name='logout'),

   path('delete',views.delete,name='delete'),
   path('projects', views.get_project,name='projects'),
   path('home', views.home,name='home'),
   path('team', views.team,name='team'),
   path('create', views.create_user,name='create'),
   path('fetchusers', views.show_employees,name='fetchusers'),
   path('0', views.easy,name='0'),
   path('1', views.intermediate,name='1'),
   path('2', views.advance,name='2'),
   path('tech', views.user_technologies,name='tech'),
   path('save_data', views.save_data,name='save_data'),
   path('create_project', views.create_project,name='create_project'),
   path('project', views.display_projects,name='project'),

   path('fusers', views.filter_employees,name='fusers'),

   
    
]
