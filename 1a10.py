import time
import timeit

# Medición con time.time()
start_time = time.time()
for i in range(1, 11):
    print(i)
    time.sleep(1)
end_time = time.time()
print("Tiempo transcurrido con time.time():", end_time - start_time)

# Medición con timeit (sin print para evitar interferencias)
def contar_con_sleep():
    for i in range(1, 11):
        time.sleep(1)

tiempo_timeit = timeit.timeit(contar_con_sleep, number=1)
print("Tiempo transcurrido con timeit:", tiempo_timeit)