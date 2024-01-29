from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import ProjectForm
from .models import Project
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from guardian.shortcuts import get_objects_for_user

def index(request):
    return render(request, "index.html")

def custom_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

@login_required
@permission_required("project.view_project")
def project_listing(request):
    project_data = get_objects_for_user(request.user, 'project.dg_view_project', klass=Project)
    return render(request, "project.html", {"projects": project_data})

@login_required
@permission_required("project.view_project")
def project_detail(request, id):
    project = get_object_or_404(Project, slug=id)
    return render(request, "detail.html", {"detail": project})

@login_required
@permission_required({("project.view_project"),("project.can_add_new_project")})
def create_project(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return HttpResponseRedirect(reverse("project:project"))
    else:
        form = ProjectForm()

    return render(request, "create_project.html", {"form": form})
