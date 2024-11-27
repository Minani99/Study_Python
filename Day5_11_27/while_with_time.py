import time

n = 0

tick = time.time() + 5

while time.time() < tick:
    n+=1
    print(n)