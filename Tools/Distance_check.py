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