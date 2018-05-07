from Supporting_Tools import Problem_Matrix
from Supporting_Tools.See_Salesman import plot_travels
from Genetic_Algorithm_Files.Evolve_Population import *
from Genetic_Algorithm_Files.Population import Population
from Supporting_Tools.Random_Permutation import random_permutation
from Supporting_Tools import Create_Dirs
from Supporting_Tools import Route
from TSP.Climbs import steep_climb


# The variables that control the outputs #
run_total = 1
# Sets up a list of the number of the cities
number_of_cities = 50
cities = [x for x in range(2, number_of_cities+1)]
# Variables that control the population
pop_size = 16
generation = number_of_cities*20
# Mutation Constant, the bigger this is the less likely mutation is to occur
mutation_constant = 100
# Creates initial Population
Current_Generation = Population(pop_size, number_of_cities)
# Saves the original values of the genes in order to reset them every-time
First_Genes = [i for i in Current_Generation.genes]
# ------------------------------------------- #
# Decides which genetic controls will be used #
# ------------------------------------------- #
# Valid mutations are {swap, invert, displace, scramble, insert, None}
mutation = "invert"
# Valid Parent Algorithms are {rank, random}
parent_selection = "rank"
# Valid Crossover Algorithms are {partially mapped, order, cycle}
crossover = "order"
# Valid Selection Algorithms are {elitism, on_fitness}
selection = "elitism"
# set up the roads between the cities
longest_distance = 4
paver = Problem_Matrix.ProblemMatrix(number_of_cities, longest_distance)
paver.road_rule = list(random_permutation(cities))
paver.make_matrix()
roads = paver.city_matrix
mutation_chance = number_of_cities/(number_of_cities*mutation_constant)
# Implements the Algorithm a certain number of times and Plots them on a graph
# Creates titles, based on genetic control variables
best_journeys = list()
best_graph_title = "Best of " + crossover + " crossover function with " + mutation + " mutation function"
average_journeys = list()
average_graph_title = "Average of " + crossover + " crossover function with " + mutation + " mutation function"
worst_journeys = list()
worst_graph_title = "Worst of " + crossover + " crossover function with " + mutation + " mutation function"
# Creates a directory for the outputted files
#dir_title = str(selection) + " " +  str(parent_selection) + " " + str(crossover) + " " + str(mutation)
dir_title = "Local Search"
Create_Dirs.main(dir_title)
for i in range(1, run_total + 1):
    title = "Run: " + str(i)
    # -------------------------------------------- #
    #          Sets up the Output File             #
    # -------------------------------------------- #
    output_title = "../Results/" + dir_title + "/Full Scores Of Population/Population Scores.Run " \
                   + str(i) + ".txt"
    output_file = open(output_title, 'w')
    Climb_Route = Route.Route(cities, True, paver)
    # results = create_result(Current_Generation, paver, generation, crossover, parent_selection,
    #                               selection, mutation, mutation_chance, output_file)
    #
    # best_journeys.append([results[0], title])
    # worst_journeys.append([results[1], title])
    # average_journeys.append([results[2], title])
    output_file.write(str(steep_climb(20,Climb_Route.route,roads)))
    output_file.close()
    # Reset the genes back to their original set
#     Current_Generation.genes = [i for i in First_Genes]
# # Plots Results of the Run Algorithm to a graph #
# plot_travels(best_journeys, best_graph_title, dir_title)
# plot_travels(worst_journeys, worst_graph_title, dir_title)
# plot_travels(average_journeys, average_graph_title, dir_title)
# # Plots the average, worst and best population scores for each generation on the graph
# for i in range(0, run_total):
#     plot_travels([best_journeys[i], worst_journeys[i], average_journeys[i]], "Run " + str(i + 1) + ", all stats",
#                  dir_title)
#

