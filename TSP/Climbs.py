from sys import maxsize
from TSP.Problem_Matrix import ProblemMatrix


def hill_climb(optimization_goal,number_of_cities,route,roads,):
    current_best_distance = sum(distance_check(route, roads, number_of_cities))
    story = []
    story.append(sum(distance_check(route, roads, number_of_cities)))
    #if the current best distance is already optimal the loop will be skipped entirely
    while current_best_distance > optimization_goal:
        # keep tabs on the part of the list you're messing with
        swap_order = list(ProblemMatrix.random_permutation(range(0,number_of_cities-1)))
        swapped_member = 2
        # then check the routes distance
        while swapped_member < number_of_cities - 1:
            temp_route = swap_member(route, int(swap_order[swapped_member]))
            temp_distance = sum(distance_check(temp_route, roads, number_of_cities))
            # is it the best we've found so far? if so save the distance and the route
            if temp_distance < current_best_distance:
                current_best_distance = temp_distance
                story.append(current_best_distance)
                swapped_member = 2
                break
            swapped_member += 1
        #   if you can't, admit defeat
        if swapped_member >= number_of_cities - 1:
            optimization_goal = maxsize
        # and then loop around       - Distance checking loop ends
    return story


def distance_check(route,roads,number_of_cities):
    distance = []
    #append the distance from the hometown to the first stop
    distance.append(roads[1][route[0]])
    for i in range(1,number_of_cities-1):
        if i < number_of_cities-1:
            a = route[i-1]
            b = route[i]
        else:
            a = route[number_of_cities-1]
            b = route[0]
        distance.append(roads[a][b])
    return distance


def swap_member(route, member):
    temp = route[member]
    route[member] = route[member -1]
    route[member -1] = temp
    return route


def steep_climb(optimization_goal,number_of_cities,route,roads):
    current_best_distance = sum(distance_check(route, roads, number_of_cities))
    current_best_route = route
    alt_routes = [[] for i in range(2,number_of_cities-1)]

    #check if optimal
    # while current_best_distance < optimization_goal:
    swapped_member = 2
    while swapped_member < number_of_cities-1: #I don't think its checking the swap of the final two cities?
        temp_route = swap_member(route,swapped_member)

        # temp_distance = sum(distance_check(temp_route,roads,number_of_cities))
        # alt_routes[swapped_member-2].append(temp_distance)
        # alt_routes[swapped_member-2].append(swapped_member)
        swapped_member += 1
    print(alt_routes)

        #sort the dictionary by the distances

        #take lowest route
            #check if its shorter than original route
            #if so check if its optimal
                #if not keep on going
                #if so return
            #if not you're done here

    return current_best_route
