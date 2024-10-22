from django.urls import path
from .views import HomeView,TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskToggleView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('toggle/<int:pk>/', TaskToggleView.as_view(), name='task_toggle'),
]