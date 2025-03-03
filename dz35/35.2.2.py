import requests
from concurrent.futures import ThreadPoolExecutor
import time

urls = [
        'https://example.com',
        'https://github.com',
        'https://booking.com'
        ]

def fetch_url(url):
    response = requests.get(url)
    print(f"URL: {url}, Status Code: {response.status_code}")

start_time = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(fetch_url, urls)

end_time = time.time()
print(f"Время выполнения: {end_time - start_time:.2f} секунд")
