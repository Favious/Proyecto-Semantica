#python3 
import atexit 
from time import time, strftime, localtime 
from datetime import timedelta 
import sys

sys.setrecursionlimit(10**6)

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

def A(m, n, s="%s"): 
    # print (s % ("A(%d,%d)" % (m, n)) )
    if m == 0: 
     return n + 1 
    if n == 0: 
     return A(m - 1, 1, s) 
    n2 = A(m, n - 1, s % ("A(%d,%%s)" % (m - 1))) 
    return A(m - 1, n2, s) 

if __name__ == "__main__":
    
    print("FUNCION DE ACKERMANN")
    m = int(input('Ingrese el valor para m: '))
    n = int(input('Ingrese el valor para n: '))
    start = time()
    atexit.register(endlog) 
    log("Start Program")
    print('A(',m,',',n,')=',A(m,n))