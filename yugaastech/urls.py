"""yugaastech URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from yugaas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('OurServices/', views.ourservices, name='ourservices'),
    path('HumanResourceManagement/', views.humanresource, name='HumanResourceManagement'),
    path('TechnologyServices/', views.technologyservices, name='TechnologyServices'),
    path('CyberSecurityServices/', views.cybersecurityservices, name='CyberSecurityServices'),
    path('LearningAcademy/', views.learningacademy, name='LearningAcademy'),
    path('Career/', views.career, name='Career'),
    path('Home/', views.home, name='Home'),
    path('About/', views.about, name='About'),
    path('Contactus/', views.contactus, name='ContactUs'),
]
"""yugaastech URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from yugaas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('OurServices/', views.ourservices, name='ourservices'),
    path('HumanResourceManagement/', views.humanresource, name='HumanResourceManagement'),
    path('TechnologyServices/', views.technologyservices, name='TechnologyServices'),
    path('CyberSecurityServices/', views.cybersecurityservices, name='CyberSecurityServices'),
    path('LearningAcademy/', views.learningacademy, name='LearningAcademy'),
    path('Career/', views.career, name='Career'),
    path('Home/', views.home, name='Home'),
    path('About/', views.about, name='About'),
    path('Contactus/', views.contactus, name='ContactUs'),
]
from django.conf.urls.static import static
from yugaastech import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)