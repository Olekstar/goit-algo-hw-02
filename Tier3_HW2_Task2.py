from collections import deque

def is_palindrome(text):
  
  # Очистити рядок від пробілів і привести до одного регістру
  text = text.lower().replace(" ", "")

  # Створити двосторонню чергу з символів рядка
  queue = deque(text)

  # Перевірити, чи збігаються символи з обох кінців черги
  while len(queue) > 1:
    if queue.popleft() != queue.pop():
      return f"не паліндромом"

  return f"паліндромом"

# Приклади використання
test_strings = ["А роза упала на лапу Азора", "Я несу суму в сумці", "1234321", "Привіт"]

results = {text: is_palindrome(text) for text in test_strings}

for text, result in results.items():
  print(f"{text}: {result}")
