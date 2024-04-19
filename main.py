# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:31:58 2024

@author: efiel

"""
from Truck import Truck
from HashMap import HashMap
from Package import Package
import pandas as pd

### code to read package file, initialzie hash map and populate it###### 


package_manifest_df = pd.read_csv('package_file.csv')

package_manifest = []


for i, row in package_manifest_df.iterrows():
    package_instance = Package(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
    package_manifest.append(package_instance)
    
hash_map_manifest = HashMap()

for package in package_manifest:
    hash_map_manifest.add(package.GetPackageId(), package)
    
###################################################################


###################################################################

####   create the three truck instances and load them #############

truck_one = Truck()
truck_two = Truck()
truck_three = Truck()

print(f'current location {truck_one.current_location}')
#print(truck_one.find_next_stop())
print(truck_one.miles_driven)
print(truck_one.total_time_elapsed)


truck_one.driver_manifest.add(hash_map_manifest.get(5).GetPackageId(), hash_map_manifest.get(5))
truck_one.driver_manifest.add(hash_map_manifest.get(7).GetPackageId(), hash_map_manifest.get(7))

#print(truck_one.driver_manifest.print_map())
#print(f'current location {truck_one.current_location}')

# print(truck_one.find_next_stop())
# stop = truck_one.find_next_stop()
# truck_one.drive_to_stop(stop)
# truck_one.deliver_package(stop)
# print(truck_one.miles_driven)
# print(truck_one.total_time_elapsed)
# print(f'current location {truck_one.current_location}')

# #print(truck_one.driver_manifest.print_map())

# print(truck_one.find_next_stop())
# stop2 = truck_one.find_next_stop()
# truck_one.drive_to_stop(stop2)
# truck_one.deliver_package(stop2)
# print(truck_one.miles_driven)
# print(truck_one.total_time_elapsed)
# #print(truck_one.driver_manifest.print_map())


# print(f'current location {truck_one.current_location}')

# print("stop 3 return to hub")
# print(truck_one.find_next_stop())
# stop3 = truck_one.find_next_stop()
# truck_one.drive_to_stop(stop3)
# #truck_one.deliver_package(stop3)
# print(truck_one.miles_driven)
# print(truck_one.total_time_elapsed)

# print(f'current location {truck_one.current_location}')

truck_one.run_route()
#truck_one.complete_stop()
#truck_one.complete_stop()

print(truck_one.miles_driven)
print(truck_one.total_time_elapsed)



####################################################################








