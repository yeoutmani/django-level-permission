from django.urls import path

from . import views

app_name = "project"

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.project_listing, name="project"),
    path("<slug:id>/", views.project_detail, name="project_detail"),
    path("project/new", views.create_project),
    path("projects/", views.project_listing, name="project"),
    path("projects/logout", views.custom_logout),

]
