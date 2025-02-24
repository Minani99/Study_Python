import threading
import time

counter = 0

lock = threading.Lock()


def increment(threadname):
    global counter
    lock.acquire()
    try:
        for a in range(100):
            time.sleep(0.01)
            counter += 1
            print(f'{threadname} count{counter}')
            # th1, th2 서브스레드
    finally:
        lock.release()


thread1 = threading.Thread(target=increment, args=('th1',))  # 서브스레드1
thread2 = threading.Thread(target=increment, args=('th2',))  # 서브스레드2

thread1.daemon = True
thread2.daemon = True

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Count: {counter}')  # 메인스레드 실행

# 프로세스의 종료: 메인스레드의 종료로 잡지만 서브스레드가 작업이 마친 상태가 아니라면
# 서브스레드 작업을 마치고 프로세스가 닫힘
# 데몬: 서브스레드를 데몬으로 설정(demon=True)하면, 메인스레드 종료시 프로세스 종료
# join(): thread1.join() => 스레드1이 마칠때까지 기다려라


# sub thread가 1개 있다.
# 위 서브스레드는 for문으로 1~100000까지 카운트 올리는 함수에 연결
# 데몬이고, join이 없다면? =데몬스레드의 종료 여부 상관 없이 메인스레드 종료시점에 프로세스 종료
# 데몬이고, join이 있다면? =메인스레드가 데몬스레드가 할 일을 전부 마칠 때까지 기다린다.
# 서브, join이 없다면? =메인스레드가 서브스레드를 기다리진 않지만 프로세스를 종료하진 않는다
# 서브, join이 있다면? =메인스레드가 서브스레드의 작업의 완료를 기다려주고 그 후에 메인 스레드가 진행
