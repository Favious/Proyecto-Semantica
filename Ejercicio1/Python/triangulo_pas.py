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
    """Funcion que recibe como parametro el número de filas del triángulo"""
    #si el número de filas es cero devolvemos vacío.
    if rows == 0:
        return []
    #si el número de filas es 1, devolvemos triangulo con una sola fila.
    elif rows == 1:
        return [[1]]
    else:
        #de lo contrario armamos el triángulo segun el número de filas
        new_row = [1]
        #llamamos nuevamente a la función para armar el triángulo
        result = triangle_pascal(rows-1)
	#guardamos la última fila.
        last_row = result[-1]
	#iteramos la cantidad de veces del valor de filas - 1.
        for i in range(len(last_row)-1):
	    #agregamos los valores a la nueva fila.
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        #agregamos a la matriz del triángulo la nueva fila
        result.append(new_row)
	#devolvemos el array con los valores del triángulo.
    return result

if __name__ == "__main__":
    
    rows= int(input('tamaño del triangulo: '))
    start = time()
    atexit.register(endlog) 
    log("Start Program")
    for x in triangle_pascal(rows):
        print (x)