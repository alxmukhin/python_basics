"""Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

data_list = [["ping", "yandex.ru"], ["ping", "youtube.com"]]
for i in range(len(data_list)):
    ping_call = subprocess.Popen(data_list[i], stdout=subprocess.PIPE)
    print(ping_call.stdout)
    for line in ping_call.stdout:
        encoding_info = chardet.detect(line)
        print(line.decode(encoding=encoding_info['encoding']))
