# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:31:37 2024

@author: efiel
"""
from HashMap import HashMap
import pandas as pd
import datetime as dt
import math

class Truck:
    
    def __init__(self):
        self.current_location = "HUB"
        self.miles_driven = 0
        self.start_time = None
        self.total_time_elapsed = dt.timedelta()
        self.air_manifest = HashMap()
        self.driver_manifest = HashMap()
        self.package_status = HashMap()
        self.distance_table = pd.read_csv('Real_Distance_Table.csv', index_col=0)

        
        
    def find_next_stop(self):
       if self.air_manifest.is_empty() and self.driver_manifest.is_empty():
           return "HUB"

       if self.air_manifest.is_empty():
           shortest_distance = float('inf')  # Use positive infinity for initialization
           next_stop = None

           for key, package in self.driver_manifest:
               distance = self.distance_table.loc[package.GetAddress(), self.current_location]
               if math.isnan(distance):
                   distance = self.distance_table.loc[self.current_location, package.GetAddress()]
               if distance <= shortest_distance:
                   shortest_distance = distance
                   next_stop = package.GetPackageId()

           if next_stop in self.driver_manifest:
                new_address = self.driver_manifest.get(next_stop).GetAddress()
                return new_address 
           else:
               return "HUB"

       else:
           shortest_distance = float('inf')
           next_stop = None
           
           for key, package in self.air_manifest:
               distance = self.distance_table.loc[package.GetAddress(), self.current_location]
               if math.isnan(distance):
                   distance = self.distance_table.loc[self.current_location, package.GetAddress()]
               if distance <= shortest_distance:
                   shortest_distance = distance
                   next_stop = package.GetPackageId()
                   
           if next_stop in self.air_manifest:
               new_address = self.air_manifest.get(next_stop).GetAddress()
               return new_address
           
           
           
           
           
       

       
        
    def deliver_package(self, nextStop):
        keys_to_delete = []
        for key,package in self.driver_manifest:
            if package.GetAddress() == nextStop:
                keys_to_delete.append(key)
                
        for key,package in self.air_manifest:
            if package.GetAddress() == nextStop:
                keys_to_delete.append(key)
        
        for key in keys_to_delete:
            if key in self.driver_manifest:
                self.save_package_tracking_info(key)
                self.driver_manifest.delete(key)
            if key in self.air_manifest:
                self.save_package_tracking_info(key)
                self.air_manifest.delete(key)
                
                
    def drive_to_stop(self, nextStop):
        distance = self.distance_table.loc[nextStop, self.current_location]
        if math.isnan(distance):
            distance = self.distance_table.loc[self.current_location, nextStop]
        if distance > 0:
            self.miles_driven += distance
            self.current_location = nextStop
            drive_time = dt.timedelta(hours = distance / 18)
            self.total_time_elapsed += (drive_time)
            
            
    def complete_stop(self, nextStop):
        self.drive_to_stop(nextStop)
        self.deliver_package(nextStop)
        
    def run_route(self):
        self.build_package_tracking_info()
        while True:
            next_stop = self.find_next_stop()
            if next_stop == "HUB":
                self.drive_to_stop(next_stop)
                break
            else:
                self.complete_stop(next_stop)
                
                
                
    def build_package_tracking_info(self):
        for key, package in self.driver_manifest:
            package_id = key
            if self.current_location == "HUB":
                location = "HUB"
            else:
                location = "En Route"
            delivery_time = "Still out for delivery"
            self.package_status.add(key, [key, location, delivery_time])
       
        for key, package in self.air_manifest:
            package_id = key
            if self.current_location == "HUB":
                location = "HUB"
            else:
                location = "En Route"
            delivery_time = "Still out for delivery"
            self.package_status.add(key, [key, location, delivery_time])
            
    def print_package_tracking_info(self):
        self.package_status.print_map()
    
        
        
                
                
    def save_package_tracking_info(self, key_to_deliver):
        for key, value in self.package_status:
            if key == key_to_deliver:
                self.package_status.add(key, [key, "Delivered", (self.start_time + self.total_time_elapsed)])
            if value[2] == "HUB":
                self.package_status.add(key, [key, "En Route", "TBD"])
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        