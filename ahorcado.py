
import  random
import os
        
        
juego =input("bienvenido al ahorcado \nSelecciona el juego dentro de las siguientes opciones: \n1-Animales\n2-comidas\n3-lenguajes de programacion\n4-colores \n")


def col():
    
    IMAGES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
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
        "AZUL",
        "ROJO",
       "VERDE",
       "AMARILLO",
        "VIOLETA"    ]
    word= random.choice(DB)
    spaces=["_"]*len(word)
    attemps=6
    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attemps])
        letter = input("elije una letra:   \n").upper()
        
        found = False
        for idx,character in enumerate(word):
            if character == letter:
                spaces[idx]=letter
                found = True
        if not found:
            attemps-=1
        if "_" not in spaces:
            os.system("cls")
            print ("GANASTE! LA PALABRA ERA: "+ word)
            
            
            
            break
            
            
        if attemps == 0:
            os.system("cls")
            print ("Perdiste  govir")
            break

def comi():
    
    IMAGES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
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
    ]
    word= random.choice(DB)
    spaces=["_"]*len(word)
    attemps=6
    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attemps])
        letter = input("elije una letra:   \n").upper()
        
        found = False
        for idx,character in enumerate(word):
            if character == letter:
                spaces[idx]=letter
                found = True
        if not found:
            attemps-=1
        if "_" not in spaces:
            os.system("cls")
            print ("GANASTE! LA PALABRA ERA: "+ word)
            
            
            
            break
            
            
        if attemps == 0:
            os.system("cls")
            print ("Perdiste  govir")
            break

def anim():
    
    IMAGES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
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
        "PERRO",
        "GATO",
       "PAJARO",
       "PEZ",
       "LEON",
    ]
    word= random.choice(DB)
    spaces=["_"]*len(word)
    attemps=6
    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attemps])
        letter = input("elije una letra:   \n").upper()
        
        found = False
        for idx,character in enumerate(word):
            if character == letter:
                spaces[idx]=letter
                found = True
        if not found:
            attemps-=1
        if "_" not in spaces:
            os.system("cls")
            print ("GANASTE! LA PALABRA ERA: "+ word)
            
            
            
            break
            
            
        if attemps == 0:
            os.system("cls")
            print ("Perdiste govir")
            break

def leng():
    
    IMAGES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
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
        letter = input("elije una letra:   \n").upper()
        
        found = False
        for idx,character in enumerate(word):
            if character == letter:
                spaces[idx]=letter
                found = True
        if not found:
            attemps-=1
        if "_" not in spaces:
            os.system("cls")
            print ("GANASTE! LA PALABRA ERA: "+ word)
            
            
            
            break
            
            
        if attemps == 0:
            os.system("cls")
            print ("Perdiste govir")
            break
        
    
         
            
if juego == "1":
    anim()
if juego == "2":
    comi()
if juego == "3":
    leng()
if juego == "4":
    col()