import time
import random

numeros0 = [random.randint(1, 1000000) for i in range(1000)]
numeros1 = [random.randint(1, 1000000) for i in range(10000)]
numeros2 = [random.randint(1, 1000000) for i in range(100000)]
numeros3 = [random.randint(1, 1000000) for i in range(1000000)]
numeros4 = [random.randint(1, 1000000) for i in range(10000000)]
numeros = [numeros0,numeros1,numeros2,numeros3,numeros4]

def max_manual(lista):
    if not lista:                   #1
        return None                 #1
    maximo = lista[0]               #1
    for numero in lista:            #2N                  T(n)= 1+1+1+1+(2N) = 4+(2*n)
        if numero > maximo:         #1 
            maximo = numero         #1
    return maximo                   #1 

def max_auto(lista):
    if not lista:                     #1                  T(n)= 1+1+1 = 3
        return None                   #1
    return max(lista)                 #1

print("Resultados de busqueda automatica")

for i in range(5):
    inicio = time.time()
    maximo_auto = max_auto(numeros[i])
    tiempo = time.time() - inicio
    print(f"{10**(i+3)} {tiempo:.10f}")

print("Resultados de busqueda manual")
    
for i in range(5):
    inicio = time.time()
    maximo_manual = max_manual(numeros[i])
    tiempo = time.time() - inicio
    print(f"{10**(i+3)} {tiempo:.10f}")
