from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class Card(Base):
    __tablename__ = "cards"
    
    id = Column(Integer, primary_key=True, index=True)
    set_name = Column(String, nullable=False)
    number = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    subtitle = Column(String, nullable=True)
    type = Column(String, nullable=False)  # Type général (Unit, Leader, etc.)
    aspects = Column(Text, nullable=True)  # Stocké en JSON/texte
    traits = Column(Text, nullable=True)
    arenas = Column(Text, nullable=True)
    cost = Column(String, nullable=True)
    power = Column(String, nullable=True)
    hp = Column(String, nullable=True)
    rarity = Column(String, nullable=False)
    is_unique = Column(Boolean, default=False)
    artist = Column(String, nullable=True)
    variant_type = Column(String, nullable=True)
    market_price = Column(String, nullable=True)
    foil_price = Column(String, nullable=True)
    front_art = Column(String, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'card',
        'polymorphic_on': type
    }

class Leader(Card):
    __tablename__ = "leaders"
    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    front_text = Column(Text, nullable=False)
    epic_action = Column(Text, nullable=False)
    double_sided = Column(Boolean, default=False)
    back_text = Column(Text, nullable=True)

    __mapper_args__ = {"polymorphic_identity": "leader"}

class Unit(Card):
    __tablename__ = "units"
    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    front_text = Column(Text, nullable=False)
    double_sided = Column(Boolean, default=False)
    special_abilities = Column(Text, nullable=True)
    actions = Column(Text, nullable=True)  # JSON ou texte avec actions spécifiques

    __mapper_args__ = {"polymorphic_identity": "unit"}

class Event(Card):
    __tablename__ = "events"
    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    event_text = Column(Text, nullable=False)
    event_cost = Column(Integer, nullable=True)

    __mapper_args__ = {"polymorphic_identity": "event"}

class Upgrade(Card):
    __tablename__ = "upgrades"
    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    upgrade_text = Column(Text, nullable=False)
    effect = Column(Text, nullable=False)
    attach_to = Column(Text, nullable=True)
    upgrade_cost = Column(Text, nullable=True)

    __mapper_args__ = {"polymorphic_identity": "upgrade"}