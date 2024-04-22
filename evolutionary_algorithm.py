import numpy as np
from random import randint, random


def gen_distances():
    # distances = [[0, 5, 14, 30],
    #              [5, 0, 10, 9],
    #              [14, 10, 0, 20],
    #              [30, 9, 20, 0], ]

    distances = [[0, 427, 619, 174, 593, 365, 358, 440, 348, 491, 368, 514, 576, 466, 422],
                 [427, 0, 390, 253, 320, 283, 72, 383, 365, 124, 188, 187, 182, 240, 161],
                 [619, 390, 0, 498, 79, 254, 389, 219, 729, 499, 272, 207, 512, 169, 246],
                 [174, 253, 498, 0, 457, 264, 185, 365, 282, 323, 228, 358, 407, 332, 271],
                 [593, 320, 79, 457, 0, 240, 328, 240, 670, 425, 230, 133, 434, 127, 191],
                 [365, 283, 254, 264, 240, 0, 237, 109, 531, 407, 95, 215, 461, 125, 142],
                 [358, 72, 389, 185, 328, 237, 0, 343, 342, 178, 146, 204, 248, 225, 144],
                 [440, 383, 219, 365, 240, 109, 343, 0, 637, 507, 197, 273, 554, 172, 228],
                 [348, 365, 729, 282, 670, 531, 342, 637, 0, 326, 466, 543, 399, 561, 482],
                 [491, 124, 499, 323, 425, 407, 178, 507, 326, 0, 312, 293, 86, 360, 284],
                 [368, 188, 272, 228, 230, 95, 146, 197, 466, 312, 0, 152, 366, 104, 61],
                 [514, 187, 207, 358, 133, 215, 204, 273, 543, 293, 152, 0, 310, 101, 93],
                 [576, 182, 512, 407, 434, 461, 248, 554, 399, 86, 366, 310, 0, 394, 326],
                 [466, 240, 169, 332, 127, 125, 225, 172, 561, 360, 104, 101, 394, 0, 82],
                 [422, 161, 246, 271, 191, 142, 144, 228, 482, 284, 61, 93, 326, 82, 0]]

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


def mutate(offspring, mutation_rate):
    if random() < mutation_rate:
        index_a = randint(1, len(offspring) - 1)
        index_b = randint(1, len(offspring) - 1)
        while index_b == index_a:
            index_b = randint(1, len(offspring) - 1)
        aux = offspring[index_b]
        offspring[index_b] = offspring[index_a]
        offspring[index_a] = aux
    return offspring


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


def evolutionary_algorithm(population_size, num_cities, max_generations, inicial_population):
    distances = gen_distances()
    if len(inicial_population) == 1:
        population = np.array([gen_random_journey(num_cities) for _ in range(population_size)])
    else:
        population = inicial_population
    generation_number = 1
    new_population = []

    for gen in range(max_generations):
        fitness_values = [fitness(journey, distances) for journey in population]
        new_population = []
        index = fitness_values.index(min(fitness_values))
        new_population.append(population[index])
        while len(new_population) < round(population_size*(2 / 3)):
            selected_parents = roulette_wheel_selection(population, fitness_values)
            new_population.append(selected_parents[0])
            new_population.append(selected_parents[1])
            child1, child2 = crossover(selected_parents[0], selected_parents[1])
            child1 = mutate(child1, mutation_rate=0.5)
            child2 = mutate(child2, mutation_rate=0.5)
            new_population.append(child1)
            new_population.append(child2)
        while len(new_population) < population_size:
            new_population.append(gen_random_journey(num_cities))

        new_population = np.array(new_population)
        population = new_population
        generation_number += 1

    index = fitness_values.index(min(fitness_values))
    # print(f"The best fitness {min(fitness_values)}")
    # print(f"The best individual {population[index]}")
    # print(f"Number of generations: {generation_number}")

    # a = gen_random_journey(4)
    return population[index], population, min(fitness_values)
