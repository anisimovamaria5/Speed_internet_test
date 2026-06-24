import requests
import time
import sys

def get_speed_internet(url: str, count_requests: int):
    """Вычисляет скорость интернета"""

    total_time = 0
    total_size = 0

    for i in range(count_requests):
        try:
            start = time.time()

            result = requests.get(url)
            content = result.content

            end = time.time()
            average_time = end - start

            size = len(content) / (1024 * 1024)
            speed = size / average_time

            total_time += average_time
            total_size += size

            print(f"Запрос {i+1}: {average_time:.2f} с, {size:.5f} МБ, {speed:.5f} МБ/с")

        except Exception as e:
            print(f"Ошибка: {e}")
    if total_time:
        average_time = total_time / count_requests
        average_speed = total_size / total_time

        print(f"Среднее время запроса: {average_time:.2f} с")
        print(f"Объем скачанных данных: {total_size:.5f} МБ")
        print(f"Средняя скорость: {average_speed:.5f} МБ/с")


if __name__ == "__main__":
    url = sys.argv[1]
    count_requests = 10
    get_speed_internet(url, count_requests)



