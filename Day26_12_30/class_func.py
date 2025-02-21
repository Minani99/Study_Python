class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("-----학생목록----")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("---------------")

    def __init__(root, name, k, m, e, s):
        root.name = name
        root.k = k
        root.m = m
        root.e = e
        root.s = s
        Student.count += 1
        Student.students.append(root)

    def get_sum(root):
        return root.k + root.m + root.e + root.s

    def get_ave(root):
        return root.get_sum() / 4

    def __str__(root):
        return "{}\t{}\t{}".format(
            root.name,
            root.get_sum(),
            root.get_ave()
        )


Student("ㅎㅇ", 10, 2, 3, 4)
Student("ㅂㅇ", 1, 20, 3, 4)
Student("ㅇㅇ", 1, 2, 30, 4)
Student("ㅈㅈ", 1, 2, 3, 40)
Student("ㅋㅋ", 1, 20, 3, 4)

Student.print()