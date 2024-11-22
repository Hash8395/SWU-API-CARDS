from fastapi import APIRouter, HTTPException
import json
from app.models.card import Leader, Unit, Event, Upgrade
from typing import List

# Charger les données des fichiers JSON
with open("Ressources/AllCardsBySet/cards_data_sor_modified.json", "r") as sor_file:
    sor_data = json.load(sor_file)["data"]

with open("Ressources/AllCardsBySet/cards_data_shd_modified.json", "r") as shd_file:
    shd_data = json.load(shd_file)["data"]

# Fusionner les données
all_cards = {"SOR": sor_data, "SHD": shd_data}

router = APIRouter()

# -------------------- ROUTES POUR LES CARTES --------------------

@router.get("/unit/{card_number}", response_model=Unit)
def get_unit(card_number: str):
    for set_name, set_data in all_cards.items():
        for card in set_data:
            if card["Type"] == "Unit" and card["Number"] == card_number:
                return Unit(**card)
    raise HTTPException(status_code=404, detail="Unit not found")

@router.get("/leader/{card_number}", response_model=Leader)
def get_leader(card_number: str):
    for set_name, set_data in all_cards.items():
        for card in set_data:
            if card["Type"] == "Leader" and card["Number"] == card_number:
                return Leader(**card)
    raise HTTPException(status_code=404, detail="Leader not found")

@router.get("/event/{card_number}", response_model=Event)
def get_event(card_number: str):
    for set_name, set_data in all_cards.items():
        for card in set_data:
            if card["Type"] == "Event" and card["Number"] == card_number:
                return Event(**card)
    raise HTTPException(status_code=404, detail="Event not found")

@router.get("/upgrade/{card_number}", response_model=Upgrade)
def get_upgrade(card_number: str):
    for set_name, set_data in all_cards.items():
        for card in set_data:
            if card["Type"] == "Upgrade" and card["Number"] == card_number:
                return Upgrade(**card)
    raise HTTPException(status_code=404, detail="Upgrade not found")

# --------- ROUTES POUR LES CARTES EXISTANTES ---------

@router.get("/{set_name}/{card_number}")
def get_card(set_name: str, card_number: str):
    set_data = all_cards.get(set_name.upper())
    if not set_data:
        raise HTTPException(status_code=404, detail="Set non trouvé")
    for card in set_data:
        if card["Number"] == card_number:
            return card
    raise HTTPException(status_code=404, detail="Carte non trouvée")

@router.get("/{set_name}")
def get_cards_by_set(set_name: str):
    set_data = all_cards.get(set_name.upper())
    if not set_data:
        raise HTTPException(status_code=404, detail="Set non trouvé")
    return set_data

@router.get("/type/{card_type}")
def get_cards_by_type(card_type: str):
    filtered_cards = []
    for set_name, set_data in all_cards.items():
        for card in set_data:
            if card["Type"].lower() == card_type.lower():
                filtered_cards.append(card)
    if not filtered_cards:
        raise HTTPException(status_code=404, detail=f"Aucune carte de type {card_type} trouvée")
    return filtered_cards

@router.get("/cost/{cost}")
def get_cards_by_cost(cost: int):
    filtered_cards = []
    for set_name, set_data in all_cards.items():
        for card in set_data:
            if int(card["Cost"]) == cost:
                filtered_cards.append(card)
    if not filtered_cards:
        raise HTTPException(status_code=404, detail=f"Aucune carte avec le coût {cost} trouvée")
    return filtered_cards

@router.get("/rarity/{rarity}")
def get_cards_by_rarity(rarity: str):
    filtered_cards = []
    for set_name, set_data in all_cards.items():
        for card in set_data:
            if card["Rarity"].lower() == rarity.lower():
                filtered_cards.append(card)
    if not filtered_cards:
        raise HTTPException(status_code=404, detail=f"Aucune carte de rareté {rarity} trouvée")
    return filtered_cards