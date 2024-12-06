import time
import random

now = time
hour = now.localtime().tm_hour  # 현재 시간의 시(hour) 추출
minute = now.localtime().tm_min  # 현재 시간의 분(minute) 추출

# 다양한 카테고리의 버거와 메뉴 항목
burger = {
    "더블쿼터파운더치즈버거": [6000, 'b'],
    "쿼터파운더치즈": [5000, 'b'],
    "불고기": [3000, 'b'],
    "더블 불고기": [3500, 'b'],
    "빅맥": [4500, 'b'],
    "치즈버거": [3000, 'b'],
    "베이컨토마토디럭스": [5000, 'b'],
    "햄버거": [2500, 'b'],
    "맥스파이시상하이": [5500, 'c'],
    "맥치킨": [4500, 'c'],
    "맥크리스피디럭스": [6000, 'c']
}

macLunch = {
    "빅맥세트": [5500, 'b'],
    "더블불고기세트": [4500, 'b'],
    "베이컨토마토디럭스세트": [6000, 'b']
}

macMorning = {
    "에그맥머핀": [2800, 'z'],
    "소시지에그맥머핀": [3000, 'z'],
    "베이컨에그맥머핀": [3300, 'b'],
    "치킨맥머핀": [3000, 'c']
}

happySnack = {
    "드립커피M": 1000,
    "제로콜라M": 1000,
    "치즈버거": 2000,
    "치즈스틱2조각": 2000,
    "후렌치후라이s": 1000
}

sideMenu = {
    "맥윙2조각": 2000,
    "맥윙4조각": 3500,
    "맥윙8조각": 6000,
    "치즈스틱4조각": 3800,
    "후렌치후라이s": 1000,
    "후렌치후라이M": 1500,
    "후렌치후라이L": 2000,
    "맥너겟4조각": 2000,
    "맥너겟8조각": 2800
}

desert = {
    "맥플러리": 3000,
    "아이스크림콘": 1000
}

mcCafe = {
    "카페라떼": 2000,
    "아이스카페라떼": 2000,
    "아이스드립커피": 1000,
    "드립커피": 1000
}

drinks = {
    "콜라M": 1000,
    "콜라L": 1500,
    "콜라제로M": 1000,
    "콜라제로L": 1500,
    "사이다M": 1000,
    "사이다L": 1500,
    "오렌지주스": 1000,
    "생수": 1000
}

change_set = {}


# ----------------------------------------------------------------------------------------------------------------------

# 시간대에 맞는 카테고리 반환
def get_available_categories(hour1, minute1):
    if (4, 0) <= (hour1, minute1) < (10, 30):
        return ["맥모닝", "버거", "사이드", "디저트", "맥카페", "음료"]  # 아침 시간
    elif (10, 30) <= (hour1, minute1) < (14, 0):
        return ["맥런치", "버거", "사이드", "디저트", "맥카페", "음료", "해피밀"]  # 점심 시간
    else:
        return ["버거", "사이드", "디저트", "맥카페", "음료", "해피밀"]  # 저녁 시간


def happy_meal(hour1, minute1):
    if (4, 0) <= (hour1, minute1) < (10, 30):
        return
    else:
        return


# 카테고리 출력
def category_output():
    for a in range(len(category)):
        print(a + 1, category[a])


# 버거 메뉴 출력 함수
def display_burger_menu(menu_items):
    print("------------버거------------")
    for i, item in enumerate(menu_items, start=1):  # 번호와 가격 출력
        print(f"{i}. {item} - {burger[item][0]}원")
    print("--------------------------")


def display_side_menu(menu_items):
    print("-----------사이드------------")
    for i, item in enumerate(menu_items, start=1):  # 번호와 가격 출력
        print(f"{i}. {item} - {sideMenu[item]}원")
    print("--------------------------")


# 버거 소분류 메뉴 필터링
def filter_menu(burger_diction, cate):
    menu = []
    for name, details in burger_diction.items():
        if cate in details[1]:  # 카테고리가 일치하는 메뉴만 필터링
            menu.append(name)
    return menu


# 버거 고르자
def burger_selection(burger1, my_cart1):
    while True:  # 버거 선택 반복문
        menu = list(burger1.keys())  # 전체 버거 목록
        display_burger_menu(menu)  # 메뉴 출력

        while True:  # 카테고리 내 메뉴 선택 반복문
            small_cate = input("전체(1) 비프(2) 치킨(3) 고름(4) 선택창(5):")

            if small_cate == '1':  # 전체 메뉴 선택
                display_burger_menu(menu)

            elif small_cate == '2':  # 비프 메뉴 선택
                beef = filter_menu(burger1, 'b')  # 'b' 카테고리인 비프 메뉴 필터링
                display_burger_menu(beef)

            elif small_cate == '3':  # 치킨 메뉴 선택
                chicken_menu = filter_menu(burger1, 'c')  # 'c' 카테고리인 치킨 메뉴 필터링
                display_burger_menu(chicken_menu)

            elif small_cate == '4':  # 메뉴 선택 종료
                select = int(input("고른 메뉴는?: "))  # 메뉴 번호 입력
                set_upgrade(menu[select - 1], my_cart1)
                my_cart1.append(menu[select - 1])  # 장바구니에 메뉴 추가
                how_cart()
                return

            elif small_cate == '5':  # 카테고리로 돌아가기
                return

            else:
                print("(메뉴 선택) 잘못된 입력 입니다. 다시 입력 하세요")


def side_selection():
    pass


# 세트업글 (미완성)
def set_upgrade(selection, mycart):
    set_how = input("세트(1) 단품(2) 이전으로(3) 처음으로(4): ")
    if set_how == '1':
        print(selection)
        print("메뉴에 +1500 입니다.")
        pass
    elif set_how == '2':
        pass
    elif set_how == '3':
        pass
    elif set_how == '4':
        pass
    else:
        print("세트/단품 잘못된 입력")
    pass


# 걍 장바구니 보여주기
def how_cart():
    print("--------------------------")
    print("장바구니 정보")
    print(myCart)
    print("--------------------------")


# 가격 계산 함수
def calculate(my_cart):
    price = []
    for i in my_cart:
        if i in burger:
            price.append(burger[i][0])
        elif i in sideMenu:
            price.append(sideMenu[i])
        else:
            pass
    sum_price = sum(price)  # 총 가격 계산
    return sum_price


# 결제 함수
def pay(payment1):
    if payment1 == '1':
        pass
    elif payment1 == '2':
        how_pay = input("결제수단: 카카오페이(1) 카드(2) 현금(3): ")
        if how_pay in ['1', '2', '3']:
            # 뭐 여기에 조건문 넣어서 카드를 넣어주십쇼 같은거 할 수 있을듯
            print("결제가 완료되었습니다")
            order_num = random.randrange(1, 100)  # 주문 번호 랜덤 생성
            print(f"주문번호: {order_num}")
            print("--------------------------")
            return
        else:
            print("잘못된 입력")
    else:
        print("잘못입력하셨습니다.")


# __name__() __main__ 아래에서 부터 메인


while True:  # 무한 반복 (주문을 계속 받기 위한 루프)
    key_while = [1, 1, 1, 1, 1]  # 각 while문의 제어 변수
    myCart = []  # 장바구니 초기화

    first = input("주문하기(1): ")  # 첫 번째 선택: 주문하기
    if first == '1':
        where = input("식사 장소를 선택하세요 매장(1) 포장(2): ")  # 매장/포장 선택
        if where == '1':  # 매장 선택
            print("매장 식사를 선택하셨습니다.")
            while key_while[0]:  # 시간에 맞는 카테고리 출력 (화면만 일단 보여줌)
                category = get_available_categories(hour, minute)  # 현재 시간에 맞는 카테고리 얻기
                category_output()  # 카테고리 출력
                input_cate = int(input("카테고리 선택: "))  # 카테고리 선택

                selected_category = category[input_cate - 1]  # 선택된 카테고리
                key_while[1] = 1  # 카테고리로 돌아갔을때 아래 반복문 다시 활성화

                while key_while[1]:  # 유저가 카테고리 선택함

                    if selected_category == '버거':
                        burger_selection(burger, myCart)  # 버거 선택 함수 호출
                    elif selected_category == '사이드':
                        display_side_menu(sideMenu)
                    else:
                        print("이 메뉴는 아직 덜준비 ㅠㅠ")

                    # 메뉴 선택 후 추가 옵션 처리
                    third_in = input("메뉴(1) 카테고리(2) 처음으로(3) 결제(4) 장바구니 비우기(5): ")

                    if third_in == '1':  # 메뉴 선택
                        continue
                    elif third_in == '2':  # 카테고리 선택
                        key_while[1] = 0
                        continue
                    elif third_in == '3':  # 처음으로 돌아가기
                        key_while[0] = 0
                        break
                    elif third_in == '4':  # 결제
                        how_cart()
                        print("총 가격")
                        print(calculate(myCart), "원")  # 계산 함수 호출
                        print("--------------------------")
                    elif third_in == '5':
                        myCart = []
                        print("**장바구니가 초기화 되었습니다.**")
                        break
                    else:
                        print("1에서 5사이를 입력해주세요")
                    while key_while[3]:
                        payment = input("추가주문(1) 주문완료(2): ")
                        pay(payment)  # 결제 함수 호출
                        key_while = [0, 0, 0, 0, 0]  # 종료
                else:
                    pass
        elif where == '2':  # 포장 선택
            print("포장을 선택하셨습니다.")  # 포장 하지마~!
            pass
        else:
            print("매장/포장중에 선택하세요")
    else:
        print("1만 입력하세요")
