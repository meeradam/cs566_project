import heapq

created_nodes = {}

class Edge:
    def __init__(self, weight, start_node, target_node):
        self.weight = weight
        self.start_node = start_node
        self.target_node = target_node

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False

        self.predecessor = None
        self.neighbours = []
        self.min_distance = float("inf")
    
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    def addEdge(self, weight, target_node):
        edge = Edge(weight, self, target_node)
        self.neighbours.append(edge)
    
def create_weighted_graph(df):
    for i in df['student_name']:
        if i not in created_nodes:
            source_node = Node(i)
            created_nodes[i]  = source_node
        else:
            source_node = created_nodes[i]
        
        source_weight = df['college_distance_from_BU'][df['student_name']==i]
        #print(source_weight)
        # print(source_node)
        friend = df['friends'].loc[df['student_name'] == i]
        if isinstance(friend.iloc[0], list):
            friend = friend.iloc[0]
        else:
            friend = ast.literal_eval(friend.iloc[0])
        for j in friend:
            #print(j)
            friend_weight = df['college_distance_from_BU'][df['student_name'] == j].iloc[0]
            # print(source_weight)
            # print(friend_weight)
            edge_weight = abs(int(source_weight) - int(friend_weight)) + 1            # print(edge_weight)
            if j not in created_nodes:
                # create friend node
                friend_node = Node(j)
                created_nodes[j] = friend_node
            else:
                friend_node = created_nodes[j]
            source_node.addEdge(edge_weight, friend_node)
    return created_nodes
