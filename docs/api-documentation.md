# Documentation de l'API

Bienvenue dans la documentation de l'API de "Spotilike". Cette documentation fournit des informations sur les différents endpoints disponibles.

## Endpoints

1. **GET - /api/albums :**
   - Récupère la liste de tous les albums.
   - [Lien vers l'endpoint](http://127.0.0.1:8000/api/albums)

2. **GET - /api/albums/:id :**
   - Récupère les détails de l'album spécifié par :id.
   - [Lien vers l'endpoint](http://127.0.0.1:8000/api/albums/1) *(exemple avec ID=1)*

3. **GET - /api/albums/:id/songs :**
   - Récupère les morceaux de l'album spécifié par :id.
   - [Lien vers l'endpoint](http://127.0.0.1:8000/api/albums/1/songs) *(exemple avec ID=1)*

4. **GET - /api/genres :**
   - Récupère la liste de tous les genres.
   - [Lien vers l'endpoint](http://127.0.0.1:8000/api/genres)

5. **GET - /api/artists/:id/songs :**
   - Récupère la liste de tous les morceaux de l'artiste spécifié par :id.
   - [Lien vers l'endpoint](http://127.0.0.1:8000/api/artists/1/songs) *(exemple avec ID=1)*

6. **POST - /api/users/signin :**
   - Ajout d'un utilisateur.
   - [Lien vers l'endpoint](http://127.0.0.1:8000/api/users/signin)

7. **POST - /api/users/login :**
   - Connexion d'un utilisateur (JWT).
   - [Lien vers l'endpoint](http://127.0.0.1:8000/api/users/login)

8. **POST - /api/albums :**
   - Ajout d'un album.
   - [Lien vers l'endpoint](http://127.0.0.1:8000/api/albums)

9. **POST - /api/albums/:id/songs :**
   - Ajout d'un morceau dans l'album spécifié par :id.
   - [Lien vers l'endpoint](http://127.0.0.1:8000/api/albums/1/songs) *(exemple avec ID=1)*

10. **PUT - /api/artists/:id :**
    - Modification de l'artiste spécifié par :id.
    - [Lien vers l'endpoint](http://127.0.0.1:8000/api/artists/1) *(exemple avec ID=1)*

11. **PUT - /api/albums/:id :**
    - Modification de l'album spécifié par :id.
    - [Lien vers l'endpoint](http://127.0.0.1:8000/api/albums/1) *(exemple avec ID=1)*

12. **PUT - /api/genres/:id :**
    - Modification du genre spécifié par :id.
    - [Lien vers l'endpoint](http://127.0.0.1:8000/api/genres/1) *(exemple avec ID=1)*

13. **DELETE - /api/users/:id :**
    - Suppression de l'utilisateur spécifié par :id.
    - [Lien vers l'endpoint](http://127.0.0.1:8000/api/users/1) *(exemple avec ID=1)*

14. **DELETE - /api/albums/:id :**
    - Suppression de l'album spécifié par :id.
    - [Lien vers l'endpoint](http://127.0.0.1:8000/api/albums/1) *(exemple avec ID=1)*

15. **DELETE - /api/artists/:id :**
    - Suppression de l'artiste spécifié par :id.
    - [Lien vers l'endpoint](http://127.0.0.1:8000/api/artists/1) *(exemple avec ID=1)*
