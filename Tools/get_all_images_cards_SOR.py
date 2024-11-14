import os
import requests

# URL de base pour obtenir l'image de chaque carte
BASE_URL = "https://api.swu-db.com/cards"
IMAGE_FORMAT = "?format=image"

# Crée un dossier pour stocker les images
OUTPUT_DIR = "images_sor"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_card_image(series, card_number):
    # Construit l'URL complète de l'image de la carte
    url = f"{BASE_URL}/{series}/{card_number}{IMAGE_FORMAT}"
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        # Définit le nom de fichier basé sur la série et le numéro de la carte
        file_name = f"{card_number}.jpg"
        file_path = os.path.join(OUTPUT_DIR, file_name)

        # Enregistre l'image dans le dossier de sortie
        with open(file_path, "wb") as image_file:
            for chunk in response.iter_content(1024):
                image_file.write(chunk)
        
        print(f"Téléchargé : {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement de la carte {series}/{card_number} : {e}")

def main():
    # faire une boucle for pour télécharger les images de la carte n°1 à la dernière
    series = "sor"  # Indique la série. Si d'autres séries existent, adapte ou ajoute une boucle pour chacune.
    
    # Boucle pour télécharger les cartes numérotées de 1 à 510
    for card_number in range(1, 511):
        download_card_image(series, card_number)

if __name__ == "__main__":
    main()