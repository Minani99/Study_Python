import datetime

burger = {'버거':
              {'비프':
                   {'더블쿼터파운더치즈버거': [6000, '111', 'Y'],
                    '쿼터파운더치즈버거': [5000, '111', 'Y'],
                    '불고기버거': [3000, '111', 'Y'],
                    '더블불고기버거': [3500, '111', 'Y'],
                    '빅맥버거': [4500, '111', 'Y'],
                    '치즈버거': [3000, '111', 'Y'],
                    '베이컨토마토디럭스버거': [5000, '111', 'Y'],
                    '햄버거': [2500, '111', 'Y']},
               '치킨':
                   {'맥스파이시상하이버거': [5500, '111', 'Y'],
                    '맥치킨버거': [4500, '111', 'Y'],
                    '맥크리스피디럭스버거': [6000, '111', 'Y']}
               }
          }
lunch = {'맥런치':
             {'빅맥세트': [5500, '010', 'Y'],
              '더블불고기세트': [4500, '010', 'Y'],
              '베이컨토마토디럭스세트': [6000, '010', 'Y']}
         }
morning = {'맥모닝':
               {'에그맥머핀': [2800, '100', 'Y'],
                '소시지에그맥머핀': [3000, '100', 'Y'],
                '베이컨에그맥머핀': [3300, '100', 'Y']}
           }
hsnack = {'해피스낵':
              {'드립커피M': [1000, '111', 'N'],
               '제로콜라M': [1000, '111', 'N'],
               '치즈버거': [2000, '111', 'N'],
               '치즈스틱2조각': [2000, '111', 'N'],
               '후렌치후라이s': [1000, '111', 'N']}
          }
side = {'사이드':
            {'맥윙2조각': [2000, '111', 'N'],
             '맥윙4조각': [3500, '111', 'N'],
             '맥윙8조각': [6000, '111', 'N'],
             '치즈스틱4조각': [3800, '111', 'N'],
             '후렌치후라이s': [1000, '111', 'N'],
             '후렌치후라이M': [1500, '111', 'N'],
             '후렌치후라이L': [2000, '111', 'N'],
             '맥너겟4조각': [2000, '111', 'N'],
             '맥너겟6조각': [2800, '111', 'N']}
        }
dessert = {'디저트':
               {'맥플러리': [3000, '111', 'N'],
                '아이스크림콘': [1000, '111', 'N']}
           }
cafe = {'맥카페':
            {'카페라떼': [2000, '111', 'N'],
             '아이스카페라떼': [2000, '111', 'N'],
             '아이스드립커피': [1000, '111', 'N'],
             '드립커피': [1000, '111', 'N']}
        }
beverage = {'음료': {'콜라M': [1000, '111', 'N'],
                   '콜라L': [1500, '111', 'N'],
                   '콜라제로M': [1000, '111', 'N'],
                   '콜라제로L': [1500, '111', 'N'],
                   '사이다M': [1000, '111', 'N'],
                   '사이다L': [1500, '111', 'N'],
                   '오렌지주스': [1000, '111', 'N'],
                   '생수': [1000, '111', 'N']
                   }
            }
hmeal = {'해피밀': {'에그맥머핀': [4000, '100', 'Y'],
                 '소시지에그맥머핀': [4200, '100', 'Y'],
                 '베이컨에그맥머핀': [4500, '100', 'Y'],
                 '치즈버거': [4200, '011', 'Y'],
                 '햄버거': [3800, '011', 'Y'],
                 '불고기버거': [4200, '011', 'Y']
                 }
         }
plus_menu = {1: {'쉬림프 스낵랩': [4000]},
             2: {'치즈스틱4조각': [3800]},
             3: {'콜라M': [1000]},
             0: {'선택안함': [0]}}
MENU = [burger, lunch, morning, hsnack, side, dessert, cafe, beverage, hmeal]
SELECTION = {
    '주문': {'1': '주문하기'},
    '장소': {'1': '포장', '2': '매장', 0: '처음으로'},
    '세트': {'1': '세트', '2': '단품', -2: '이전으로', 0: '처음으로'},
    '사이즈': {'1': '일반', '2': '라지', -3: '이전으로', 0: '처음으로', -1: '취소'},
    '사이드': {'1': '감자튀김', '2': '코울슬로', -4: '이전으로', 0: '처음으로', -1: '취소'},
    '해피밀사이드': {'1': '파인애플', -4: '이전으로', 0: '처음으로', -1: '취소'},
    '음료': {'1': '콜라', '2': '사이다', '3': '오렌지주스', '4': '생수', -5: '이전으로', 0: '처음으로', -1: '취소'},
    '해피밀음료': {'1': '오렌지주스', '2': '생수'},
    '수량': {0: '처음으로', -1: '취소', '★': '수량입력>'},
    '옵션1': {'1': '장바구니담기', '2': '사이즈변경', '3': '사이드변경', '4': '음료변경', '5': '수량변경', 0: '처음으로', -1: '취소'},  # 세트
    '옵션2': {'1': '장바구니담기', '2': '수량변경', 0: '처음으로', -1: '취소'},  # 단품
    '결제': {'1': '결제하기', '-1': '결제안함'},
    '추가주문': {'1': '주문 완료', '-1': '추가 주문'},
    '결제방법': {'1': '신용카드', '2': '모바일결제'}
}
ARR_TITLE = ['===>>카테고리===============================================',
             '===>>메뉴===========================',
             '===>>장소선택===============================================',
             '===>>세트선택===============================================',
             '===>>세트사이즈=============================================',
             'Q. 원하는 카테고리 혹은 메뉴를 입력하세요>',
             '===>>사이드=================================================',
             '===>>음료===================================================',
             '===>>옵션변경===============================================',
             '--지금 담은 메뉴 확인--',
             '===>>수량==================================================',
             '',
             '★★장바구니에 담긴 메뉴가 있습니다. 결제하시겠습니까?',
             '===>★함께 즐기면 더욱 좋습니다==============================',
             '===>주문===================================================']

index = 1  # 인덱스변수
time_category = []  # 시간대별 메뉴 담을 리스트
str_category = ''  # 카테고리 들어갈 string변수
lab_sml_category = ''  # 선택한 소분류를 넣어놓을 변수(소분류의 세부메뉴 출력 시 필요)
input_string = ''  # SELECTION 선택지 출력 시 사용 (가로로 보여주기 위함)
end_flag = ''  # 주문 완료 후 되돌아갈 때 원하는 위치(1.주문하기)로 보내기 위한 플래그 변수
pay_flag = ''  # 결제 물어볼 때 사용하는 플래그 변수
menu_info = {}  # 현재 선택한 메뉴
cart = {}  # 장바구니
cart_index = 1  # 장바구니 추가 시 번호 매길 변수
dest = 0  # While문 조건 변수
ask3 = '1'  # 입력한 메뉴 인덱스를 넣어놓는 변수


## 시간 string 타입으로 변환 함수
def make_time(t):
    if len(str(t)) == 1:
        return '0' + str(t)
    else:
        return str(t)


## 시간대 별 카테고리 생성 함수
def make_cat(num):
    for i in MENU:
        for j in i:
            for k in i[j]:
                if i in time_category:  # 이미 동일한 카테고리가 있다면 continue
                    continue
                else:
                    if type(i[j][k]) is dict:  # dic타입 => 소분류 있음
                        time_category.append(i)
                    elif type(i[j][k]) is list:  # list타입 => 소분류 없음
                        mealnum = i[j][k][1][num]  # '111'(아점저)에 해당하는 문자열 mealnum에 넣어둠
                        if mealnum == '1':
                            time_category.append(i)


## SELECTION dict 호출 함수
def make_selection(opt_name, check):
    input_str = ''
    for key, element in SELECTION[opt_name].items():
        if check == 'A' and element == '이전으로':  # 옵션 변경 에서는 '이전으로' 버튼 비활성화
            pass
        else:
            input_str += ('{}.{} '.format(key, element))  # 옵션 변경 출력
    input_num1 = input(input_str)
    return input_num1


## 옵션 생성 함수
def make_option(opt_name, title_num, check):
    print(ARR_TITLE[title_num])
    input_num = make_selection(opt_name, check)

    if int(input_num) <= 0:
        destination = int(input_num)
        return destination
    else:
        if opt_name == '수량':
            menu_info[opt_name] = input_num
        else:
            menu_info[opt_name] = SELECTION[opt_name][input_num]  # 고른거 넣기
        return 9


while dest <= 0:
    dest = -1
    cart = {}  # 장바구니 비우기
    index = 1  # 인덱스 초기화
    end_flag = ''  # 주문완료 flag 초기화

    ## 1.주문하기
    ask1 = make_selection('주문', 'B')
    if ask1 == '1':
        print(ARR_TITLE[2])
        input_string = ''
        for key, element in SELECTION['장소'].items():
            input_string += ('{}.{} '.format(key, element))

        ## 1.포장/2.매장
        ask2 = input(input_string)
        if int(ask2) <= 0:
            continue
        else:
            menu_info['장소'] = (SELECTION['장소'][ask2])
        while dest <= -1:
            dest = -2
            pay_flag = ''  # 결제 flag 초기화
            menu_info = {}  # 선택메뉴 초기화
            str_category = ''  # 카테고리 출력 변수 초기화
            menu_flag = ''  # 해피밀 flag 초기화
            index = 1  # 인덱스 초기화

            now = datetime.datetime.now()
            time = int(make_time(now.hour) + make_time(now.minute))  # hhmm
            if 400 < time < 1030:
                make_cat(0)
            elif 1030 < time < 1400:
                make_cat(1)
            else:
                make_cat(2)

            ## 카테고리 생성
            for category in time_category:
                for cat in category:
                    str_category = ('{} {}.{}'.format(str_category, str(index), cat))
                    index += 1

            ## 전체 메뉴 보여주기
            while dest <= -2:
                dest = -3
                ask3 = ask3[0]
                print(ARR_TITLE[0])
                print(str_category.strip())  # 카테고리 출력
                str_sml_category = '10.전체'
                arr_sml_category = ['전체']
                for cat1 in time_category[int(ask3) - 1]:
                    index = 1  # 소분류 인덱스
                    menu_index = 1  # 세부메뉴 인덱스
                    str_title = ''

                    for cat2 in time_category[int(ask3) - 1][cat1]:
                        # dict => 소분류있음
                        if type(time_category[int(ask3) - 1][cat1][cat2]) is dict:
                            if str_title == '':
                                str_title = ARR_TITLE[1]
                                print(str_title)
                                # 소분류 출력
                                for sml in time_category[int(ask3) - 1][cat1].keys():
                                    str_sml_category = '{} {}.{}'.format(str_sml_category, ('1' + str(index)), sml)
                                    index += 1
                                    arr_sml_category.append(sml)
                                print(str_sml_category)

                            # 세부 메뉴 출력
                            for cat3 in time_category[int(ask3) - 1][cat1][cat2]:
                                # 소분류 선택 시에 그에 맞는 메뉴를 보여주어야 함
                                if lab_sml_category != '':
                                    if lab_sml_category == cat2:  # if 선택한 이름 == 반복하고있는 소분류
                                        print('{}. {} {}'.format(ask3 + '-' + str(menu_index), cat3,
                                                                 time_category[int(ask3) - 1][cat1][cat2][cat3][0]))
                                        menu_index += 1
                                # 모든 메뉴 출력
                                else:
                                    print('{}. {} {}'.format(ask3 + '-' + str(menu_index), cat3,
                                                             time_category[int(ask3) - 1][cat1][cat2][cat3][0]))
                                    menu_index += 1

                        # list => 소분류없음
                        elif type(time_category[int(ask3) - 1][cat1][cat2]) is list:
                            # 세부 메뉴 출력
                            if str_title == '':
                                str_title = ARR_TITLE[1]
                                print(str_title)
                            print('{}. {} {}'.format(ask3 + '-' + str(menu_index), cat2,
                                                     time_category[int(ask3) - 1][cat1][cat2][0]))
                            menu_index += 1
                print()

                ## 장바구니 확인
                if cart != {} and pay_flag == '':
                    print(ARR_TITLE[12])
                    ask9 = make_selection('결제', 'B')

                    ## 결제
                    if ask9 == '1':
                        ## 함께 즐기면 더욱 좋습니다
                        while True:
                            print()
                            print(ARR_TITLE[13])
                            menu_index = 1
                            for P in plus_menu:
                                for p in plus_menu[P]:
                                    if P == 0:
                                        print('{}. {}'.format(P, p))
                                    else:
                                        print('{}. {} : {}원'.format(P, p, plus_menu[P][p][0]))
                            ask10 = input(ARR_TITLE[5])

                            ## 끼워팔기 메뉴 선택
                            if int(ask10) > 0:
                                for p in plus_menu[int(ask10)]:
                                    menu_info['메뉴'] = p
                                    menu_info['메뉴정보'] = plus_menu[int(ask10)][p]
                                    menu_info['수량'] = '1'
                                cart[cart_index] = menu_info
                                print('{} 을/를 장바구니에 담았습니다.'.format(cart[cart_index]['메뉴']))
                                cart_index += 1

                            ## 결제
                            else:
                                # 장바구니 출력
                                print()
                                print(ARR_TITLE[14])
                                print('-장소 : {}'.format(SELECTION['장소'][ask2]))
                                total = 0
                                for C in cart:
                                    string1 = ''
                                    quan = 1
                                    for c in cart[C]:
                                        if c == '메뉴':
                                            print('{}){}'.format(C, cart[C][c]))
                                        elif c == '수량':
                                            if string1 != '':
                                                print('옵션:{}'.format(string1))
                                            print('{}:{}'.format(c, cart[C][c]))
                                            quan = cart[C][c]
                                        elif c == '메뉴정보':
                                            print('가격:{}원'.format(cart[C][c][0]))
                                            total += int(cart[C][c][0]) * int(quan)
                                        else:
                                            string1 += '{}({}) '.format(c, cart[C][c])
                                print('TOTAL:{}원'.format(total))

                                ## 추가주문 확인
                                ask11 = make_selection('추가주문', 'B')
                                if int(ask11) < 0:
                                    dest = int(ask11)
                                    break

                                ## 주문완료
                                ask12 = make_selection('결제방법', 'B')
                                print('주문번호:000번')  ##주문번호 출력
                                print('주문완료! 감사합니다:)')  ##주문완료
                                print()
                                dest = 0
                                end_flag = 'X'
                                break

                    else:  # 결제안함
                        pay_flag = 'X'  # 'X' -> 장바구니에 담겨도 결제를 물어보지 않음

                if end_flag == 'X':  # 주문완료 후, 해당 while문 탈출
                    break

                # Q. 원하는 카테고리 혹은 메뉴를 입력하세요
                ask3 = input(ARR_TITLE[5])
                # 1. 카테고리 선택
                if ask3 in str_category:
                    print('< {}.{} >'.format(ask3, list(time_category[int(ask3) - 1].keys())[0]))

                # 2. 소분류 선택
                elif ask3 in str_sml_category:
                    print('< {}.{} >'.format(ask3, arr_sml_category[int(ask3[1])]))
                    if int(str(ask3[1])) > 0:
                        lab_sml_category = arr_sml_category[int(ask3[1])]  # 선택한 소분류 이름
                    else:
                        lab_sml_category = ''
                    ask3 = ask3[0]  # ask3은 카테고리의 라벨넘버로 변경

                # 3. 세부메뉴 선택
                #   menu_info에 메뉴 정보 저장
                else:
                    # 1. 버거 (소메뉴 존재)
                    if ask3[0] == '1':
                        index = 1
                        for i in time_category[int(ask3[0]) - 1]:
                            if lab_sml_category == '':
                                if int(ask3[2:]) > 8:
                                    lab_sml_category = '치킨'
                                    index = 9  # 치킨 버거 메뉴 index -> 9부터 시작
                                else:
                                    lab_sml_category = '비프'
                                    index = 1
                            for j in time_category[int(ask3[0]) - 1][i][lab_sml_category]:
                                if index == int(ask3[2:]):
                                    menu_info['메뉴'] = j
                                    menu_info['메뉴정보'] = time_category[int(ask3[0]) - 1][i][lab_sml_category][j]
                                index += 1
                    # 1. 버거 외의 메뉴
                    else:
                        for k in time_category[int(ask3[0]) - 1]:
                            for l in time_category[int(ask3[0]) - 1][k]:
                                if index == int(ask3[2]):
                                    menu_info['메뉴'] = l
                                    menu_info['메뉴정보'] = time_category[int(ask3[0]) - 1][k][l]
                                index += 1

                    ## 세트/단품
                    while dest <= -3:
                        dest = -4
                        # 해피밀/맥런치 세트의 경우, 예외가 있기 때문에 flag로 미리 확인해준다
                        for m in hmeal['해피밀']:
                            if m == menu_info['메뉴']:
                                menu_flag = 'H'
                        for l in lunch['맥런치']:
                            if l == menu_info['메뉴']:
                                menu_flag = 'L'

                        # 세트/단품 선택이 필요한 메뉴
                        if menu_info['메뉴정보'][2] == 'Y':
                            # 1.세트/2.단품
                            print(ARR_TITLE[3])
                            input_string = ''

                            # 맥런치 -> ask4를 1(세트)로 고정 후 이동 / 그 외에는 세트,단품 선택 필요
                            if menu_flag == 'L':
                                ask4 = '1'
                            else:
                                for key, element in SELECTION['세트'].items():
                                    input_string += ('{}.{} '.format(key, element))
                                ask4 = input(input_string)

                            if int(ask4) <= 0:
                                dest = int(ask4)
                                ask3 = ask3[0]
                                break
                            else:
                                # 세트선택
                                if ask4 == '1':
                                    menu_info['메뉴정보'][0] += 1500  # 가격 +1500 추가
                                    # 사이즈
                                    while dest <= -4:
                                        dest = -5
                                        ret_val = make_option('사이즈', 4, 'B')
                                        if ret_val <= 0:
                                            dest = ret_val
                                            break
                                        # 사이드
                                        while dest <= -5:
                                            dest = -6
                                            if menu_flag == 'Y':
                                                ret_val = make_option('해피밀사이드', 6, 'B')
                                            else:
                                                ret_val = make_option('사이드', 6, 'B')
                                            if ret_val <= 0:
                                                dest = ret_val
                                                break
                                            # 음료
                                            while dest <= -6:
                                                if menu_flag == 'Y':
                                                    ret_val = make_option('해피밀음료', 7, 'B')
                                                else:
                                                    ret_val = make_option('음료', 7, 'B')
                                                if ret_val <= 0:
                                                    dest = ret_val
                                                    break
                                                else:
                                                    menu_info['수량'] = '1'
                                                    dest = 1
                                # 단품선택
                                elif ask4 == '2':
                                    menu_info['수량'] = '1'
                                    dest = 1

                        # 세트 혹은 단품 고정 메뉴
                        else:
                            menu_info['수량'] = '1'
                            dest = 1

            ## 장바구니 담기 전 마지막 옵션,수량 변경
            while dest >= 1:
                # 메뉴정보 위치 변경
                menu_info_copy = menu_info
                menu_info = {}
                for menu in menu_info_copy:
                    if menu == '메뉴정보':
                        continue
                    menu_info[menu] = menu_info_copy[menu]
                menu_info['메뉴정보'] = menu_info_copy['메뉴정보']

                ###지금 담은 메뉴###
                print()
                print(ARR_TITLE[9])
                for key, value in menu_info.items():
                    if type(value) == list:
                        print('{}: {}'.format('금액', str(value[0]) + '원'))
                    else:
                        print('{}: {}'.format(key, value))

                print(ARR_TITLE[8])

                # 세트 선택일 경우
                if (menu_info['메뉴정보'][2] == 'Y' and menu_info.get('사이드') != None):
                    input_string = ''
                    for key, element in SELECTION['옵션1'].items():
                        input_string += ('{}.{} '.format(key, element))
                    ask8 = input(input_string)
                    if int(ask8) <= 0:  # 처음으로
                        dest = int(ask8)
                        break
                    elif ask8 == '1':  # 장바구니
                        cart[cart_index] = menu_info
                        cart_index += 1
                        dest = -1
                        break
                    elif ask8 == '2':  # 사이즈 변경
                        ret_val = make_option('사이즈', 4, 'A')
                        if ret_val <= 0:
                            dest = ret_val
                            break
                    elif ask8 == '3':  # 사이드 변경
                        if menu_flag == 'Y':
                            ret_val = make_option('해피밀사이드', 6, 'A')
                        else:
                            ret_val = make_option('사이드', 6, 'A')
                        if ret_val <= 0:
                            dest = ret_val
                            break
                    elif ask8 == '4':  # 음료 변경
                        if menu_flag == 'Y':
                            ret_val = make_option('해피밀음료', 7, 'A')
                        else:
                            ret_val = make_option('음료', 7, 'A')
                        if ret_val <= 0:
                            dest = ret_val
                            break
                    elif ask8 == '5':  # 수량 변경
                        ret_val = make_option('수량', 10, 'A')
                        if ret_val <= 0:
                            dest = ret_val
                            break

                # 단품 선택일 경우
                else:
                    input_string = ''
                    for key, element in SELECTION['옵션2'].items():
                        input_string += ('{}.{} '.format(key, element))
                    ask8 = input(input_string)
                    if int(ask8) <= 0:
                        dest = int(ask8)
                        break
                    elif ask8 == '1':  # 장바구니
                        cart[cart_index] = menu_info
                        cart_index += 1
                        dest = -1
                        break
                    elif ask8 == '2':  # 수량 변경
                        ret_val = make_option('수량', 10, 'A')
                        if ret_val <= 0:
                            dest = ret_val
                            break
