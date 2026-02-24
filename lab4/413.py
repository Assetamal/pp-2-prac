import json
import re

def resolve_path(data, path):
    # Разделяем путь на токены: ключи и индексы
    tokens = re.findall(r'\w+|\[\d+\]', path)
    current = data

    try:
        for token in tokens:
            if token.startswith('['):
                # Индекс массива
                index = int(token[1:-1])
                current = current[index]
            else:
                # Ключ объекта
                current = current[token]
        # Вернуть компактное JSON-представление значения
        return json.dumps(current, separators=(',', ':'))
    except (KeyError, IndexError, TypeError):
        return "NOT_FOUND"

# Чтение JSON
data = json.loads(input())

# Чтение числа запросов
n = int(input())
for _ in range(n):
    query = input().strip()
    print(resolve_path(data, query))