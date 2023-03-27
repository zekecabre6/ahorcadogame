from tkinter import*
from unittest import result
import random
import os
import time

reset=""
numeros=["5","4","3","2","1"]
def game():
    juego =input("bienvenido al ahorcado \nSelecciona el juego dentro de las siguientes opciones: \n1-Animales\n2-comidas\n3-lenguajes de programacion\n4-colores \n5 o enter-ALEATORIO\n")



    def col():
        IMAGES = ['''
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========''', '''
Te queda un ultimo intento! 
      cuidado!
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========''', '''
        +---+
        |   |
        O   |
        /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
         +---+
         |   |
         O   |
             |
             |
             |
        =========''', '''
         +---+
         |   |
             | 
             |
             |
             |
        =========''']

        DB=["NEGRO",
            "AZUL",
            "MARRON",
            "GRIS",
            "VERDE",
            "NARANJA",
            "ROSA",
            "PURPURA",
            "ROJO",
            "BLANCO",
            "AMARILLO"]
        word= random.choice(DB)
        spaces=["_"]*len(word)
        attemps=6
        while True:
            os.system("cls")
            for character in spaces:
                print(character, end=" ")
            print(IMAGES[attemps])
            letter = input("colores\nElije una letra:   \n").upper()
        
            found = False
            for idx,character in enumerate(word):
                if character == letter:
                    spaces[idx]=letter
                    found = True
            if not found:
                attemps-=1
            if "_" not in spaces:
                print ("GANASTE! LA PALABRA ERA: "+ word)
                time.sleep(2)
                for n in numeros:
                    print ("reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
                
                
                
            if attemps == 0:
                
                print ("Perdiste  :( )")
                time.sleep(2)
                for n in numeros:
                    print ("Perdiste "+ "la palabra era ",word + " reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
                    

            
    def comi():
        IMAGES = ['''
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========''', '''
Te queda un ultimo intento! 
      cuidado!
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========''', '''
        +---+
        |   |
        O   |
        /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
         +---+
         |   |
         O   |
             |
             |
             |
        =========''', '''
         +---+
         |   |
             | 
             |
             |
             |
        =========''']

        DB=[
            "ARROZ",
            "POLLO",
            "MILANESAS",
            "GUISO",
            "ASADO",
            "HAMBURGUESA",
            "PANCHO",
            "PIZZA",
            "CANELONES",
            "SORRENTINOS",
            "FIDEOS",
            "SUSHI",
            "PAELLA",
            "RATATUILLE",
            "EMPANADA",
            "ESTOFADO",
            "ENSALADA",
            "ESPAGUETTI",
            "LANGOSTINOS",
            "PURE"
        ]
        word= random.choice(DB)
        spaces=["_"]*len(word)
        attemps=6
        while True:
            os.system("cls")
            for character in spaces:
                print(character, end=" ")
            print(IMAGES[attemps])
            letter = input("comidas\nElije una letra:   \n").upper()
            
            found = False
            for idx,character in enumerate(word):
                if character == letter:
                    spaces[idx]=letter
                    found = True
            if not found:
                attemps-=1
            if "_" not in spaces:
                print ("GANASTE! LA PALABRA ERA: "+ word)
                time.sleep(2)
                for n in numeros:
                    print ("reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
                
                
                
            if attemps == 0:
                
                print ("Perdiste  govir")
                time.sleep(2)
                for n in numeros:
                    print ("Perdiste "+ "la palabra era ",word + " reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
    def anim():
        IMAGES = ['''
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========''', '''
Te queda un ultimo intento! 
      cuidado!
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========''', '''
        +---+
        |   |
        O   |
        /|  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
         +---+
         |   |
         O   |
             |
             |
             |
        =========''', '''
         +---+
         |   |
             | 
             |
             |
             |
        =========''']

        DB=[
            "PERRO",
            "ELEFANTE",
            "JIRAFA",
            "RINOCERONTE",
            "LORO",
            "HIPOPOTAMO",
            "HIENA",
            "CONEJO",
            "TIGRE",
            "DODO",
            "GATO",
            "PAJARO",
            "PEZ",
            "LEON",
            "BALLENA",
            "PUMA",
            "MONO",
        
        ]
        word= random.choice(DB)
        spaces=["_"]*len(word)
        attemps=6
        while True:
            os.system("cls")
            for character in spaces:
                print(character, end=" ")
            print(IMAGES[attemps])
            letter = input("animales\nElije una letra:   \n").upper()
            
            found = False
            for idx,character in enumerate(word):
                if character == letter:
                    spaces[idx]=letter
                    found = True
            if not found:
                attemps-=1
            if "_" not in spaces:
                print ("GANASTE! LA PALABRA ERA: "+ word)
                time.sleep(2)
                for n in numeros:
                    print ("reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
                
                
                
            if attemps == 0:
                
                print ("Perdiste  govir")
                time.sleep(2)
                for n in numeros:
                    print ("Perdiste "+ "la palabra era ",word + " reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
    def leng():
        IMAGES = ['''
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========''', '''
Te queda un ultimo intento! 
      cuidado!
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========''', '''
        +---+
        |   |
        O   |
        /|  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
         +---+
         |   |
         O   |
             |
             |
             |
        =========''', '''
         +---+
         |   |
             | 
             |
             |
             |
        =========''']

        DB=[
            "C",
            "PYTHON",
            "JAVASCRIPT",
            "JAVA",
            "PHP",
        ]
        word= random.choice(DB)
        spaces=["_"]*len(word)
        attemps=6
        while True:
            os.system("cls")
            for character in spaces:
                print(character, end=" ")
            print(IMAGES[attemps])
            letter = input("lenguajes de programacion\nElije una letra:   \n").upper()
            
            found = False
            for idx,character in enumerate(word):
                if character == letter:
                    spaces[idx]=letter
                    found = True
            if not found:
                attemps-=1
            if "_" not in spaces:
                print ("GANASTE! LA PALABRA ERA: "+ word)
                time.sleep(2)
                for n in numeros:
                    print ("reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
                
                
                
            if attemps == 0:
                
                print ("Perdiste  govir")
                time.sleep(2)
                for n in numeros:
                    print ("Perdiste "+ "la palabra era ",word + " reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
        
    
        
    XD=["1",
        "2",
        "3",
        "4"]  
    
    if juego == "5":
        juego=random.choice(XD)  
    if juego == "":
        juego=random.choice(XD) 
            
    if juego == "1":
        anim()

    if juego == "2":
        comi()

    if juego == "3":
        leng()

    if juego == "4":
        col()

game()



