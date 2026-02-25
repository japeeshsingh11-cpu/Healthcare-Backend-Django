"""
URL configuration for healthcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.views import RegisterView
from core.views import (
    PatientViewSet,
    DoctorViewSet,
    PatientDoctorMappingViewSet,
)

# Create router
router = DefaultRouter()
router.register("patients", PatientViewSet, basename="patients")
router.register("doctors", DoctorViewSet, basename="doctors")
router.register("mappings", PatientDoctorMappingViewSet, basename="mappings")

# urlpatterns = [
#     path("admin/", admin.site.urls),

#     # Authentication APIs
#     path("api/auth/register/", RegisterView.as_view(), name="register"),
#     path("api/auth/login/", TokenObtainPairView.as_view(), name="login"),

#     # API routes
#     path("api/", include(router.urls)),
# ]

from django.http import HttpResponse

def home(request):
    return HttpResponse("Healthcare Backend is Running ✅")

urlpatterns = [
    path("", home),   # add this line
    path("admin/", admin.site.urls),
    path("api/auth/register/", RegisterView.as_view()),
    path("api/auth/login/", TokenObtainPairView.as_view()),
    path("api/", include(router.urls)),
]