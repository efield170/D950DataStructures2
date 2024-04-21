# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:31:58 2024

@author: efiel

"""
from Truck import Truck
from HashMap import HashMap
from Package import Package
import pandas as pd
import datetime as dt



def main():
    
    package_tracking_manifest = HashMap()


    package_manifest_df = pd.read_csv('package_file.csv', header= None)
    
    package_manifest = []
    
    
    for i, row in package_manifest_df.iterrows():
        package_instance = Package(row[0],row[1],row[2],row[3],row[4],row[5],row[6], row[7])
        package_manifest.append(package_instance)
        
    hash_map_manifest = HashMap()
    
    for package in package_manifest:
        hash_map_manifest.add(package.GetPackageId(), package)
        
    ##print("checking p[ackage ID 1 existence:", hash_map_manifest.get(15))
        
    ###################################################################
    
    
    ###################################################################
    
    ####   create the three truck instances and load them #############
    
    truck_one = Truck()
    truck_two = Truck()
    truck_three = Truck()
    truck_one.start_time = dt.datetime(2024, 4, 19, 8, 0 ,0)
    truck_two.start_time = dt.datetime(2024, 4, 19, 8, 0 ,0)
    
    
    ### POPULATE TRUCK 1###
    
    truck_one.air_manifest.add(hash_map_manifest.get(15).GetPackageId(), hash_map_manifest.get(15))
    truck_one.air_manifest.add(hash_map_manifest.get(34).GetPackageId(), hash_map_manifest.get(34))
    truck_one.air_manifest.add(hash_map_manifest.get(16).GetPackageId(), hash_map_manifest.get(16))
    truck_one.air_manifest.add(hash_map_manifest.get(20).GetPackageId(), hash_map_manifest.get(20))
    truck_one.air_manifest.add(hash_map_manifest.get(21).GetPackageId(), hash_map_manifest.get(21))
    truck_one.air_manifest.add(hash_map_manifest.get(13).GetPackageId(), hash_map_manifest.get(13))
    truck_one.air_manifest.add(hash_map_manifest.get(39).GetPackageId(), hash_map_manifest.get(39))
    truck_one.air_manifest.add(hash_map_manifest.get(8).GetPackageId(), hash_map_manifest.get(8))
    truck_one.air_manifest.add(hash_map_manifest.get(30).GetPackageId(), hash_map_manifest.get(30))
    truck_one.air_manifest.add(hash_map_manifest.get(5).GetPackageId(), hash_map_manifest.get(5))
    truck_one.air_manifest.add(hash_map_manifest.get(37).GetPackageId(), hash_map_manifest.get(37))
    truck_one.air_manifest.add(hash_map_manifest.get(1).GetPackageId(), hash_map_manifest.get(1))
    truck_one.air_manifest.add(hash_map_manifest.get(14).GetPackageId(), hash_map_manifest.get(14))
    
    #print(truck_one.driver_manifest.print_map())
    
    truck_one.driver_manifest.add(hash_map_manifest.get(19).GetPackageId(), hash_map_manifest.get(19))
    truck_one.driver_manifest.add(hash_map_manifest.get(17).GetPackageId(), hash_map_manifest.get(17))
    truck_one.driver_manifest.add(hash_map_manifest.get(10).GetPackageId(), hash_map_manifest.get(10))
    
    ### POPULATE TRUCK 2###
    
    truck_two.air_manifest.add(hash_map_manifest.get(6).GetPackageId(), hash_map_manifest.get(6))
    truck_two.air_manifest.add(hash_map_manifest.get(31).GetPackageId(), hash_map_manifest.get(31))
    truck_two.air_manifest.add(hash_map_manifest.get(26).GetPackageId(), hash_map_manifest.get(26))
    truck_two.air_manifest.add(hash_map_manifest.get(29).GetPackageId(), hash_map_manifest.get(29))
    
    
    truck_two.driver_manifest.add(hash_map_manifest.get(3).GetPackageId(), hash_map_manifest.get(3))
    truck_two.driver_manifest.add(hash_map_manifest.get(18).GetPackageId(), hash_map_manifest.get(18))
    truck_two.driver_manifest.add(hash_map_manifest.get(38).GetPackageId(), hash_map_manifest.get(38))
    truck_two.driver_manifest.add(hash_map_manifest.get(36).GetPackageId(), hash_map_manifest.get(36))
    truck_two.driver_manifest.add(hash_map_manifest.get(32).GetPackageId(), hash_map_manifest.get(32))
    truck_two.driver_manifest.add(hash_map_manifest.get(26).GetPackageId(), hash_map_manifest.get(26))
    truck_two.driver_manifest.add(hash_map_manifest.get(7).GetPackageId(), hash_map_manifest.get(7))
    truck_two.driver_manifest.add(hash_map_manifest.get(22).GetPackageId(), hash_map_manifest.get(22))
    truck_two.driver_manifest.add(hash_map_manifest.get(24).GetPackageId(), hash_map_manifest.get(24))
    truck_two.driver_manifest.add(hash_map_manifest.get(23).GetPackageId(), hash_map_manifest.get(23))
    truck_two.driver_manifest.add(hash_map_manifest.get(11).GetPackageId(), hash_map_manifest.get(11))
    truck_two.driver_manifest.add(hash_map_manifest.get(12).GetPackageId(), hash_map_manifest.get(12))
    
    
    
    ### POPULATE TRUCK 3###
    truck_three.driver_manifest.add(hash_map_manifest.get(9).GetPackageId(), hash_map_manifest.get(9))
    truck_three.driver_manifest.add(hash_map_manifest.get(40).GetPackageId(), hash_map_manifest.get(40))
    truck_three.driver_manifest.add(hash_map_manifest.get(28).GetPackageId(), hash_map_manifest.get(28))
    truck_three.driver_manifest.add(hash_map_manifest.get(2).GetPackageId(), hash_map_manifest.get(2))
    truck_three.driver_manifest.add(hash_map_manifest.get(4).GetPackageId(), hash_map_manifest.get(4))
    truck_three.driver_manifest.add(hash_map_manifest.get(27).GetPackageId(), hash_map_manifest.get(27))
    truck_three.driver_manifest.add(hash_map_manifest.get(33).GetPackageId(), hash_map_manifest.get(33))
    truck_three.driver_manifest.add(hash_map_manifest.get(35).GetPackageId(), hash_map_manifest.get(35))
    
    #Prompt needed info from user
    print("Welcom to the WGUPS Delivery Tracking Portal")
    current_time = input("What is the current time? (HH:MM): ")
    chosen_time = dt.datetime.strptime(current_time, "%H:%M")
    package_to_track = (input("Enter the Package ID for the chose package or press Enter for all packages "))
    
    
    
    
    truck_one.run_route()
    truck_two.run_route()
    
    truck_three_earliest_start = dt.datetime(2024,4,19,10,20)
    
    if truck_two.start_time + truck_two.total_time_elapsed >= truck_three_earliest_start:
        truck_three.start_time = truck_two.start_time + truck_two.total_time_elapsed
    else:
        truck_three.start_time = truck_three_earliest_start
        
    truck_three.run_route()
    
    for key, value in truck_one.package_status:
        delivery_time = value[2].time()
        if delivery_time <= chosen_time.time():
            location = "Delivered"
            delivery_time = value[2]
        else:
            location = "En Route"
            delivery_time = "TBD"
        
        package_tracking_manifest.add(key, [key, location, delivery_time])
        
    for key, value in truck_two.package_status:
        delivery_time = value[2].time()
        if delivery_time <= chosen_time.time():
            location = "Delivered"
            delivery_time = value[2]
        else:
            location = "En Route"
            delivery_time = "TBD"
        
        package_tracking_manifest.add(key, [key, location, delivery_time])
        
    for key, value in truck_three.package_status:
        delivery_time = value[2].time()
        if delivery_time <= chosen_time.time():
            location = "Delivered"
            delivery_time = value[2]
        if chosen_time.time() < truck_three.start_time.time():
            location = "HUB"
            delivery_time = "TBD"
        else:
            location = "En Route"
            delivery_time = "TBD"
        
        package_tracking_manifest.add(key, [key, location, delivery_time])
    
    
   # package_tracking_manifest.print_map()
    
    if package_to_track == "":
        for key, value in package_tracking_manifest:
            print(f'Package ID: {value[0]}')
            print(f'    Package Status/location: {value[1]}')
            print(f'    Delivery Time: {value[2]}')
            print()
            
    else:
        if int(package_to_track) in package_tracking_manifest:
            for key, value in package_tracking_manifest:
                if key == int(package_to_track):
                     print(f'Package ID: {value[0]}')
                     print(f'    Package Status/location: {value[1]}')
                     print(f'    Delivery Time: {value[2]}')
                     print()
        else:
            print("Sorry, that package was not found in todays deliveries.")
            
    print(truck_three.start_time)

    
   # print(truck_one.miles_driven)
    #print(truck_one.total_time_elapsed)
  #  truck_one.print_package_tracking_info()
    
   # print(truck_two.miles_driven)
  #  print(truck_two.total_time_elapsed)
    #truck_two.print_package_tracking_info()
    
    #print(truck_three.miles_driven)
    #print(truck_three.total_time_elapsed)
    #truck_three.print_package_tracking_info()
    
    ####################################################################
    
if __name__ == "__main__":
    main()








