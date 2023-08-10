import os
import time
import bcrypt
from colorama import init, Fore, Style


def createUser(): # Create user and password
    user = input(Fore.GREEN+"Dame el usuario: ")
    password = input((Fore.BLUE+"Dame la contraseñas: ")).encode('utf-8') # Passing to Bytes for using the bcrypt functions
    
    salt = bcrypt.gensalt() # Generate salt
    
    hashed = bcrypt.hashpw(password, salt)
    
    while True:
        passwordVerify = input((Fore.BLUE+"Ingresa la contraseña de nuevo: ")).encode('utf-8')
        
        if bcrypt.checkpw(passwordVerify, hashed):
            print(Fore.GREEN+"Los datos se han guardado correctamente! ")
            break
        else:
            print(Fore.RED+"Los datos son incorrectos, intenta de nuevo")
            time.sleep(1.3)
            os.system("cls")
            print(Fore.GREEN+"Usuario: ", user)
            
    return hashed, user
   
createUser()