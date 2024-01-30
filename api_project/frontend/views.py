from django.shortcuts import get_object_or_404, render
from api_app.models import Album, Artist
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
    return render(request, 'frontend/albums.html', {'albums': albums})

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
        else:
            print(f"Failed to fetch songs for album {album_id}. Status code: {songs_response.status_code}")
    print(all_songs)

    return render(request, 'frontend/all_songs.html', {'songs': all_songs})

def all_artists(request):
    response = requests.get('http://localhost:8000/api/artists/')
    artists = response.json() if response.status_code == 200 else []
    return render(request, 'frontend/artists.html', {'artists': artists})

def album_detail(request, album_id):
    selected_album = get_object_or_404(Album, pk=album_id)
    return render(request, 'frontend/album_detail.html', {'album': selected_album})

def artist_detail(request, artist_id):
    selected_artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'frontend/artist_detail.html', {'artist': selected_artist})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Connexion réussie!')
                return redirect('index')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

