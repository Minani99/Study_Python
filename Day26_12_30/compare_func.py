# class S:
#     def __init__(root, name, math, eng):
#         root.name = name
#         root.math = math
#         root.eng = eng
#
#     def __eq__(root, other):
#         return root.eng != other.eng
#
#
# a = S(name="1번", math=50, eng=50)
# b = S(name="2번", math=50, eng=60)
#
# print(a==b)

class Student:
    count = 0

    def __init__(root, name, k, m, e, s):
        root.name = name
        root.k = k
        root.m = m
        root.e = e
        root.s = s
        Student.count+=1
        print(f"{Student.count}번째 학생 생성")

    def get_sum(root):
        return root.k + root.m + root.e + root.s

    def get_ave(root):
        return root.get_sum() / 4

    def __str__(root):
        return "{}{}{}".format(
            root.name,
            root.get_sum(),
            root.get_ave()
        )

    def __eq__(root, value):
        return root.get_sum() == value.get_sum()

    def __ne__(root, other):
        return root.get_sum() != other.get_sum()

    def __gt__(root, other):
        return "호엥"
        # return root.get_sum() > other.get_sum()

    def __ge__(root, other):
        return root.get_sum() >= other.get_sum()

    def __lt__(root, other):
        return root.get_sum() < other.get_sum()

    def __le__(root, other):
        return root.get_sum() <= other.get_sum()



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
