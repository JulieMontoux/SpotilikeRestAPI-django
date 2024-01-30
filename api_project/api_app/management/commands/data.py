import json
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Importe des données depuis un fichier JSON vers la base de données'

    def handle(self, *args, **options):
        with open('chemin/vers/votre/fichier.json', 'r') as file:
            data = json.load(file)

            for item in data:
                Album.objects.create(
                    champ1=item['champ1'],
                    champ2=item['champ2'],
                    # Ajoutez d'autres champs selon votre modèle
                )

        self.stdout.write(self.style.SUCCESS('Les données ont été importées avec succès.'))
