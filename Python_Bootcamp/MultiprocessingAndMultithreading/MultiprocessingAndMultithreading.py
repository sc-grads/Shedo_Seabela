import multiprocessing as mp
import time
def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= 1
        lock.release()


if __name__ == '__main__':
    balance = mp.Value('i', 500)
    print(f'Balance BEFORE running processes: {balance.value}')

    lock = mp.Lock()


    p1 = mp.Process(target=deposit, args=(balance, lock))
    p2 = mp.Process(target=withdraw, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


    print(f'Balance AFTER running processes: {balance.value}')