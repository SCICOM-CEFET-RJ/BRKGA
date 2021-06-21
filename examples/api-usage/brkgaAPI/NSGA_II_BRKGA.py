#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 22:42:23 2021

@author: fpgdesa
"""

import random
from copy import deepcopy
import pandas as pd


class NSGA_II_BRKGA:
    
       
    def evolution(self,
                  pe,
                  pm,
                  n,
                  rhoe,
                  p,
                  refDecoder,
                  current_population,
                  next_population):
        
        i = 0
        j = 0

        while i < pe:
            for j in range(n):
                next_population.population[i,j] = current_population.population[current_population.fitness[i][0],j] 
                
            next_population.fitness[i] = (i, current_population.fitness[i][1])
            
            i += 1
         
        while i < (p - pm):

            eliteParent = random.randint(0,pe - 1)
            noneliteParent = pe + random.randint(0, p - pe - 1)

            for j in range(n):
                
                sourceParent =  eliteParent if random.random() < rhoe else noneliteParent
                
                next_population.population[i,j] = current_population.population[current_population.fitness[int(sourceParent)][0], j] 
                
                
            i += 1
         
        # We'll introduce 'pm' mutants:
        while i < p:
            for j in range(n):
                next_population.population[i,j] = random.random()
            
            i += 1
         
        for i in range(int(pe), int(p)):
            next_population.fitness[i] = (i, refDecoder.decode(next_population.population[i]))
        
        
        import pdb; pdb.set_trace()
        
        
        combined_population = self.__combine_population(current_population,
                                                        next_population
                                                        ) 
                
              
        
        return deepcopy(next_population)
    
    
    
    
    def __combine_population(current_population, next_population):
        
        concatenate = [current_population, next_population]        
        
        return pd.concat(concatenate)
    
    
    
    def fast_nondominated_sort(self, population):
        population.fronts = [[]]
        for individual in population.population:
            individual.domination_count = 0
            individual.dominated_solutions = []
            for other_individual in population:
                if individual.dominates(other_individual):
                    individual.dominated_solutions.append(other_individual)
                elif other_individual.dominates(individual):
                    individual.domination_count += 1
            if individual.domination_count == 0:
                individual.rank = 0
                population.fronts[0].append(individual)
        i = 0
        while len(population.fronts[i]) > 0:
            temp = []
            for individual in population.fronts[i]:
                for other_individual in individual.dominated_solutions:
                    other_individual.domination_count -= 1
                    if other_individual.domination_count == 0:
                        other_individual.rank = i+1
                        temp.append(other_individual)
            i = i+1
            population.fronts.append(temp)
    
    
    