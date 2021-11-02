from threading import Thread
import time

def func1():
    while True:
        time.sleep(6)
        print("func1()")
        time.sleep(1)

def func2():
    while True:
        time.sleep(3)
        print("func2()")

if __name__ == '__main__':
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
