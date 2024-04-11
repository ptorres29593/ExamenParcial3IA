import numpy as np


def gen_distances():
    distances = [[0, 5, 14, 30],
                 [5, 0, 10, 9],
                 [14, 10, 0, 20],
                 [30, 9, 20, 0], ]

    # distances = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #               [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #               [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #               [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #               [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #               [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #               [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    #               [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    #               [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    #               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    #               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    #               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    #               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    #               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],]

    # for i in range(16):
    #     for j in range(16):

    return distances


def gen_random_journey(length):
    cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    selected_cities = cities[:length]
    random_journey = np.array(selected_cities)
    np.random.shuffle(random_journey)

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


def evolutionary_algorithm(population_size, num_cities):
    distances = gen_distances()
    population = np.array([gen_random_journey(num_cities) for _ in range(population_size)])
    # a = gen_random_journey(4)
    return population


if __name__ == '__main__':
    #    print(evolutionary_algorithm(10, 15))
    print(fitness(gen_random_journey(4), gen_distances()))
