import os
import hashlib
import time

def create_game_directory(game_name):
    game_path = f"./Games/{game_name}"
    if os.path.exists(game_path) or not os.makedirs(game_path, exist_ok=True):
        raise Exception("Erreur lors de la création du répertoire de jeu.")
    return game_path

def initialize_game_files(user_id, deck, visibility, game_description):
    # Génération de l'ID de la partie
    game_name = hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]

    # Créer le répertoire de la partie
    game_path = create_game_directory(game_name)

    # Créer le fichier de la partie
    game_file_path = os.path.join(game_path, "GameFile.txt")
    with open(game_file_path, "w") as f:
        f.write(f"Partie créée par {user_id} avec le deck {deck}.")

    return game_name