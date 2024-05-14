#    Ethan Field Student#: 010155334

from Truck import Truck
from HashMap import HashMap
#import Pandas as pd
from Package import Package

from Pandaz import Pandaz
import datetime as dt



def main():
    
   # pd = Pandaz()
    package_tracking_manifest = HashMap() #used to store all delivery info

    
    package_manifest_df = Pandaz.read_csv('package_file.csv')
    
    package_manifest = [] #used to store the days packages 
    
    #load packages into the system
    for row in package_manifest_df:
        package_instance = Package(*row)
        package_manifest.append(package_instance)
     
    #print(package_manifest)
    hash_map_manifest = HashMap()
    
    for package in package_manifest:
        hash_map_manifest.add(package.GetPackageId(), package)
        
    
    ####   choose the operating day, create the three truck instances and select the start time for the two drivers #############
    chosen_day = dt.datetime(2024,4,19)
    
    truck_one = Truck()
    truck_one.distance_table = Pandaz.read_csv("Real_Distance_table.csv")
    print(f"distance table type: {type(truck_one.distance_table)}")
    #print("distance table data: " + truck_one.distance_table.print_map())
    truck_two = Truck()
    truck_two.distance_table = Pandaz.read_csv("Real_Distance_table.csv")

    truck_three = Truck()
    truck_three.distance_table = Pandaz.read_csv("Real_Distance_table.csv")

    truck_one.start_time = dt.datetime(2024, 4, 19, 8, 0 ,0)
    truck_two.start_time = dt.datetime(2024, 4, 19, 9, 5 ,0)
    
    
    ### POPULATE TRUCK 1 with work ###
  #  hash_map_manifest.print_map()
    #print(hash_map_manifest.get(4))
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
    
    
    truck_one.driver_manifest.add(hash_map_manifest.get(19).GetPackageId(), hash_map_manifest.get(19))
    truck_one.driver_manifest.add(hash_map_manifest.get(17).GetPackageId(), hash_map_manifest.get(17))
    truck_one.driver_manifest.add(hash_map_manifest.get(10).GetPackageId(), hash_map_manifest.get(10))
    
    ### POPULATE TRUCK 2 with work###
    
    truck_two.air_manifest.add(hash_map_manifest.get(6).GetPackageId(), hash_map_manifest.get(6))
    truck_two.air_manifest.add(hash_map_manifest.get(31).GetPackageId(), hash_map_manifest.get(31))
    truck_two.air_manifest.add(hash_map_manifest.get(25).GetPackageId(), hash_map_manifest.get(25))
    truck_two.air_manifest.add(hash_map_manifest.get(29).GetPackageId(), hash_map_manifest.get(29))
    truck_two.air_manifest.add(hash_map_manifest.get(40).GetPackageId(), hash_map_manifest.get(40))

    
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
    
    
    
    ### POPULATE TRUCK 3 with work###
    truck_three.driver_manifest.add(hash_map_manifest.get(9).GetPackageId(), hash_map_manifest.get(9))
    truck_three.driver_manifest.add(hash_map_manifest.get(12).GetPackageId(), hash_map_manifest.get(12))
    truck_three.driver_manifest.add(hash_map_manifest.get(28).GetPackageId(), hash_map_manifest.get(28))
    truck_three.driver_manifest.add(hash_map_manifest.get(2).GetPackageId(), hash_map_manifest.get(2))
    truck_three.driver_manifest.add(hash_map_manifest.get(4).GetPackageId(), hash_map_manifest.get(4))
    truck_three.driver_manifest.add(hash_map_manifest.get(27).GetPackageId(), hash_map_manifest.get(27))
    truck_three.driver_manifest.add(hash_map_manifest.get(33).GetPackageId(), hash_map_manifest.get(33))
    truck_three.driver_manifest.add(hash_map_manifest.get(35).GetPackageId(), hash_map_manifest.get(35))
    
    #Prompt needed info from user
    print("Welcom to the WGUPS Delivery Tracking Portal")
    current_time = input("What is the current time? (HH:MM): ")
    chosen_time_input = dt.datetime.strptime(current_time, "%H:%M").time()
    chosen_time = dt.datetime.combine(chosen_day, chosen_time_input)
    package_to_track = (input("Enter the Package ID for the chose package or press Enter for all packages "))
    
    
    
    
    truck_one.run_route() #truck one delivers entire manifest
    
    truck_two.run_route() #truck two delivers entire manifest before returning to begin truck three
    
    truck_three_earliest_start = dt.datetime(2024,4,19,10,20) #earliest time truck three can start because of last package to arrive at hub from sorting facility
    
    if truck_two.start_time + truck_two.total_time_elapsed >= truck_three_earliest_start: #if driver 2 finishes after 10:20 he can start truck 3 right away
        truck_three.start_time = truck_two.start_time + truck_two.total_time_elapsed
    else:
        truck_three.start_time = truck_three_earliest_start #if driver 2 gets back before 10:20am he will have to wait at the hub for the last package
        
    truck_three.run_route() #Truck 3 runs its route and delivers entire manifest 
    
    for key, value in truck_one.package_status: #populate tracking info with truck ones deliveries 
        delivery_time = value[2].time()
        if delivery_time <= chosen_time.time(): #check to see if package was delivered before chosen time
            location = "Delivered"
            delivery_time = value[2]
        elif chosen_time.time() < truck_one.start_time.time(): #if picked before start time all packages are at the hub
            location = "HUB"
            delivery_time = "TBD"
        else: #if it is not delivered or at the hub then it is on the truck
            location = "En Route"
            delivery_time = "TBD"
        
        package_tracking_manifest.add(key, [key, location, delivery_time])
        
    for key, value in truck_two.package_status: #repeat for truck 2
        delivery_time = value[2].time()
        if delivery_time <= chosen_time.time():
            location = "Delivered"
            delivery_time = value[2]
        elif chosen_time.time() < truck_two.start_time.time():
            location = "HUB"
            delivery_time = "TBD"
        else:
            location = "En Route"
            delivery_time = "TBD"
        
        package_tracking_manifest.add(key, [key, location, delivery_time])
        
    for key, value in truck_three.package_status: #repeat for truck 3
        delivery_time = value[2].time()
        if delivery_time <= chosen_time.time():
            location = "Delivered"
            delivery_time = value[2]
        elif chosen_time.time() < truck_three.start_time.time():
            location = "HUB"
            delivery_time = "TBD"
        else:
            location = "En Route"
            delivery_time = "TBD"
        
        package_tracking_manifest.add(key, [key, location, delivery_time])
    
    
    
    if package_to_track == "": #if all packages then print all required info for display and calculate total milage for display
        for key, value in package_tracking_manifest:
            print(f'Package ID: {value[0]}')
            print(f'    Package Status/location: {value[1]}')
            print(f'    Delivery Time: {value[2]}')
            print()
        total_miles = truck_one.caluclate_milage_at_time(chosen_time) + truck_two.caluclate_milage_at_time(chosen_time) + truck_three.caluclate_milage_at_time(chosen_time)
        print(f"The total miles traveled by truck 1 at {chosen_time.time()} is {truck_one.caluclate_milage_at_time(chosen_time)}")
        print(f"The total miles traveled by truck 2 at {chosen_time.time()} is {truck_two.caluclate_milage_at_time(chosen_time)}")
        print(f"The total miles traveled by truck 3 at {chosen_time.time()} is {truck_three.caluclate_milage_at_time(chosen_time)}")
        print(f"The total miles traveld by all trucks at {chosen_time.time()} is {total_miles}")
    
    else: #if the user wants to see a specific package then iterate through the days manifest and print all info for display
        if int(package_to_track) in package_tracking_manifest:
            for key, value in package_tracking_manifest:
                if key == int(package_to_track):
                     print(f'Package ID: {value[0]}')
                     print(f'    Package Status/location: {value[1]}')
                     print(f'    Delivery Time: {value[2]}')
                     print()
            total_miles = truck_one.caluclate_milage_at_time(chosen_time) + truck_two.caluclate_milage_at_time(chosen_time) + truck_three.caluclate_milage_at_time(chosen_time)
            print(f"The total miles traveled by truck 1 at {chosen_time.time()} is {truck_one.caluclate_milage_at_time(chosen_time)}")
            print(f"The total miles traveled by truck 2 at {chosen_time.time()} is {truck_two.caluclate_milage_at_time(chosen_time)}")
            print(f"The total miles traveled by truck 3 at {chosen_time.time()} is {truck_three.caluclate_milage_at_time(chosen_time)}")
            print(f"The total miles traveld by all trucks at {chosen_time.time()} is {total_miles}")
        else:
            print("Sorry, that package was not found in todays deliveries.")
            

    
if __name__ == "__main__":
    main()








