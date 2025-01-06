class Stu:
    def __init__(self):
        pass


class Person:
    def __init__(self):
        pass


a = Stu()

students = [Stu(), Stu(), Person()]  #식별자없이 리스트 인덱스 통한 참조 (동적상황)


for i in students:
    i.isinstance(i, Stu)


#------------------------------------------------------------------------------

