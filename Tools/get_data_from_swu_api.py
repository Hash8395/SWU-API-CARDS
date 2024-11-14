import requests
import json

# URL de l'API
api_url = "https://api.swu-db.com/cards/search?q=ty:upgrade"

# Récupérer les données depuis l'API
response = requests.get(api_url)

if response.status_code == 200:
    cards_data = response.json()

    # Enregistrer les données dans un fichier JSON
    output_json_path = '/home/angelo/Dev/SWUOnline/Database/cards_data.json'
    with open(output_json_path, 'w') as json_file:
        json.dump(cards_data, json_file, indent=4)
    
    print(f"Les cartes ont été récupérées et enregistrées dans : {output_json_path}")
else:
    print(f"Erreur lors de la récupération des données de l'API : {response.status_code}")
