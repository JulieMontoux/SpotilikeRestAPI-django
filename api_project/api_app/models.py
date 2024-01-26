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
    artist_id = models.ManyToManyField(Artist)

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre_id = models.ManyToManyField(Genre)

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
