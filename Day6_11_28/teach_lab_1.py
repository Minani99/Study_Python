import time

for i in range(20):
    t = time.time()
    t_str = str(t)
    t_rounded = t_str[7:12]

    what = input("맞춰보셔유(xxx.)>> ")

    if t_rounded == what:
        print("ㅊㅊ")
        break
    else:
        print(f"hint: {int(t)}")
        print(t_rounded)
print("20번끝")