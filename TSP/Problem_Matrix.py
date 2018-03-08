
import numpy as np
import random as rnd

class ProblemMatrix:
    city_matrix = None

    def __init__(self, size: int, longest: int):
        self.size = size
        self.longest = longest



    def Make_Matrix(self):
        city_weights = (self.size,self.size)
        city_weights = np.zeros(city_weights)
        for i in range(0,self.size):
            for j in range(self.size-1,0,-1):
                if i != j :
                    randWeighting = rnd.randint(1,self.longest)
                    city_weights[i][j] = randWeighting
                    city_weights[j][i] = randWeighting
        self.city_matrix = city_weights


