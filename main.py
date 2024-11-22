from fastapi import FastAPI
from app.routes import cards, games, users  # Importer vos fichiers de routes

app = FastAPI()

# Inclure les routeurs
app.include_router(cards.router, prefix="/cards", tags=["Cartes"])
app.include_router(games.router, prefix="/games", tags=["Parties"])
# app.include_router(users.router, prefix="/users", tags=["Utilisateurs"])

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API Star Wars Unlimited"}