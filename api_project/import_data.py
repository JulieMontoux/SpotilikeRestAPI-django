import os
import django
import json
from django.db import transaction
from django.contrib.auth.hashers import make_password

# Spécifiez le fichier de paramètres du projet Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_project.settings")
django.setup()

from api_app.models import Genre, Artist, Album, Song, Utilisateur

with open('data.json', 'r') as f:
    data = json.load(f)

# Fonction pour gérer la création ou récupération d'objets avec try-except
def create_or_get(model, defaults=None, **kwargs):
    try:
        instance = model.objects.get(**kwargs)
        print(f"{model.__name__} existant trouvé: {instance}")
    except model.DoesNotExist:
        instance = model.objects.create(**kwargs, **defaults)
        print(f"{model.__name__} créé: {instance}")
    except model.MultipleObjectsReturned:
        instance = model.objects.filter(**kwargs).first()
        print(f"{model.__name__} existant trouvé (en utilisant le premier): {instance}")
    
    return instance

# Insérer les genres
for genre_data in data['genre']:
    title = genre_data['title']
    description = genre_data['description']
    genre_instance = create_or_get(Genre, defaults={'description': description}, title=title)

# Insérer les artistes
for artist_data in data['artist']:
    name = artist_data['name']
    avatar = artist_data['avatar']
    biography = artist_data['biography']
    artist_instance = create_or_get(Artist, defaults={'avatar': avatar, 'biography': biography}, name=name)

# Insérer les utilisateurs
for user_data in data['users']:
    username = user_data['username']
    email = user_data['email']
    password = make_password(user_data['password'])
    user_instance = create_or_get(Utilisateur, defaults={'email': email, 'password': password}, username=username)


# Insérer les albums
for album_data in data['album']:
    title = album_data['title']
    cover = album_data['cover']
    release_date = album_data['release_date']
    artist_instance = create_or_get(Artist, name=album_data['artist'])
    album_instance = create_or_get(Album, defaults={'cover': cover, 'release_date': release_date, 'artist': artist_instance}, title=title)

for song_data in data['song']:
    artist_instance = create_or_get(Artist, name=song_data['artist'])
    album_instance = create_or_get(Album, title=song_data['album'], artist=artist_instance)
    genre_instance = create_or_get(Genre, title=song_data['genres'])

    # Création de la chanson sans les genres
    song_instance, created = Song.objects.get_or_create(
        title=song_data['title'],
        duration=song_data['duration'],
        artist=artist_instance,
        album=album_instance,
        genre=genre_instance
    )

    print(f"Chanson créée: {song_instance}")
