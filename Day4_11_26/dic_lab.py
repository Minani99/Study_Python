def num2():
    pets = [
        {"name": "구름", "age": 5},
        {"name": "초코", "age": 3}
    ]
    for i in pets:
        print(f"{i["name"]} {i["age"]}살")

#딕셔너리 형태로 1부터 9까지 숫자가 각 몇번씩 나왔는지 카운트
def num3():
    num = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
    counter = {}#딕셔너리 내부 키 검사방법 >> get() >> None

    for i in num:
        if i in counter:
            counter[i] = counter[i] + 1
        else:
            counter[i] = 1

    print(counter)

def num4():
    c = {
        "name" : "기사",
        "level" : 12,
        "items" : {
            "sword" : "불꽃의 검",
            "armor" : "풀플레이트"
        },
        "skill" : ["베기", "세게 베기", "아주 세게 베기"]
    }

    # for key in c:
    #     if type(c[key]) is str:
    #         print(key, c["name"])
    #
    #     elif type(c[key]) is int:
    #         print(key, c["level"])
    #
    #     elif type(c[key]) is dict:
    #         for i in c[key]:
    #             print(i, c["items"][i])
    #     else:
    #         # for i in c[key]:
    #         #     print("{} : {}".format(key,i))
    #         for i in range(len(c[key])):
    #             print(key, c["skill"][i])

    for key in c:
        if type(c[key]) is list:
            for i in c[key]:
                print("{} : {}".format(key,i))
        elif type(c[key]):
            print("{} : {}".format(key,c[key]))
        else:
            print("{} : {}".format(key,c[key]))


num2()
num3()
num4()