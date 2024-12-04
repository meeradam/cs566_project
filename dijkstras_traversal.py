from variables import *
from generate_students import *
from create_weighted_graph import *
from traverse_graphs import *
import time
import matplotlib.pyplot as plt

n_students = [50, 100, 150, 200, 250, 500, 750, 1000, 1250, 1500, 1750, 2000]
# n_students = [100]
dijkstra_time = []

"""
PERFORMING TRAVERSALS ON WEIGHTED GRAPHS
"""

for i in range(len(n_students)):
    start_time = time.time()
    print(f"For {n_students[i]} students")
    max_friends = int(n_students[i]/5)
    print(f"Each student has {max_friends} maximum number of friends")

    df_students = generate_student_list(n_students[i], max_friends, weighted = True)
    # print(df_students)
    created_nodes = create_weighted_graph(df_students)
    # print(created_nodes)

    algorithm = Dijkstra()
    name, node = list(created_nodes.items())[i]
    algorithm.calculate(node)

    target_name, target_node = list(created_nodes.items())[5]
    algorithm.get_shortest_path(node)
    # print(target_name, target_node)
    algorithm.get_shortest_path(target_node)
    dijkstra_time.append((time.time() - start_time) * 1000)

# print(dijkstra_time)
plt.plot(n_students, dijkstra_time)
plt.xlabel('Number of students')
plt.ylabel('Time taken (ms)')
plt.title("Friend Recommendation using Dijkstra's Algorithm")
plt.show()
