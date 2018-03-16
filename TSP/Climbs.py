from sys import maxsize
from TSP.Problem_Matrix import ProblemMatrix
from TSP.Climb_Tools import *


def hill_climb(optimization_goal, route, roads):
    current_best_distance = distance_check(route, roads)
    story = []
    story.append(distance_check(route, roads))
    #if the current best distance is already optimal the loop will be skipped entirely
    while current_best_distance > optimization_goal:
        # keep tabs on the part of the list you're messing with
        swapped_member = 2
        while swapped_member < int(len(roads)) - 3:
            temp_distance = next_distance(route, swapped_member, roads)
            if current_best_distance > temp_distance:
                story.append(temp_distance)
                current_best_distance = temp_distance
                route = swap_member(route, swapped_member)
                break
            else:
                swapped_member += 1
        if swapped_member >= int(len(roads)) - 3:
            optimization_goal = maxsize
    return story


def repeated_climb(optimization_goal, route, roads, resets):
    story = []
    one_hill = hill_climb(optimization_goal, route, roads)
    for distance in one_hill:
        story.append(distance)
    for i in range(0, resets):
        route = list(ProblemMatrix.random_permutation(route))
        one_hill = hill_climb(optimization_goal, route, roads)
        for distance in one_hill:
            story.append(distance)
    return story


def steep_climb(optimization_goal, route, roads):
    current_best_distance = distance_check(route, roads)
    story = []
    story.append(distance_check(route, roads))
    while current_best_distance > optimization_goal:
        alt_routes = best_distance(route, roads)
        if alt_routes[0] < current_best_distance:
            story.append(current_best_distance)
            current_best_distance = alt_routes[0]
            route = swap_member(route,alt_routes[1])
        else:
            optimization_goal = maxsize
    return story


def repeated_steep_climb(optimization_goal, route, roads, resets):
    story = []
    one_hill = steep_climb(optimization_goal, route, roads)
    for distance in one_hill:
        story.append(distance)
    for i in range(0, resets):
        route = list(ProblemMatrix.random_permutation(route))
        one_hill = steep_climb(optimization_goal, route, roads)
        for distance in one_hill:
            story.append(distance)
    return story


