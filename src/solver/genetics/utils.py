from logistics.types import RoadNetwork
from logistics.utils import plot_route
from solver.genetics.types import RoutePopulation


def create_route_population(population_size: int, road_network: RoadNetwork) -> RoutePopulation:
    pop: RoutePopulation = RoutePopulation(
        population_size=population_size,
        num_of_cities=len(road_network),
        routes=[plot_route(road_network) for i in range(population_size)],
    )
    pop.routes = sorted(pop.routes, key=lambda x: x.route_score)
    return pop


def create_next_generation(
    population: RoutePopulation,
    road_network: RoadNetwork,
    recombination_method: str,
    reproduciton_style: str,
    mutation_technique: str,
    mutation_chance: int | None = 10,
    sort_rank: bool = False,
) -> RoutePopulation:
    return population


def create_all_generations(
    population: RoutePopulation,
    road_network: RoadNetwork,
    recombination: str,
    reproduciton_style: str,
    mutation_technique: str,
    mutation_chance: int | None = 10,
    generation_num: int = 10,
    sort_rank: bool = False,
) -> RoutePopulation:
    for i in range(generation_num):
        population = create_next_generation(
            population=population,
            road_network=road_network,
            sort_rank=sort_rank,
            recombination_method=recombination,
            reproduciton_style=reproduciton_style,
            mutation_technique=mutation_technique,
            mutation_chance=mutation_chance,
        )
    return population
