from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('create_review/<int:movie_id>/<int:user_id>/', views.create_review, name='create_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('review/<int:movie_id>/', views.review, name='review'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
    path('make_db/', views.make_db, name='make_db'),
]