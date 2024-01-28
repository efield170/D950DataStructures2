# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:31:37 2024

@author: efiel
"""
from HashMap import HashMap

class Truck:
    
    def __init__(self):
        self.current_location = "HUB"
        self.miles_driven = 0
        self.start_time = None
        self.total_time_elapsed = None
        self.air_manifest = HashMap()
        self.driver_manifest = HashMap()
        
        ##### need to make a function that converts miles into time 
        
    def find_next_stop(self):
        
        if self.air_manifest.is_empty() and self.driver_manifest.is_empty():
            return "HUB"
        
        if self.air_manifest.is_empty():
            
            for key, package in self.driver_manifest:
                print("test")
            
            return "next ground stop"
        
        else: 
            return "next air stop"