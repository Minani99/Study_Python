#딕셔너리에 총점/평균 필드를 만들어도 될듯

s1 = {"name": "stu1", "grade": 1, "main": "국어", "score": {"국": 100, "영": 40, "수": 70, "컴": 20}}
s2 = {"name": "stu2", "grade": 1, "main": "국어", "score": {"국": 90, "영": 100, "수": 10, "컴": 20}}
s3 = {"name": "stu3", "grade": 1, "main": "국어", "score": {"국": 50, "영": 40, "수": 100, "컴": 80}}
s4 = {"name": "stu4", "grade": 1, "main": "국어", "score": {"국": 100, "영": 100, "수": 100, "컴": 10}}
s5 = {"name": "stu5", "grade": 1, "main": "국어", "score": {"국": 10, "영": 40, "수": 90, "컴": 100}}

# ratio = [[100],[50,50],[40,40,20],[25,25,25,25],[20,20,20,20,20]]  #이거 아마 장학금 분배하기위해 미리 하는 리스트인듯
# -> 이거 인덱스 번호 == 명

stu_list = [s1, s2, s3, s4, s5]

total = 0
listX=[] #성적 총합 받아서 넣어줄 리스트
result = [] #학생이름, 성적 넣어줄 리스트

for i in stu_list:
    for j in i["score"]:
        if i["main"] != j: #비전공과면 이면
            if i["score"][j]*1.1 > 100: #>> 1.1 변수로 바꾸는게 더 좋음
                total=100
            else:
                total += i["score"][j] * 1.1
        else: #전공과목
            total += i["score"][j]
    listX.append((i["name"], int(total)))
    i['총점'] = int(total)
    total = 0 #학생 한명에 대한 성적 합산이 끝나고 변수를 초기화

for name, score in listX:
    result.append((score,name))
result.sort(reverse=True)

#입력 시작
scholarship = int(input("지급할 장학금 액수 입력 >> "))
person = int(input("장학금 지급 인원 설정 >> "))

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
    student_name = result[i][1]
    print(f"{student_name} 학생은 {amounts[i]:.2f}원 받음")


# score = 0 #>> 최대 점수를 기억하기 위한 임시 변수
# who = 0 #>> 최대 점수의 주인
# rank_list = [] #>>1등부터 순차적으로 나열
#
# for i in range(person):
#     for j in stu_list:
#         if j["총점"] > score: #아무나 하나 가지고옴
#             score = j["총점"] #일단 최대점수
#             who = stu_list.index(i) #인덱스 기록 st_list
#     rank_list.append(stu_list.pop(who))
#     score = 0
#     who = 0
#
# for i in range(len(ratio[person-1])):
#     pass