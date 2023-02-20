import multiprocessing as mp
def squares(numbers, squares_list):
    for n in numbers:
        squares_list.append(n ** 2)
    print(f'square_list inside process {squares_list}')
def cubes(numbers, result):
    i = 0
    for num in numbers:
        result[i] = num ** 3
        i += 1
    print(f'result Array inside process/function: {result[::]}')

if __name__ == '__main__':

    numbers = [1, 2, 3]
    squares_list = list()


    p = mp.Process(target=squares, args=(numbers, squares_list))
    p.start()
    p.join()


    print(f'squares_list outsite process {squares_list}')

    result = mp.Array('i', len(numbers))


    p1 = mp.Process(target=cubes, args=(numbers, result))
    p1.start()
    p1.join()

    print(f'result Array outside process {result[::]}')