from funcion import *
import os

#funcion para borrar la pantalla al continuar
def clear_screen():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')  

# Función para mostrar el menú
def menu():
    print("Menu:")
    print("1. cargar archivo")
    print("2. imprimir lista de usuarios")
    print("3. asignar likes, dislikes y falowers a los usuarios")
    print("4. cargar un archivo con usuarios con mas de 2000 likes ")
    print("5. filtrar por usuarios con mas haters")
    print("6. informar promedio de followers")
    print("7. guardar de forma ascendente los nombres en un .json")
    print("8. informar el usurio con mas likes")
    print("9. cerrar el programa")

    opcion = input("Opción: ")
    return opcion

# Función principal del programa
while True:
    clear_screen()
    opcion = menu()

    if opcion == "1":
        cargar_archivo()
    elif opcion == "2":
        for usuario in lista:
            print(usuario)
    elif opcion == "3":
        asignar_likes(usuario)
    elif opcion == "4":
        filtrar_por_likes()
    elif opcion == "5":
        filtrar_por_haters()
    elif opcion == "6":
        calcular_promedio_followers(lista)
    elif opcion == "7":
        ordenar_por_nombre_y_guardar(lista)
    elif opcion == "8":
        imprimir_usuario_con_mas_likes(lista)
    elif opcion == "9":
        print("cerrar el programa")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    input("Presione Enter para continuar...")