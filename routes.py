import json
from fastapi import APIRouter, HTTPException

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

# Créer un routeur FastAPI
router = APIRouter()

# Route pour obtenir une carte spécifique
@router.get("/cards/{set_name}/{card_number}")
def get_card(set_name: str, card_number: str):
    set_data = all_cards.get(set_name.upper())
    if not set_data:
        raise HTTPException(status_code=404, detail="Set non trouvé")
    for card in set_data:
        if card["Number"] == card_number:
            return card
    raise HTTPException(status_code=404, detail="Carte non trouvée")

# Route pour obtenir toutes les cartes d'un set
@router.get("/cards/{set_name}")
def get_cards_by_set(set_name: str):
    set_data = all_cards.get(set_name.upper())
    if not set_data:
        raise HTTPException(status_code=404, detail="Set non trouvé")
    return set_data

# Route pour obtenir les cartes par type
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

# Route pour obtenir les cartes par coût
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

# Route pour obtenir les cartes par rareté
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