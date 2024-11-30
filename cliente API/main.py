import requests

url = "http://localhost:8000/animes/"

def obtener_animes() -> dict:
    """
    Función que obtiene los nombres de los animes
    Returns:
        [json]: [json con los nombres de los animes]
    """
    try:
        respuesta = requests.get(f'{url}Obtener_Animes')
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        return e

def gets(name: str, columna: str) -> str:
    """
    Función que obtiene la información de un anime
    Args:
        name (str): [nombre del anime]
        columna (str): [columna de la tabla]
    Returns:
        str : Devuelve la información del anime
    """
    try:
        respuesta = requests.get(f'{url}{columna}', params={'name': name})
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        return e

def obtener_descripcion() -> str:
    """
    Función que obtiene la descripción de un anime
    Returns:
        str : Devuelve la descripción del anime
    """
    name = input("Ingrese nombre del anime: ")
    return gets(name, "descripcion")

def obtener_clasificacion() -> str:
    """
    Función que obtiene la clasificación de un anime
    Returns:
        str : Devuelve la clasificación del anime
    """
    name = input("Ingrese nombre del anime: ")
    return gets(name, "clasificacion")

def obtener_categoria() -> str:
    """
    Función que obtiene la categoría de un anime
    Returns:
        str : Devuelve la categoría del anime
    """
    name = input("Ingrese nombre del anime: ")
    return gets(name, "categoria")

def obtener_estudio() -> str:
    """
    Función que obtiene el estudio de un anime
    Returns:
        str : Devuelve el estudio del anime
    """
    name = input("Ingrese nombre del anime: ")
    return gets(name, "estudio")

def obtener_episodios() -> int:
    """
    Función que obtiene los episodios de un anime
    Returns:
        int : Devuelve la cantidad de episodios del anime
    """
    name = input("Ingrese nombre del anime: ")
    return gets(name, "episodios")

def puts(name: str, columna: str, value: str | float | int) -> str:
    """
    Función que actualiza la información de un anime
    Args:
        name (str): [nombre del anime]
        columna (str): [columna de la tabla]
        value (str | float | int): [valor a actualizar]
    Returns:
        str : Devuelve la respuesta de la actualización
    """
    try:
        respuesta = requests.put(f'{url}actualizar {columna}', params={'name': name, columna: value})
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        return e

def actualizar_episodios() -> str:
    """
    Función que actualiza los episodios de un anime
    Returns:
        str : Devuelve la respuesta de la actualización de los episodios
    """
    
    name = input("Ingrese nombre del anime: ")
    episode = int(input("Ingrese cantidad de episodios: "))
    return puts(name, "episodios", episode)

def actualizar_descripcion() -> str:
    """
    Función que actualiza la descripción de un anime
    Returns:
        str : Devuelve la respuesta de la actualización de la descripción
    """
    name = input("Ingrese nombre del anime: ")
    descripcion = input("Ingrese descripcion: ")
    return puts(name, "descripcion", descripcion)

def actualizar_rating() -> str:
    """
    Función que actualiza el rating de un anime
    Returns:
        str : Devuelve la respuesta de la actualización del rating
    """
    name = input("Ingrese nombre del anime: ")
    rating = float(input("Ingrese rating: "))
    return puts(name, "rating", rating)

def actualizar_nombre() -> str:
    """
    Función que actualiza el nombre de un anime
    Returns:
        str : Devuelve la respuesta de la actualización del nombre
    """
    name = input("Ingrese nombre del anime: ")
    new_name = input("Ingrese nuevo nombre: ")
    return puts(name, "nombre", new_name)

def eliminar_anime():
    pass

def menu():
    """
    Funcion que muestra el menu de opciones
    """
    try:
        while True:
            op = int(input("1. Obtener Animes\n2. Obtener descripcion\n3. Obtener clasificacion\n4. Obtener categoria\n5. Obtener estudio\n6. Obtener episodios\n7. Actualizar episodios\n8. Actualizar descripcion\n9Actualizar rating\n10. Actualizar nombre\n12. Eliminar anime\n12. Salir\nIngrese opcion: "))
            
            if op == 1:
                print(obtener_animes())
            elif op == 2:
                print(obtener_descripcion())
            elif op == 3:
                print(obtener_clasificacion())
            elif op == 4:
                print(obtener_categoria())
            elif op == 5:
                print(obtener_estudio())
            elif op == 6:
                print(obtener_episodios())
            elif op == 7:
                print(actualizar_episodios())
            elif op == 8:
                print(actualizar_descripcion())
            elif op == 9:
                print(actualizar_rating())
            elif op == 10:
                print(actualizar_nombre())
            elif op == 11:
                print(eliminar_anime())
            elif op == 12:
                break
    except ValueError:
        print("Ingrese un valor valido")
        menu()

menu()