from fastapi import APIRouter,HTTPException
from src.manejo_archivo import *

anime_router = APIRouter()

nombre_archivo = f"{ruta}anime.json"
anime = abrir_archivo(nombre_archivo)

@anime_router.get("/Obtener_Animes")
def Obtener_Animes() -> list:
    """
    Obtiene todos los animes
    Returns:
        list: Lista de animes
    """
    nombres = []
    for dic_anime in anime:
        nombre = dic_anime["name"]
        if nombre not in nombres:
            nombres.append(nombre)
    return nombres

def gets(columna :str,name : str) -> str | int:
    """
    Obtiene el valor de una columna de un anime
    Args:
        columna (str): Nombre de la columna
        name (str): Nombre del anime
    Returns:
        str | int: Valor de la columna
    """
    for dic_anime in anime:
        if name == dic_anime["name"]:
            return dic_anime[columna]
    raise HTTPException(status_code=404, detail="Anime no encontrado")

@anime_router.get("/descripcion")
def descripcion(name : str) -> str:
    """
    Obtiene la descripcion de un anime
    Args:
        name (str): Nombre del anime
    Returns:
        str: Descripcion del anime
    """
    return gets("description",name)

@anime_router.get("/clasificacion")
def clasificacion(name : str):
    """
    Obtiene la clasificacion de un anime
    Args:
        name (str): Nombre del anime
    Returns:
        str: Clasificacion del anime
    """
    return gets("Rating",name)

@anime_router.get("/categoria")
def categoria(name : str) -> str:
    """
    Obtiene la categoria de un anime
    Args:
        name (str): Nombre del anime
    Returns:
        str: Categoria del anime
    """
    return gets("categorie",name)

@anime_router.get("/estudio")
def estudio(name : str) -> str:
    """
    Obtiene el estudio de un anime
    Args:
        name (str): Nombre del anime
    Returns:
        str: Estudio del anime
    """
    return gets("studio",name)

@anime_router.get("/episodios")
def episodios(name) -> int:
    """
    Obtiene los episodios de un anime
    Args:
        name (str): Nombre del anime
    Returns:
        int: Episodios del anime
    """
    return gets("episode",name)

def puts(columna :str,name :str,value : str | int) -> str:
    """
    Actualiza el valor de una columna de un anime
    Args:
        columna (str): Nombre de la columna
        name (str): Nombre del anime
        value (str | int): Nuevo valor de la columna
    Returns:
        str: Mensaje de confirmacion
    """
    for index, dic_anime in enumerate(anime):
        if name == dic_anime["name"]:
            anime[index][columna] = value
            guardar_archivo(nombre_archivo,anime)
    raise HTTPException(status_code=404, detail="Anime no encontrado")

@anime_router.put("/actualizar episode")
def actualizar_episode(name: str,episode: int) -> str:
    """
    Actualiza los episodios de un anime
    Args:
        name (str): Nombre del anime
        episode (int): Nuevos episodios
    Returns:
        str: Mensaje de confirmacion
    """
    return puts("episode",name,episode)

@anime_router.put("/actualizar description")
def actualizar_description(name: str,description: str) -> str:
    """
    Actualiza la descripcion de un anime
    Args:
        name (str): Nombre del anime
        description (str): Nueva descripcion
    Returns:
        str: Mensaje de confirmacion
    """
    return puts("description",name,description)

@anime_router.put("/actualizar Rating")
def actualizar_Rating(name: str,Rating: float) -> str:
    """
    Actualiza el rating de un anime
    Args:
        name (str): Nombre del anime
        Rating (float): Nueva clasificacion
    Returns:
        str: Mensaje de confirmacion
    """
    return puts("Rating",name,str(Rating))

@anime_router.put("/actualizar name")
def actualizar_name(name: str, new_name : str) -> str:
    """
    Actualiza el nombre de un anime
    Args:
        name (str): Nombre del anime
        new_name (str): Nuevo nombre del anime
    Returns:
        str: Mensaje de confirmacion
    """
    return puts("name",name,new_name)

@anime_router.post("/Agregar_anime")
def agregar_anime(name, descrition, Rating, episode, categorie, studio) -> str:
    """
    Agrega un anime
    Args:
        name (str): Nombre del anime
        descrition (str): Descripcion del anime
        Rating (float): Clasificacion del anime
        episode (int): Episodios del anime
        categorie (str): Categoria del anime
        studio (str): Estudio del anime
    Returns:
        str: Mensaje de confirmacion
    """
    anime.append({
        "name": name,
        "description": descrition,
        "Rating": Rating,
        "episode": episode,
        "categorie": categorie,
        "studio": studio
    })
    guardar_archivo(nombre_archivo,anime)
    return f"Se agrego correctamente"

@anime_router.delete("/eliminar_anime")
def delete(name : str) -> str:
    """
    Elimina un anime
    Args:
        name (str): Nombre del anime
    Returns:
        str: Mensaje de confirmacion
    """
    for index, dic_anime in enumerate(anime):
        if name == dic_anime["name"]:
            anime.pop(index)
            guardar_archivo(nombre_archivo,anime)
            return f"Se elimino correctamente"
    raise HTTPException(status_code=404, detail="Anime no encontrado")