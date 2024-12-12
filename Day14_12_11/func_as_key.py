game_item = [
    {
        "이름": "아드레날린각인서",
        "가격": 300000
    },
    {
        "이름": "저주받은인형각인서",
        "가격": 180000
    },
    {
        "이름": "타격의대가각인서",
        "가격": 80000
    }]


# def price(gi):
#     return gi["가격"]

#
# print("제일싼거")
# print(min(game_item, key=price))
#
# print("제일싼거")
# print(max(game_item, key=price))

print("제일싼거")
print(min(game_item, key=lambda gi: gi["가격"]))

print("제일싼거")
print(max(game_item, key=lambda gi: gi["가격"]))


max_value = lambda a,b:a if a>b else b
ssum = lambda *args :sum(args)
print(ssum(1,2,3,4,5,6))

game_item.sort(key=lambda gi:gi["가격"])
for i in game_item:
    print(i)