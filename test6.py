class Student:
    def __init__(self,Name,Grade):
        self.name = Name
        self.grade = Grade


s1 = Student("Anna", "A")

print(s1.grade)

s1.grade = "B"
print(s1.grade)