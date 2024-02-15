import queue
import time
import random

request_queue = queue.Queue()
request_id = 0  # Ініціалізація лічильника заявок

def generate_request():
    """Функція для генерації однієї нової заявки."""
    global request_id
    request_id += 1
    print(f"Вхідна заявка ID: {request_id}")
    request_queue.put(request_id)

def process_request():
    """Функція для обробки однієї заявки з черги."""
    if not request_queue.empty():
        current_request_id = request_queue.get()
        print(f"Початок обробки заявки з ID: {current_request_id}")
        time.sleep(2)
        print(f"Заявка з ID: {current_request_id} оброблена")
        request_queue.task_done()
    else:
        print("Черга порожня, очікування нових заявок...")

try:
    while True:
        # Імітація випадковості генерації заявок
        if random.random() < 0.5:  # 50% шанс генерації нової заявки
            generate_request()
        
        # Обробка заявки, якщо вона є в черзі
        process_request()
        
        # Імітація випадкової затримки між ітераціями
        time.sleep(random.uniform(1, 3))
except KeyboardInterrupt:
    print("\Завершення програми за запитом користувача...")
 