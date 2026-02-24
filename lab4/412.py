import json

def compare_json(a, b, path=""):
    diffs = []

    # Получаем все ключи из обоих объектов (если это словари)
    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a.keys()) | set(b.keys())
        for key in keys:
            new_path = f"{path}.{key}" if path else key
            val_a = a.get(key, "<missing>")
            val_b = b.get(key, "<missing>")
            diffs.extend(compare_json(val_a, val_b, new_path))
    else:
        # Сравниваем значения, если они не словари
        if a != b:
            val_a = json.dumps(a, separators=(',', ':')) if a != "<missing>" else "<missing>"
            val_b = json.dumps(b, separators=(',', ':')) if b != "<missing>" else "<missing>"
            diffs.append(f"{path} : {val_a} -> {val_b}")

    return diffs

# Чтение входных данных
a = json.loads(input())
b = json.loads(input())

# Сравнение
differences = compare_json(a, b)

# Вывод
if differences:
    for line in sorted(differences):
        print(line)
else:
    print("No differences")