from collections import deque
import pandas as pd
from collections import defaultdict

student_graph_file = 'student_adjacency_list.csv'

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


student_graph = Graph()
student_graph.loadGraph(student_graph_file)
# student_graph.printGraph()

student_graph.bfs('Kaylee Wise')