from django.shortcuts import render
from api_app.models import Album, Song
import requests

def base(request):
    return render(request, 'frontend/base.html')

def index(request):
    return render(request, 'frontend/index.html')

def login_view(request):
    return render(request, 'frontend/login.html')

def signup_view(request):
    return render(request, 'frontend/signup.html')

def all_albums(request):
    response = requests.get('http://localhost:8000/api/albums/')
    albums = response.json() if response.status_code == 200 else []
    return render(request, 'frontend/all_albums.html', {'albums': albums})

def all_songs(request):
    albums_response = requests.get('http://localhost:8000/api/albums/')
    
    if albums_response.status_code == 200:
        albums = albums_response.json()
    else:
        albums = []

    all_songs = []
    for album in albums:
        album_id = album['id']
        songs_response = requests.get(f'http://localhost:8000/api/albums/{album_id}/songs/')
        
        if songs_response.status_code == 200:
            songs = songs_response.json()
            all_songs.extend(songs)

    return render(request, 'frontend/all_songs.html', {'songs': all_songs})
