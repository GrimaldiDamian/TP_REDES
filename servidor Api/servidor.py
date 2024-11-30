import fastapi
from src.anime import *

app = fastapi.FastAPI()
app.include_router(anime_router, prefix="/animes", tags=["animes"])