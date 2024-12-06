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

mcLunch = {
    "빅맥세트": [5500, 'b'],
    "더블불고기세트": [4500, 'b'],
    "베이컨토마토디럭스세트": [6000, 'b']
}

mcMorning = {
    "에그맥머핀": [2800, 'z'],
    "소시지에그맥머핀": [3000, 'z'],
    "베이컨에그맥머핀": [3300, 'b'],
    "치킨맥머핀": [3000, 'c']
}

happySnack = {
    "드립커피M": [1000, 'z'],
    "제로콜라M": [1000, 'z'],
    "치즈버거": [2000, 'z'],
    "치즈스틱2조각": [2000, 'z'],
    "후렌치후라이s": [1000, 'z']
}

sideMenu = {
    "맥윙2조각": [2000, 'z'],
    "맥윙4조각": [3500, 'z'],
    "맥윙8조각": [6000, 'z'],
    "치즈스틱4조각": [3800, 'z'],
    "후렌치후라이s": [1000, 'z'],
    "후렌치후라이M": [1500, 'z'],
    "후렌치후라이L": [2000, 'z'],
    "맥너겟4조각": [2000, 'z'],
    "맥너겟8조각": [2800, 'z']
}

desert = {
    "맥플러리": [3000, 'z'],
    "아이스크림콘": [1000, 'z'],
}

mcCafe = {
    "카페라떼": [2000, 'z'],
    "아이스카페라떼": [2000, 'z'],
    "아이스드립커피": [1000, 'z'],
    "드립커피": [1000, 'z']
}

drinks = {
    "콜라M": [1000, 'z'],
    "콜라L": [1500, 'z'],
    "콜라제로M": [1000, 'z'],
    "콜라제로L": [1500, 'z'],
    "사이다M": [1000, 'z'],
    "사이다L": [1500, 'z'],
    "오렌지주스": [1000, 'z'],
    "생수": [1000, 'z']
}

change_set = {}

# 시간대별 카테고리 딕셔너리
time_categories = {
    "morning": ["맥모닝", "버거", "사이드", "디저트", "맥카페", "음료"],
    "lunch": ["맥런치", "버거", "사이드", "디저트", "맥카페", "음료", "해피밀"],
    "dinner": ["버거", "사이드", "디저트", "맥카페", "음료", "해피밀"]
}

happy_meal = {
    "에그맥머핀": [2800, 'z'],
    "소시지에그맥머핀": [3000, 'z'],
    "베이컨에그맥머핀": [3300, 'b'],
    "불고기": [3000, 'b'],
    "햄버거": [2500, 'b'],
    "치즈버거": [3000, 'b']
}


# ----------------------------------------------------------------------------------------------------------------------

# 시간대에 맞는 카테고리 반환
def get_time_period(hour1, minute1):
    if (4, 0) <= (hour1, minute1) < (10, 30):
        return "morning"
    elif (10, 30) <= (hour1, minute1) < (14, 0):
        return "lunch"
    else:
        return "dinner"


# 시간대에 맞게 해피밀 걸름
def get_happy_meal(hour1, minute1):
    period = get_time_period(hour1, minute1)
    if period == "morning":
        happy_meal.pop("불고기", None)
        happy_meal.pop("햄버거", None)
        happy_meal.pop("치즈버거", None)
    else:
        happy_meal.pop("에그맥머핀", None)
        happy_meal.pop("소시지에그맥머핀", None)
        happy_meal.pop("베이컨에그맥머핀", None)


def get_available_categories(hour1, minute1):
    period = get_time_period(hour1, minute1)
    return time_categories[period]


# 카테고리 출력
def category_output():
    for a in range(len(category)):
        print(a + 1, category[a])


# 메뉴 출력 함수
def display_menu(menu_items, oi):
    print("------------메뉴------------")
    for i, item in enumerate(menu_items, start=1):  # 번호와 가격 출력
        print(f"{i}. {item} - {oi[item][0]}원")
    print("--------------------------")


# 필터링 함수
def filter_menu(burger_dict, cate):
    filtered_menu = []

    for name, details in burger_dict.items():
        if cate in details[1]:
            filtered_menu.append(name)

    return filtered_menu


# 버거 고르자
def burger_selection(burger1, my_cart1):
    while True:  # 버거 선택 반복문
        menu = list(burger1.keys())  # 전체 버거 목록
        display_menu(menu, burger)  # 메뉴 출력

        while True:  # 카테고리 내 메뉴 선택 반복문
            small_cate = input("전체(1) 비프(2) 치킨(3) 고름(4) 선택창(5):")

            if small_cate == '1':  # 전체 메뉴 선택
                display_menu(menu, burger)
                menu = menu = list(burger1.keys())

            elif small_cate == '2':  # 비프 메뉴 선택
                beef = filter_menu(burger1, 'b')  # 'b' 카테고리인 비프 메뉴 필터링
                display_menu(beef, burger)
                menu = beef

            elif small_cate == '3':  # 치킨 메뉴 선택
                chicken_menu = filter_menu(burger1, 'c')  # 'c' 카테고리인 치킨 메뉴 필터링
                display_menu(chicken_menu, burger)
                menu = chicken_menu

            elif small_cate == '4':  # 메뉴 선택 종료
                select = int(input("고른 메뉴는?: "))  # 메뉴 번호 입력
                print(f"선택메뉴: [{menu[select - 1]}]")

                set_upgrade(menu[select - 1], my_cart1)  # 세트 업그레이드 처리
                how_cart()
                return

            elif small_cate == '5':  # 카테고리로 돌아가기
                return

            else:
                print("(메뉴 선택) 잘못된 입력 입니다. 다시 입력 하세요")


def menu_selection(other_menu, my_cart):
    menu = list(other_menu.keys())
    display_menu(menu, other_menu)
    while True:
        select1 = input("고름(1) 선택창(2): ")
        if select1 == '1':
            select = int(input("고른 메뉴는?: "))  # 메뉴 번호 입력
            print(f"선택메뉴: [{menu[select - 1]}]")
            my_cart.append(menu[select - 1])  # 장바구니에 메뉴 추가
            how_cart()
            break
        elif select1 == '2':
            key_while[1] = 0
            break
        else:
            continue


# 세트업글
def set_upgrade(selection, my_cart):
    set_price = 1500  # 세트 추가 비용
    large_price = 500  # 라지 업그레이드 비용

    print(f"선택하신 메뉴: {selection}")
    set_how = input("세트(1) 단품(2) 선택창(3): ")

    if set_how == '1':
        size = input("세트 사이즈 선택: 일반(1) 라지(2): ")
        if size == '2':  # 라지 선택
            set_price += large_price

        print(f"세트 추가 비용: +{set_price}원")

        # 세트메뉴 구성
        print("\n음료 메뉴 선택:")
        drink_menu = list(drinks.keys())
        display_menu(drink_menu, drinks)
        drink_choice = int(input("음료 번호를 선택하세요: "))
        chosen_drink = drink_menu[drink_choice - 1]

        print("\n사이드 메뉴 선택:")
        side_menu_list = list(sideMenu.keys())
        display_menu(side_menu_list, sideMenu)
        side_choice = int(input("사이드 번호를 선택하세요: "))
        chosen_side = side_menu_list[side_choice - 1]

        updated_name = selection + "세트"
        total_price = (
                burger[selection][0]  # 기본 버거 가격
                + set_price  # 세트 추가 비용
                + drinks[chosen_drink][0]  # 음료 가격
                + sideMenu[chosen_side][0]  # 사이드 가격
        )

        set_item = {
            "name": updated_name,
            "drink": chosen_drink,
            "side": chosen_side,
            "price": total_price,
        }
        my_cart.append(set_item)
        print(f"\n**{updated_name} 추가됨.\n세트 가격: {total_price}원**")

    elif set_how == '2':  # 단품 선택
        print(f"{selection} 단품이 선택되었습니다.")
        my_cart.append(selection)  # 단품은 그냥 이름만 추가

    elif set_how in ['3']:
        print("이전 단계로 돌아갑니다.")
        return

    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")


# 걍 장바구니 보여주기
def how_cart():
    print("--------------------------")
    print("장바구니 정보")
    if not myCart:
        print("장바구니가 비어 있습니다.")
    else:
        for item in myCart:
            if isinstance(item, dict):  # 세트 항목인 경우
                print(item["name"])  # 세트 이름만 출력
            else:  # 단품 항목인 경우
                print(item)  # 메뉴 이름만 출력
    print("--------------------------")


# 가격 계산 함수
def calculate(my_cart):
    total_price = 0
    for item in my_cart:
        if isinstance(item, dict):  # 세트 메뉴 항목일 경우
            total_price += item["price"]
        elif item in burger:  # 버거 단품일 경우
            total_price += burger[item][0]
        elif item in sideMenu:  # 사이드 단품일 경우
            total_price += sideMenu[item][0]
        elif item in drinks:  # 음료 단품일 경우
            total_price += drinks[item][0]
        elif item in desert:  # 디저트 단품일 경우
            total_price += desert[item][0]
        elif item in mcCafe:  # 맥카페 단품일 경우
            total_price += mcCafe[item][0]
        else:
            print(f"가격을 찾을 수 없는 항목: {item}")

    return total_price


# 결제 함수
def pay(payment1):
    while True:
        if payment1 == '2':
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
                continue
        else:
            print("잘못입력하셨습니다.")


# __name__() __main__ 아래에서 부터 메인


while True:  # 무한 반복 (주문을 계속 받기 위한 루프)
    key_while = [1, 1, 1, 1, 1]  # 각 while문의 제어 변수
    myCart = []  # 장바구니 생성

    first = input("주문하기(1): ")  # 첫 번째 선택: 주문하기
    if first == '1':
        where = input("식사 장소를 선택하세요 매장(1) 포장(2): ")  # 매장/포장 선택
        if where == '1':  # 매장 선택
            print("매장 식사를 선택하셨습니다.")
            while key_while[0]:  # 시간에 맞는 카테고리 출력 (화면만 일단 보여줌)
                get_happy_meal(hour, minute)
                category = get_available_categories(hour, minute)  # 현재 시간에 맞는 카테고리 얻기
                category_output()  # 카테고리 출력
                input_cate = int(input("카테고리 선택: "))  # 카테고리 선택

                selected_category = category[input_cate - 1]  # 선택된 카테고리
                key_while[1] = 1  # 카테고리로 돌아갔을때 아래 반복문 다시 활성화

                while key_while[1]:  # 유저가 카테고리 선택함
                    if selected_category == '버거':
                        burger_selection(burger, myCart)  # 버거 선택 함수 호출
                    elif selected_category == '맥런치':
                        menu_selection(mcLunch, myCart)
                    elif selected_category == '맥모닝':
                        menu_selection(mcMorning, myCart)
                    elif selected_category == '사이드':
                        menu_selection(sideMenu, myCart)
                    elif selected_category == '디저트':
                        menu_selection(desert, myCart)
                    elif selected_category == '맥카페':
                        menu_selection(mcCafe, myCart)
                    elif selected_category == '음료':
                        menu_selection(drinks, myCart)
                    elif selected_category == '해피밀':
                        menu_selection(happy_meal, myCart)
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
                        myCart.clear()
                        print("**장바구니가 초기화 되었습니다.**")
                        break
                    else:
                        print("1에서 5사이를 입력해주세요")
                    while key_while[2]:
                        payment = input("추가주문(1) 주문완료(2): ")
                        if payment == '1':
                            key_while[1] = 0
                            break
                        elif payment == '2':
                            pay(payment)  # 결제 함수 호출
                        else:
                            print("추가주문 오류")
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
