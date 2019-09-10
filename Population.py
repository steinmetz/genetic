from DNA import DNA
from random import *
import numpy as np

class Population:
    def __init__(self, target, mutation_rate, popmax):
        self.target = target
        self.mutation_rate = mutation_rate
        self.popmax = popmax
        
        self.generations = 0
        self.finished = False
        self.perfect_score = 1
        
        self.best = ""
         
        
        self.population = []
        for i in range(self.popmax):
            self.population.append(DNA(len(self.target)))
        
        
        
    def natural_selection(self):
        self.mating_pool = []
        
        max_fitness = 0 
        
        for p in self.population:
            if p.fitness > max_fitness:
                max_fitness = p.fitness
                max_man = p
        print(max_fitness)       
        print(max_man.genes)
        if("".join(max_man.genes) == self.target):
            self.finished = True
            print(self.generations)
         
        for dna in self.population:
            fitness = np.interp(dna.fitness, (0, max_fitness), (0, 1))
            #fitness = map(dna.fitness, 0, max_fitness, 0, 1)
            n = int(np.floor(fitness * 100))
            for i in range(n):
                self.mating_pool.append(dna)
            dna.scaled_fit = fitness
        
        
    def generate(self):
        for i in range(len(self.population)):
            index_mom = randrange(len(self.mating_pool))
            index_dad = randrange(len(self.mating_pool))
            mom = self.mating_pool[index_mom]
            dad = self.mating_pool[index_dad]
            child = mom.crossover(dad)
            child.mutate(self.mutation_rate)
            self.population[i] = child
            
        self.generations += 1
        
        
    def calc_fitness(self):
        for p in self.population:
            p.calc_fitness(self.target)
        
    
    def evaluate(self):
        pass
        
         
