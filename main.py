from regineBacktracking import n_queens_backtracking
from Lee import lee_algorithm
from regineAlpinist import hill_climbing
from regineAlpinist import print_board
from comis_voiajor import comis_voiajor
from comis_voiajor import citeste_date_intrare
from calirea_simulata import cautare_simulata
from calirea_simulata import numar_conflicte
from execution_time import measure_time
from comis_voiajor_genetic import City
from comis_voiajor_genetic import comis_voiajor_genetic


def main():
    while True:
        print("Meniu:")
        print("1. ALG Lee (lab 1)")
        print("2. N Regine cu alpinist (lab 6)")
        print("3. Comis voiajor (lab 7)")
        print("4. N regine cu călire simulată (lab 8)")
        print("5. Comis voiajor algoritm genetic (lab 9)")
        print("6. Grafic cu variația timpului de execuție")
        print("7. Informații despre autor")
        print("8. Ieșire")

        option = input("Selectați o opțiune: ")

        if option == "1":
            matrix = [
                [0, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 1, 0]
            ]
            start = (0, 0)
            end = (3, 3)
            shortest_path = lee_algorithm(matrix, start, end)
            print(shortest_path)
        elif option == "2":
            solution = hill_climbing(8)
            print(solution)
            print_board(solution)
            solution = hill_climbing(16)
            print(solution)
            print_board(solution)
            solution = hill_climbing(32)
            print(solution)
            print_board(solution)
            solution = hill_climbing(64)
            print(solution)
            print_board(solution)
        elif option == "3":
            n, orase, distante, start = citeste_date_intrare('comis_voiajor_input1.txt')
            if n is not None:
             comis_voiajor(n, orase, distante, start)
            n, orase, distante, start = citeste_date_intrare('comis_voiajor_input2.txt')
            if n is not None:
             comis_voiajor(n, orase, distante, start)
            n, orase, distante, start = citeste_date_intrare('comis_voiajor_input3.txt')
            if n is not None:
             comis_voiajor(n, orase, distante, start)
        elif option == "4":
            n = int(input("Numarul pentru cautare simulata: "))
            stare_finala = cautare_simulata(n)
            print("Starea finală: ", stare_finala)
            print("Numărul de conflicte: ", numar_conflicte(stare_finala))
            n = int(input("Numarul pentru cautare simulata: "))
            stare_finala = cautare_simulata(n)
            print("Starea finală: ", stare_finala)
            print("Numărul de conflicte: ", numar_conflicte(stare_finala))
            n = int(input("Numarul pentru cautare simulata: "))
            stare_finala = cautare_simulata(n)
            print("Starea finală: ", stare_finala)
            print("Numărul de conflicte: ", numar_conflicte(stare_finala))
        elif option == "5":
            cities = [
                City(60, 200),
                City(180, 200),
                City(80, 180),
                City(140, 180),
                City(20, 160),
                City(100, 160),
                City(200, 160),
                City(140, 140),
                City(40, 120),
                City(100, 120),
                City(180, 100),
                City(60, 80),
                City(120, 80),
                City(180, 60),
                City(20, 40),
                City(100, 40),
                City(200, 40),
                City(20, 20),
                City(60, 20),
                City(160, 20)
            ]
            population_size = 100
            num_generations = 1000
            mutation_rate = 0.01
            best_tour = comis_voiajor_genetic(cities, population_size, num_generations, mutation_rate)
            best_tour.calculate_distance()
            print("Cea mai scurtă rută găsită:")
            for city in best_tour.cities:
                print(city.x, city.y)
            print("Distanta totala:", best_tour.distance)
        elif option == "6":
            n_values = [4, 8, 12]
            runs = 5
            results = []
            for n in n_values:
                results.append(measure_time(n, runs))
            backtracking_times = [0.0001, 0.0002, 0.004, 0.13, 3.61, 130.3]
            lee_times = [0.0002, 0.0002, 0.0003, 0.0006, 0.001, 0.002]
            hill_climbing_times = [0.0004, 0.003, 0.02, 0.15, 1.8, 22.6]
            n_values = [4, 6, 8, 10, 12, 14]
        elif option == "7":
            print("Dumitriu Beniamin grupa 3131B")
        elif option == "8":
            break
        else:
            print("Opțiune invalidă. Selectați din nou.")

if __name__ == "__main__":
    main()