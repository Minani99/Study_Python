
def hanoi(n, start, last, help):
    global count
    if n == 1:
        count += 1
        print(f"{start} -> {last}")
    else:
        hanoi(n - 1, start, help, last)
        count += 1
        print(f"{start} -> {last}")
        hanoi(n - 1, help, last, start)

count = 0

n = int(input("원판: "))
hanoi(n, "A", "C", "B")
print(f"총 이동 횟수: {count}")
