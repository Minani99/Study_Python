import time


def draw():  # 타워 그리기
    print(f"count: {count}")

    output = ""
    for i in range(height - 1, -1, -1):
        for t in tower:
            if len(t) <= i:
                output += " " * (height + 2)
            else:
                output += "*" * t[i] + " " * (height + 2 - t[i])
        output += "\n"
    print(output + "──────────────────────────────")


def hanoi_tower(n, a, b, c):  # 개수, 시작, 경유, 도착
    global count

    if n == 1:
        tower[c].append(tower[a].pop())  # a > c 원반이동
        count += 1
        # draw()
        # time.sleep(interval)
        return

    hanoi_tower(n - 1, a, c, b)  # 맨 아래 빼고 나머지 a > b

    tower[c].append(tower[a].pop())  # 맨 아래거 a > c
    count += 1
    draw()
    time.sleep(interval)

    hanoi_tower(n - 1, b, a, c)  # 맨 아래 빼고 나머지 b > c
    return


height = 5  # 높이
count = 0  # 이동 횟수
interval = 1  # 시간 간격
tower = [[i for i in range(height, 0, -1)], [], []]

draw()  # 처음 상태 출력
time.sleep(interval)

hanoi_tower(height, 0, 1, 2)  # tower[0] tower[1] tower[2]
