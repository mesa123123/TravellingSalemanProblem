import pylab as pyl


def plot_travels(journeys, title):
    longest_journey = 0
    shortest_journey = 0
    for journey in journeys:
        if len(journey[0]) > longest_journey:
            longest_journey = len(journey[0])
    xValues = range(0, longest_journey)
    while len(xValues) > int(shortest_journey):
        shortest_journey = len(xValues)
        for journey in journeys:
            if len(journey[0]) < len(xValues):
                journey[0].append(journey[0][-1])
                if len(journey[0]) < shortest_journey:
                    shortest_journey = len(journey[0])
    for journey in journeys:
        pyl.plot(xValues, journey[0], label= journey[1])
    # pyl.legend(loc='upper right')
    pyl.xlabel('Generation')
    pyl.ylabel('Population Best')
    pyl.title(title)
    pyl.savefig("../Results/Performance Graphs/Graph " \
                   + title + ".png", bbox_inches='tight')
    pyl.gcf().clear()
