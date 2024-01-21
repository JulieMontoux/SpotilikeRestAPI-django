# Projet "Spotilike"

## Description

Le projet "Spotilike" est une application web développée avec le framework Django et Django Rest Framework. L'objectif principal de cette application est de reproduire de Spotify en affichant des albums, morceaux, artistes...
D'un point de vue pédagogique, il permet d'apprendre à créer et exploiter une API.

### Principaux Composants

1. **Django Rest Framework (DRF):**
   - **Description :** Django Rest Framework est un puissant framework Django pour la construction d'API RESTful. Il facilite la création d'API Web robustes en utilisant les fonctionnalités familières de Django, tout en offrant une flexibilité et des outils spécifiques aux API.

2. **Drf-yasg (Swagger pour l'API):**
   - **Description :** Drf-yasg est un package qui ajoute une interface Swagger (OpenAPI) à votre API Django Rest Framework. Cela permet une documentation interactive et visuelle des endpoints de l'API, facilitant le test et l'utilisation par les développeurs.

3. **Base de Données SQLite :**
   - **Description :** SQLite est le moteur de base de données par défaut utilisé par Django. Il offre une solution légère et simple, idéale pour le développement et les petites applications. Cependant, il peut être remplacé par d'autres moteurs de base de données plus robustes en fonction des besoins de l'application.

4. **Frontend Django :**
   - **Description :** Le frontend de l'application est construit en utilisant les fonctionnalités de template de Django. Il permet aux utilisateurs de naviguer à travers l'application, de découvrir de la musique, de gérer leurs playlists, et d'interagir avec l'API pour obtenir des informations sur les artistes, albums et morceaux.

### Fonctionnalités Principales

- **Gestion des Utilisateurs :** Inscription, connexion, et gestion de profils utilisateur.
- **Catalogue Musical :** Exploration d'artistes, albums et morceaux.
- **Fonction de Recherche :** Recherche avancée pour trouver rapidement des morceaux, artistes ou albums.
- **Swagger API Documentation :** Interface interactive pour explorer et tester les endpoints de l'API.

### Configuration du Projet

1. **Environnement Virtuel :**
   - Créez un environnement virtuel : `python -m venv venv`
   - Activez l'environnement virtuel : Sur macOS/Linux - `source venv/bin/activate`, Sur Windows (PowerShell) - `.\venv\Scripts\Activate`

2. **Installation des Dépendances :**
   - Installez les dépendances requises : `pip install -r requirements.txt`

3. **Appliquer les Migrations :**
   - Appliquez les migrations pour créer la base de données : `python manage.py migrate`

4. **Lancement du Serveur de Développement :**
   - Lancez le serveur Django : `python manage.py runserver`

5. **Accès à l'Application :**
   - Accédez à l'application via votre navigateur à l'adresse : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

6. **Swagger API Documentation :**
   - Consultez la documentation interactive de l'API via Swagger : [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

### Utilisateurs de Test

- **Utilisateur Admin :**
  - Nom d'utilisateur : admin
  - Mot de passe : admin123
