from django.contrib import admin
from .models import Project
from guardian.admin import GuardedModelAdmin

class ProjectAdmin(GuardedModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
