# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:31:37 2024

@author: efiel
"""
from HashMap import HashMap
import pandas as pd

class Truck:
    
    def __init__(self):
        self.current_location = "HUB"
        self.miles_driven = 0
        self.start_time = None
        self.total_time_elapsed = None
        self.air_manifest = HashMap()
        self.driver_manifest = HashMap()
        self.distance_table = pd.read_csv('Real_Distance_Table.csv', index_col=0)

        
        ##### need to make a function that converts miles into time 
        
    def find_next_stop(self):
       if self.air_manifest.is_empty() and self.driver_manifest.is_empty():
           return "HUB"

       if self.air_manifest.is_empty():
           shortest_distance = float('inf')  # Use positive infinity for initialization
           next_stop = None

           for key, package in self.driver_manifest:
               distance = self.distance_table.loc[package.GetAddress(), self.current_location]
               if distance < shortest_distance:
                   next_stop = package.GetPackageId()

           if next_stop in self.driver_manifest:
                new_address = self.driver_manifest.get(next_stop).GetAddress()
                self.driver_manifest.delete(next_stop)
                return new_address

       else:
           return "next air stop"