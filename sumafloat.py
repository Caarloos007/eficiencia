import time
import random
import timeit

def medir_tiempo_suma_float():
    lista = [random.uniform(1, 5000) for _ in range(5000)] 
    start_time = time.time()
    suma = sum(lista)
    end_time = time.time()
    print("Tiempo transcurrido con time.time():", end_time - start_time)
    print("Suma:", suma)
    return lista

def suma_lista_float(lista):
    return sum(lista)

# Medición con time.time()
lista = medir_tiempo_suma_float()

# Medición con timeit
tiempo_timeit = timeit.timeit(lambda: suma_lista_float(lista), number=1)
print("Tiempo transcurrido con timeit:", tiempo_timeit)