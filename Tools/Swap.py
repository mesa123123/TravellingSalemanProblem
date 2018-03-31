import Tools.Distance_check as Dcheck

def swap_member(route, member):
    temp = route[member]
    route[member] = route[member + 1]
    route[member + 1] = temp
    return route


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


def next_distance(route, member, roads):
    stats = []
    stats.append(swap_member([i for i in route], 7))
    stats.append(Dcheck.distance_check(stats[0], roads))
    return stats
