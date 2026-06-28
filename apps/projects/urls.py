from django.urls import path

from apps.projects.views import ProjectListCreateAPIView

urlpatterns = [
    path(
        "",
        ProjectListCreateAPIView.as_view(),
        name="projects",
    ),
]