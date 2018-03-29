import pylab as pyl
from sys import maxsize
from cycler import cycler

def plot_travels(journeys, optimization_goal, optimization_show = True):
    longest_journey = 0
    shortest_journey = 0
    for journey in journeys:
        if len(journey[0]) > longest_journey:
            longest_journey = len(journey[0])
    xValues = range(0, longest_journey)
    optimization_line = [optimization_goal] * len(xValues)
    while len(xValues) > int(shortest_journey):
        shortest_journey = len(xValues)
        for journey in journeys:
            if len(journey[0]) < len(xValues):
                journey[0].append(journey[0][-1])
                if len(journey[0]) < shortest_journey:
                    shortest_journey = len(journey[0])
    if optimization_show:
        pyl.plot(xValues, optimization_line, 'r--')
    for journey in journeys:
        pyl.plot(xValues, journey[0], label= journey[1])
    pyl.legend(loc='upper left')
    pyl.xlabel('Successful Iterations')
    pyl.ylabel('Distance of Iteration')
    pyl.title('Travelling Salesman Heuristic Searches')
    pyl.show()