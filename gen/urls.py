from django.urls import path
from gen import views

from gen.views import AboutView

urlpatterns = [
   
    path('projects/', views.projectdisplay, name= 'projects'),
    path('', AboutView.as_view(),name='about'),
    
]