from random import *

class DNA:
    
    
    def __init__(self, lenght):
        self.lenght = lenght
        self.genes = []
        self.fitness = 0
        self.scaled_fitness = 0
        
        for i in range(lenght):
            self.genes.append(self.newchar())
        
        
    def newchar(self):
        return chr(randrange(32, 123))
    
    
    def calc_fitness(self, target):
        score = 0
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                score = score + 10
               
        self.fitness = score / len(target) + randrange(1, 3)
        
    
    def crossover(self, partner):
        child = DNA(len(self.genes))
        mid = randrange(len(self.genes))
        for i in range(len(self.genes)):
            if i < mid:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child
    
    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random() < mutation_rate:
                self.genes[i] = self.newchar()
