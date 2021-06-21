#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 22:39:54 2021

@author: fpgdesa
"""
import random
from copy import deepcopy

class StandardBRKGA:    
       
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
                next_population.population[i].update_allele(j,current_population.population[i].get_chromossome()[j])   
                
            next_population.population[i].update_fitness(current_population.population[i].get_fitness())
            
            i += 1
         
        while i < (p - pm):

            eliteParent = random.randint(0,pe - 1)
            noneliteParent = pe + random.randint(0, p - pe - 1)

            for j in range(n):
                
                sourceParent =  eliteParent if random.random() < rhoe else noneliteParent
                
                next_population.population[i].update_allele(j,current_population.population[int(sourceParent)].get_chromossome()[j])   
                
            i += 1
         
        # We'll introduce 'pm' mutants:
        while i < p:
            for j in range(n):
                next_population.population[i].update_allele(j,random.random())
            i += 1
         
        for i in range(int(pe), int(p)):
            next_population.population[i].update_fitness(refDecoder.decode(next_population._getChromossome(i)))

        next_population._sortFitness()
        
        return deepcopy(next_population)
    