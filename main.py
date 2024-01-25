# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:31:58 2024

@author: efiel

"""
from HashMap import HashMap
import pandas as pd

package_manifest = pd.read_csv('package_file.csv')

print(package_manifest.head())
