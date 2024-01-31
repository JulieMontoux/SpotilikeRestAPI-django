from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Album, Genre, Artist, Song, User
from .serializers import (
    AlbumSerializer, GenreSerializer, ArtistSerializer,
    SongSerializer, UserSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework_jwt.utils import jwt_response_payload_handler

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from rest_framework_jwt.views import ObtainJSONWebToken

class CustomJSONWebToken(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        self.request = request  
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(username=request.data['username'])
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response.data['token'] = token

        return response


# GET - /api/albums
@api_view(['GET'])
def album_list(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

# GET - /api/albums/:id
@api_view(['GET'])
def album_detail(request, id):
    album = generics.get_object_or_404(Album, id=id)
    serializer = AlbumSerializer(album)
    return Response(serializer.data)

# GET - /api/albums/:id/songs
@api_view(['GET'])
def album_songs(request, id):
    songs = Song.objects.filter(album_id=id)
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

# GET - /api/genres
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

# GET - /api/artists/:id/songs
@api_view(['GET'])
def artist_songs(request, id):
    songs = Song.objects.filter(artist=id)
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

# POST - /api/users/signin
@api_view(['POST'])
def user_signin(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Configuration de l'authentification JWT
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# POST - /api/users/login
@api_view(['POST'])
def user_login(request):
    # Extraire les données de la requête
    username = request.data.get('username')
    password = request.data.get('password')

    # Vérifier si le nom d'utilisateur et le mot de passe sont présents
    if username is None or password is None:
        return Response({'error': 'Veuillez fournir un nom d\'utilisateur et un mot de passe'},
                        status=status.HTTP_400_BAD_REQUEST)

    # Utiliser la vue obtain_jwt_token pour obtenir le token
    response = obtain_jwt_token(request)
    
    # Vérifier si l'authentification a réussi
    if response.status_code == status.HTTP_200_OK:
        # Ajouter des informations supplémentaires au résultat si nécessaire
        user = User.objects.get(username=username)
        # Ajouter d'autres informations à la réponse si nécessaire

    return response

# POST - /api/albums
@api_view(['POST'])
def album_create(request):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST - /api/albums/:id/songs
@api_view(['POST'])
def song_create(request, id):
    album = generics.get_object_or_404(Album, id=id)
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(album=album)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT - /api/artists/:id
@api_view(['PUT'])
def artist_update(request, id):
    artist = generics.get_object_or_404(Artist, id=id)
    serializer = ArtistSerializer(artist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT - /api/albums/:id
@api_view(['PUT'])
def album_update(request, id):
    album = generics.get_object_or_404(Album, id=id)
    serializer = AlbumSerializer(album, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT - /api/genres/:id
@api_view(['PUT'])
def genre_update(request, id):
    genre = generics.get_object_or_404(Genre, id=id)
    serializer = GenreSerializer(genre, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE - /api/users/:id
@api_view(['DELETE'])
def user_delete(request, id):
    user = generics.get_object_or_404(User, id=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# DELETE - /api/albums/:id
@api_view(['DELETE'])
def album_delete(request, id):
    album = generics.get_object_or_404(Album, id=id)
    album.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# DELETE - /api/artists/:id
@api_view(['DELETE'])
def artist_delete(request, id):
    artist = generics.get_object_or_404(Artist, id=id)
    artist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#Autres endpoints

# GET - /api/artists
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

# GET - /api/users
@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# GET - /api/songs
@api_view(['GET'])
def song_list(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)