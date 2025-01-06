# class Human:
#     def __init__(self):
#         self.name = "human"
#
#     def h_test(self):
#         pass
#
#
# class Student(Human):
#     def __init__(self):
#         self.age = 16
#         pass
#
#
# student = Student()
#
# s = Student()
#
# print(s)
# s.name = "배고픔"
# print(s.name)
# print(s.age)
#
#
# print(isinstance(student, Human))
# print(type(student) == Human)

class Student:
    def study(self):
        print("공부공부")


class Teacher:
    def teach(self):
        print("코치코치")


classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
