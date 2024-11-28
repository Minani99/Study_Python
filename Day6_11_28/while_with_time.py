import time

n = 0
tick = time.time() +5 #>>1970년 1월1일 0,0,0 기준 흐른시간
while time.time() < tick:
    n += 1

print(n)