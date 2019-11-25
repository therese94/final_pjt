from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>/', views.index, name='index'),
    path('make_db/', views.make_db, name='make_db'),
    # path('todos/<int:todo_id>/', views.todo_update_delete),
    # path('users/<int:user_id>/', views.user_detail),
]
