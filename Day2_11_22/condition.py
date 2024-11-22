def combine_not():
    my_condition = "개피곤"
    can_i = my_condition > "상태좋음"
    print("마법의 소라고동님 지금 집에가도 될까요 ?")
    print(f"{can_i}")
    can_i = not can_i
    print("제발요")
    print(f"{can_i}")

def number_check():
    value = input("뭐 아무거나 입력해봐:")

    if value.isdigit():
        print("숫자네 ㅇㅇ")
        print('자이거>>{}'.format(30 + int(value)))

# num = int(input("숫자입력>>"))
# if num > 0:
#     print("양")
# elif num < 0:
#     print("음")
# else:
#     print("0")

def even_num():
    x = int(input(">> "))

    y = x / 2
    if y == int(y):  # y가 정수인지 확인
        print("짝수")
    else:
        print("홀수")

    if x[-1] in "02468":
        print("짝수")
