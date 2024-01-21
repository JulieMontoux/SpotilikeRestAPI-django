from rest_framework import serializers
from .models import Genre, Artist, Album, Song, User, GenreSong, ArtistAlbum

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GenreSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreSong
        fields = '__all__'

class ArtistAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistAlbum
        fields = '__all__'