import multiprocessing as mp
import time


def name_and_time(name):
    print(f'Hello {name}, current time is {time.time()}')
    print('Sleeping for 2 seconds ...')
    time.sleep(2)
    print('After sleeping ... exiting function.')


if __name__ == '__main__':
    process_list = list()


    for i in range(10):

        process = mp.Process(target=name_and_time, args=('Andrei',))
        process_list.append(process)


    for p in process_list:
        p.start()


    for p in process_list:
        p.join()

    print('Other instructions of the main module...')
    print('End of Script')