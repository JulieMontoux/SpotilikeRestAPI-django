from django.db import models
from django.db.models.signals import post_migrate

#Django crée automatiquement un champ ID

class Genre(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    @classmethod
    def create_initial_data(cls):
        cls.objects.create(title='Grunge', description='Alternative rock genre emerged in the early \'90s.')
        cls.objects.create(title='Hip Hop', description='Dominant music style in the \'90s urban culture.')
        cls.objects.create(title='Eurodance', description='Electronic dance genre popular in European clubs.')

class Artist(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/')
    biography = models.TextField()

    @classmethod
    def create_initial_data(cls):
        cls.objects.create(name='Nirvana', avatar='../images/nirvana.jpeg', biography='Influential grunge band from Seattle.')
        cls.objects.create(name='Tupac Shakur', avatar='../images/tupac.jpeg', biography='Iconic rapper and actor in the \'90s.')
        cls.objects.create(name='2 Unlimited', avatar='../images/2unlimited.jpeg', biography='Eurodance duo known for energetic hits.')

class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers/')
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    @classmethod
    def create_initial_data(cls):
        cls.objects.create(title='Nevermind', cover='../images/nevermind.jpeg', release_date='1991-09-24', artist_id=1)
        cls.objects.create(title='All Eyez on Me', cover='../images/alleyezonme.jpeg', release_date='1996-02-13', artist_id=2)
        cls.objects.create(title='Get Ready!', cover='../images/getready.jpeg', release_date='1992-08-26', artist_id=3)

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    @classmethod
    def create_initial_data(cls):
        cls.objects.create(title='Smells Like Teen Spirit', duration='262', genre_id=1, album_id=1, artist_id=1)
        cls.objects.create(title='California Love', duration='266', genre_id=2, album_id=2, artist_id=2)
        cls.objects.create(title='Get Ready for This', duration='205', genre_id=3, album_id=3, artist_id=3)

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()

    @classmethod
    def create_initial_data(cls):
        cls.objects.create(username='90sFan', password='hashed_pass', email='90sfan@email.com')
        cls.objects.create(username='MusicLover', password='hashed_pass', email='music@email.com')
        cls.objects.create(username='DanceKing', password='hashed_pass', email='dance@email.com')

# Table d'association entre Genre et Song (many-to-many)
class GenreSong(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    @classmethod
    def create_initial_data(cls):
        cls.objects.create(song_id=1, genre_id=1)
        cls.objects.create(song_id=2, genre_id=2)
        cls.objects.create(song_id=3, genre_id=3)

# Table d'association entre Artist et Album (many-to-many)
class ArtistAlbum(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    @classmethod
    def create_initial_data(cls):
        cls.objects.create(artist_id=1, album_id=1)
        cls.objects.create(artist_id=2, album_id=2)
        cls.objects.create(artist_id=3, album_id=3)

# Ajoutez des signaux pour déclencher la création des données initiales après les migrations
def create_initial_data(sender, **kwargs):
    Genre.create_initial_data()
    Artist.create_initial_data()
    Album.create_initial_data()
    Song.create_initial_data()
    User.create_initial_data()
    GenreSong.create_initial_data()
    ArtistAlbum.create_initial_data()

# Attachez le signal post_migrate à la fonction create_initial_data
post_migrate.connect(create_initial_data, sender=models)