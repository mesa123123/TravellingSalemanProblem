import copy
import random as rnd

from logistics.types import RoadNetwork
from solver.genetics.mutations.interface import Mutation, mutate
from solver.genetics.types import RoutePopulation
from solver.genetics.reproduction.interface import ReproductionMethod, reproduce


def sort_population_by_route_score(population: RoutePopulation) -> RoutePopulation:
    population.routes.sort(key=lambda d: d.route_score)
    return population


def sort_population_by_random(population: RoutePopulation) -> RoutePopulation:
    population.routes = rnd.sample(population.routes, k=len(population.routes))
    return population


def create_next_generation(
    population: RoutePopulation,
    road_network: RoadNetwork,
    crossover,
    sort_rank: bool,
    reproduction: ReproductionMethod,
    reproduciton_style: ReproductionStyle,
    select,
    mutation_technique: Mutation,
    mutation_chance: int | None = 10,
) -> RoutePopulation:
    ngen_pop: RoutePopulation = copy.deepcopy(population)
    ngen_pop: RoutePopulation = (
        sort_population_by_route_score(ngen_pop) if sort_rank else sort_population_by_random(ngen_pop)
    )
    # Here we need to create a reproduction function to sort out the new gen
    ngen_pop: RoutePopulation = reproduce(ngen_pop, road_network, reproduction, reproduction_style) 
    if mutation_chance:
        ngen_pop.routes = [
            mutate(route, road_network, mutation_technique, mutation_chance) for route in ngen_pop.routes
        ]
    return ngen_pop


def create_all_generations(
    population: RoutePopulation,
    road_network: RoadNetwork,
    crossover,
    parent_selection,
    select,
    mutation_technique: Mutation,
    generation_num=10,
    mutation_chance: int | None = 10,
) -> RoutePopulation:
    for i in range(generation_num):
        population = create_next_generation(
            population, road_network, crossover, parent_selection, select, mutation_technique, mutation_chance
        )
    return population
