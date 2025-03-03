import math
import time
import multiprocessing

def calculate_sqrt_sum(number):
    sum=0.0
    for i in range(1, number+1):
        sum += math.sqrt(i)
    return sum
def main():
    numbers= [254658, 1269875, 95863656, 58647929, 862196355, 5962466]
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_sqrt_sum, numbers)
    end = time.time()
    print('Последовательные результаты: ', results)
    print('Время выполнения в сек.: ', end - start)

if __name__ == '__main__':
    main()