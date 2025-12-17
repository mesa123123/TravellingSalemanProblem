from math import ceil, floor

from logistics.types import Route
from src.solver.genetics.types import RoutePopulation


# keeps the best of parents and then adds all of the children except the worst
def young_elitism(parent_pop, children_pop):
    pop_size: int = parent_pop.population_size
    new_routes: list[Route] = parent_pop.routes[0] + [children_pop.routes[i] for i in range(0, pop_size - 1)]
    return RoutePopulation(pop_size, parent_pop.num_of_cities, new_routes)


# Returns the top 10 of either the children and the parents or just returns the children
def top_ten_both_generations(parent_pop, children_pop):
    pop_size: int = parent_pop.population_size
    new_routes: list[Route] = [parent_pop.routes[i] for i in range(0, floor(pop_size / 2))] + [
        children_pop.routes[i] for i in range(0, ceil(pop_size / 2))
    ]
    return RoutePopulation(pop_size, parent_pop.num_of_cities, new_routes)
