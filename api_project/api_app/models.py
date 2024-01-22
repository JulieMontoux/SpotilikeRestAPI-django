from django.db import models

#Django crée automatiquement un champ ID

class Genre(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Artist(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/')
    biography = models.TextField()

class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers/')
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField()
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

# Ajout des données
#Genre.objects.create(title='Grunge', description='Alternative rock genre emerged in the early \'90s.')
#Genre.objects.create(title='Hip Hop', description='Dominant music style in the \'90s urban culture.')
#Genre.objects.create(title='Eurodance', description='Electronic dance genre popular in European clubs.')

#Artist.objects.create(name='Nirvana', avatar='./assets/nirvana.jpeg', biography='Influential grunge band from Seattle.')
#Artist.objects.create(name='Tupac Shakur', avatar='./assets/tupac.jpeg', biography='Iconic rapper and actor in the \'90s.')
#Artist.objects.create(name='2 Unlimited', avatar='./assets/2unlimited.jpeg', biography='Eurodance duo known for energetic hits.')

#Album.objects.create(title='Nevermind', cover='./assets/nevermind.jpeg', release_date='1991-09-24', artist_id=1)
#Album.objects.create(title='All Eyez on Me', cover='./assets/alleyezonme.jpeg', release_date='1996-02-13', artist_id=2)
#Album.objects.create(title='Get Ready!', cover='./assets/getready.jpeg', release_date='1992-08-26', artist_id=3)

#Song.objects.create(title='Smells Like Teen Spirit', duration='4:38', genre_id=1, album_id=1, artist_id=1)
#Song.objects.create(title='California Love', duration='4:44', genre_id=2, album_id=2, artist_id=2)
#Song.objects.create(title='Get Ready for This', duration='3:42', genre_id=3, album_id=3, artist_id=3)

#User.objects.create(username='90sFan', password='hashed_pass', email='90sfan@email.com')
#User.objects.create(username='MusicLover', password='hashed_pass', email='music@email.com')
#User.objects.create(username='DanceKing', password='hashed_pass', email='dance@email.com')

#GenreSong.objects.create(song_id=1, genre_id=1)
#GenreSong.objects.create(song_id=2, genre_id=2)
#GenreSong.objects.create(song_id=3, genre_id=3)

#ArtistAlbum.objects.create(artist_id=1, album_id=1)
#ArtistAlbum.objects.create(artist_id=2, album_id=2)
#ArtistAlbum.objects.create(artist_id=3, album_id=3)