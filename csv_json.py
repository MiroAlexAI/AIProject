import csv
import json

csv_file_path = 'data.csv'
json_file_path = 'jsonfile.json'

data = []

# Чтение CSV файла и добавление данных в список
with open(csv_file_path, encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Запись данных в JSON файл
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
