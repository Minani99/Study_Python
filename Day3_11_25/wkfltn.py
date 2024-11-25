def num3():
    number = [273, 103, 5, 32, 65, 9, 72, 800, 99]

    for num in number:
        count = 0
        while num > 0:
            num = num // 10
            count += 1
        print(f"{number[num]} 는 {count} 자릿수입니다")

def num4():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    out = [[], [], []]

    for i in a:
        out[(i+2)%3].append(i)

    print(out)

def num5():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, len(a) // 2):
        j = (i * 2) + 1
        print(f"i={i}, j={j}")
        a[j] = a[j] ** 2

    print(a)

num3()
num4()
num5()