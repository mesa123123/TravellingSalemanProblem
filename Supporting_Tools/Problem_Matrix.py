import numpy as np
import random as rnd
from Supporting_Tools.Random_Permutation import random_permutation
from os.path import exists

class ProblemMatrix:
    city_matrix = None
    road_rule = None
    size = None
    longest = None

    def __init__(self, size: int, longest: int):
        self.size = size + 1
        self.longest = longest
        cities_model = [x for x in range(2, size)]
        self.road_rule = random_permutation(cities_model)

    def make_matrix(self):
        matrix_file_name = "Roads " + str(self.size) + " " + str(self.longest) + ".txt"
        if not exists(matrix_file_name):
            city_weights = (self.size, self.size)
            city_weights = np.zeros(city_weights)
            for i in range(0, self.size):
                for j in range(self.size-1, 0, -1):
                    if i != j:
                        rand_weighting = round(rnd.uniform(1, self.longest), 3)
                        city_weights[i][j] = rand_weighting
                        city_weights[j][i] = rand_weighting
            self.city_matrix = city_weights
            with open(matrix_file_name, 'w') as matrix_file:
                for line in self.city_matrix:
                    for distance in line:
                        matrix_file.write(str(distance) + " ")
                    matrix_file.write("\n")
            matrix_file.close()
        else:
            with open(matrix_file_name) as matrix_file:
                content = matrix_file.readlines()
            content = [item.split() for item in content]
            for i in range(0, len(content)):
                for j in range(0, len(content[i])):
                    content[i][j] = float(content[i][j])
            self.city_matrix = content
