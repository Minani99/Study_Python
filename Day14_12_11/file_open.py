import random

han = list("가나다라마바사아자차카타파하")

# 파일에 데이터 생성
with open("info.txt", "w") as file:
    for i in range(1000):
        n = random.choice(han) + random.choice(han)
        w = random.randrange(40, 100)
        h = random.randrange(150, 190)

        file.write("{} {} {}\n".format(n, w, h))

# 파일에서 데이터 읽고 처리
with open("info.txt", "r") as file:
    for i in file:
        (n, w, h) = i.strip().split()  # 공백으로 분리

        if (not n) or (not w) or (not h):
            continue

        bmi = int(w) / ((int(h) / 100) ** 2)
        result = ""

        if bmi > 25:
            result = "과체중"
        elif 18.5 <= bmi <= 25:
            result = "정상"
        else:
            result = "저체중"

        print("\n".join([
            "이름: {}".format(n),
            "몸무게: {}".format(w),
            "키: {}".format(h),
            "BMI: {:.2f}".format(bmi),  # 소수점 2자리로 표시
            "결과: {}".format(result),
        ]))
        print()
