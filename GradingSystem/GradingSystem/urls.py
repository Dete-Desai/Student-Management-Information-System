"""GradingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from accounts.views import smishome, smislogin, smisregister, smisprofile, delete_user, LogOut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('smis/', include('accounts.urls')),

    path('', smishome, name="smishome"),
    path('smis!=account?auth=0/', smislogin, name="smislogin"),
    path('smis:?register<user/', smisregister, name="smisregister"),
    path('smis#profile??:auth=1', smisprofile, name="smisprofile"),
    path('LogOut/', LogOut, name='smislogout'),

    path('delete/(<username>[\w|\W.-]+)/', delete_user, name='delete-user')
]
