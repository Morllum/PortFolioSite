from django.urls import path
from . import views  

urlpatterns = [
    path('home/', views.home, name='home'),
    path('About/', views.about, name='About'),
    path('Projects/', views.projects, name='Projects'),
    path('Contact/', views.contact, name='Contact')
]