from django.urls import path
from gen import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('projects', views.projectdisplay, name= 'projects'),
    path('aboutpage', views.aboutpage, name= 'about'),
    
]