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


# ----------------------------------------------------------------------------------------------------------------------

# 시간대에 맞는 카테고리 반환
def get_available_categories(hour1, minute1):
    if (4, 0) <= (hour1, minute1) < (10, 30):
        return ["맥모닝", "사이드", "디저트", "맥카페", "음료"]  # 아침 시간
    elif (10, 30) <= (hour1, minute1) < (14, 0):
        return ["맥런치", "버거", "사이드", "디저트", "맥카페", "음료", "해피밀"]  # 점심 시간
    else:
        return ["버거", "사이드", "디저트", "맥카페", "음료", "해피밀"]  # 저녁 시간


# 카테고리 출력
def category_output():
    for a in range(len(category)):
        print(a + 1, category[a])


# 메뉴 출력 함수
def display_menu(menu_items):
    print("------------버거------------")
    for i, item in enumerate(menu_items, start=1):  # 번호와 가격 출력
        print(f"{i}. {item} - {burger[item][0]}원")
    print("--------------------------")


# 카테고리별 메뉴 필터링
def filter_menu(burger_diction, cate):
    menu = []
    for name, details in burger_diction.items():
        if cate in details[1]:  # 카테고리가 일치하는 메뉴만 필터링
            menu.append(name)
    return menu


# 버거 선택 함수
def burger_selection(burger1, mycart1, key_while1):
    while key_while1[1]:  # 버거 선택 반복문
        menu = list(burger1.keys())  # 전체 버거 목록
        display_menu(menu)  # 메뉴 출력

        while key_while1[2]:  # 카테고리 내 메뉴 선택 반복문
            small_cate = input("전체(1) 비프(2) 치킨(3) 고름(4):")

            if small_cate == '1':  # 전체 메뉴 선택
                display_menu(menu)

            elif small_cate == '2':  # 비프 메뉴 선택
                beef = filter_menu(burger1, 'b')  # 'b' 카테고리인 비프 메뉴 필터링
                display_menu(beef)

            elif small_cate == '3':  # 치킨 메뉴 선택
                chicken_menu = filter_menu(burger1, 'c')  # 'c' 카테고리인 치킨 메뉴 필터링
                display_menu(chicken_menu)

            elif small_cate == '4':  # 메뉴 선택 종료
                select = int(input("고른 메뉴는?: "))  # 메뉴 번호 입력
                mycart1.append(menu[select - 1])  # 장바구니에 메뉴 추가
                key_while1[1] = 0  # 반복 종료
                break

            else:
                print("잘못된 입력입니다. 다시 입력하세요")
        print(f"담긴 메뉴: {mycart1}")  # 장바구니 내용 출력


while True:  # 무한 반복 (주문을 계속 받기 위한 루프)
    key_while = [1, 1, 1, 1, 1]  # 각 while문의 제어 변수
    myCart = []  # 장바구니 초기화
    price = []  # 가격 리스트 초기화
    sum_price = 0  # 총 가격 초기화

    first = input("주문하기(1): ")  # 첫 번째 선택: 주문하기
    if first == '1':
        where = input("식사 장소를 선택하세요 매장(1) 포장(2): ")  # 매장/포장 선택
        if where == '1':  # 매장 선택
            print("매장 식사를 선택하셨습니다.")
            while key_while[0]:  # 시간에 맞는 카테고리 출력
                category = get_available_categories(hour, minute)  # 현재 시간에 맞는 카테고리 얻기
                category_output()  # 카테고리 출력
                input_cate = int(input("카테고리 선택: "))  # 카테고리 선택

                selected_category = category[input_cate - 1]  # 선택된 카테고리

                if selected_category == '버거':
                    burger_selection(burger, myCart, key_while)  # 버거 선택 함수 호출
                else:
                    print("아직 덜준비 ㅠㅠ")

                # 메뉴 선택 후 추가 옵션 처리
                third_in = input("메뉴(1) 카테고리(2) 처음으로(3) 결제(4): ")
                if third_in == '1':  # 메뉴 선택
                    key_while[2] = 1
                    key_while[1] = 0
                    continue

                elif third_in == '2':  # 카테고리 선택
                    key_while[1] = 1
                    key_while[2] = 1
                    continue

                elif third_in == '3':  # 처음으로 돌아가기
                    key_while[0] = 0
                    break
                elif third_in == '4':  # 결제
                    print("--------------------------")
                    print("장바구니 정보")
                    print(myCart)
                    print("--------------------------")

                    price = []
                    for i in myCart:
                        if i in burger:
                            price.append(burger[i][0])  # 가격 합산

                    sum_price = sum(price)  # 총 가격 계산
                    print("총 가격")
                    print(sum_price, "원")
                    print("--------------------------")

                    while key_while[3]:
                        payment = input("추가주문(1) 주문완료(2): ")
                        if payment == '1':
                            pass
                        elif payment == '2':
                            how_pay = input("결제수단: 카카오페이(1) 카드(2) 현금(3): ")
                            if how_pay in ['1', '2', '3']:
                                print("결제가 완료되었습니다")
                                order_num = random.randrange(1, 100)  # 주문 번호 랜덤 생성
                                print(f"주문번호: {order_num}")
                                print("--------------------------")
                                key_while = [0, 0, 0, 0, 0]  # 종료
                                break
                            else:
                                print("잘못된 입력")
                        else:
                            print("잘못입력하셨습니다.")
                else:
                    pass
        elif where == '2':  # 포장 선택
            print("포장을 선택하셨습니다.")
            pass
        else:
            pass
    else:
        pass
