"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

list_data = [4, 8, 12]
dict_data = {"1": "2460", "2": "2475"}
upload_data = {"List": list_data, "Integer": 525, "Dictionary": dict_data}

with open("file.yaml", "w") as f_n:
    yaml.dump(upload_data, f_n, default_flow_style=False, allow_unicode=True)

with open("file.yaml") as f:
    download_data = yaml.load(f, Loader=yaml.FullLoader)
    print(download_data)

if upload_data == download_data:
    print("Cовпадают")
else:
    print("Не совпадают")
