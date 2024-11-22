import time
from generate_students import *
from create_graph import *
# from traverse_graphs import *

n_students = 20
max_friends = 5

df_students = generate_student_list(n_students, max_friends)
# df_students.to_csv('students.csv', index=None)

# df = pd.read_csv('students.csv')
df_graph = create_student_graph(df_students)
print(df_graph)



