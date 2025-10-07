from memory_profiler import profile

@profile
def crear_lista(n):
    lista = [i for i in range(n)]
    return lista

@profile
def crear_generador(n):
    for i in range(n):
        yield i

if __name__ == "__main__":
    n = 10**6  
    # Medición de memoria con lista
    lista = crear_lista(n)
    # Medición de memoria con generador
    gen = crear_generador(n)
    for _ in gen:
        pass