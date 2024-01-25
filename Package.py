# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:31:26 2024

@author: efiel
"""

class Package:
    
    
    def __init__(self,package_id, address, city, state, zip_code, deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        
    def GetPackageId(self):
        return self.package_id
    
    def GetAddress(self):
        return  self.address
    
    def GetCity(self):
        return self.city
    
    def GetState(self):
        return self.state
    
    def GetZipCode(self):
        return self.zip_code
    
    def GetDeadline(self):
        return self.deadline
    
    def GetWeight(self):
        return self.weight