#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 21:21:34 2021

@author: fpgdesa
"""
 
class individual:
    
    def __init__(self, n):
        
        self.chromossome = n*[0]
        self.fitness =  0       
        
    def get_chromossome(self):
        return self.chromossome
    
    def get_fitness(self):
        return self.fitness
    
    def update_allele(self, i, value):
        self.chromossome[i] = value
        
    def update_fitness(self, value):
        self.fitness = value
        
    