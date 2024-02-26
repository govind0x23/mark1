from django.contrib import admin
from .models import employees
from .models import technologies
from .models import projects

admin.site.register(employees)
admin.site.register(technologies)
admin.site.register(projects)

