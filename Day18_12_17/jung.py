import random as ra
from dataclasses import replace

tax_tab = []
before_array = []  # 이전라인
sub = 0
outlier = []  # 이상치 리스트
find_outlier = []
with open('근로소득세_문제.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        # 필요 없는 라인 제거
        if (line[0:5].strip().replace(',', '', ).isdigit()) == False:
            continue
        # 데이터 정제
        line = line.strip().replace(',', '').replace('-', '0').split('\t')
        line_c = map(lambda x: int(x), line)  # 숫자로 변경, line_c 한 번 쓰면 날아감
        line = list(line_c)  # line에 다시 넣음
        tax_tab.append(line)

before1 = ''
index = 1
e_index = []
# print(tax_tab)
## 이상치 찾기
for line in tax_tab:
    if before_array != []:  # 첫줄은 패스
        for l in range(12):
            for b in range(12):
                # 인덱스가 같은 것 차이 비교하기
                if l == b:
                    if line[l] - before_array[b] < 0:

                        # outlier.clear()
                        # 잘못된 라인의 위 아래 두 줄씩  (before_array라인 인덱스의 -2 -1 +1 +2)
                        for i in range(tax_tab.index(before_array) - 2, tax_tab.index(before_array) + 3, 1):
                            outlier.append(tax_tab[i])

                        e_index.append(l)  # 잘못된 곳의 열 인덱스를 저장해둠
                        find_outlier.append(outlier)
                        outlier = []
    before_array = line

# 잘못된 라인의 +-2줄이 모두 들어간 find_outlier를 돌며 잘못된 곳을 찾는다
index = 0
for f in find_outlier:  # 다섯 묶음
    l = e_index[index]  # e_index는 잘못된 열이 들어가있는 리스트, index값으로 하나씩 꺼내면서 참조한다
    index += 1
    for o in f:  # 한 묶음
        if l <= 2:
            value1 = int(str(0 - o[l]).replace('-', ''))
        else:
            value1 = o[(int(l) - 1)] - o[l]

        # 비교(value와 before)
        if before1 != '':

            # before1의 3%를 구하고 value1 - before1이 그 3%가 넘는다면 오류찾음
            if (value1 - before1) < 0:
                sub = int(str(value1 - before1).replace('-', ''))
            else:
                sub = (value1 - before1)
            if sub > before1 * 0.03:
                before1 = ''
                # 결측치 정상치로 변경(윗줄+아랫줄 / 2) (만약 아랫줄도 결측치일 경우->해결해야함)
                for tax_line in tax_tab:
                    if tax_line[0] == o[0]:
                        tax_tab[tax_tab.index(tax_line)][l] = int('{:.0f}'.format(
                            (tax_tab[tax_tab.index(tax_line) - 1][l] + tax_tab[tax_tab.index(tax_line) + 1][l]) / 2))
                before1 = ''
                break

        # before_value에 넣기
        before1 = value1

index = 1
list_all = []


def a(v):
    return "{:.0f}".format(v)


def x(**kwargs):
    i_tax = 0
    SAL = sal * 1000
    perc = {'국민연금': (4.5 * 0.01), '건강보험': (3.545 * 0.01), '요양보험': (12.95 * 0.01), '고용보험': (0.9 * 0.01)}
    dec = lambda x: int(("{:.0f}".format(x)).replace(("{:.0f}".format(x))[-1], '0'))

    # 근로소득세(월급의 부양가족수 반영한 세금)
    for tax_line in tax_tab:
        try:
            if tax_line[0] <= sal < tax_line[1]: i_tax = tax_line[f_num + 1]
        except:
            print('error! 텍스트 파일에서 해당 월급을 찾을 수 없습니다.')

    # 국민연금/건강보험/요양보험/고용보험/근로소득세/지방소득세
    tax_list = [dec(SAL * perc['국민연금']), dec(SAL * perc['건강보험']), dec((dec(SAL * perc['건강보험'])) * perc['요양보험']),
                dec(SAL * perc['고용보험']), i_tax, dec(i_tax * 0.1)]
    list_all.append({'이름': name, '나이': age, '월급': SAL, '부양가족수': f_num,
                     '국민연금': tax_list[0], '건강보험': tax_list[1], '요양보험': tax_list[2],
                     '고용보험': tax_list[3], '근로소득세': tax_list[4], '지방소득세': tax_list[5],
                     '월 예상 실수령액': SAL - sum(tax_list)})


def print_list(list):
    print()
    for i in list:
        print('{}: {}'.format(i, list[i]))


for i in range(10):
    # 이름
    name = '사람' + str(index)
    # 나이
    age = ra.randrange(20, 60)
    # 월급
    sal = (ra.randrange(3000, 10000))
    # 부양가족수
    f_num = ra.randrange(1, 10)
    # 국민연금/건강보험/요양보험/고용보험/근로소득세/지방소득세/월 예상 실수령액
    x(name=name, age=age, sal=sal, f_num=f_num)
    index += 1

list_all.sort(key=lambda l: l['월 예상 실수령액'], reverse=True)
print(list(map(print_list, list_all)))
