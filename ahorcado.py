
import random
import os
import time
reset=""
numeros=["5","4","3","2","1"]
def game():
    juego =input("bienvenido al ahorcado \nSelecciona el juego dentro de las siguientes opciones: \n1-Animales\n2-comidas\n3-lenguajes de programacion\n4-colores \n5-ALEATORIO\n")



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
                for n in numeros:
                    print ("reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
                
                
                
            if attemps == 0:
                
                print ("Perdiste  govir")
                for n in numeros:
                    print ("Perdiste reinicia el juego en "+n)
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
                for n in numeros:
                    print ("reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
                
                
                
            if attemps == 0:
                
                print ("Perdiste  govir")
                for n in numeros:
                    print ("Perdiste reinicia el juego en "+n)
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
            "ELEFANTE",
            "JIRAFA",
            "RINOCERONTE",
            "LORO",
            "HIPOPOTAMO",
            "HIENA",
            "CONEJO",
            "TIGRE",
            "DODO"
            "GATO",
            "PAJARO",
            "PEZ",
            "LEON",
            "BALLENA",
            "PUMA",
            "MONO",
            ""
        
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
                for n in numeros:
                    print ("reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
                
                
                
            if attemps == 0:
                
                print ("Perdiste  govir")
                for n in numeros:
                    print ("Perdiste reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
    def leng():
        print ("ahorcado de lenguajes de programacion")
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
                for n in numeros:
                    print ("reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
                
                
                
            if attemps == 0:
                
                print ("Perdiste  govir")
                for n in numeros:
                    print ("Perdiste reinicia el juego en "+n)
                    time.sleep(1)
                    os.system("cls")
                game()
        
    
        
    XD=["1",
        "2",
        "3",
        "4"]  
    if reset =="r":
        game()
    if juego == "5":
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