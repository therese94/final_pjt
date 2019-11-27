from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<int:user_id>/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('potential/<int:user_id>/<int:movie_id>/', views.potential, name='potential'),
#     # path('todos/<int:todo_id>/', views.todo_update_delete),
#     # path('users/<int:user_id>/', views.user_detail),
]
