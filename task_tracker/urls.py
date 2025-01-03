from django.urls import path
from task_tracker import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
    path("task-create", views.TaskCreateView.as_view(), name="task-view"),
    path("update/<int:pk>/", views.TaskDetailView.as_view(), name="task-detail")
]