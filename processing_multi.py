import multiprocessing as mp
import os
import  time
import random

def power(n):
    return n ** 2


# if __name__ == '__main__':
#     ls = [22, 33, 44, 55]
#     res = []
#     for x in ls:
#         res.append(power(x))
#     print(res)
#     res = [power(x) for x in ls]
#     print(res)
#     with mp.Pool(processes=4) as pool:
#         res = pool.map(power, ls)
#     print(res)
#     if __name__ == '__main__':
#         with mp.Pool(4) as pool:
#             async_data = [pool.apply_async(power, (x,))for x in ls]
#             result = [x.get() for x in async_data]

# def work():
#     pid = os.getpid()
#     print(f'Process ID: {pid} started')
#     time.sleep(random.randint(1, 3))
#     print(f'Process ID: {pid} ended')
#
# if __name__ == '__main__':
#     processes = []
#     for i in range(4):
#         p = mp.Process(target=work)
#         p.start()
#     for p in processes:
#         p.join()
#
#     print(f'All processes ended')

def producer(queue, n_items):
    for i in range(n_items):
        item = random.randint(1, 100)
        queue.put(item)
        print(f'Producer maked {item}')
        time.sleep(random.uniform(.1, .5))
    queue.put(None)
    print('Producer done')


def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        result = item ** 2
        print(f'Consumer maked {item} -> {result}')
        time.sleep(random.uniform(.2, .6))
    print('Consumer done')


if __name__ == '__main__':
    queue = mp.Queue()
    p_producer = mp.Process(target=producer, args=(queue, 10))
    p_consumer = mp.Process(target=consumer, args=(queue,))
    p_producer.start()
    p_consumer.start()
    p_producer.join()
    p_consumer.join()
    print('main process done')