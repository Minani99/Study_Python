import random

floor_10 = lambda x: int(x) // 10 * 10 # 일의 자리 버리기
salary_key = lambda x: int(x) // 12000 # 표에서 값 찾을 때 쓸 키
person_info = lambda **kwargs: { # 사람 정보
    "이름": kwargs.get("name", "아무개"),
    "나이": kwargs.get("age", 20),
    "연봉": kwargs.get("annual_salary", 10000000),
    "부양가족수": kwargs.get("family", 1)
}
cy = lambda ax, ay, bx, by, cx: ((by - ay) * cx + ay * bx - by * ax) / (bx - ax) # 일차함수 값 구하기

data = [] # 세금 데이터
people = [] # 사람 정보

# 랜덤한 사람 만들기
for i in range(1, 11): # 1 ~ 10
    name = f"사람{i}"
    age = random.randrange(20, 61) # 20이상 60이하
    annual_salary = random.randrange(10000000, 120000001) # 1000만이상 1.2억이하
    family = random.randrange(1, 11) # 1이상 10이하
    people.append({"개인정보": person_info(name=name, age=age, annual_salary=annual_salary, family=family)})

# 파일 데이터 리스트에 담기
with open("salary_file.txt", "r", encoding="utf-8") as file: # index 11부터 데이터 존재
    data = [[int(j.replace(",", "").replace("-", "0")) for j in i.strip().split("\t")] for i in file.readlines()[11:]]

# 각 열에서 예측값 대비 얼마나 차이나는지 비율 구하기 (예측값은 등차수열로 계산)
s = [0 for i in range(2, len(data[0]))]
for i in range(2, len(data)): # i-2, i-1, i행 비교
    for j in range(2, len(data[i])): # 1 2열은 제외
        if data[i - 1][j] == 0: # 0일 경우 1배로 계산
            s[j - 2] += 1
        else: # 위아래 평균 대비 비율 (월급 간격 차이 고려)
            s[j - 2] += cy(data[i - 2][0], data[i - 2][j], data[i][0], data[i][j], data[i - 1][0]) / data[i - 1][j]
s = [i / (len(data) - 2) for i in s]

# 비율에 안맞는 값 바꾸기 (첫 행은 정상적이라 가정)
for i in range(2, len(data)):
    for j in range(2, len(data[i])):
        # 0이 있어야 할 자리에 다른 숫자가 있을 경우 : data[i - 1][j]가 문제
        if data[i - 2][j] == 0 and data[i - 1][j] > 0 and data[i][j] == 0:
            c = data[i - 1][j]
            data[i - 1][j] = 0
            print(f"{i}행 {j + 1}열 {c} -> 0 으로 계산")
            continue

        # 대상이 0이거나 위에 0이다가 아래에 새로 숫자 시작되는 경우
        if data[i - 1][j] == 0 or (data[i - 2][j] == 0 and data[i][j] > 0):
            continue

        # 나머지 경우 원래 비율과 안맞으면 data[i][j]가 문제
        r = cy(data[i - 2][0], data[i - 2][j], data[i][0], data[i][j], data[i - 1][0]) / data[i - 1][j]
        if abs(r - s[j - 2]) > 0.1: # 0.1 넘게 차이나는 경우 (0.07부터 문제의 4개만 걸러짐, 여기서 비교하는 데이터 97%는 0.01 미만)
            c = data[i][j]
            data[i][j] = int(cy(data[i - 2][0], data[i - 2][j], data[i - 1][0], data[i - 1][j], data[i][0]))
            print(f"{i + 1}행 {j + 1}열 {c} -> {data[i][j]} 으로 계산")
print("─" * 32)

# 계산
for p in people:
    person = p["개인정보"] # {'이름': '사람7', '나이': 58, '연봉': 106290462, '부양가족수': 6}
    info = {}
    key = salary_key(person["연봉"])  # 8857
    for d in data:
        if not (d[1] > key >= d[0]): # d[1] > key 부터 계산
            continue

        info["국민연금"] = min(floor_10(person["연봉"] * 45 / 12000), 277650) # 0.045/12 와 같이 하면 소숫점때문에 오차 나옴
        info["건강보험"] = floor_10(person["연봉"] * 3545 / 1200000)
        info["요양보험"] = floor_10(info["건강보험"] * 1295 / 10000)
        info["고용보험"] = floor_10(person["연봉"] * 9 / 12000)
        info["근로소득세"] = floor_10(d[person["부양가족수"] + 1])
        info["지방소득세"] = floor_10(info["근로소득세"] * 1 / 10)
        info["년 예상 실수령액"] = person["연봉"] - sum(x for k, x in info.items()) * 12
        info["월 환산금액"] = round(info["년 예상 실수령액"] / 12)
        p["세금정보"] = info # {'국민연금': 277650, '건강보험': 313990, ...}
        break # 찾았으면 탐색 종료하고 다음 사람으로

    if not info: # 표에서 찾지 못한 경우 (ex. 월 990+)
        pass

# 정렬 (세금정보 있는 사람만)
result = list(filter(lambda x: "세금정보" in x, people))
result.sort(key=lambda x: x["세금정보"]["년 예상 실수령액"], reverse=True)

# 출력
for p in result:
    print(", ".join(f"{key}: {value}" for key, value in p["개인정보"].items())) # 이름: 사람7, 나이: 58, 연봉: 106290462, 부양가족수: 6
    for key, value in p["세금정보"].items(): # {'국민연금': 277650, '건강보험': 313990, ...}
        print(f"{key}\t{value:,} 원")
    print("─" * 32)