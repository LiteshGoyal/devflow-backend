from django.urls import path

from apps.teams.views import TeamListCreateAPIView

urlpatterns = [
    path("",TeamListCreateAPIView.as_view(),name="teams",),
]
