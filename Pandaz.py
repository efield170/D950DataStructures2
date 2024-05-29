# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 05:39:29 2024

@author: efiel
"""

from HashMap import HashMap
from Package import Package


class Pandaz(object):
    #def __init__(self):
    #   self.distance_table = None
    
    @staticmethod
    def read_csv(file_path):
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = line.strip().split(',')
                if len(parsed_line) > 8 and len(parsed_line) < 12:  ###this is going to cause problems so I need to sepearate into two functions 
                    notes = ','.join(parsed_line[7:]) ## maybe add an and statment for if the parsed line is < 15 or something 
                    parsed_line = parsed_line[:7] + [notes]
                data.append(parsed_line)
       # print(data)
        return data
    
    def __iter__(self):
        for row in self.data:
            yield row
    
    def load_packages_from_csv(self,file_path):
        package_data = self.read_csv(file_path)
        package_map = HashMap()
        for row in package_data:
            package_instance = Package(*row)
            package_map.add(package_instance.GetPackageId(), package_instance)
        return package_map
    
    @staticmethod        
    def load_distance_table(file_path):
        data = Pandaz.read_csv(file_path)
        headers = data[0]
        distance_map = HashMap()
        for row in data[1:]:
            row_map = HashMap()
            for i in range(1,len(row)):
              #  print(type(row[i]), row[i])
                if row[i] == '':
                    row_map.add(headers[i], None) #if distance map value is empty assign none 

                else:    
                    row_map.add(headers[i], float(row[i]))
            distance_map.add(row[0], row_map)
        #print(type(distance_map))
        #distance_map.print_map()  removed 5/29
        return distance_map
        
    @staticmethod
    def get_distance(start, end):
        distance_table = Pandaz.load_distance_table("Real_Distance_Table.csv")
        if distance_table is not None:
            start_map = distance_table.find(start)
            if start_map is not None:
                distance = start_map.find(end)
                if distance is not None:
                    return distance
        return None