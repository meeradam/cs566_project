import heapq
import pandas as pd
import ast
import random
import time
from collections import deque, defaultdict
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def dijkstra(self, start_node):
        distances = {node: float('infinity') for node in self.adjacency_list}
        distances[start_node] = 0
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Skip if the current distance is not optimal
            if current_distance > distances[current_node]:
                continue

            # Check neighbors
            for neighbor in self.adjacency_list[current_node]:
                weight = self.edge_weights[(current_node, neighbor)]
                distance = current_distance + weight

                # If a shorter path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def printShortestPaths(self, start_node, n):
        distances = self.dijkstra(start_node)
        # Sort nodes by distance
        sorted_distances = sorted(distances.items(), key=lambda x: x[1])
        # print(f"Shortest paths from {start_node}:")
        for node, distance in sorted_distances[:n]:
            print(f"Node: {node}, Distance: {distance} \n")

# # Load the graph
# student = student_graph.loadGraph('student_adjacency_list.csv')

# # Perform Dijkstra's algorithm for n students
# n = 10  # Number of students to print results for
# start_time = time.time()
# student_graph.printShortestPaths(student, n)
# time_taken = time.time() - start_time
# print(f"Dijkstra's algorithm took {time_taken:.4f} seconds")
