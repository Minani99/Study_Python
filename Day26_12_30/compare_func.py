# class S:
#     def __init__(self, name, math, eng):
#         self.name = name
#         self.math = math
#         self.eng = eng
#
#     def __eq__(self, other):
#         return self.eng != other.eng
#
#
# a = S(name="1번", math=50, eng=50)
# b = S(name="2번", math=50, eng=60)
#
# print(a==b)

class Student:
    count = 0

    def __init__(self, name, k, m, e, s):
        self.name = name
        self.k = k
        self.m = m
        self.e = e
        self.s = s
        Student.count+=1
        print(f"{Student.count}번째 학생 생성")

    def get_sum(self):
        return self.k + self.m + self.e + self.s

    def get_ave(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}{}{}".format(
            self.name,
            self.get_sum(),
            self.get_ave()
        )

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, other):
        return self.get_sum() != other.get_sum()

    def __gt__(self, other):
        return "호엥"
        # return self.get_sum() > other.get_sum()

    def __ge__(self, other):
        return self.get_sum() >= other.get_sum()

    def __lt__(self, other):
        return self.get_sum() < other.get_sum()

    def __le__(self, other):
        return self.get_sum() <= other.get_sum()



student = [
    Student("배고파", 10, 20, 30, 40),
    Student("목말라", 20, 20, 30, 40),
    Student("추워", 30, 40, 50, 60)
]

student_a = student[0]
student_b = student[1]

print(student_a == student_b)
print(student_a != student_b)
print(student_a > student_b)
print(student_a >= student_b)
print(student_a < student_b)
print(student_a <= student_b)
