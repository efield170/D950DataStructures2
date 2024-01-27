# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:06:25 2024

@author: efiel
"""

import numpy as np

def nearest_neighbor(graph):
    num_nodes = len(graph)
    unvisited = set(range(1, num_nodes))  # Nodes are labeled from 1 to num_nodes - 1
    path = [0]  # Starting from node 0

    while unvisited:
        current_node = path[-1]
        nearest_neighbor = min(unvisited, key=lambda x: graph[current_node][x])
        path.append(nearest_neighbor)
        unvisited.remove(nearest_neighbor)

    # Return to the starting node to complete the cycle
    path.append(path[0])
    return path

# Example usage:
# Define a distance matrix (graph) for the traveling salesman problem
graph = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])

result_path = nearest_neighbor(graph)
print("Nearest Neighbor Path:", result_path)
