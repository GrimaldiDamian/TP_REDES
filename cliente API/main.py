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

def obtener_descripcion() -> dict:
    """
    Función que obtiene la descripción de un anime
    Returns:
        [json]: [json con la descripción del anime]
    """
    try:
        name = str(input("Ingrese nombre del anime: "))
        respuesta = requests.get(f'{url}descripcion', params={'name': name})
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        return e

def obtener_clasificacion() -> dict:
    """
    Función que obtiene la clasificación de un anime
    Returns:
        [json]: [json con la clasificación del anime]
    """
    try:
        name = input("Ingrese nombre del anime: ")
        print(name)
        respuesta = requests.get(f'{url}clasificacion', params={'name': name})
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        return e

def obtener_categoria() -> dict:
    """
    Función que obtiene la categoría de un anime
    Returns:
        [json]: [json con la categoría del anime
    """
    try:
        name = input("Ingrese nombre del anime: ")
        respuesta = requests.get(f'{url}categoria', params={'name': name})
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        return e

def obtener_estudio() -> dict:
    """
    Función que obtiene el estudio de un anime
    Returns:
        [json]: [json con el estudio del anime]
    """
    try:
        name = input("Ingrese nombre del anime: ")
        respuesta = requests.get(f'{url}estudio', params={'name': name})
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        return e

def obtener_episodios() -> dict:
    """
    Función que obtiene los episodios de un anime
    Returns:
        [json]: [json con los episodios del anime]
    """
    try:
        name = input("Ingrese nombre del anime: ")
        respuesta = requests.get(f'{url}episodios', params={'name': name})
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        return e

def actualizar_episodios():
    pass

def actualizar_descripcion():
    pass

def actualizar_nombre():
    pass

def eliminar_anime():
    pass

def menu():
    """
    Funcion que muestra el menu de opciones
    """
    try:
        while True:
            op = int(input("1. Obtener Animes\n2. Obtener descripcion\n3. Obtener clasificacion\n4. Obtener categoria\n5. Obtener estudio\n6. Obtener episodios\n7. Actualizar episodios\n8. Actualizar descripcion\n9. Actualizar nombre\n10. Eliminar anime\n11. Salir\nIngrese opcion: "))
            
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
                print(actualizar_nombre())
            elif op == 10:
                print(eliminar_anime())
            elif op == 11:
                break
    except ValueError:
        print("Ingrese un valor valido")
        menu()

menu()