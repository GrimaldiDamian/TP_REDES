import requests

url = "localhost:8000/animes/"

def obtener_animes():
    respuesta = requests.get(f'{url}Obtener_Animes')
    respuesta.raise_for_status()
    return respuesta.json()

def obtener_descripcion():
    pass

def obtener_clasificacion():
    pass

def obtener_categoria():
    pass

def obtener_estudio():
    pass

def obtener_episodios():
    pass

def actualizar_episodios():
    pass

def actualizar_descripcion():
    pass

def actualizar_nombre():
    pass

def eliminar_anime():
    pass

def menu():
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

menu()