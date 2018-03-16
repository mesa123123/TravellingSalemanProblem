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
            alt_route = next_distance(route, swapped_member, roads)
            if alt_route[1] < current_best_distance:
                current_best_distance = alt_route[1]
                story.append(alt_route[1])
                route = alt_route[0]
                break
            else:
                swapped_member += 1
        if swapped_member >= int(len(roads)) - 3:
            optimization_goal = maxsize
    return story


def repeated_climb(optimization_goal, route, roads, resets, steep = False):
    story = []
    if not steep:
        one_hill = hill_climb(optimization_goal, route, roads)
    else:
        one_hill = steep_climb(optimization_goal, route, roads)
    for distance in one_hill:
        story.append(distance)
    for i in range(0, resets):
        route = list(ProblemMatrix.random_permutation(route))
        if not steep:
            one_hill = hill_climb(optimization_goal, route, roads)
        else:
            one_hill = steep_climb(optimization_goal, route, roads)
        for distance in one_hill:
            story.append(distance)
    return story


def steep_climb(optimization_goal, route, roads):
    current_best_distance = distance_check(route, roads)
    story = []
    story.append(current_best_distance)
    while current_best_distance > optimization_goal:
        alt_route = best_distance(route, roads)
        if alt_route[1] < current_best_distance:
            story.append(alt_route[1])
            current_best_distance = alt_route[1]
            route = alt_route[0]
        else:
            optimization_goal = maxsize
    return story


# def repeated_steep_climb(optimization_goal, route, roads, resets):
#     story = []
#     one_hill = steep_climb(optimization_goal, route, roads)
#     for distance in one_hill:
#         story.append(distance)
#     for i in range(0, resets):
#         route = list(ProblemMatrix.random_permutation(route))
#         one_hill = steep_climb(optimization_goal, route, roads)
#         for distance in one_hill:
#             story.append(distance)
#     return story


