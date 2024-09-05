from django.urls import path
from .views import signup, login_view, logout_view, research_create_view,innovation_create_view
from . import views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Redirect to login for now
    path('create-research/', views.research_create_view, name='create_research'), #For Creating Research 
    path('create-innovation/', innovation_create_view, name='create_innovation'),
]
