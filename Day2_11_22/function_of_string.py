#format()

def f_one():
    "{}".format(10)  # format의 매개변수를 {}안에 넣어줌 (대체) *문자열로
    a = "{}{}{}".format(10, "포맷", 20)
    print(a)
    print("{}".format(100))

    money = "{}만원".format(5000)
    goal = "하 하늘에서 {}떨어졌으면 좋겠다".format(money)
    zz = "{}{}{}".format("겠냐", "ㅋㅋ", " ㄹㅇㅋㅋ")
    print(goal, zz)

    n, h, w = input("이름과 키와 몸무게 입력:").split(',')
    bmi = int(w) / ((int(h) / 100) ** 2)
    print("[{}]님의 bmi는 [{}]입니다.".format(n, format(bmi, ".2f")))

#자리수 나타내기
def f_139():
    a = "{:+5d}".format(52) #+5d +<<부호 붙히기 5d = 5칸부터 출력
    b = "{:=+5d}".format(52)
    c = "{:+05d}".format(52) #0으로 채움
    print(a)
    print(b)
    print(c)

#float format 사용하기
def f_140():
    print("{:f}".format(52.123))
    print("{:15f}".format(52.123))
    print("{:+15f}".format(52.123))
    print("{:+015f}".format(52.123))
    print("{:15.2f}".format(52.123))
    #의미없는 소수점 제거하기
    print("{:g}".format(52.00))
#대소문자 변환
def a_to_A():
    a = "Hello"
    a_A = a.upper()
    A_a = a_A.lower()
    print(a_A)
    print(A_a)
    print(a)
#문자열 양옆의 공백 제거
#lstrip >> 좌측 공백 제거
#rstrip >> 우측 공백 제거
def p_strip():
    text = """      그거 아세요 ?? 귤에 붙어 있는 하얀거 이름은 귤락입니다"""
    print(text)
    print(text.strip())

#is~~ (문자열 구성 파악하기)
def is_what():
    print("abc123".isalnum())
    print("مثال".isalnum())
    print("!q@w".isalnum())

#find() / rfind() >> 문자 찾기
#fild() << 왼쪽부터 찾기
#rfind() << 오른쪽에서 부터 찾기
def whereString():
    st = "찰떡아이스는 찰떡? 세알이였고"
    print(st.find("찰떡"))
    print(st.rfind("찰떡"))
    # in 연산자 >> 포함되어 있는지 확인만함
    print("세알" in st)
    print("하와이안 피잔 캐나다에서 만들었죠" in st)

#split()
def cutString():
    a="10 20 30 40 50".split(" ")
    print(a)
    print(type(a))

def f_string():
    print(f'제가 또 계란{3+1}개를 기가 맥히게 삶습니다')