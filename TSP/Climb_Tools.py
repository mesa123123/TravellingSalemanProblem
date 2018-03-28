
def next_distance(route, member, roads):
    stats = []
    stats.append(swap_member([i for i in route], member))
    stats.append(distance_check(stats[0], roads))
    return stats


def best_distance(route, roads):
    alt_routes = [[] for i in range(1, int(len(roads)) - 2)]
    swap_member = 0
    # Finds all possible switches and calculates them by distannce
    while swap_member < int(len(roads)) - 3:
        temp_stats = next_distance(route, swap_member, roads)
        alt_routes[swap_member].append(temp_stats[0])
        alt_routes[swap_member].append(temp_stats[1])
        swap_member += 1
    # sort the alternate by the distances
    alt_routes = sorted(alt_routes, key=lambda x: x[1])
    return alt_routes[0]


def distance_check(route,roads):
    number_of_cities = int(len(roads)) - 1
    distance = []
    #append the distance from the hometown to the first stop
    try:
        distance.append(roads[1][route[0]])
    except IndexError:
        print("Error: ", route[0])
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
            print("Error: ", a, " ", b)
    return sum(distance)


def swap_member(route, member):
        temp = route[member]
        route[member] = route[member + 1]
        route[member + 1] = temp
        return route


