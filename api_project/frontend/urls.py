from django.urls import path
from . import views
from api_app import views as v

urlpatterns = [
    path('/base', views.base, name='base'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('albums/', views.all_albums, name='albums'),
    path('artists/', views.all_artists, name='artists'),
    path('album_detail/<int:album_id>/', views.album_detail, name='album_detail'),
    path('artist_detail/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('user_login/', views.user_login, name='user_login')
]
