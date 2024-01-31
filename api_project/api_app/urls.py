from django.urls import path
from .views import (
    album_list, album_detail, album_songs,
    genre_list, artist_songs, user_signin,
    user_login, album_create, song_create,
    artist_update, album_update, genre_update,
    user_delete, album_delete, artist_delete, artist_list, user_list, song_list
)

urlpatterns = [
    path('albums/', album_list, name='album-list'),
    path('albums/<int:id>/', album_detail, name='album-detail'),
    path('albums/<int:id>/songs/', album_songs, name='album-songs'),
    path('albums/create/', album_create, name='album-create'),
    path('albums/<int:id>/songs/create/', song_create, name='song-create'),
    path('albums/<int:id>/update/', album_update, name='album-update'),
    path('albums/<int:id>/delete/', album_delete, name='album-delete'),
    path('genres/', genre_list, name='genre-list'),
    path('genres/<int:id>/update/', genre_update, name='genre-update'),
    path('artists/', artist_list, name='artist-list'),
    path('artists/<int:id>/songs/', artist_songs, name='artist-songs'),
    path('artists/<int:id>/update/', artist_update, name='artist-update'),
    path('artists/<int:id>/delete/', artist_delete, name='artist-delete'),
    path('users/', user_list, name='user-list'),
    path('users/signin/', user_signin, name='user-signin'),
    path('users/login/', user_login, name='user-login'),
    path('users/<int:id>/delete/', user_delete, name='user-delete'),
    path('songs/', song_list, name='song-list'),

]
