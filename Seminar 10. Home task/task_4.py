"""Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

data_list = ["разработка", "администрирование", "protocol", "standard"]
for i in range(len(data_list)):
    print()
    word_encoded = str.encode(data_list[i], encoding="utf-8")
    print(f"Слово в байтовом представлении: {word_encoded}")
    word_decode = bytes.decode(word_encoded, "utf-8")
    print(f"Слово в строковом представлении: {word_decode}")
