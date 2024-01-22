from django.shortcuts import render
from api_app.models import Album, Song
import requests

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
    response = requests.get('http://localhost:8000/api/songs/')
    songs = response.json() if response.status_code == 200 else []
    return render(request, 'frontend/all_songs.html', {'songs': songs})