from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('todos/<int:todo_id>/', views.todo_update_delete),
    # path('users/<int:user_id>/', views.user_detail),
]
