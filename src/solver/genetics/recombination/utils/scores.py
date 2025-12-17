# Completes a partially mapped crossover
import random as rnd

from solver.genetics.types import RoutePopulation


def random_recombination_score_method(population: RoutePopulation) -> RoutePopulation:
    population.routes.sort(key=lambda d: d.route_score)
    return population


def ranked_recombination_score_method(population: RoutePopulation) -> RoutePopulation:
    population.routes = rnd.sample(population.routes, k=len(population.routes))
    return population
