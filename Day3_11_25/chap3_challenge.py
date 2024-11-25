import datetime

def chat():
    now = datetime.datetime.now()
    user = input("입력: ")

    if "안녕" in user:
        print(">안녕하세요.")
    elif "몇시" in user or "몇 시" in user:
        print(f">지금은 {now.hour}시 입니다.")
    else:
        print(user)

def num():
    n = int(input("정수를 입력하세요: "))
    if n%2 == 0:
        print(f"{n}은 2로 나누어 떨어집니다.")
    else:
        print(f"{n}은 2로 나누어 떨어지지 않습니다.")

    if n%3 == 0:
        print(f"{n}은 3로 나누어 떨어집니다.")
    else:
        print(f"{n}은 3로 나누어 떨어지지 않습니다.")

    if n%4 == 0:
        print(f"{n}은 4로 나누어 떨어집니다.")
    else:
        print(f"{n}은 4로 나누어 떨어지지 않습니다.")

    if n%5 == 0:
        print(f"{n}은 5로 나누어 떨어집니다.")
    else:
        print(f"{n}은 5로 나누어 떨어지지 않습니다.")


chat()
num()