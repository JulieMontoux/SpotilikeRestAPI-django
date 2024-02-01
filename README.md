# Projet "Spotilike"

## Description

Le projet "Spotilike" est une application web développée avec le framework Django et Django Rest Framework. L'objectif principal de cette application est de reproduire de Spotify en affichant des albums, morceaux, artistes.
D'un point de vue pédagogique, il permet d'apprendre à créer et exploiter une API.

### Fonctionnalités Principales

- **Gestion des Utilisateurs :** Inscription, connexion.
- **Catalogue Musical :** Exploration d'artistes, albums et morceaux.
- **Swagger API Documentation :** Interface interactive pour explorer et tester les endpoints de l'API.

### Configuration du Projet

1. **Environnement Virtuel :**
   - Créez un environnement virtuel : `python -m venv venv`
   - Activez l'environnement virtuel : Sur macOS/Linux - `source venv/bin/activate`, Sur Windows (PowerShell) - `.\venv\Scripts\Activate`

2. **Installation des Dépendances :**
   - Installez les dépendances requises : `pip install -r requirements.txt`

3. **Appliquer les Migrations :**
   - Appliquez les migrations pour créer la base de données : `python manage.py migrate`
   - Charger les images en dur : `python manage.py collectstatic`

4. **Lancement du Serveur de Développement :**
   - Changer de dossier : `cd api_project`
   - Lancez le serveur Django : `python manage.py runserver`
**Accès à l'Application :**
   - Accédez à l'application via votre navigateur à l'adresse : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
**Swagger API Documentation :**
   - Consultez la documentation interactive de l'API via Swagger : [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
**Accès Administration :**
   - Consultez la documentation interactive de l'API via Swagger : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

5. **Insérer les données:**
   `python import_data.py`
**Utilisateur Admin Test:**
   - Nom d'utilisateur : Rap91
   - Mot de passe : ILoveRap91

6. **Vider la BDD :**
   `python manage.py flush`
