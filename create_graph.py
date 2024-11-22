import pandas as pd
import ast

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addNode(self, node):
        if node not in self.adjacency_list.keys():
            self.adjacency_list[node] = []
            return True
        return False
    
    def printGraph(self):
        for node in self.adjacency_list:
            print(f"{node} : {self.adjacency_list[node]}")
    
    def addEdge(self, node1, node2):
        if node1 in self.adjacency_list.keys() and node2 in self.adjacency_list.keys():
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)
            return True
        return False
    
    def saveGraph(self):
        df = pd.DataFrame([(node, friend) for node, friends in self.adjacency_list.items() for friend in friends], columns = ['Node', 'Friends'])
        # df.to_csv('student_adjacency_list.csv', index=False)
        return df

def create_student_graph(df):
    student_graph = Graph()
    for i in df['student_name']:
        student_graph.addNode(i)
        friend = df['friends'].loc[df['student_name'] == i]
        if isinstance(friend.iloc[0], list):
            friend = friend.iloc[0]
        else:
            friend = ast.literal_eval(friend.iloc[0])
        for j in friend:
            # print(j)
            student_graph.addEdge(i, j)
    
    df = student_graph.saveGraph()
    return df
