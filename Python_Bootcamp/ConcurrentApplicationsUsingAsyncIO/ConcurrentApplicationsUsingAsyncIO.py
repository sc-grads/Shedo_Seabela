import asyncio
import time


def sync_f():
    print('one', end=' ')
    time.sleep(
        1)
    print('two', end=' ')



async def async_f():
    print('one', end=' ')
    await asyncio.sleep(1)

    print('two', end=' ')


async def main():
    tasks = [async_f() for _ in range(3)]

    await asyncio.gather(*tasks)


s = time.time()
asyncio.run(main())
print(f'Execution time (ASYNC):{time.time() - s}')

print('\n')

s = time.time()
for _ in range(3):
    sync_f()
print(f'Execution time (SYNC):{time.time() - s}')