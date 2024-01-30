from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.URLField()
    biography = models.TextField()

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = models.URLField()
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def formatted_duration(self):
        total_duration = sum(song.duration for song in self.song_set.all())
        minutes, seconds = divmod(total_duration, 60)
        return f"{minutes} min {seconds} sec"

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username
