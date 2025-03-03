import requests
import time

url = 'https://example.com'

start_time = time.time()
r = requests.get(url)
end_time = time.time()

print(r.status_code)
print(r.encoding)
print(r.text)
print(f"Время выпонения: {end_time - start_time}")
