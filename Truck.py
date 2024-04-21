# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:31:37 2024

@author: efiel
"""
from HashMap import HashMap
import pandas as pd
import datetime as dt
import math

class Truck: #I decided an OOP approach would be the easiest/cleanest method 
    
    def __init__(self):
        self.current_location = "HUB"
        self.miles_driven = 0
        self.start_time = None
        self.total_time_elapsed = dt.timedelta()
        self.air_manifest = HashMap() #Holds all packages with an ealry delivery time loaded on truck
        self.driver_manifest = HashMap() #Holds all EOD packages loaded on truck
        self.package_status = HashMap() #Holds all delivery info for this truck
        self.distance_table = pd.read_csv('Real_Distance_Table.csv', index_col=0)

        
        
    def find_next_stop(self): #nearest neighbor algo to find next stop and return the address as a string
       if self.air_manifest.is_empty() and self.driver_manifest.is_empty(): 
           return "HUB" #if both manifests are empty the route is finished and should return to the hub

       if self.air_manifest.is_empty():      #if air is delivered start on ground
           shortest_distance = float('inf')  # Use positive infinity for initialization so first comparison is always true 
           next_stop = None

           for key, package in self.driver_manifest:  #iterate over ground manifest to find the next shortest distance stop
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

       else: #deliver air packages first using same algo as above and return the string address
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
           
           
           
           
           
       

       
        
    def deliver_package(self, nextStop):         #This function handles the driver delivering the package
        keys_to_delete = []                      #it takes the address provided to it and looks through all the mainfests to find matching keys
        for key,package in self.driver_manifest: #and then adds thsoe keys to a list 
            if package.GetAddress() == nextStop:
                keys_to_delete.append(key)
                
        for key,package in self.air_manifest:
            if package.GetAddress() == nextStop:
                keys_to_delete.append(key)
        
        for key in keys_to_delete:              #it then iterates over that list to delete those keys from either the driver or air manifest
            if key in self.driver_manifest:
                self.save_package_tracking_info(key)
                self.driver_manifest.delete(key)
            if key in self.air_manifest:
                self.save_package_tracking_info(key)
                self.air_manifest.delete(key)
                
                
    def drive_to_stop(self, nextStop): #this function handles adding the distance and time for each delivery
        distance = self.distance_table.loc[nextStop, self.current_location]
        if math.isnan(distance): #find the distance between the two stops by finding which orientation provides a value
            distance = self.distance_table.loc[self.current_location, nextStop]
        if distance > 0: #if distance is not negative update time elapsed, current stop and miles
            self.miles_driven += distance
            self.current_location = nextStop
            drive_time = dt.timedelta(hours = distance / 18)
            self.total_time_elapsed += (drive_time)
            
            
    def complete_stop(self, nextStop): #function to help make logic more clear and simulate a real driver 
        self.drive_to_stop(nextStop)
        self.deliver_package(nextStop)
        
    def run_route(self): ##function to help make logic more clear and simulate a real driver 
        self.build_package_tracking_info()
        while True:
            next_stop = self.find_next_stop()
            if next_stop == "HUB":
                self.drive_to_stop(next_stop)
                break #escape loop and stop tracking info when you return to hub and day is up
            else:
                self.complete_stop(next_stop)
                
                
                
    def build_package_tracking_info(self): #build the data structure that is going to store delivery info for later display
        for key, package in self.driver_manifest: 
            package_id = key
            if self.current_location == "HUB": 
                location = "HUB"
            else: #this else statement is no longer needed as all routes start at the HUB but is here to catch any unknow starting locations
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
            
    def print_package_tracking_info(self): #function used for testing and development 
        self.package_status.print_map()
    
        
        
                
                
    def save_package_tracking_info(self, key_to_deliver): #used to update the package status with either delivered or en route if the truck has left the hub and made its first delivery
        for key, value in self.package_status:
            if key == key_to_deliver:
                self.package_status.add(key, [key, "Delivered", (self.start_time + self.total_time_elapsed)])
            if value[2] == "HUB":
                self.package_status.add(key, [key, "En Route", "TBD"])
                
    
    def calculate_elapsed_time(self, current_time): #calculate the amount of time since the truck started delivering
        return (current_time - self.start_time).total_seconds() / 3600 #convert to hours
    
    def caluclate_milage_at_time(self, current_time): #calculate how many miles have been driven at a certain time 
        elapsed_time = self.calculate_elapsed_time(current_time)
        if elapsed_time < 0:
            return 0
        distance_traveled = elapsed_time * 18#mph average 
        if self.miles_driven < distance_traveled:
            return self.miles_driven
        return distance_traveled
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        