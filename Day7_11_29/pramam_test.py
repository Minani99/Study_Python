# x = 100
# x = 200 + x
#
# def x(x,y):
#     x=5
#     x=x+100
#     print(x)
#
# x(100,x)
# print(x)
# aaa = x

#def로 만드는 사용자 정의 함수의 이름도 식별자
#def x() gkatnfmf wjddml gn a = x 라는 코드를 작성하면 A() 호출가능
#
# def xx(l):
#     for i in l:
#         return i
# a = 100
a = ["123","234",1,2 ]
print(a)
print(id(a))#a의 메모리 주소
import time
t = str(time.time()).split(".")[0][1]
def func1():
    print("1번 함수 실행")
def func2():
    print("5보다 자금")

def xx(l):
    hello = "xx"
    print(hello)
    print(id(hello),"hello의 실제 위치")
    if int(t) > 5:
        return l[0]
    else:
        return l[3]
s = func1
lists = []
for i in range(10):
    lists.append(s)
xx(lists)()
xx(lists)()
print(id(a))

for i in range(500):
    print(i," ",id(i),"실제 주소")

print(id(a))
pointer = id(a)

print(id(pointer))