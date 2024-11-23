from variables import *
from generate_students import *

n_students = [50]

"""
PERFORMING TRAVERSALS ON WEIGHTED GRAPHS
"""

for i in range(len(n_students)):
    print(f"For {n_students[i]} students")
    max_friends = int(n_students[i]/5)
    print(f"Each student has {max_friends} maximum number of friends")

    df_students = generate_student_list(n_students[i], max_friends, weighted = True)
    print(df_students)
