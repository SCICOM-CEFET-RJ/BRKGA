# This class builds the population of chromossomes

import numpy as np
from Individual import individual


class Population:

    def __init__(self, population):

        self.population = population

    @classmethod
    def from_Population(cls, p, n):        
        
        population = [individual(n) for i in range(p)]

        return cls(population)

    def _sortFitness(self):
        return self.population.sort(key= lambda ind: ind.fitness)

    def _setFitness(self, i, f):

        self.population[i].update_fitness(f)


    def _getChromossome(self, i):
        
        try:

            chromossome = self.population[i].get_chromossome()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        
        except AssertionError as error:
            print(error)

        return chromossome

    def __operator(self, i, j):
        
        chromossome = self.population[i].get_chromossome()
        allele = chromossome[j]

        return allele

    def __vectorOperator(self,i):

        try:
            
            chromossome = self.population[i].get_chromossome()

        except AssertionError as error:

            print(error)

        return chromossome       

    def getN(self):
        return len(self.population[0].get_chromossome())

    def getP(self):
        return len(self.population)

    def getBestFitness(self):
        return self.population[0].get_fitness()

    def getFitness(self,i):
        return self.population[i].get_fitness()
    
    def getChromossome(self, i):        
        try:                        
            chromossome = self.population[i].get_chromossome()
        
        except AssertionError as error:
            print(error)

        return chromossome
    
    def get_individual(self, i):
        return self.population[i]













