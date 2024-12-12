# 제너레이터 함수
def test():
    print("A")
    yield 1
    print("B")
    yield 2
    print("C")

output = test()

print("-------------------")
a = next(output)
print(a)
print("-------------------")
b = next(output)
print(b)
print("-------------------")
c = next(output)
print(c)
print("-------------------")
next(output)