from Genetic_Algorithm_Files.Score_Pop import score_pop
from Genetic_Algorithm_Files.Selection import selection


def create_result(population, paver, generation, crossover, parent, select,
                  mutation=None, mutation_chance=0.1, output_file=None):
    roads = paver.city_matrix
    score_pop(population, roads)
    optimal_route = list()
    worst_route = list()
    average_of_population = list()
    optimal_route.append(population.genes[0][0])
    worst_route.append(population.genes[len(population.genes)-1][0])
    average_of_population.append(average_scores(population.genes))
    for i in range(0, generation):
        Person = selection(population, roads, crossover, parent, select, mutation, mutation_chance)
        # Attach the best, worst and population average their corresponding list
        optimal_route.append(Person.genes[0][0])
        worst_route.append(Person.genes[len(Person.genes)-1][0])
        average_of_population.append(average_scores(Person.genes))
    # if we want to output the results to a file
    if output_file != None:
        print_to_file(output_file, optimal_route, worst_route, average_of_population, generation)
    return [optimal_route, worst_route, average_of_population]


def print_to_file(output_file, optimal_route, worst_route, average_of_population, generation):
    output_file.write("Best: ")
    for i in range(0, generation):
        output_file.write('{}, '.format(optimal_route[i]))
    output_file.write('\n-----------------------------------------------------------------------------------\n')
    output_file.write("Worst: ")
    for i in range(0, generation):
        output_file.write('{}, '.format(worst_route[i]))
    output_file.write('\n-----------------------------------------------------------------------------------\n')
    output_file.write("Average: ")
    for i in range(0, generation):
        output_file.write('{}, '.format(average_of_population[i]))
    output_file.write('\n-----------------------------------------------------------------------------------\n')


def average_scores(genes):
    gene_total = 0
    for i in range(0,len(genes)):
        gene_total += genes[i][0]
    return gene_total/len(genes)