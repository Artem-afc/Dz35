import math
import time
import threading

def calculate_sqrt_sum(number, results, index):
    sum=0.0
    for i in range(1, number+1):
        sum += math.sqrt(i)
    results[index] = sum


def main():
    numbers= [254658, 1269875, 9586366, 586479, 86219635, 5962466]
    results = [None]*len(numbers)
    threads = []
    start = time.time()
    for i,n in enumerate(numbers):
        thread = threading.Thread(target=calculate_sqrt_sum, args=(n,results,i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


    end = time.time()
    print('Потоковые результаты: ', results)
    print('Время выполнения в сек.: ', end - start)

if __name__ == '__main__':
    main()