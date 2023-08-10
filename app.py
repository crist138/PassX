import time
import json
import os
from colorama import init, Fore, Style
from Funciones.new_user import *

data = {}
data['user'] = []
data['usuarios'] = []


title = """
██████╗░░█████╗░░██████╗░██████╗  ██╗░░██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝  ╚██╗██╔╝
██████╔╝███████║╚█████╗░╚█████╗░  ░╚███╔╝░
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗  ░██╔██╗░
██║░░░░░██║░░██║██████╔╝██████╔╝  ██╔╝╚██╗
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚═╝░░╚═╝
"""

title_blue = Fore.BLUE + title


def menu():
    while True:
            print(title_blue)
            print("Que deseas hacer: ")
            option = int(input("1.- Guardar datos: \n2.- Actualizar datos\n3.- Borrar datos\n"))
            choiceOption(option)
            

def choiceOption(option):
    if option == 1:
        os.system("cls")
        createUser()
    
    
def cargando():
    statusLoad = ["|", "/", "-", "\\"]
    
    for _ in range(4):
        for status in statusLoad:
            
            print(f"Cargando {status}", end="\r")
            time.sleep(0.2)
        
    print("Listo!", end="\r")
    time.sleep(1)
    os.system("cls")
    
archivo = "info.json"

if os.path.exists(archivo):
    menu()
else:
    print("No tienes el archivo para acceder, a continuacion se creara")
    time.sleep(3)
    os.system("cls")
    cargando()
    
    # Creacion de contraseña en caso de no tener el archivo 
    password = input("Crea una nueva contraseña: ")
    data['user'].append({
        'password': password
    })

    with open("info.json", 'w') as f:
        print("El archivo ha sido creado")
        time.sleep(1)
        json.dump(data, f, indent=4)
        menu()
        