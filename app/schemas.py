from pydantic import BaseModel
from typing import Optional, List

class CardBase(BaseModel):
    set_name: str
    number: str
    name: str
    subtitle: Optional[str] = None
    type: str
    aspects: Optional[str] = None
    traits: Optional[str] = None
    arenas: Optional[str] = None
    cost: Optional[str] = None
    power: Optional[str] = None
    hp: Optional[str] = None
    rarity: str
    is_unique: bool = False
    artist: Optional[str] = None
    variant_type: Optional[str] = None
    market_price: Optional[str] = None
    foil_price: Optional[str] = None
    front_art: Optional[str] = None

class Leader(CardBase):
    front_text: str
    epic_action: str
    double_sided: bool = False
    back_text: Optional[str] = None

class Unit(CardBase):
    front_text: str
    double_sided: bool = False
    special_abilities: Optional[str] = None
    actions: Optional[str] = None

class Event(CardBase):
    event_text: str
    event_cost: Optional[int] = None

class Upgrade(CardBase):
    upgrade_text: str
    effect: str
    attach_to: Optional[str] = None
    upgrade_cost: Optional[str] = None