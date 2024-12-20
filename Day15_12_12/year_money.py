import random as rm

# 이름 리스트
name_list = ["사람" + str(i + 1) for i in range(10)]


def salary(file_path="salary_file.txt", encoding="utf-8"):
    try:
        with open(file_path, "r", encoding=encoding) as f:
            # 2차원 배열로 변환
            data = []
            for line in f:
                row = line.strip().replace('-', '0').split("\t")
                row = [int(value.replace(",", "")) for value in row]  # 모든 값을 정수로 변환
                data.append(row)  # 2차원 배열에 추가
            return data
    except FileNotFoundError:
        print(f"파일 '{file_path}'이(가) 존재하지 않습니다.")
        return []
    except Exception as e:
        print(f"오류 발생: {e}")
        return []


def calculate_taxes(before, **kwargs):
    np = before * 0.045  # 국민연금
    hi = before * 0.033  # 건강보험
    lci = hi * 0.1  # 요양보험
    ei = before * 0.008  # 고용보험

    # 소득세 / 아직 부양가족 고려안함
    if before < 1060000:  # 이사람들은 소득세 x
        income_tax = 0
    elif before < 5000000:
        income_tax = before * 0.06
    else:
        income_tax = before * 0.15

    li = income_tax * 0.1  # 지방소득세

    total_taxes = np + hi + lci + ei + income_tax + li
    net_salary = before - total_taxes  # 실수령액

    person = {
        "name": "",
        "age": 0,
        "dependent": 0,
        "월급" : before,
        "국민연금": int(np),
        "건강보험": int(hi),
        "요양보험": int(lci),
        "고용보험": int(ei),
        "소득세": int(income_tax),
        "지방소득세": int(li),
        "실수령액": int(net_salary)
    }

    for key, value in kwargs.items():
        if key == "name":
            person["name"] = value
        elif key == "age":
            person["age"] = int(value)
        elif key == "dependent":
            person["dependent"] = int(value)
        else:
            print("잘못된 입력")
            continue

    for i, j in person.items():
        print(i, ":", j)


# 이상치 탐지 함수
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
                        f"{index + 1}번 줄 (연봉:{salary1}), 부양가족 {j} -> {j + 1} 세금 증가 ({taxes[j - 1]} -> {taxes[j]})"
                    )

            if salary1 < 1060:
                for j in range(len(taxes)):
                    if taxes[j] != 0:
                        error.append(
                            f"{index + 1}번째 줄 (연봉:{salary1}) 부양가족이 없는데 세금이 있음 (세금: {taxes[j]})"
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


file_path = "../Day17_12_16/salary_file.txt"
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
print("-"*50)
calculate_taxes(1000000, name="징징이", age=20, dependent=1)
