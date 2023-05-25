import random

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        dx = abs(self.x - city.x)
        dy = abs(self.y - city.y)
        return (dx ** 2 + dy ** 2) ** 0.5

class Tour:
    def __init__(self, cities):
        self.cities = cities
        self.distance = 0

    def calculate_distance(self):
        total_distance = 0
        num_cities = len(self.cities)
        for i in range(num_cities):
            from_city = self.cities[i]
            to_city = self.cities[(i + 1) % num_cities]
            total_distance += from_city.distance(to_city)
        self.distance = total_distance

    def swap_cities(self, i, j):
        self.cities[i], self.cities[j] = self.cities[j], self.cities[i]

class Population:
    def __init__(self, cities, population_size):
        self.cities = cities
        self.population_size = population_size
        self.tours = []

        for _ in range(population_size):
            tour = Tour(random.sample(cities, len(cities)))
            self.tours.append(tour)

    def sort_tours(self):
        self.tours.sort(key=lambda x: x.distance)

    def crossover(self, parent1, parent2):
        child = Tour(parent1.cities[:])
        start = random.randint(0, len(parent1.cities) - 1)
        end = random.randint(start + 1, len(parent1.cities))
        child.cities[start:end] = parent2.cities[start:end]

        missing_cities = [city for city in parent1.cities if city not in child.cities]
        for i in range(len(child.cities)):
            if child.cities[i] is None:
                child.cities[i] = missing_cities.pop(0)
        return child

    def mutate(self, tour, mutation_rate):
        for i in range(len(tour.cities)):
            if random.random() < mutation_rate:
                j = random.randint(0, len(tour.cities) - 1)
                tour.swap_cities(i, j)

def comis_voiajor_genetic(cities, population_size, num_generations, mutation_rate):
    population = Population(cities, population_size)
    best_tour = None

    for _ in range(num_generations):
        population.sort_tours()
        best_tour = population.tours[0]
        if best_tour.distance == 0:
            break

        new_population = Population(cities, population_size)
        new_population.tours[:population_size // 2] = population.tours[:population_size // 2]

        for i in range(population_size // 2, population_size):
            parent1 = random.choice(population.tours[:population_size // 2])
            parent2 = random.choice(population.tours[:population_size // 2])
            child = new_population.crossover(parent1, parent2)
            new_population.tours[i] = child

            new_population.mutate(child, mutation_rate)

        population = new_population

    return best_tour

def main():
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

if __name__ == "__main__":
    main()
