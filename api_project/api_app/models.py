from django.db import models
from django.db.models.signals import post_migrate

#Django crée automatiquement un champ ID

class Genre(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Artist(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    biography = models.TextField()

class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = models.CharField(max_length=255)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()


# Table d'association entre Genre et Song (many-to-many)
class GenreSong(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


# Table d'association entre Artist et Album (many-to-many)
class ArtistAlbum(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
