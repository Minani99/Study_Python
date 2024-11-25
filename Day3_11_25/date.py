import datetime

now = datetime.datetime.now()
print(type(now)) #now 변수에 담긴 것은 date.datetime 객체
print(f"{now.year}년 {now.month}월 {now.day}일")
print(f"{now.hour}시 {now.minute}분 {now.second}초")

print("{}년{}월{}일{}시{}분{}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

if now.hour < 12:
    print(f"지금은 {now.hour}시로 오전")
else:
    print(f"지금은 {now.hour}시로 오후")

if now.weekday() == 1 and now.hour < 12 and now.month==11:
    print("조건 3개 만족")