import os

import pylab as pyl


def create_dirs(title):
    if not os.path.exists("../Results"):
        os.makedirs("../Results")
    if not os.path.exists("../Results/" + title):
        os.makedirs("../Results/" + title)
    if not os.path.exists("../Results/" + title + "/Full Scores Of Population"):
        os.makedirs("../Results/" + title + "/Full Scores Of Population")
    if not os.path.exists("../Results/" + title + "/Performance Graphs"):
        os.makedirs("../Results/" + title + "/Performance Graphs")


def create_travel_plots(journeys, title, dir_title):
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
        pyl.plot(xValues, journey[0], label=journey[1])
    # pyl.legend(loc='upper right')
    pyl.xlabel("Generation")
    pyl.ylabel("Population Best")
    pyl.title(title)
    pyl.savefig("../Results/" + dir_title + "/Performance Graphs/Graph " + title + ".png", bbox_inches="tight")
    pyl.gcf().clear()
