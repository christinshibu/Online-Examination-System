"""
URL configuration for exam_project project.

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
from django.urls import path 
from core import views

# New imports for serving media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_login, name='login'), # Step 2: Login validation
    path('register/', views.register_student, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('profile/', views.profile_view, name='profile'),    
    path('exam/', views.exam_view, name='exam'),
    path('submit/', views.exam_view, name='submit_exam'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('logout/', views.student_logout, name='logout'),    
]

# This connects your MEDIA_ROOT to the browser so photos can be displayed
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)