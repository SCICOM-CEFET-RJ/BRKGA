# This class builds the population of chromossomes

import numpy as np

class Population:

    def __init__(self, population):

        self.population = population        

    @classmethod
    def fromPopulation(cls, p, n):        
        
        population = np.zeros(shape=(p,n)) 
        fitness = [(i,0) for i in range(p)]

        return cls([population, fitness])

    def __sortFitness(self):
        return np.sort(-self.fitness)

    def __setFitness(self, i, f):

        self.population[1][i] = (i,f)


    def __getChromossome(self, i):
        
        try:
            population = self.population[0]
            fitness = self.population[1]
            chromossome = population[fitness[i][0]]
        
        except AssertionError as error:

            print(error)

        return chromossome

    def __operator(self, i, j):
        
        population = self.population[0]
        chromossome = population[i]
        allele = chromossome[j]

        return allele

    def __vectorOperator(self,i):

        try:
            population = self.population[0]
            fitness = self.population[1]
            chromossome = population[fitness[i][0]]
        
        except AssertionError as error:

            print(error)

        return chromossome       

    def getN(self):
        return np.shape(self.population[0])[1]

    def getP(self):
        return len(self.population[1])

    def getBestFitness(self):
        return self.population[1][0][1]

    def getFitness(self,i):
        return self.population[1][i][1]
    
    def getChromossome(self, i):
        
        try:
            population = self.population[0]
            fitness = self.population[1]
            chromossome = population[fitness[i][0]]
        
        except AssertionError as error:

            print(error)

        return chromossome














