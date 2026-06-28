from django.urls import path

from apps.organizations.views import (
    OrganizationDetailAPIView,
    OrganizationListCreateAPIView,
)

urlpatterns = [
    path(
        "",
        OrganizationListCreateAPIView.as_view(),
        name="organizations",
    ),
    path(
        "<uuid:pk>/",
        OrganizationDetailAPIView.as_view(),
        name="organization-detail",
    ),
]