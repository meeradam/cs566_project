import pandas as pd
from faker import Faker
import random

fake = Faker()
boston_colleges = ['BU', 'BC', 'Harvard', 'MIT', 'NEU', 'UMass']
max_friends = 20
n_students = 100

student_name = []
student_college = []
for i in range(0, n_students):

    # inital list of student names
    name = fake.name()
    student_name.append(name)
    student_college.append(random.choice(boston_colleges))

student_name = list(set(student_name))

d = {'student_name':student_name, 'college':student_college}
df = pd.DataFrame(data = d)

friend_list = []
for i in df['student_name']:
    # create a list of friends for student
    student_friends = []
    n_friends = random.randint(1, max_friends+1)
    #print(n_friends)

    for j in range(n_friends):
        friend = random.choice(student_name)
        student_friends.append(friend)
        # make sure all unique friends
        student_friends = list(set(student_friends))

        # drop name if itself
        student_friends = [x for x in student_friends if x != i]
    
    friend_list.append(student_friends)

friends = {'friends': friend_list}
df['friends'] = friend_list
df.to_csv('boston_students.csv', index=None)