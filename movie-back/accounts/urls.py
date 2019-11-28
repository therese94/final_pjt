from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('potential/<int:user_id>/<int:movie_id>/', views.potential, name='potential'),
    path('follow/<int:user_id>/<int:following_id>/', views.follow, name='follow'),
]
