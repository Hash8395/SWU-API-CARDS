from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse
from app.utils.session_manager import get_user_session
from app.utils.game_helpers import create_game_directory, initialize_game_files

router = APIRouter()

@router.post("/create")
def create_game(
    deck: str = Query(None),
    visibility: str = Query(None),
    gameDescription: str = Query("Game #")
):
    # Vérification de session
    user_id = get_user_session()
    if not user_id:
        raise HTTPException(status_code=401, detail="Utilisateur non connecté")

    # Créer la partie
    game_name = initialize_game_files(user_id, deck, visibility, gameDescription)
    return {"message": f"Partie créée avec l'ID {game_name}"}