from collections import Counter
from faker import Faker
import random

fake = Faker()

students = []

for x in range(100):
    student = {
        'name': fake.name(),
        'age': random.randint(18,25),
        'major': random.choice(['Computer Science','Mathematics','Physics']),
        'gpa': round(random.uniform(2.0,4.0),2),
        'is_international': random.choice([True,False])
    }
    students.append(student)


listOfNames = list()

for student in students:
    listOfNames.append(student['name'].split(' ')[0])


a = Counter(listOfNames)

for name, count in a.items():
    if count > 1:
        print(f'{name}: {count} times')




