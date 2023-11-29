from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_home, name='projects_home'),
    path('create_post', views.create_post, name='create_post'),
    path('<int:pk>', views.PostDetailView.as_view(), name='project_detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='project_update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='project_delete'),
]