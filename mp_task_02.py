import threading
import time
import multiprocessing
import math
import asyncio

# Функции для АТ-01

# запускать с n = 700008
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


def sequence():
    start_time = time.time()

    fibonacci(700008)
    trapezoidal_rule(math.sin, 0, math.pi, 20000000)

    end_time = time.time()
    # время старта start_time
    # вычисление fibonacci от значения 700008
    # вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    # время окончания end_time
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    start_time = time.time()
    threads = []

    thread_1 = threading.Thread(target=fibonacci, args=(700008,))
    threads.append(thread_1)
    thread_1.start()
    thread_2 = threading.Thread(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000,))
    threads.append(thread_2)
    thread_2.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    # время старта start_time
    # вычисления на потоках:
    # 1. вычисление fibonacci от значения 700008
    # 2. вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    # время окончания end_time
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    start_time = time.time()
    processes = []

    process_1 = multiprocessing.Process(target=fibonacci, args=(700008,), daemon=True)
    processes.append(process_1)
    process_1.start()
    process_2 = multiprocessing.Process(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000,), daemon=True)
    processes.append(process_2)
    process_2.start()

    for process in processes:
        process.join()

    end_time = time.time()
    # время старта start_time
    # вычисления на процессах:
    # 1. вычисление fibonacci от значения 700008
    # 2. вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    # время окончания end_time
    print(f'processes time: {end_time - start_time: 0.2f} \n')


async def function():
    start_time = time.time()

    fibonacci(700008)
    trapezoidal_rule(math.sin, 0, math.pi, 20000000)

    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')

if __name__ == '__main__':
    sequence()
    threads()
    processes()
    asyncio.run(function())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        fibonacci = 6
        trapezoidal_rule = 2.000000000000087
        sequence time:  ???
        
        fibonacci = 6
        trapezoidal_rule = 2.000000000000087
        threads time:  ??? 
        
        fibonacci = 6
        trapezoidal_rule = 2.000000000000087
        processes time:  ???
    """
