import threading
import time

def name_and_time(name):
    print(f'Hello {name}, current time is {time.time()}')
    print('Sleeping for 2 seconds ...')
    time.sleep(2)
    print('After sleeping ... exiting function.')

if __name__ == '__main__':
    thread_list = list()

    for i in range(10):

        thread = threading.Thread(target=name_and_time, args=('Andrei',))
        thread_list.append(thread)

    for t in thread_list:
        t.start()


    for t in thread_list:
        t.join()

    print('Other instructions of the main module...')
    print('End of Script')

