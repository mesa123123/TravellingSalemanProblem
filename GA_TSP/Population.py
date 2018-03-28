from GA_TSP import Random_Permutation
from TSP.Climb_Tools import distance_check
from TSP.Problem_Matrix import ProblemMatrix

class Population():
    population = None
    roads = None

    def __init__(self, number_of_cities,longest_road, population_size):
        paver = ProblemMatrix(number_of_cities+1,longest_road)
        paver.Make_Matrix()
        self.roads = paver.city_matrix
        cities = [x for x in range(2,number_of_cities+1)]
        x = [[0] for i in range(0,population_size)]
        y = Random_Permutation.send_all(cities)
        for i in range(0,len(x)):
                x[i].append(y[i])
        for gene in x:
              gene[0] = distance_check(gene[1],self.roads)
        self.population = x


    def crossover(self):
        pass