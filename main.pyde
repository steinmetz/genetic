from Population import Population



target = "charles"
mutation_rate = 0.01
popmax = 200
population = Population(target, mutation_rate, popmax)

def setup():
    pass

def draw():
    population.calc_fitness()
    population.natural_selection()
    population.generate()
    population.evaluate()
    
    if population.finished:
        noLoop()
