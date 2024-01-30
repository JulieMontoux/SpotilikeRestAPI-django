# RESTE A FAIRE

## RENDU

(### I. REPOSITORY GITHUB

Créer un nouveau repository github respectant la nomenclature suivante : technologie-api-pokemon
Exemple : fastapi-spotilike / express-spotilike)

(### II. BASE DE DONNÉES

Créer la structure de votre base de données à laquelle se connectera votre API. Vous avez le choix entre SQL et NoSQL, dans les deux cas, un diagramme du schéma de données sera à fournir en guise de documentation.
ALBUM
Titre
Pochette [Image] Date de sortie
Liste des morceaux Artiste
UTILISATEUR
Nom d’utilisateur Mot de passe Email
MORCEAU
Titre Durée Artiste Genre.s Album
ARTISTE
Nom d’artiste Avatar [Image] Biographie
GENRE
Titre Description)

### Insertion des données

(### III. API REST

Créer une API REST exposant les endpoints suivants :

1. GET - /api/albums : Récupère la liste de tous les albums
2. GET - /api/albums/:id : Récupère les détails de l’album précisé par :id
3. GET - /api/albums/:id/songs : Récupère les morceaux de l’album précisé par :id
4. GET - /api/genres : Récupère la liste de tous les genres
5. GET - /api/artists/:id/songs : Récupère la liste de tous les morceaux de l’artiste précisé par :id
6. POST - /api/users/signin : Ajout d’un utilisateur
7. POST - /api/users/login : Connexion d’un utilisateur (JWT)
8. POST - /api/albums : Ajout d’un album
9. POST - /api/albums/:id/songs : Ajout d’un morceau dans l’album précisé par :id
10. PUT - /api/artists/:id : Modification de l’artiste précisé par :id
11. PUT - /api/albums/:id : Modification de l’album précisé par :id
12. PUT - /api/genres/:id : Modification du genre précisé par :id
13. DELETE - /api/users/:id : Suppression de utilisateur précisé par :id
14. DELETE - /api/albums/:id : Suppression de l’album précisé par :id
15. DELETE - /api/artists/:id : Supression de l’artiste précisé par :id
Le respect des bonnes pratiques lors de la réalisation d’une API REST est primordial, les codes d’erreur HTTP devront être utilisés à bon escient. Attention pour l’endpoint 15, il vous faudra supprimer en cascade tous les éléments associés à l’artiste.)

### IV. AUTHENTIFICATION JWT

A l’aide du JWT, il vous faudra soumettre à authentification les endpoints concernant la supression de données à savoir les endpoints dont le verbe HTTP est DELETE.

### V. FRONTEND

Concernant la réalisation du frontend, vous avez le choix de la technologie, il vous faudra réaliser les quatre pages ci-suit :
(Une page listant tous les albums)
(Une page affichant les informations détaillées d’un album)
(Une page listant tous les artistes)
(Une page affichant les informations détaillées d’un artiste)
(Ne pas oublier de permettre la navigation entre chacune des pages.)

## SOUTENANCE

### ORAL - 10 À 15 MINUTES

Il faudra vous munir d'un diaporama contenant les éléments suivants : Présentation du projet
Choix des technologies
Présentation du modèle de données
Gestion de projet / Découpage des tâches
Démonstration de l’API et du frontend
Analyse des écarts
Conclusion / Axes d'amélioration

### QUESTIONS / RÉPONSES - 10 MINUTES

Il y aura quelques questions pour le groupe ainsi qu'une question par personne.
LIVRABLES ATTENDUS
Dans votre repository doit apparaître un dossier docs contenant les fichiers propres à la documentation, votre API, ainsi qu'un README.md permettant à n'importe qui de pouvoir lancer et utiliser votre API.
Je souhaite avoir par mail ou bien par message privé discord, le lien de votre repository GitHub ainsi que les noms et prénoms des personnes du groupe.
