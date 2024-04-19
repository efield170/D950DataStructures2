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
        self.package_status = {}
        #self.current_package_id = None;
        self.distance_table = pd.read_csv('Real_Distance_Table.csv', index_col=0)

        
        ##### need to make a function that converts miles into time 
        
    def find_next_stop(self):
       if self.air_manifest.is_empty() and self.driver_manifest.is_empty():
           #print("both manifests are empty")
           # put in sperate function for distance self.miles_driven += self.distance_table.loc["HUB", self.current_location]
           #self.current_package_id = None
           #print("I got called")
           return "HUB"

       if self.air_manifest.is_empty():
           #print("air maifest is emtpy")
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
                # put in seperate function for distance self.miles_driven += self.distance_table.loc[new_address, self.current_location]
                # put in seperate function for deleting self.driver_manifest.delete(next_stop)
               # self.current_location = new_address
                #self.current_package_id = next_stop
                return new_address 
           else:
              
               #self.current_package_id = None
               #print("now I got called")
               return "HUB"

       else:
          # print("I am called")
           shortest_distance = float('inf')
           next_stop = None
           
           for key, package in self.air_manifest:
               distance = self.distance_table.loc[package.GetAddress(), self.current_location]
               if math.isnan(distance):
                   distance = self.distance_table.loc[self.current_location, package.GetAddress()]
                   #print(f'Package ID: {package.GetPackgeID()}, Distance: {distance}')
               if distance <= shortest_distance:
                   shortest_distance = distance
                   next_stop = package.GetPackageId()
                   #print(f"Shortest distance updated: {shortest_distance}, Next Stop: {next_stop}")
                   
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
                #print(f'deleting key {key}')
                self.driver_manifest.delete(key)
            if key in self.air_manifest:
                self.save_package_tracking_info(key)
                #print(f'deleting key {key}')
                self.air_manifest.delete(key)
                
                
    def drive_to_stop(self, nextStop):
       # print(f'next stop: {nextStop}, current location: {self.current_location}')
        distance = self.distance_table.loc[nextStop, self.current_location]
        if math.isnan(distance):
            distance = self.distance_table.loc[self.current_location, nextStop]
       # print(f"Distance: {distance}")
        if distance > 0:
            self.miles_driven += distance
            self.current_location = nextStop
            drive_time = dt.timedelta(hours = distance / 18)
            self.total_time_elapsed += (drive_time)
            
            
    def complete_stop(self, nextStop):
        #nextStop = self.find_next_stop()
        self.drive_to_stop(nextStop)
        self.deliver_package(nextStop)
        #save package delivery info 
        
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
            self.package_status[key] = [key, location, delivery_time]
       # print(self.package_status)
       
        for key, package in self.air_manifest:
            package_id = key
            if self.current_location == "HUB":
                location = "HUB"
            else:
                location = "En Route"
            delivery_time = "Still out for delivery"
            self.package_status[key] = [key, location, delivery_time]
            
    def print_package_tracking_info(self):
        print(self.package_status)
        
        
                
                
    def save_package_tracking_info(self, key_to_deliver):
        for key, value in self.package_status.items():
            if key == key_to_deliver:
                self.package_status[key] = [key, "Delivered", (self.start_time + self.total_time_elapsed)]
            if value[2] == "HUB":
                self.package_status[key][2] == "En Route"
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        