from pydantic import BaseModel
from typing import List, Optional

class CardBase(BaseModel):
    Set: str
    Number: str
    Name: str
    Subtitle: Optional[str] = None  # Certains types peuvent ne pas avoir de sous-titre
    Type: str
    Aspects: List[str]  # Liste des aspects, comme "Vigilance", "Villainy"
    Traits: List[str]  # Liste des traits comme "IMPERIAL", "MANDALORIAN"
    Arenas: List[str]  # Zones où la carte peut être jouée, par exemple "Ground"
    Cost: str  # Coût de la carte
    Power: Optional[str] = None  # Pour les unités ou les Leaders avec une valeur de puissance
    HP: Optional[str] = None  # Points de vie de la carte
    Rarity: str  # Rare, Common, etc.
    Unique: bool  # Indique si la carte est unique ou non
    Artist: Optional[str] = None  # Artiste (optionnel)
    VariantType: Optional[str] = None  # Type de variante (optionnel)
    MarketPrice: Optional[str] = None  # Prix sur le marché (optionnel)
    FoilPrice: Optional[str] = None  # Prix foil (optionnel)
    FrontArt: Optional[str] = None  # L'URL de l'image de la carte (optionnel)

class Leader(CardBase):
    FrontText: str  # Texte avant, qui décrit les effets de la carte
    EpicAction: str  # Action épique, spécifique aux Leaders
    DoubleSided: bool  # Si la carte est double face
    BackText: Optional[str] = None  # Texte de l'autre côté (si DoubleSided est vrai)

class Unit(CardBase):
    FrontText: str  # Action ou texte lié à l'unité
    DoubleSided: bool = False  # Les unités ne sont généralement pas double face
    SpecialAbilities: Optional[str] = None  # Capacité spéciale, si nécessaire
    Actions: Optional[List[str]] = None  # Actions spécifiques comme "Exhaust" ou autres capacités

class Event(CardBase):
    EventText: str  # Texte spécifique à l'événement
    Cost: Optional[int] = None  # Coût pour jouer cet événement, si applicable

class Upgrade(CardBase):
    UpgradeText: str  # Texte de l'amélioration
    Effect: str  # Description de l'effet de l'amélioration
    AttachTo: Optional[str] = None  # À quelle unité cette amélioration peut être attachée
    UpgradeCost: Optional[str] = None  # Coût de l'amélioration si applicable