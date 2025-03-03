import requests
from multiprocessing import Pool
import time

urls = [
        'https://example.com',
        'https://teachmeskills.by',
        'https://github.com'
        ]

def fetch_url(url):
    response = requests.get(url)
    print(f"URL: {url}, Status Code: {response.status_code}")

if __name__ == '__main__':
    start_time = time.time()

    with Pool(processes=3) as pool:
        pool.map(fetch_url, urls)

    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time:.2f} секунд")
