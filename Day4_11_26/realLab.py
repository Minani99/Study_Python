student = {
    "A": {"grade": 1, "main": "국어", "score": [100, 80, 70, 20]},
    "B": {"grade": 2, "main": "영어", "score": [50, 100, 10, 40]},
    "C": {"grade": 3, "main": "수학", "score": [10, 20, 100, 40]},
    "D": {"grade": 4, "main": "컴퓨터", "score": [40, 30, 20, 100]},
    "E": {"grade": 2, "main": "영어", "score": [80, 100, 40, 20]},
}

total_scores = {}

print(student)

#가산점 넣기
for key in student:
    if student[key]["main"] == "국어":
        for i in range(4):
            student[key]["score"][i] *= 1.1
        student[key]["score"][0] /= 1.1
    elif student[key]["main"] == "영어":
        for i in range(4):
            student[key]["score"][i] *= 1.1
        student[key]["score"][1] /= 1.1
    elif student[key]["main"] == "수학":
        for i in range(4):
            student[key]["score"][i] *= 1.1
        student[key]["score"][2] /= 1.1
    elif student[key]["main"] == "컴퓨터":
        for i in range(4):
            student[key]["score"][i] *= 1.1
        student[key]["score"][3] /= 1.1

    total_scores[key] = sum(student[key]["score"])

#입력 시작
scholarship = int(input("지급할 장학금 액수 입력 >> "))
person = int(input("장학금 지급 인원 설정 >> "))

#정렬을 위해 딕셔너리를 리스트형태로 변환
students = list(total_scores.items())

print(student)

#튜플로 위치 바꿈 (정렬함수 쓰려고)
sortScore = []
for name, score in total_scores.items():
    sortScore.append((score, name))
#앙기모찌
sortScore.sort(reverse=True)

#받는 인원에 따라 장학금 분배
if person == 1:
    amounts = [scholarship]
elif person == 3:
    amounts = [scholarship * 0.4, scholarship * 0.4, scholarship * 0.2]
else:
    amounts = [scholarship / person] * person

#출력 ----------------------------------------------------------------
print(f"총 장학금 {scholarship}원, {person}명에게 지급")
for i in range(person):
    student_name = sortScore[i][1]
    print(f"{student_name} 학생은 {amounts[i]:.2f}원 받음")


# subject = ["국어", "영어", "수학", "컴퓨터"]
#
# def inputScore():
#     for i in student:
#         for j in subject:
#             student[i]["score"].append(int(input(f"{i}학생의 {j}점수를 입력하세요:")))