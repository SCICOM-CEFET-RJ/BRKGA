from Population import Population
import random


class BRKGA:

    def __init__(self,
                 n,  # - n: number of genes in each chromosome
                 p,  # - p: number of elements in each population
                 pe, # - pe: pct of elite items into each population
                 pm, # - pm: pct of mutants introduced at each generation into the population
                 rhoe, # - rhoe: probability that an offspring inherits the allele of its elite parent
                 refDecoder, # 
                 refRNG, #
                 k = 1, # - K: number of independent Populations
                 MAX_Threads = 1): # - MAX_THREADS: number of threads to perform parallel decoding

        random.seed(1234)       
        self.n = n
        self.p = p
        self.pe = pe
        self.pm = pm
        self.rhoe = rhoe
        self.refDecoder = refDecoder
        self.k = k
        self.MAX_Threads = MAX_Threads
        
        self.current_population = [Population.fromPopulation(p,n) 
                                   for i in range(k)]

        self.previous_population = self.current_population

    def reset(self):
        
        for i in range(self.k):
            self.initialize(i)


    def evolve(self, generations = 1):
        # inserir controle de erro

        for i in range(1, generations +1):
            for j in range(self.k):
                self.evolution(self.current_population[j], 
                               self.previous_population[j])
                
                self.current_population[j], 
                self.previous_population[j] = self.swap(self.current_population[j], 
                                                        self.previous_population[j])


    def exchangeElite(self, M):
        # inserir checagem de erro

        for i in range(self.k):
            dest = self.p - 1
            for j in range(self.k):
                if j == 1 : continue

                for m in range(M):
                    bestOfJ = self.current_population[j]._getChromossome(m)
                    self.current_population[i].getChromossome(dest) = bestOfJ

                    self.current_population[i].fitness[dest][1] =  self.current_population[j].fitness[m][1]


                    dest -= 1

        for j in range(self.k):
            self.current_population[j].__sortFitness()


    def evolution(self, current, next):
        
        i = 0
        j = 0

        while i < self.pe:
            for j in range(self.n):
                next.population[i,j] = current.population[current.fitness[i][0], j] 
                
            next.fitness[i] = (i, current.fitness[i][1])
            
            i += 1
            
        while i < (self.p - self.pm):

            eliteParent = random.randint(self.pe)
            noneliteParent = self.pe + random.randint(self.p - self.pe)

            for j in range(self.n):
                sourceParent =  eliteParent if random.random() < self.rhoe else noneliteParent

            i += 1

        # We'll introduce 'pm' mutants:
        while i < self.p:
            for j in range(self.n):
                next.population[i,j] = random.random()
            
            i += 1

        for i in range(self.pe, self.p):
            next.fitness[i] = (i, random.random())

        next._sortFitness()


    def getPopulation(self, k = 0):
        try:
            self.current_population[k]
        except:
            print("Invalid population identifier.")

    def getBestChromossome(self):
        bestK = 0 

        for i in range(self.k):
            if self.current_population[i].getBestFitness() < self.current_population[bestK].getBestFitness():
                bestK = i
        
        return self.current_population[bestK].getChromossome(0)

    def getBestFitness(self):
        best = self.current_population[0].fitness[0][1]

        for i in range(self.k):
            if self.current_population[i].fitness[0][1] < best :
                best = self.current_population[i].fitness[0][1]

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

    def initialize(self, i):
        for j in range(self.p):
            for k in range(self.n):
                self.current_population[i][j,k] = random.random()    
        
        for j in range(self.p):
            self.current_population[i]._setFitness(j, self.refDecoder.decode(self.current_population[i][j]))

        self.current_population[i]._sortFitness()    
        
    def swap(self, s1, s2):
        return s2, s1