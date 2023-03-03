"""Задание 3.

Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

dict_default = {
    "название": None,
    "цена": None,
    "количество": None,
    "ед.": None
}
number_of_goods = int(input("Укажите количество товаров которое вы хотите"
                            " занести в базу: "))
database_structure = []
i = 0
while i < number_of_goods:
    dict_base = dict_default.copy()
    dict_base["название"] = input("Введите название изделия: ")
    dict_base["цена"] = int(input("Введите цену изделия: "))
    dict_base["количество"] = int(input("Введите количество изделий: "))
    dict_base["ед."] = input("Введите единицу измерения изделия: ")
    structure_row = (i, dict_base)
    database_structure.append(structure_row)
    i += 1
for i in database_structure:
    print(i)
names = []
prices = []
quantities = []
measurement_items = []
i = 0
while i < number_of_goods:
    dict_tem_1 = database_structure[i]
    dict_temp_2 = dict_tem_1[1]
    names.append(dict_temp_2["название"])
    prices.append(dict_temp_2["цена"])
    quantities.append(dict_temp_2["количество"])
    measurement_items.append(dict_temp_2["ед."])
    i += 1
dict_database = dict_default.copy()
dict_database["название"] = names
dict_database["цена"] = prices
dict_database["количество"] = quantities
dict_database["ед."] = measurement_items
for i in dict_database:
    print(f"{i}: {dict_database.get(i)}")
