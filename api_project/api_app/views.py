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
    songs = Song.objects.filter(artists=id)
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

# POST - /api/users/login
@api_view(['POST'])
def user_login(request):
    # Ajoutez votre logique d'authentification JWT ici
    # Ceci est juste un espace réservé
    return Response({'message': 'User login successful'}, status=status.HTTP_200_OK)

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