import random

name_list = ["사람1", "사람2", "사람3", "사람4", "사람5", "사람6", "사람7", "사람8", "사람9", "사람10"]


def salary():
    result = []
    try:
        with open("salary_file.txt", "r", encoding="utf-8") as f:
            for line in f:
                values = line.strip().split("\t")
                values = [value.replace('-', '0') for value in values]
                result.append(values)
    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")
    except Exception as e:
        print(f"알 수 없는 오류: {e}")
    return result



for x in salary():
    print(x)


def create_person(**kwargs):
    # 기본값 설정
    name = kwargs.get("name", random.choice(name_list))
    age = kwargs.get("age", random.randint(20, 60))
    dependents = kwargs.get("dependents", random.randint(1, 11))

    return {
        "이름": name,
        "나이": age,
        "부양가족수": dependents,
    }

# def cal_salary():
