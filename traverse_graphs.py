from collections import deque
import pandas as pd
from collections import defaultdict

student_graph_file = 'student_adjacency_list.csv'
student = 'James Robbins'

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def loadGraph(self, file_name):
        df = pd.read_csv(file_name, header=None, names=['Node', 'Friend'])
        adjacency_dict = defaultdict(list)
        for _, row in df.iterrows():
            node = row["Node"].strip()
            friend = row["Friend"].strip()
            adjacency_dict[node].append(friend)

        # Convert defaultdict to a regular dictionary
        self.adjacency_list = dict(adjacency_dict)
        
    def printGraph(self):
        for node, friends in self.adjacency_list.items():
            print(f"{node} : {friends}")
    
    def bfs(self, node):
        visited = set()
        visited.add(node)
        traversal_order = []

        queue = deque([node])
        while queue:
            current_node = queue.popleft()
            #print(current_node)
            for adjacent_node in self.adjacency_list[current_node]:
                if adjacent_node not in visited:
                    visited.add(adjacent_node)
                    traversal_order.append(current_node)
                    queue.append(adjacent_node)
        return traversal_order

    def dfs(self, node):
        visited = set()
        stack = [node]
        traversal_order = []
        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                # print(current_node)
                visited.add(current_node)
                traversal_order.append(current_node)
                for adjacent_node in self.adjacency_list[current_node]:
                    if adjacent_node not in visited:
                        stack.append(adjacent_node)

        return traversal_order
    
    def recommendFriends(self, traversal_order, node):

        direct_friends = set(self.adjacency_list.get(node, []))
        # print(direct_friends)
        recommendations = {}

        for friend in traversal_order:
            if friend not in direct_friends and friend != node:
                mutual_friends = len(direct_friends & set(self.adjacency_list.get(friend, [])))
                recommendations[friend] = mutual_friends
            
        return sorted(recommendations.items(), key=lambda x: -x[1])



student_graph = Graph()
student_graph.loadGraph(student_graph_file)
# student_graph.printGraph()

# BFS
bfs_traversal_order = student_graph.bfs(student)
print(student_graph.recommendFriends(bfs_traversal_order, student))

# DFS
# dfs_traversal_order = student_graph.dfs(student)
# print(student_graph.recommendFriends(dfs_traversal_order, student))

