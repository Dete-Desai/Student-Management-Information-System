from django.urls import path
from . import views

urlpatterns = [
    #path('', views.smishome, name="smishome"),
    #path('smis!=account?auth=0/', views.smislogin, name="smislogin"),
    #path('smis:?register<user/', views.smisregister, name="smisregister"),
    #path('smis#profile??:auth=1', views.smisprofile, name="smisprofile"),
    path('smisforms/', views.smisforms, name="smisforms"),
    path('smisresults/', views.smisresults, name="smisresults"),
    path('smistranscript/', views.smistranscript, name="smistranscript"),
]