class Student:
    score = 90
    stestList = []

    def __init__(root, name, age, e, m):
        root.name = name
        root.age = age
        root.e = e
        root.m = m
        root.ap()

    def ap(root):
        first = root.name[0]
        if first == "김" and root.e >= Student.score:  # 영어점수 90 이상
            Student.stestList.append(root)
        else:  # 3번쨰 객체 이후 생성되는 객체는 강제로 소멸
            root.__del__()

    def __str__(root):
        # 객체 정보를 문자열로 반환
        return f"Student(name={root.name}, age={root.age}, e={root.e}, m={root.m})"
    
    def __del__(root):
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
