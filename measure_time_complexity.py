import time
from generate_students import *
from create_graph import *
from traverse_graphs import *
import matplotlib.pyplot as plt

# n_students = [50, 100, 150, 200, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 5000]
n_students = [50, 100, 150, 200, 250, 500, 750]

total_time_bfs = []
total_time_dfs = []

recommend_friends_bfs = []
recommend_friends_dfs = []

for i in range(len(n_students)):
    print(f"For {n_students[i]} students")
    max_friends = int(n_students[i]/5)
    print(f"Each student has {max_friends} maximum number of friends")
    df_students = generate_student_list(n_students[i], max_friends)
    # df_students.to_csv('../students.csv', index=None)

    # df = pd.read_csv('students.csv')
    df_graph = create_student_graph(df_students)
    # df_graph.to_csv('../student_graph.csv', index=None)
    # print(df_graph)

    student, student_graph = get_student_graph(df_graph)
    # print(student_graph)
    #print(f"Performing BFS traversal")
    recommended_friends_bfs, time_taken_bfs = BFS(student_graph, student)
    #print(f"Performing DFS traversal")
    recommended_friends_dfs, time_taken_dfs = DFS(student_graph, student)

    # convert to ms
    total_time_bfs.append(time_taken_bfs * 1000)
    total_time_dfs.append(time_taken_dfs * 1000)

    recommend_friends_bfs.append(time_taken_bfs * 1000)
    recommend_friends_dfs.append(time_taken_dfs * 1000)


# print(recommend_friends_bfs)
# print(recommend_friends_dfs)


fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Friend Recommendations using BFS and DFS")
ax1.plot(n_students, total_time_bfs, label="BFS")
ax1.plot(n_students, total_time_dfs, label="DFS")
# ax1.xlabel('Number of students')
ax1.set_title('Traversal time in ms')
ax1.set_xlabel("Number of students")

ax2.plot(n_students, recommend_friends_bfs, label="BFS")
ax2.plot(n_students, recommend_friends_dfs, label="DFS")
ax2.set_title('Recommend time in ms')
ax2.set_xlabel("Number of students")
ax1.legend()
plt.show()
