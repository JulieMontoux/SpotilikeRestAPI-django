from django.urls import path
from .views import (
    album_list, album_detail, album_songs,
    genre_list, artist_songs, user_signin,
    user_login, album_create, song_create,
    artist_update, album_update, genre_update,
    user_delete, album_delete, artist_delete
)

urlpatterns = [
    path('albums/', album_list, name='album-list'),
    path('albums/<int:id>/', album_detail, name='album-detail'),
    path('albums/<int:id>/songs/', album_songs, name='album-songs'),
    path('genres/', genre_list, name='genre-list'),
    path('artists/<int:id>/songs/', artist_songs, name='artist-songs'),
    path('users/signin/', user_signin, name='user-signin'),
    path('users/login/', user_login, name='user-login'),
    path('albums/create/', album_create, name='album-create'),
    path('albums/<int:id>/songs/create/', song_create, name='song-create'),
    path('artists/<int:id>/update/', artist_update, name='artist-update'),
    path('albums/<int:id>/update/', album_update, name='album-update'),
    path('genres/<int:id>/update/', genre_update, name='genre-update'),
    path('users/<int:pk>/delete/', user_delete, name='user-delete'),
    path('albums/<int:pk>/delete/', album_delete, name='album-delete'),
    path('artists/<int:pk>/delete/', artist_delete, name='artist-delete'),
]
