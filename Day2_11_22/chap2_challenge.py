import math

def sphere():
    r = float(input("구의 반지름을 입력해주세요:"))
    pi = math.pi
    v = 4/3*pi*r**3
    sr = 4*pi*r**2
    print(f"구의 부피는:{v:.2f}입니다")
    print(f"구의 겉넓이는:{sr:.2f}입니다")

def pita():
    x = float(input("밑변 입력:"))
    y = float(input("높이 입력:"))
    r = math.sqrt(x**2+y**2)
    print(f"빗변의 길이는{r:.2f}입니다.")