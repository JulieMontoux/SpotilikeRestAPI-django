from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Album, Genre, Artist, Song, Utilisateur, UtilisateurManager
from .serializers import (
    AlbumSerializer, GenreSerializer, ArtistSerializer,
    SongSerializer, UserSerializer
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from rest_framework_jwt.views import ObtainJSONWebToken
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.decorators import permission_classes

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
    user = Utilisateur.objects.create_superuser(
        email=request.data.get('email'),
        username=request.data.get('username'),
        password=request.data.get('password')
    )
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

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
@permission_classes([IsAuthenticated])
def user_delete(request, id):
    user = generics.get_object_or_404(Utilisateur, id=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# DELETE - /api/albums/:id
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def album_delete(request, id):
    album = generics.get_object_or_404(Album, id=id)
    album.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# DELETE - /api/artists/:id
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
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
    users = Utilisateur.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# GET - /api/songs
@api_view(['GET'])
def song_list(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        password = request.data.get('password')
        hashed_password = make_password(password)
        request.data['password'] = hashed_password

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(ObtainJSONWebToken):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.user
        if user.is_active:
            refresh_token = response.data['refresh']
            access_token = response.data['access']

            custom_response_data = {
                'refresh_token': refresh_token,
                'access_token': access_token,
                'username': user.username,
                'email': user.email,
            }

            return Response(custom_response_data)
        else:
            return Response({'message': 'User is not active'}, status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            user_info = {
                'email': user.email,
                'username': user.username,
            }
            return Response({'access_token': access_token, 'user': user_info}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)
