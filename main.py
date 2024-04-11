import numpy as np

def gen_distances():
    distances = [[0, 5, 14, 30],
                 [5, 0, 10, 9],
                 [14, 10, 0, 20],
                 [30, 9, 20, 0], ]
    return distances

def gen_random_journey(num_cities):
    cities = ['A', 'B', 'C', 'D']
    selected_cities = cities[:num_cities]
    random_journey = np.array(selected_cities)
    np.random.shuffle(random_journey)
    return random_journey

def fitness(journey, distances, cities):
    total_distance = 0
    num_cities = len(journey)
    
    for i in range(num_cities - 1):
        city1 = journey[i]
        city2 = journey[i + 1]
        total_distance += distances[cities.index(city1)][cities.index(city2)]
    
    # Agregar la distancia desde la ultima ciudad de regreso a la primera
    city1 = journey[-1]
    city2 = journey[0]
    total_distance += distances[cities.index(city1)][cities.index(city2)]
    
    return total_distance

def evolutionary_algorithm(population_size, num_cities):
    distances = gen_distances()
    cities = ['A', 'B', 'C', 'D']
    population = np.array([gen_random_journey(num_cities) for _ in range(population_size)])
    for journey in population:
        print("Journey:", journey, "Fitness:", fitness(journey, distances, cities),"Km")
    return population

if __name__ == '__main__':
    evolutionary_algorithm(10, 4)