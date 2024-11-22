from pydantic import BaseModel

class Game(BaseModel):
    id: str
    description: str
    visibility: str
    player_1: str
    player_2: str
    status: str