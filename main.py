import random

def anagrama(palabra):
    lista1 = list(palabra)
    indx = len(palabra)-1
    i = 0
    palabraf = ""
    
    while i < indx:
        randindx = random.randrange(i, indx+1)
        palabraf += lista1[randindx]
        del lista1[randindx]
        indx = indx - 1
        
    palabraf += lista1[i]
        
    return palabraf

def selectRandomWord(archivo):
    f = open(archivo, "r")
    listapal = []
    for pal in f:
        listapal.append(pal.strip())
    f.close()

    return listapal[random.randrange(0, len(listapal))]

def chequeo(palorig, pal2):
    while pal2 != palorig:
        print("No es esa palabra, escriba de nuevo")
        pal2 = input("")
    
    print("La palabra es correcta, buen trabajo :)")

    
archivo = "wordlist.txt"
palabraDesordenar = selectRandomWord(archivo)
palabraOriginal = palabraDesordenar
palabraObtenida = anagrama(palabraDesordenar)
print(palabraObtenida)

paluser = input("Introduzca la palabra que representa: ")

chequeo(palabraOriginal, paluser)
