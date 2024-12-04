import threading
import time
import multiprocessing
import math
import requests
import asyncio

# список url для АТ-01
urls = ['https://www.example.com'] * 10


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequence():
    start_time = time.time()

    for url in urls:
        fetch_url(url)

    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    start_time = time.time()
    threads = []

    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    # время старта start_time
    # выполнение с помощью потоков функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех потоков)
    # время окончания end_time
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    start_time = time.time()
    processes = []

    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=(url,), daemon=True)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    # время старта start_time
    # выполнение с помощью процессов функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех потоков)
    # время окончания end_time
    print(f'processes time: {end_time - start_time: 0.2f} \n')


async def function():
    start_time = time.time()

    for url in urls:
        fetch_url(url)

    end_time = time.time()
    print(f'function time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()
    asyncio.run(function())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):

        sequence time:  ???

        threads time:  ???

        processes time:  ???
    """
