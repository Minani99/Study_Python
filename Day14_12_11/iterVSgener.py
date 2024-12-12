import time


def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"


list_job = iter([longtime_job() for i in range(5)])
print(next(list_job))

print("#" * 10)
list_job = (longtime_job() for i in range(5))

print(next(list_job))
