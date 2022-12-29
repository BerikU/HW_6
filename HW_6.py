# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
from tokenize import group
# from random import sample
# len_list = int(input("Insert the size of the list: "))
# my_list = [i for i in sample(range(1, len_list*2), len_list)]
# print("Randomized list: ", my_list)
# sort_list = [my_list[i]
#              for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
# print("Sorted list: ", sort_list)

# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

# n = int(input("Insert a number above 20: "))
# if n < 20:
#     raise ValueError("Incorrect number was entered")
#
# items_range = range(20, n + 1)
# source_list = list(items_range)
# print(f"Primary {source_list}")
#
# filtered_list = list(filter(lambda x: x % 20 == 0 or x % 21 == 0, source_list))
# print(f"Filtered {filtered_list}")

# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

# from itertools import groupby
#
#
# def dictionary(*args):
#     if "" not in args:
#         return {k: list(names) for k, names in groupby(sorted(args), key=lambda i: i[0]) if k}
#     return "Error"
#
#
# print(dictionary("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))
