from brkgaAPI.Population import Population
import random
from copy import deepcopy

class BRKGA:

    def __init__(self,
                 n,  # - n: number of genes in each chromosome
                 p,  # - p: number of elements in each population
                 pe, # - pe: pct of elite items into each population
                 pm, # - pm: pct of mutants introduced at each generation into the population
                 rhoe, # - rhoe: probability that an offspring inherits the allele of its elite parent
                 refDecoder, # 
                 refEvolution,
                 k = 1, # - K: number of independent Populations
                 MAX_Threads = 1): # - MAX_THREADS: number of threads to perform parallel decoding

        random.seed(1234)       
        self.n = n
        self.p = p
        self.pe = pe * p
        self.pm = pm * p
        self.rhoe = rhoe
        self.refDecoder = refDecoder
        self.refEvolution = refEvolution
        self.k = k
        self.MAX_Threads = MAX_Threads
        
        
        
        self.current_population = [Population.from_Population(p,n) 
                                   for i in range(k)]
        
        
        
        for i in range(k): self.initialize(i)       
        
        self.previous_population = deepcopy(self.current_population)

    def reset(self):
        
        for i in range(self.k):
            self.initialize(i)
    
    # remove os M piores de uma população e insere M melhores de outra
    def exchangeElite(self, M):
        # inserir checagem de erro

        for i in range(self.k):
            dest = self.p - 1
            for j in range(self.k):
                if j == i : continue

                for m in range(M):
                    
                    bestOfJ = self.current_population[j].get_individual(m)
                    
                    self.current_population[i].population[dest] = bestOfJ                    

                    dest -= 1

        for j in range(self.k):
            self.current_population[j]._sortFitness()  

    
    def initialize(self, i):
      
        for j in range(self.p):
            for k in range(self.n):
                self.current_population[i].population[j].update_allele(k,random.random())    
       
        for j in range(self.p):
            self.current_population[i]._setFitness(j, self.refDecoder.decode(self.current_population[i]._getChromossome(j)))

       # import pdb; pdb.set_trace()

        self.current_population[i]._sortFitness()  

    
    def evolve(self, generations = 1):
        # inserir controle de erro
         for i in range(1, generations + 1):
            for j in range(self.k):
                self.previous_population[j] = self.evolution(self.current_population[j], 
                                                             self.previous_population[j])
                
                self.current_population[j], self.previous_population[j] = deepcopy(self.previous_population[j]), deepcopy(self.current_population[j])


    def evolution(self, current_population, next_population):
        
        #import pdb;pdb.set_trace()
        next_population_evolved = self.refEvolution.evolution(self.pe,
                                                              self.pm,
                                                              self.n,
                                                              self.rhoe,
                                                              self.p,
                                                              self.refDecoder,
                                                              current_population,
                                                              next_population
                                                              )
               
        
        return next_population_evolved
        


    def getPopulation(self, k = 0):
        try:
            population = self.current_population[k]
        except:
            print("Invalid population identifier.")
        
        return population

    def getBestChromossome(self):
        bestK = 0 

        for i in range(self.k):
            if self.current_population[i].getBestFitness() < self.current_population[bestK].getBestFitness():
                bestK = i
        
        return self.current_population[bestK].getChromossome(0)

    def getBestFitness(self):
        best = self.current_population[0].getFitness(0)

        for i in range(self.k):
            if self.current_population[i].getFitness(0) < best :
                best = self.current_population[i].getFitness(0)

        return best 

    def getN(self):
        return self.n

    def getP(self):
        return self.p

    def getPe(self):
        return self.pe

    def getPm(self):
        return self.pm

    def getPo(self):
        return (self.p - self.pe - self.pm)

    def getRhoe(self):
        return self.rhoe

    def getK(self):
        return self.k

    def getMAX_THREADS(self):
        return self.MAX_Threads     
        
    def swap(self, s1, s2):
        return (deepcopy(s2), deepcopy(s1))
