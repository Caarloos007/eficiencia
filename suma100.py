import time
import random
import timeit

def medir_tiempo_suma():
    lista = [random.randint(1, 5000) for _ in range(5000)] 
    start_time = time.time()
    suma = sum(lista)
    end_time = time.time()
    print("Tiempo transcurrido con time.time():", end_time - start_time)
    print("Suma:", suma)
    return lista

def suma_lista(lista):
    return sum(lista)

# Medición con time.time()
lista = medir_tiempo_suma()

# Medición con timeit
tiempo_timeit = timeit.timeit(lambda: suma_lista(lista), number=1)
print("Tiempo transcurrido con timeit:", tiempo_timeit)