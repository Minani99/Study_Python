def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return "0은 좀.."
    return x / y


n_sum = 0
last_input = ""
print("계산기를 시작합니다. 종료하려면 'exit'를 입력하세요.")

while True:
    user = input(f"{n_sum} >> ")  # 유저 인풋

    if user.isdigit():  # 숫자인지 확인
        if last_input in ['+', '-', '*', '/']:  # 마지막에 연산자를 입력했다면
            number = int(user)  # 받은 문자를 정수로 바꿔주고
            if last_input == '+':
                n_sum = add(n_sum, number)  # sum값에다 더해줌
            elif last_input == '-':
                n_sum = sub(n_sum, number)
            elif last_input == '*':
                n_sum = mul(n_sum, number)
            elif last_input == '/':
                n_sum = div(n_sum, number)
                if n_sum == "0은 좀..":
                    print("0으로 나눌 수 없습니다.")
                    n_sum = 0
            print(f">> {n_sum}")
        else:
            n_sum = int(user)
        last_input = ""  # 마지막 입력문자 초기화

    elif user in ['+', '-', '*', '/']:  # 연산자를 입력했다면
        last_input = user  # 라스트 인풋에 추가

    elif user == 'exit':  # 종료
        print("계산기를 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
