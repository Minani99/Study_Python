class Student:
    score = 90
    stestList = []

    def __init__(self, name, age, e, m):
        self.name = name
        self.age = age
        self.e = e
        self.m = m
        self.ap()

    def ap(self):
        first = self.name[0]
        if first == "김" and self.e >= Student.score:  # 영어점수 90 이상
            Student.stestList.append(self)
        else:  # 3번쨰 객체 이후 생성되는 객체는 강제로 소멸
            self.__del__()

    def __str__(self):
        # 객체 정보를 문자열로 반환
        return f"Student(name={self.name}, age={self.age}, e={self.e}, m={self.m})"
    
    def __del__(self):
        print("소멸")
        pass


Student("김미나", 19, 90, 40)
Student("박미나", 19, 50, 40)
Student("김미나", 19, 60, 40)
Student("오미나", 19, 70, 40)
Student("김병만", 19, 90, 40)

for i in Student.stestList:
    print(str(i))

# 학생을 만드는 클래스를 정의하고 해당 클래스는 이름 나이 영어 수학 4가지필드
# 5명의 학생
# 클래스 변수를 통해서 성이 김씨인 사람 중 영어점수가 90 이상만 저장
