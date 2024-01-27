# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:31:37 2024

@author: efiel
"""
from HashMap import HashMap

class Truck:
    
    def __init__(self):
        self.miles = 0
        self.start_time = None
        self.total_time = None
        self.air_manifest = HashMap()
        self.driver_manifest = HashMap()
        
        ##### need to make a function that converts miles into time 
        