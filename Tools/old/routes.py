import json
import os
import hashlib
import time
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse

# Charger les données des fichiers JSON
with open("Ressources/AllCardsBySet/cards_data_sor_modified.json", "r") as sor_file:
    sor_data = json.load(sor_file)["data"]

with open("Ressources/AllCardsBySet/cards_data_shd_modified.json", "r") as shd_file:
    shd_data = json.load(shd_file)["data"]

# Fusionner les données en un seul dictionnaire pour les accéder facilement
all_cards = {
    "SOR": sor_data,
    "SHD": shd_data
}

# Simuler une gestion de sessions (remplacez par une solution persistante)
sessions = {}

# Créer un routeur FastAPI
router = APIRouter()

# --------- ROUTES POUR LES CARTES EXISTANTES ---------

@router.get("/cards/{set_name}/{card_number}")
def get_card(set_name: str, card_number: str):
    set_data = all_cards.get(set_name.upper())
    if not set_data:
        raise HTTPException(status_code=404, detail="Set non trouvé")
    for card in set_data:
        if card["Number"] == card_number:
            return card
    raise HTTPException(status_code=404, detail="Carte non trouvée")

@router.get("/cards/{set_name}")
def get_cards_by_set(set_name: str):
    set_data = all_cards.get(set_name.upper())
    if not set_data:
        raise HTTPException(status_code=404, detail="Set non trouvé")
    return set_data

@router.get("/cards/type/{card_type}")
def get_cards_by_type(card_type: str):
    filtered_cards = []
    for set_name, set_data in all_cards.items():
        for card in set_data:
            if card["Type"].lower() == card_type.lower():
                filtered_cards.append(card)
    if not filtered_cards:
        raise HTTPException(status_code=404, detail=f"Aucune carte de type {card_type} trouvée")
    return filtered_cards

@router.get("/cards/cost/{cost}")
def get_cards_by_cost(cost: int):
    filtered_cards = []
    for set_name, set_data in all_cards.items():
        for card in set_data:
            if int(card["Cost"]) == cost:
                filtered_cards.append(card)
    if not filtered_cards:
        raise HTTPException(status_code=404, detail=f"Aucune carte avec le coût {cost} trouvée")
    return filtered_cards

@router.get("/cards/rarity/{rarity}")
def get_cards_by_rarity(rarity: str):
    filtered_cards = []
    for set_name, set_data in all_cards.items():
        for card in set_data:
            if card["Rarity"].lower() == rarity.lower():
                filtered_cards.append(card)
    if not filtered_cards:
        raise HTTPException(status_code=404, detail=f"Aucune carte de rareté {rarity} trouvée")
    return filtered_cards

# --------- ROUTES POUR LA GESTION DES PARTIES ---------

# Fonction pour générer un identifiant de partie
def generate_game_id():
    return hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]

# Endpoint pour créer une partie
@router.post("/games/create")
def create_game(
    deck: str = Query(None),
    decklink: str = Query(None),
    deckTestMode: str = Query(""),
    format: str = Query(None),
    visibility: str = Query(None),
    gameDescription: str = Query("Game #"),
    favoriteDeckLink: str = Query("0"),
    startingHealth: str = Query("")
):
    # Simuler une session utilisateur (remplacer par une gestion de session réelle)
    user_id = sessions.get("userid")
    if not user_id:
        raise HTTPException(status_code=401, detail="Utilisateur non connecté")

    # Gestion des paramètres liés à favoriteDeckLink
    favoriteDeckIndex = None
    if favoriteDeckLink != "0":
        favDeckArr = favoriteDeckLink.split("<fav>")
        if len(favDeckArr) == 1:
            favoriteDeckLink = favDeckArr[0]
        else:
            favoriteDeckIndex = favDeckArr[0]
            favoriteDeckLink = favDeckArr[1]

    # Génération du nom de la partie
    game_name = generate_game_id()
    game_path = f"./Games/{game_name}"

    # Création du répertoire pour la partie
    if os.path.exists(game_path) or not os.makedirs(game_path, exist_ok=True):
        raise HTTPException(status_code=500, detail="Erreur lors de la création du répertoire de jeu.")

    # Création des clés des joueurs
    p1_key = hashlib.sha256(f"{time.time()}".encode()).hexdigest()
    p2_key = hashlib.sha256(f"{time.time()*2}".encode()).hexdigest()

    # Écrire le fichier GameFile.txt
    game_file_path = os.path.join(game_path, "GameFile.txt")
    with open(game_file_path, "w") as f:
        f.write(f"Partie créée avec l'ID {game_name}")

    # Initialisation d'un fichier gamelog.txt
    log_file_path = os.path.join(game_path, "gamelog.txt")
    with open(log_file_path, "w") as f:
        f.write("Log de la partie initialisé.")

    # Redirection vers l'endpoint de connexion au jeu
    redirect_url = f"/games/join?gameName={game_name}&playerID=1&deck={deck}&fabdb={decklink}&format={format}"
    return RedirectResponse(url=redirect_url)

# Endpoint pour rejoindre une partie
@router.get("/games/join")
def join_game(gameName: str, playerID: int, deck: str, fabdb: str, format: str):
    return {
        "message": f"Joueur {playerID} a rejoint la partie {gameName} avec le deck {deck}.",
        "format": format
    }