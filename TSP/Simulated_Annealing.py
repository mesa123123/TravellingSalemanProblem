from TSP.Climb_Tools import *
from TSP.Problem_Matrix import ProblemMatrix
import random as rnd
from math import exp



def simulated_annealing(route, roads, init_temp):
    current_best_distance = distance_check(route, roads)
    temp = init_temp
    final_temp = init_temp//30
    story = []
    story.append(current_best_distance)
    #if the current best distance is already optimal the loop will be skipped entirely
    while temp >= final_temp:
        alt_route = best_distance(route, roads)
        cost = alt_route[1] - current_best_distance
        if cost < 0:
            story.append(alt_route[1])
            current_best_distance = alt_route[1]
            route = alt_route[0]
        elif rnd.uniform(0,1) < acceptance_probability(cost, temp):
            story.append(alt_route[1])
            current_best_distance = alt_route[1]
            route = alt_route[0]
        temp = cool(temp, final_temp)
    return story


def cool(temp, final_temp):
    return temp - final_temp


def acceptance_probability(cost, temp):
    return exp(-cost/temp)

def repeated_anneal(route, roads, init_temp, resets):
    story = []
    one_hill = simulated_annealing(route, roads, init_temp)
    for distance in one_hill:
        story.append(distance)
    for i in range(0, resets):
        route = list(ProblemMatrix.random_permutation(route))
        one_hill = simulated_annealing(route, roads, init_temp)
        for distance in one_hill:
            story.append(distance)
    return story