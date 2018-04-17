from Tools.Distance_check import distance_check
from Tools.Random_Permutation import random_permutation
from Tools.Swap import *
import random as rnd
from math import exp


def simulated_annealing(route, roads, init_temp):
    current_best_distance = distance_check(route, roads)
    temp = init_temp
    final_temp = init_temp/100
    story = []
    story.append(current_best_distance)
    #if the current best distance is already optimal the loop will be skipped entirely
    swap_roof = len(route) - 2
    swapped_point = rnd.randint(0, swap_roof)
    while temp >= final_temp*2:
        alt_route = next_distance(route, swapped_point, roads)
        cost = alt_route[1] - current_best_distance
        if cost < 0:
            story.append(alt_route[1])
            current_best_distance = alt_route[1]
            route = alt_route[0]
            swapped_point = rnd.randint(0,swap_roof)
            temp = cool(temp, final_temp)
        elif rnd.uniform(0,1) < acceptance_probability(cost, temp):
            story.append(alt_route[1])
            current_best_distance = alt_route[1]
            route = alt_route[0]
            swapped_point = rnd.randint(0,swap_roof)
            temp = cool(temp, final_temp)
        else:
            if(swapped_point < swap_roof):
                swapped_point += 1
            else:
                swapped_point = rnd.randint(0,swap_roof)
                temp = cool(temp, final_temp)
    return story


def steep_simulated_annealing(route, roads, init_temp, temp_reduction):
    current_best_distance = distance_check(route, roads)
    temp = init_temp
    final_temp = init_temp/temp_reduction
    story = []
    story.append(current_best_distance)
    #if the current best distance is already optimal the loop will be skipped entirely
    while temp >= final_temp*2:
        alt_route = best_distance(route, roads)
        cost = alt_route[1] - current_best_distance
        if cost < 0:
            story.append(alt_route[1])
            current_best_distance = alt_route[1]
            route = alt_route[0]
        elif rnd.uniform(0,1) < acceptance_probability(cost, temp):
            rnd.shuffle(alt_route[0])
            explored = alt_route[0]
            story.append(distance_check(explored, roads))
            current_best_distance = distance_check(explored, roads)
            route = explored
        temp = cool(temp, final_temp)
    return story


def cool(temp, final_temp):
    return temp - final_temp


def acceptance_probability(cost, temp):
    return exp(-cost/temp)

def repeated_anneal(route, roads, init_temp, resets, steep = False):
    story = []
    if not steep:
        one_hill = simulated_annealing(route, roads, init_temp)
    else:
        one_hill = steep_simulated_annealing(route, roads, init_temp)
    for distance in one_hill:
        story.append(distance)
    for i in range(0, resets):
        route = list(random_permutation(route))
        if not steep:
            one_hill = simulated_annealing(route, roads, init_temp)
        else:
            one_hill = steep_simulated_annealing(route, roads, init_temp)
        for distance in one_hill:
            story.append(distance)
    return story


