class Student:
 amount_of_students = 0
 def __init__(self, height=160):
     self.height = height
     Student.amount_of_students += 1
 def grow(self, height=1):
     self.height+=height

sasha = Student()
masha = Student(height=170)

sasha.grow(height=15)

print(sasha.height)
print(masha.height)

print(Student.amount_of_students)

