#python3

import sys
import atexit 
from time import time, strftime, localtime 
from datetime import timedelta 


def secondsToStr(elapsed=None): 
    if elapsed is None: 
     return strftime("%Y-%m-%d %H:%M:%S", localtime()) 
    else: 
     return str(timedelta(seconds=elapsed)) 

def log(s, elapsed=None): 
    line = "="*40 
    print(line) 
    print(secondsToStr(), '-', s) 
    if elapsed: 
     print("Elapsed time:", elapsed) 
    print(line) 
    print() 

def endlog(): 
    end = time() 
    elapsed = end-start 
    log("End Program", secondsToStr(elapsed)) 

def triangle_pascal(rows):
    # creamos una lista que contendra los dos primeras lineas
    lista = [[1],[1,1]]
 
    # bucle que se generara tantas veces como lineas vayamos a tener
    for i in range(1,rows-1):
 
        # inicializamos la linea
        linea = [1]
 
        # bucle por cada uno de los valores de la anterior linea
        for j in range(0,len(lista[i])-1):
 
            # añadimos a la lista los nuevos valores
            # sumamos el valor de la lista anterior con el siguinte
            linea.extend([ lista[i][j] + lista[i][j+1] ])
 
        # añadimos el ultimo valor a la nueva linea
        # siempre es un 1 igual que el primero
        linea += [1]
 
        # añadimos la linea a la lista
        lista.append(linea)
 
    #devolvemos la lista ya creada
    return lista


if __name__ == "__main__":
    
    rows= int(input('tamaño del triangulo: '))
    start = time()
    atexit.register(endlog) 
    log("Start Program")
    for x in triangle_pascal(rows):
        print (x)
 