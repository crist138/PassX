import json
import os
import time
import bcrypt
from colorama import init, Fore, Style

usuarios = {}

def loadUsers():
    global usuarios
    try:
        if os.path.exists("./info.json"):
            with open("./info.json", "r") as f:
                usuarios = json.load(f)
    except FileNotFoundError:
        print("El archivo no existe")
    except FileExistsError:
        print("Ocurrio un error con el archivo")
    except:
        print("Ocurrio un error con el programa")


def createUser(): # Create user and password
    while True:
        user = input(Fore.GREEN+"Dame el usuario: ")
        if user is not usuarios:
            break
        else: 
            print("Ese usuario ya existe, intenta de nuevo")
    
        password = input((Fore.BLUE+"Dame la contraseñas: ")).encode('utf-8') # Passing to Bytes for using the bcrypt functions
        
        salt = bcrypt.gensalt() # Generate salt
        
        hashed = bcrypt.hashpw(password, salt)
        hashed_hex = hashed.hex()
        
        while True:
            passwordVerify = input((Fore.BLUE+"Ingresa la contraseña de nuevo: ")).encode('utf-8')
            
            if bcrypt.checkpw(passwordVerify, hashed):
                usuarios[user] = hashed_hex
                uploadUser()
                    
                print(Fore.GREEN+"Los datos se han guardado correctamente! ")
                break
            
            else:
                print(Fore.RED+"Los datos son incorrectos, intenta de nuevo")
                time.sleep(1.3)
                os.system("cls")
                print(Fore.GREEN+"Usuario: ", user)
                
   
def uploadUser():
    with open("./info.json", "w") as f:
        json.dump(usuarios, f, indent=4)
   
loadUsers()
createUser()