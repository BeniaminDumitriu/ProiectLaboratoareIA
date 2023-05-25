import time
from regineBacktracking import n_queens_backtracking
from regineLee import queens_lee
from regineAlpinist import hill_climbing

def measure_time(n, runs):
    times = []
    
    # Măsurăm timpul de execuție pentru algoritmul de backtracking
    total_time = 0
    for i in range(runs):
        start_time = time.time()
        n_queens_backtracking(n)
        end_time = time.time()
        total_time += end_time - start_time
    times.append(('Backtracking', total_time / runs))
    
    # Măsurăm timpul de execuție pentru algoritmul lui Lee
    total_time = 0
    for i in range(runs):
        start_time = time.time()
        queens_lee(n)
        end_time = time.time()
        total_time += end_time - start_time
    times.append(('Lee', total_time / runs))
    
    # Măsurăm timpul de execuție pentru algoritmul alpinistului
    total_time = 0
    for i in range(runs):
        start_time = time.time()
        hill_climbing(n)
        end_time = time.time()
        total_time += end_time - start_time
    times.append(('Hill Climbing', total_time / runs))
    
    return times

# Măsurăm timpul de execuție pentru dimensiunile de 4x4, 8x8, 12x12
n_values = [4, 8, 12]
runs = 5
results = []
for n in n_values:
    results.append(measure_time(n, runs))



# Datele pentru fiecare algoritm
backtracking_times = [0.0001, 0.0002, 0.004, 0.13, 3.61, 130.3]
lee_times = [0.0002, 0.0002, 0.0003, 0.0006, 0.001, 0.002]
hill_climbing_times = [0.0004, 0.003, 0.02, 0.15, 1.8, 22.6]

# Dimensiunile tablei de șah
n_values = [4, 6, 8, 10, 12, 14]