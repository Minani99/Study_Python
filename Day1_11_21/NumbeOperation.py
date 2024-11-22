#숫자 연산자
print("1+2=",1+2)

firstNum = int(input("첫 번재 숫자 입력(정수):"))
SecondNum = int(input("두 번재 숫자 입력(정수):"))
while 1:
    operation = input("할 연산 고르셈 (+,-,*,/,%) (종료:그만):")
    if operation == '+':
        print(firstNum + SecondNum)
    elif operation == '-':
        print(firstNum - SecondNum)
    elif operation == '*':
        print(firstNum * SecondNum)
    elif operation == '/':
        print(float(firstNum / SecondNum))
    elif operation == '%':
        print(firstNum % SecondNum)
    elif operation =="그만":
        print("프로그램 종료")
        break
    else:
        print("잘못 입력한듯")