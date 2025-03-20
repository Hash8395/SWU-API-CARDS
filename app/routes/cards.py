from fastapi import APIRouter, HTTPException, Depends
import json
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models.card import Card, Leader as LeaderModel, Unit as UnitModel, Event as EventModel, Upgrade as UpgradeModel
from app.schemas import Leader, Unit, Event, Upgrade
from typing import List

# Charger les données des fichiers JSON
with open("Ressources/AllCardsBySet/cards_data_sor_modified.json", "r") as sor_file:
    sor_data = json.load(sor_file)["data"]

with open("Ressources/AllCardsBySet/cards_data_shd_modified.json", "r") as shd_file:
    shd_data = json.load(shd_file)["data"]

with open("Ressources/cards_data_event.json", "r") as event_file:
    event_data = json.load(event_file)["data"]

# Fusionner les données
all_cards = {"SOR": sor_data, "SHD": shd_data, "EVENT": event_data}

router = APIRouter()

# Créer les tables
Base.metadata.create_all(bind=engine)

# Dépendance pour obtenir la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route pour initialiser la base de données avec les données des cartes
@router.post("/init-db")
def init_db(db: Session = Depends(get_db)):
    for set_name, set_data in all_cards.items():
        for card in set_data:
            card_type = card["Type"].lower()
            if card_type == "leader":
                db_card = LeaderModel(
                    set_name=set_name,
                    number=card["Number"],
                    name=card["Name"],
                    type=card["Type"],
                    rarity=card["Rarity"],
                    front_text=card.get("FrontText", ""),
                    epic_action=card.get("EpicAction", ""),
                    double_sided=card.get("DoubleSided", False),
                    back_text=card.get("BackText", "")
                )
            elif card_type == "unit":
                db_card = UnitModel(
                    set_name=set_name,
                    number=card["Number"],
                    name=card["Name"],
                    type=card["Type"],
                    rarity=card["Rarity"],
                    front_text=card.get("FrontText", ""),
                    double_sided=card.get("DoubleSided", False),
                    special_abilities=card.get("SpecialAbilities", ""),
                    actions=card.get("Actions", "")
                )
            elif card_type == "event":
                db_card = EventModel(
                    set_name=set_name,
                    number=card["Number"],
                    name=card["Name"],
                    type=card["Type"],
                    rarity=card["Rarity"],
                    event_text=card.get("FrontText", ""),
                    event_cost=card.get("Cost", 0)
                )
            elif card_type == "upgrade":
                db_card = UpgradeModel(
                    set_name=set_name,
                    number=card["Number"],
                    name=card["Name"],
                    type=card["Type"],
                    rarity=card["Rarity"],
                    upgrade_text=card.get("UpgradeText", ""),
                    effect=card.get("Effect", ""),
                    attach_to=card.get("AttachTo", ""),
                    upgrade_cost=card.get("UpgradeCost", "")
                )
            else:
                db_card = Card(
                    set_name=set_name,
                    number=card["Number"],
                    name=card["Name"],
                    type=card["Type"],
                    rarity=card["Rarity"],
                    cost=card.get("Cost", ""),
                    power=card.get("Power", ""),
                    hp=card.get("HP", ""),
                    is_unique=card.get("Unique", False),
                    artist=card.get("Artist", ""),
                    variant_type=card.get("VariantType", ""),
                    market_price=card.get("MarketPrice", ""),
                    foil_price=card.get("FoilPrice", ""),
                    front_art=card.get("FrontArt", "")
                )
            db.add(db_card)
    db.commit()
    return {"message": "Base de données initialisée avec succès"}

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