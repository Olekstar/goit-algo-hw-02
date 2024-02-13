import queue
import time

request_queue = queue.Queue()

def generate_requests(n):
    """Функція для генерації n нових заявок."""
    for i in range(n):
        request_id = i + 1
        print(f"Вхідна заявка ID: {request_id}")
        request_queue.put(request_id)

def process_requests_with_delay():
    """Функція для послідовної обробки заявок з черги з імітацією затримки обробки."""
    while not request_queue.empty():
        request_id = request_queue.get()
        print(f"Початок обробки заявки з ID: {request_id}")
        time.sleep(2)
        print(f"Заявка з ID: {request_id} оброблена")
        request_queue.task_done()

generate_requests(5)
process_requests_with_delay()
