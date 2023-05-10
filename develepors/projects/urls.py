from django.urls import path
from . import views

  
urlpatterns = [
    path('',views.home,name="projects"),
    path('project/<str:pk>/', views.project, name="project"),    
    path('project_form', views.createProject, name="createProject"),    
    path('update_form/<str:pk>/', views.updateProject, name="updateProject"),    
    path('delete_form/<str:pk>/', views.deleteProject, name="deleteProject"),    
]
