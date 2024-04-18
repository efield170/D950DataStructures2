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


print(truck_one.find_next_stop())

truck_one.driver_manifest.add(hash_map_manifest.get(5).GetPackageId(), hash_map_manifest.get(5))
truck_one.driver_manifest.add(hash_map_manifest.get(7).GetPackageId(), hash_map_manifest.get(7))



print(truck_one.find_next_stop())
print(truck_one.find_next_stop())
print(truck_one.find_next_stop())




####################################################################








