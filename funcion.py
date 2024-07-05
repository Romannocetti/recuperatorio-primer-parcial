import random
import json

#recibimos el nombre del archivo
def cargar_archivo():
    """
    Solicita al usuario ingresar el nombre del archivo 'post.csv' para cargarlo.
    Muestra un mensaje de confirmación una vez que se carga correctamente.
    """
    while True:
        NOMBRE = input("Ingrese el archivo que desea cargar: ")
        if NOMBRE == "post.csv":
            break
        else:
            print("El archivo no existe")
    print("--------------------------------------------------------------------------")
    print(f"Se ha cargado el archivo: {NOMBRE}")


def get_path_actual(nombre_archivo):
    """
    Obtiene la ruta completa del archivo especificado en función del directorio actual.

    Args:
    - nombre_archivo (str): Nombre del archivo del cual se desea obtener la ruta.

    Returns:
    - str: Ruta completa del archivo.
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

with open(get_path_actual("post.csv"), "r", encoding="utf-") as archivo:
    lista = []
    encabezado = archivo.readline().strip("\n").split(",")

    for linea in archivo.readlines():
        usuario = {}
        linea = linea.strip("\n").split(",")

        id, user, likes, dislikes, followers = linea 
        usuario["id"] = id
        usuario["user"] = user
        usuario["likes"] = int(likes)
        usuario["dislikes"] = int(dislikes)
        usuario["followers"] = int(followers)
        lista.append(usuario)



def asignar_likes(usuario):
    
    """Asigna valores aleatorios a cada usuario en la lista proporcionada.

    Args:
    lista (list): Lista de diccionarios donde cada diccionario representa a un usuario.
    """
    import random
    for usuario  in lista:
        usuario ["likes"] = random.randint(500,3000)
        usuario ["dislikes"] = random.randint(300,3500)
        usuario ["followers"] = random.randint(10000, 20000)


def filtrar_por_likes():
    """
    Filtra y guarda en un archivo separado por los usuarios que tienen mas de 2000 likes.

    Args:
    - tipo (str): usurario que tiene mas de 2000 likes.
    """
    with open(get_path_actual("post_likes.csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[1].keys())) + "\n"
        archivo.write(encabezado)
        
        for usuario in lista:
            if usuario['likes'] > 2000:
                values = [str(value) if isinstance(value, (int, float)) else value for value in usuario.values()]
                linea = ",".join(values) + "\n"
                archivo.write(linea)

def filtrar_por_haters():
    """
    Filtra y guarda en un archivo separado por los usuarios que tienen mas dislikes que likes.

    Args:
    - tipo (str): usurario que tiene mas de 2000 likes.
    """
    with open(get_path_actual(f"pudranse_haters.csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[1].keys())) + "\n"
        archivo.write(encabezado)
        
        for usuario in lista:
            if usuario['dislikes'] > usuario['likes']:
                values = [str(value) if isinstance(value, (int, float)) else value for value in usuario.values()]
                linea = ",".join(values) + "\n"
                archivo.write(linea)



def calcular_promedio_followers(lista):
    """
    Calcula y muestra el promedio de followers de todos los usuarios en la lista.

    Args:
    - lista (list): Lista de diccionarios representando a los usuarios, donde cada diccionario tiene la clave 'followers'.

    Returns:
    - float: Promedio de followers de todos los usuarios.
    """
    if not lista:
        print("La lista de usuarios está vacía.")
        return

    total_followers = sum(usuario['followers'] for usuario in lista)
    cantidad_usuarios = len(lista)
    promedio_followers = total_followers / cantidad_usuarios

    print(f"Promedio de followers de todos los usuarios: {promedio_followers:.2f}")

    return promedio_followers


def ordenar_por_nombre_y_guardar(lista):
    """
    Ordena los datos por nombre de usuario ascendente y guarda el listado ordenado en un archivo JSON.

    Args:
    - lista (list): Lista de diccionarios representando a los usuarios, donde cada diccionario tiene la clave 'user'.
    """
    # Ordenar la lista por nombre de usuario ascendente
    lista_ordenada = sorted(lista, key=lambda x: x["user"])

    # Guardar la lista ordenada en un archivo JSON
    nombre_archivo = "usuarios_ordenados_por_nombre.json"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista_ordenada, archivo, indent=4, ensure_ascii=False)

    print(f"Se han guardado los usuarios ordenados por nombre en '{nombre_archivo}'.")

def imprimir_usuario_con_mas_likes(lista):
    """
    Imprime al usuario con más likes de la lista proporcionada.

    Args:
    - lista (list): Lista de diccionarios donde cada diccionario representa a un usuario.

    Returns:
    - dict: Diccionario del usuario con más likes.
    """
    if not lista:
        print("La lista de usuarios está vacía.")
        return None

    # Inicializamos variables para el seguimiento del usuario con más likes
    max_likes = -1
    usuario_con_mas_likes = None

    # Iteramos sobre cada usuario en la lista
    for usuario in lista:
        if usuario['likes'] > max_likes:
            max_likes = usuario['likes']
            usuario_con_mas_likes = usuario

    if usuario_con_mas_likes:
        print(f"Usuario con más likes:")
        print(f"Nombre de usuario: {usuario_con_mas_likes['user']}")
        print(f"Likes: {usuario_con_mas_likes['likes']}")
        print("------------------------")
        return usuario_con_mas_likes
    else:
        print("No se encontró ningún usuario con likes en la lista.")
        return None




