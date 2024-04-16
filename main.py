import numpy as np
from random import randint, random


def gen_distances():
    # distances = [[0, 5, 14, 30],
    #              [5, 0, 10, 9],
    #              [14, 10, 0, 20],
    #              [30, 9, 20, 0], ]

    distances = [[0, 25, 45, 17, 86, 52, 1, 97, 4, 36, 34, 29, 35, 46, 18],
                 [25, 0, 22, 5, 79, 28, 2, 78, 70, 53, 12, 28, 6, 74, 20],
                 [45, 22, 0, 19, 60, 15, 41, 82, 4, 1, 56, 10, 10, 87, 24],
                 [17, 5, 19, 0, 87, 96, 68, 33, 51, 93, 51, 63, 95, 1, 46],
                 [86, 79, 60, 87, 0, 95, 92, 8, 58, 57, 30, 28, 23, 40, 39],
                 [52, 28, 15, 96, 95, 0, 36, 96, 84, 84, 84, 76, 60, 52, 87],
                 [1, 2, 41, 68, 92, 36, 0, 13, 36, 4, 80, 95, 41, 48, 25],
                 [97, 78, 82, 33, 8, 96, 13, 0, 20, 53, 8, 50, 75, 38, 22],
                 [4, 70, 4, 51, 58, 84, 36, 20, 0, 53, 63, 15, 70, 4, 63],
                 [36, 53, 1, 93, 57, 84, 4, 53, 53, 0, 41, 97, 87, 16, 80],
                 [34, 12, 56, 51, 30, 84, 80, 8, 63, 41, 0, 44, 70, 67, 83],
                 [29, 28, 10, 63, 28, 76, 95, 50, 15, 97, 44, 0, 23, 32, 84],
                 [35, 6, 10, 95, 23, 60, 41, 75, 70, 87, 70, 23, 0, 15, 99],
                 [46, 74, 87, 1, 40, 52, 48, 38, 4, 16, 67, 32, 15, 0, 45],
                 [18, 20, 24, 46, 39, 87, 25, 22, 63, 80, 83, 84, 99, 45, 0]]

    # for i in range(16):
    #     for j in range(16):

    # n = 15
    # distances = []

    # for i in range(0, n):
    #     fila = []
    #     for j in range(0,n):
    #         if i == j:
    #             fila.append(0)
    #         elif j < i: 
    #             fila.append(distances[j][i])
    #         else:
    #             fila.append(randint(1, 100))
    #     distances.append(fila)

    return distances


def gen_random_journey(length):
    cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    selected_cities = cities[1:length]
    random_journey = np.array(selected_cities)
    np.random.shuffle(random_journey)
    random_journey = np.insert(random_journey, 0, 'A')

    return random_journey


def fitness(journey, distances):
    cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    indexes = []

    for movement in journey:
        for i, city in enumerate(cities):
            if movement == city:
                indexes.append(i)

    distance = 0

    for i, index in enumerate(indexes):

        if i == len(indexes) - 1:
            distance += distances[i][indexes[0]]
        else:
            distance += distances[index][indexes[i + 1]]

    return distance


def crossover(first, second):
    crossover_point = randint(2, len(first) - 2)

    child1 = second.copy()
    child2 = first.copy()

    for i in range(crossover_point):
        for j, step in enumerate(child1):
            if step == first[i]:
                aux = child1[i]
                child1[i] = first[i]
                child1[j] = aux
                break

    for i in range(crossover_point):
        for j, step in enumerate(child2):
            if step == second[i]:
                aux = child2[i]
                child2[i] = second[i]
                child2[j] = aux
                break

    return child1, child2


def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probabilities = [fitness / total_fitness for fitness in fitness_values]
    cumulative_probabilities = [sum(selection_probabilities[:i + 1]) for i in range(len(selection_probabilities))]
    selected_parents = []
    for _ in range(2):
        random_value = randint(0, 1)
        for i, cumulative_probability in enumerate(cumulative_probabilities):
            if random_value <= cumulative_probability:
                selected_parents.append(population[i])
                break
    return selected_parents


def evolutionary_algorithm(population_size, num_cities, max_generations):
    distances = gen_distances()
    population = np.array([gen_random_journey(num_cities) for _ in range(population_size)])
    generation_number = 1
    new_population = []

    for gen in range(max_generations):
        fitness_values = [fitness(journey, distances) for journey in population]
        new_population = []
        index = fitness_values.index(min(fitness_values))
        new_population.append(population[index])
        while len(new_population) < round(population_size / 2):
            selected_parents = roulette_wheel_selection(population, fitness_values)
            new_population.append(selected_parents[0])
            new_population.append(selected_parents[1])
            child1, child2 = crossover(selected_parents[0], selected_parents[1])
            new_population.append(child1)
            new_population.append(child2)
        while len(new_population) < population_size:
            new_population.append(gen_random_journey(num_cities))

        new_population = np.array(new_population)
        population = new_population
        generation_number += 1

    index = fitness_values.index(min(fitness_values))
    print(f"The best fitness {min(fitness_values)}")
    print(f"The best individual {population[index]}")
    print(f"Number of generations: {generation_number}")


    # a = gen_random_journey(4)
    return population


def main():
    print(evolutionary_algorithm(10, 10, 100))


if __name__ == '__main__':
    main()
