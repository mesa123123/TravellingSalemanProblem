from sys import maxsize
from TSP.Problem_Matrix import ProblemMatrix


def hill_climb(optimization_goal,number_of_cities,route,roads,):
    current_best_distance = sum(distance_check(route, roads, number_of_cities))
    story = []
    story.append(sum(distance_check(route, roads, number_of_cities)))
    #if the current best distance is already optimal the loop will be skipped entirely
    while current_best_distance > optimization_goal:
        # keep tabs on the part of the list you're messing with
        swapped_member = 2
        # then check the routes distance
        while swapped_member < number_of_cities - 2:
            temp_route = swap_member(route, swapped_member)
            temp_distance = sum(distance_check(temp_route, roads, number_of_cities))
            if temp_distance < current_best_distance:
                current_best_distance = temp_distance
                story.append(current_best_distance)
                swapped_member = 2
                break
            else:
                swapped_member += 1
        #   if you can't, admit defeat
        if swapped_member >= number_of_cities - 2:
            optimization_goal = maxsize
        # and then loop around       - Distance checking loop ends
    return story


def steep_climb(optimization_goal,number_of_cities,route,roads):
    current_best_distance = sum(distance_check(route, roads, number_of_cities))
    story = []
    story.append(sum(distance_check(route, roads, number_of_cities)))
    while current_best_distance > optimization_goal:
        alt_routes = [[] for i in range(1,number_of_cities-1)]
        swapped_member = 0
        #Finds all possible switches and calculates them by distannce
        while swapped_member < number_of_cities-2:
            temp_route = swap_member([i for i in route],swapped_member)
            temp_distance = sum(distance_check(temp_route,roads,number_of_cities))
            alt_routes[swapped_member].append(temp_distance)
            alt_routes[swapped_member].append(swapped_member)
            swapped_member += 1
        #sort the dictionary by the distances
        alt_routes = sorted(alt_routes, key=lambda x:x[0])
        if alt_routes[0][0] < current_best_distance:
            story.append(current_best_distance)
            current_best_distance = alt_routes[0][0]
            if current_best_distance < optimization_goal:
                story.append(current_best_distance)
                return story
            else:
                route = swap_member(route,alt_routes[0][1])
                #check if its shorter than original route
        else:
            optimization_goal = maxsize

    return story


def distance_check(route,roads,number_of_cities):
    distance = []
    #append the distance from the hometown to the first stop
    try:
        distance.append(roads[1][route[0]])
    except IndexError:
        print(route[0])
    for i in range(1,number_of_cities-1):
        if i < number_of_cities-1:
            a = route[i-1]
            b = route[i]
        else:
            a = route[number_of_cities-1]
            b = route[0]
        try:
            distance.append(roads[a][b])
        except IndexError:
            print(a, " ", b)
    return distance


def swap_member(route, member):
        temp = route[member]
        route[member] = route[member + 1]
        route[member + 1] = temp
        return route
