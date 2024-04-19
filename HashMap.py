# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 18:03:30 2024

@author: efiel
"""

class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size
        
    def getHash(self, key):
        hash = 1234
        for char in str(key):
            hash = (hash * 15) ^ ord(char)
        return hash % self.size
        
    def add(self, key, value):
        key_hash = self.getHash(key)
        key_value = [key, value]
        
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
        
        
    def get(self, key):
        key_hash = self.getHash(key)
        
        if self.map[key_hash] is not None:
            for value_pair in self.map[key_hash]:
                if value_pair[0] == key:
                    return value_pair[1]
        return None
        
    def delete(self, key):
        key_hash = self.getHash(key)
        
        if self.map[key_hash] is None:
            return False
        
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        
    def is_empty(self):
        for bucket in self.map:
            if bucket is not None:
                return False
        return True
        
        
    def __iter__(self):
        for item in self.map:
            if item is not None:
                for key, value in item:
                    yield key,value
        
        
    def __contains__(self, key):
        key_hash = self.getHash(key)
        bucket = self.map[key_hash]
        if bucket is not None:
            for (k, _) in bucket:
                if k == key:
                    return True
        return False
        
    def print_map(self):
        print("Current HashMap:")
        for index, bucket in enumerate(self.map):
            if bucket:
                print(f"Bucket {index}:")
                for key, value in bucket:
                    print(f"  - Key: {key}, Value: {value}")
            else:
                print(f"Bucket {index}: Empty")