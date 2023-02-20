import multiprocessing as mp

def increment(counter):
    counter.value += 1

def my_increment(my_counter):
    my_counter += 1


if __name__ == '__main__':
    my_counter = 1
    counter = mp.Value('i', 1)
    process = mp.Process(target=increment, args=(counter,))
    process.start()
    process.join()

    print(f'counter of type multiprocessing.Value is {counter.value}')


    for i in range(10):
        process = mp.Process(target=my_increment, args=(my_counter,))
        process.start()
        process.join()

    print(f'my_counter of type integer is {my_counter}')