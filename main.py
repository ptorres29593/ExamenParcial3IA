import numpy as np
from random import randint

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

#Original Pablo
#def gen_random_journey(length):
    #cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              #'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    #selected_cities = cities[:length]
    #random_journey = np.array(selected_cities)
    #np.random.shuffle(random_journey)

    #return random_journey

def gen_random_journey(length):
    # Define la lista de ciudades excluyendo 'A'
    cities = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Agrega 'A' como la primera ciudad en la lista de ciudades seleccionadas
    selected_cities = ['A'] + cities[:length - 1]

    # Convierte la lista de ciudades seleccionadas en un array de NumPy
    random_journey = np.array(selected_cities)

    # Mezcla aleatoriamente el orden de las ciudades en el recorrido
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


import numpy as np  # Importa la librería NumPy bajo el alias np

def crossover(parent1, parent2):
    # Crear un mapeo para rastrear qué letras han sido seleccionadas en cada hijo
    child1_mapping = {}  # Inicializa un diccionario para el hijo 1
    child2_mapping = {}  # Inicializa un diccionario para el hijo 2

    child1 = []  # Inicializa una lista para el hijo 1
    child2 = []  # Inicializa una lista para el hijo 2

    for gene1, gene2 in zip(parent1, parent2):  # Itera sobre los genes de los padres
        # Agregar genes de los padres al hijo sin repetición de letras
        if gene1 not in child1_mapping:  # Verifica si el gen no está en el mapeo del hijo 1
            child1.append(gene1)  # Agrega el gen al hijo 1
            child1_mapping[gene1] = True  # Agrega el gen al mapeo del hijo 1
        if gene2 not in child2_mapping:  # Verifica si el gen no está en el mapeo del hijo 2
            child2.append(gene2)  # Agrega el gen al hijo 2
            child2_mapping[gene2] = True  # Agrega el gen al mapeo del hijo 2

    # Completar los hijos con las letras faltantes de los padres en el orden en que aparecen
    for gene1, gene2 in zip(parent1, parent2):  # Itera sobre los genes de los padres nuevamente
        if gene1 not in child1:  # Verifica si el gen no está en el hijo 1
            child1.append(gene1)  # Agrega el gen al hijo 1
        if gene2 not in child2:  # Verifica si el gen no está en el hijo 2
            child2.append(gene2)  # Agrega el gen al hijo 2

    return np.array(child1), np.array(child2)  # Devuelve los hijos como arrays de NumPy



#def evolutionary_algorithm(population_size, num_cities):
    #distances = gen_distances()
    #population = np.array([gen_random_journey(num_cities) for _ in range(population_size)])
    # a = gen_random_journey(4)
    #return population

def evolutionary_algorithm(population_size, num_cities):
    # Generar las distancias entre las ciudades
    distances = gen_distances()

    # Inicializar la población aleatoria
    population = np.array([gen_random_journey(num_cities) for _ in range(population_size)])

    # Iterar sobre las generaciones del algoritmo evolutivo
    for generation in range(num_generations):
        new_population = []  # Lista para almacenar la nueva población

        # Generar nuevos individuos para la próxima generación
        for _ in range(population_size // 2):
            # Seleccionar dos padres de la población actual
            parent1, parent2 = select_parents(population)

            # Aplicar el crossover para generar dos hijos
            child1, child2 = crossover(parent1, parent2)

            # Agregar los hijos a la nueva población
            new_population.extend([child1, child2])

        # Actualizar la población con la nueva generación
        population = np.array(new_population)

    return population


if __name__ == '__main__':
    #    print(evolutionary_algorithm(10, 15))
    sjourney = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    print(fitness(sjourney, gen_distances()))
