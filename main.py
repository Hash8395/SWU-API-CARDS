from fastapi import FastAPI
from routes import router

app = FastAPI()

# Inclure les routes depuis le fichier routes.py
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API Star Wars Unlimited"}