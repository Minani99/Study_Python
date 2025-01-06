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

    def __init__(self, name, k, m, e, s):
        self.name = name
        self.k = k
        self.m = m
        self.e = e
        self.s = s
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.k + self.m + self.e + self.s

    def get_ave(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_ave()
        )


Student("ㅎㅇ", 10, 2, 3, 4)
Student("ㅂㅇ", 1, 20, 3, 4)
Student("ㅇㅇ", 1, 2, 30, 4)
Student("ㅈㅈ", 1, 2, 3, 40)
Student("ㅋㅋ", 1, 20, 3, 4)

Student.print()