from memory_profiler import profile
import tracemalloc

@profile
def crear_lista(n):
    lista = [i for i in range(n)]
    return lista

@profile
def crear_generador(n):
    for i in range(n):
        yield i

def medir_con_tracemalloc_lista(n):
    tracemalloc.start()
    lista = [i for i in range(n)]
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Lista - Memoria actual: {current / 10**6:.2f} MB; Pico: {peak / 10**6:.2f} MB")

def medir_con_tracemalloc_generador(n):
    tracemalloc.start()
    gen = (i for i in range(n))
    for _ in gen:
        pass
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Generador - Memoria actual: {current / 10**6:.2f} MB; Pico: {peak / 10**6:.2f} MB")

if __name__ == "__main__":
    n = 10**6
    # Medición de memoria con memory_profiler
    lista = crear_lista(n)
    gen = crear_generador(n)
    for _ in gen:
        pass

    # Medición de memoria con tracemalloc
    medir_con_tracemalloc_lista(n)
    medir_con_tracemalloc_generador(n)