# This class builds the population of chromossomes

import numpy as np

class Population:

    def __init__(self, object_population):

        self.population = object_population[0]
        self.fitness = object_population[1]        

    @classmethod
    def fromPopulation(cls, p, n):        
        
        population = np.zeros(shape=(p,n)) 
        fitness = [(i,0) for i in range(p)]

        return cls([population, fitness])

    def _sortFitness(self):
        return self.fitness.sort(key= lambda tup: tup[1])

    def _setFitness(self, i, f):

        self.fitness[i] = (i,f)


    def _getChromossome(self, i):
        
        try:

            chromossome = self.population[self.fitness[i][0]]
        
        except AssertionError as error:
            print(error)

        return chromossome

    def __operator(self, i, j):
        
        chromossome = self.population[i]
        allele = chromossome[j]

        return allele

    def __vectorOperator(self,i):

        try:
            
            chromossome = self.population[self.fitness[i][0]]
        
        except AssertionError as error:

            print(error)

        return chromossome       

    def getN(self):
        return np.shape(self.population)[1]

    def getP(self):
        return len(self.population)

    def getBestFitness(self):
        return self.fitness[0][1]

    def getFitness(self,i):
        return self.fitness[i][1]
    
    def getChromossome(self, i):        
        try:                        
            chromossome = self.population[self.fitness[i][0]]
        
        except AssertionError as error:
            print(error)

        return chromossome














