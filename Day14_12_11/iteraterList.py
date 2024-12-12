import random

r = iter([str(random.random())[:3] for i in range(10)])

for i in r:
    print(i)
