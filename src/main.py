from src.genetic_algorithm_files.evolve_population import create_result
from src.genetic_algorithm_files.population import Population
from src.supporting_tools.create_dirs import create_dirs
from src.supporting_tools.problem_matrix import ProblemMatrix
from src.supporting_tools.random_permutation import random_permutation
from src.supporting_tools.see_salesman import plot_travels

# The variables that control the outputs #
RUN_TOTAL: int = 50
# Sets up a list of the number of the cities
NUMBER_OF_CITIES: int = 50
CITIES: list[int] = list(range(2, NUMBER_OF_CITIES + 1))
# Variables that control the population
POP_SIZE: int = 16
GENERATION: int = 1000
# Tracks the amount of completed runs on the algorithm
COUNT: int = 1
# Mutation Constant, the bigger this is the less likely mutation is to occur
MUTATION_CONSTANT: int = 100
# Creates initial Population
CURRENT_GENERATION: Population = Population(POP_SIZE, NUMBER_OF_CITIES)
# Saves the original values of the genes in order to reset them every-time
if isinstance(CURRENT_GENERATION.genes, list[list[int]]):
    FIRST_GENES = [i for i in CURRENT_GENERATION.genes]
# ------------------------------------------- #
# Decides which genetic controls will be used #
# ------------------------------------------- #
# Valid mutations are {swap, invert, displace, scramble, insert, No}
mutation: str = "invert"
# Valid Parent Algorithms are {rank, random}
parent_selection: str = "rank"
# Valid Crossover Algorithms are {partially mapped, order, cycle}
crossover: str = "No"
# Valid Selection Algorithms are {elitism, on_fitness}
selection: str = "elitism"
# set up the roads between the cities
longest_distance: int = 4
paver: ProblemMatrix = ProblemMatrix(NUMBER_OF_CITIES, longest_distance)
paver.road_rule: list = list(random_permutation(CITIES))
paver.make_matrix()
roads = paver.city_matrix
mutation_chance: float = NUMBER_OF_CITIES / (NUMBER_OF_CITIES * MUTATION_CONSTANT)
# Implements the Algorithm a certain number of times and Plots them on a graph
# Creates titles, based on genetic control variables
best_journeys = list()
best_graph_title = "Best of " + crossover + " crossover function with " + mutation + " mutation function"
average_journeys = list()
average_graph_title = "Average of " + crossover + " crossover function with " + mutation + " mutation function"
worst_journeys = list()
worst_graph_title = "Worst of " + crossover + " crossover function with " + mutation + " mutation function"
# Creates a directory for the outputted files
# dir_title = str(selection) + " " +  str(parent_selection) + " " + str(crossover) + " " + str(mutation)
dir_title = "Local Search"
create_dirs(dir_title)
for i in range(1, RUN_TOTAL + 1):
    title = "Run: " + str(i)
    # -------------------------------------------- #
    #          Sets up the Output File             #
    # -------------------------------------------- #
    output_title = "../Results/" + dir_title + "/Full Scores Of Population/Population Scores.Run " + str(i) + ".txt"
    output_file = open(output_title, "w")
    results = create_result(
        CURRENT_GENERATION,
        paver,
        GENERATION,
        crossover,
        parent_selection,
        selection,
        mutation,
        mutation_chance,
        output_file,
    )
    best_journeys.append([results[0], title])
    worst_journeys.append([results[1], title])
    average_journeys.append([results[2], title])
    output_file.close()
    # Displays the completed runs of the algorithm so the user doesn't get impatient
    print("completed \t" + str(COUNT))
    COUNT += 1
    # Reset the genes back to their original set
    CURRENT_GENERATION.genes = [i for i in FIRST_GENES]
# Plots Results of the Run Algorithm to a graph #
plot_travels(best_journeys, best_graph_title, dir_title)
plot_travels(worst_journeys, worst_graph_title, dir_title)
plot_travels(average_journeys, average_graph_title, dir_title)
# Displays the completed runs of the algorithm so the user doesn't get impatient
# Plots the average, worst and best population scores for each generation on the graph
for i in range(0, RUN_TOTAL):
    plot_travels(
        [best_journeys[i], worst_journeys[i], average_journeys[i]],
        "Run " + str(i + 1) + ", all stats",
        dir_title,
    )
