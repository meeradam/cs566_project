from collections import deque
import pandas as pd
from collections import defaultdict
import time
import heapq

# student_graph_file = 'student_adjacency_list.csv'
#student = student_graph_file['Node'][0]

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def loadGraph(self, df):
        # df = pd.read_csv(file_name, header=None, names=['Node', 'Friend'])
        student = df['Node'][1]
        adjacency_dict = defaultdict(list)
        for _, row in df.iterrows():
            node = row["Node"].strip()
            friend = row["Friends"].strip()
            adjacency_dict[node].append(friend)

        # Convert defaultdict to a regular dictionary
        self.adjacency_list = dict(adjacency_dict)
        return student
        
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
            traversal_order.append(current_node)
            #print(current_node)
            for adjacent_node in self.adjacency_list[current_node]:
                if adjacent_node not in visited:
                    visited.add(adjacent_node)

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
    
    def getFriendList(self, traversal_order, node):

        direct_friends = set(self.adjacency_list.get(node, []))
        # print(direct_friends)
        friend_list = {}

        for friend in traversal_order:
            if friend not in direct_friends and friend != node:
                mutual_friends = len(direct_friends & set(self.adjacency_list.get(friend, [])))
                friend_list[friend] = mutual_friends
            
        return sorted(friend_list.items(), key=lambda x: -x[1])
    
    def recommendFriends(self, friend_list, n_mutual_friend):
        """
        Recommend friends with at least more than equal to the defined number of mutual friends
        """
        recommended_friends = []
        for i in range(len(friend_list)):
            if int(friend_list[i][1]) >= n_mutual_friend:
                recommended_friends.append(friend_list[i][0])
        #print(recommended_friends)
        return recommended_friends


def get_student_graph(df):
    student_graph = Graph()
    student = student_graph.loadGraph(df)
    return student, student_graph
# student_graph.printGraph()

# BFS
def BFS(student_graph, student):
    # print("Performing BFS traversal")
    start_time = time.time()
    bfs_traversal_order = student_graph.bfs(student)
    friend_list = student_graph.getFriendList(bfs_traversal_order, student)
    # print(friend_list)
    recommended_friends = student_graph.recommendFriends(friend_list, 2)
    time_taken = time.time() - start_time
    # print(f"Took {time_taken}s")
    return recommended_friends, time_taken

# DFS
def DFS(student_graph, student):
    # print("Performing DFS traversal")
    start_time = time.time()
    dfs_traversal_order = student_graph.dfs(student)
    friend_list = student_graph.getFriendList(dfs_traversal_order, student)
    # print(friend_list)
    recommended_friends = student_graph.recommendFriends(friend_list, 2)
    time_taken = time.time() - start_time
    # print(f"Took {time_taken}s")
    return recommended_friends, time_taken

# Dijkstra Algorithm
class Dijkstra:
    def __init__(self):
        self.heap = []
    
    def calculate(self, start_node):
        print(start_node)
        start_node.min_distance = 0
        heapq.heappush(self.heap, start_node)
        
        while self.heap:
            # pop element with the lowest distance
            actual_node = heapq.heappop(self.heap)
            if actual_node.visited:
                continue
            #  consider the neighbors
            for edge in actual_node.neighbours:
                # print(edge)
                start = edge.start_node
                target = edge.target_node
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    # update the heap
                    heapq.heappush(self.heap, target)
                    # [F-19, F-17]
            actual_node.visited = True
    
    def get_shortest_path(self, node):
        print(f"The shortest path to the vertext is: {node.min_distance}")
        actual_node = node
        while actual_node is not None:
            print(actual_node.name, end=" ")
            actual_node = actual_node.predecessor

df = pd.read_csv('student_adjacency_list.csv')
student, student_graph = get_student_graph(df)
print(student)
recommended_friends, time_taken = BFS(student_graph, student)
print(recommended_friends)