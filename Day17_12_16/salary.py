import random as rm

# 이름 리스트
name_list = ["클로이모레츠", "냥뇽녕냥", "짐캐리", "김채원", "김지우", "코난", "아리아나그란데", "엠마왓슨", "김민정", "유지민"]
no_one = lambda x: int(x) // 10 * 10


def salary(file_path="salary_file.txt", encoding="utf-8"):
    try:
        with open(file_path, "r", encoding=encoding) as f:
            data = []
            for line in f:
                row = line.strip().replace('-', '0').split("\t")
                row = [int(value.replace(",", "")) for value in row]
                data.append(row)
            return data
    except FileNotFoundError:
        print(f"파일 '{file_path}'이(가) 존재하지 않습니다.")
        return []
    except Exception as e:
        print(f"오류 발생: {e}")
        return []


def calculate_taxes(data, before, **kwargs):
    np = before * 0.045  # 국민연금
    hi = before * 0.033  # 건강보험
    lci = hi * 0.1  # 요양보험
    ei = before * 0.008  # 고용보험

    person = {
        "이름": kwargs.get("이름", ""),
        "나이": kwargs.get("나이", 0),
        "부양가족": kwargs.get("부양가족", 0),
        "월급": no_one(before),
        "국민연금": no_one(int(np)),
        "건강보험": no_one(int(hi)),
        "요양보험": no_one(int(lci)),
        "고용보험": no_one(int(ei)),
        "소득세": 0,
        "지방소득세": 0,
        "실수령액": 0
    }

    income_tax = 0  # 소득세
    li = 0  # 지방소득세
    for row in data:
        try:
            s1 = row[0] * 10000
            s2 = row[1] * 10000
            t = row[2:]

            if s1 < before <= s2:
                income_tax = t[person["부양가족"]]
                li = income_tax * 0.1
                break

        except Exception as e:
            print(f"소득세 계산 중 에러: {e}")

    total_taxes = np + hi + lci + ei + income_tax + li
    net_salary = before - total_taxes  # 실수령액

    person["소득세"] = no_one(int(income_tax))
    person["지방소득세"] = no_one(int(li))
    person["실수령액"] = no_one(int(net_salary))

    return person


def detect_error(data):
    error = []
    prev_taxes = None
    for index, row in enumerate(data):
        try:
            salary1 = row[0]
            salary2 = row[1]
            taxes = row[2:]

            print(f"{index + 1} > 연봉 범위: {salary1} ~ {salary2}, 세금: {taxes}")

            for j in range(1, len(taxes)):
                if taxes[j] > taxes[j - 1]:
                    error.append(
                        f"{index + 1}번 줄 (연봉: {salary1}), 부양가족 {j} -> {j + 1} 세금 증가 ({taxes[j - 1]} -> {taxes[j]})"
                    )

            if salary1 < 1060:
                for j in range(len(taxes)):
                    if taxes[j] != 0:
                        error.append(
                            f"{index + 1}번째 줄 (연봉: {salary1}) 부양가족이 없는데 세금이 있음 (세금: {taxes[j]})"
                        )
            elif 1060 < salary1 < 5000:
                if prev_taxes is not None:
                    for j in range(len(taxes)):
                        if prev_taxes[j] == 0 or taxes[j] == 0:
                            continue
                        if abs(prev_taxes[j] - taxes[j]) > max(prev_taxes[j] * 0.06, 1000000):
                            error.append(
                                f"{index + 1}번 줄 (연봉: {salary1}) 세금 값이 이전 값과 차이가 큼 (부양가족 {j + 1})"
                            )
            elif salary1 >= 5000:
                if prev_taxes is not None:
                    for j in range(len(taxes)):
                        if prev_taxes[j] == 0 or taxes[j] == 0:
                            continue
                        if abs(prev_taxes[j] - taxes[j]) > max(prev_taxes[j] * 0.15, 1000000):
                            error.append(
                                f"{index + 1}번 줄 (연봉: {salary1}) 세금 값이 이전 값과 차이가 큼 (부양가족 {j + 1})"
                            )

            prev_taxes = taxes

        except Exception as e:
            error.append(f"{index + 1}번 줄에서 알 수 없는 오류 발생: {e}")
    return error


# ------ㅡmain------------


# 파일 로드 및 실행
file_path = "salary_file.txt"
data = salary(file_path)

if data:
    print("데이터 로드 완료.")
    errors = detect_error(data)

    if errors:
        print("\n발견된 이상치:")
        for err in errors:
            print(err)
    else:
        print("이상치가 발견되지 않았습니다.")
print("-" * 50)

# 무작위 이름과 세금 계산
p_name = rm.sample(name_list, 10)

list_sort = []

for i in range(len(name_list)):
    list_sort.append(calculate_taxes(
        data,
        before=rm.randrange(7700000, 99000000),
        이름=p_name[i],
        나이=rm.randrange(20, 40),
        부양가족=rm.randrange(0, len(data[0]) - 2))
    )

list_sort.sort(key=lambda x: x["실수령액"], reverse=True)

for person in list_sort:
    print("[세금 계산 결과]")
    for key, value in person.items():
        print(f"{key}: {value}")
    print("-" * 50)