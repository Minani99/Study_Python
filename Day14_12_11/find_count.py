import datetime
import sys
import time

sys.setrecursionlimit(10000) # 깊이 제한 해제
now = datetime.datetime.now()
count = 0


def finds(x):
    global count
    count += 1
    time.sleep(1)

    n = datetime.datetime.now()

    if x == 55:
        return count
    else:
        return finds(n.second)


print(finds(now.second))