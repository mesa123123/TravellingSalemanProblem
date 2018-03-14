'''
def simulated_annealing(init_temp, init_place, final_temp):
    temp = init_temp
    place = init_place
    while temp > final_temp:
        while inner_loop_criteria = False:
            new_place = Perturb(place)
            delta_cost = cost(new_place) - cost(place)
            if delta_cost < 0:
                place = new_place
            elif random.random(0,1) > acceptance_probability(delta_cost, temp):
                place = new_place
        temp = schedule(temp, final_temp)


def perturb:
    pass


def cost:
    pass


def schedule(temp, final_temp):
    pass


def acceptance_probability(delta_cost, temp):
    pass
'''