'''Подсчитать, сколько было выделено памяти под переменные в ранее разарботанных программах в рамках первых 3 уроков.
Проанализировать результат и определить программы с наиболее эффективнымиспользованием памяти
Проанализируем варианты решения задачи 3_7'''
from collections.abc import Mapping, Sequence, Set
from sys import getsizeof
import random


# постановка задачи
SIZE_M = 100
MIN_ITEM = -100
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)]


# по файлу вцелом. Способ №1
def file_getsizeof(*args, storage=[]):
    file_memory = 0
    for array in args:
        file_memory += array_getsizeof(array, storage)
    return file_memory


def array_getsizeof(data, storage=[]):
    if id(data) in storage:
        return 0
    storage.append(id(data))
    if isinstance(data, str):
        return getsizeof(data)
    elif isinstance(data, Mapping):
        return getsizeof(data) + sum(array_getsizeof(k) + array_getsizeof(v) for k, v in data.items())
    elif isinstance(data, Sequence) or isinstance(data, Set):
        return getsizeof(data) + sum(array_getsizeof(x, storage) for x in data)
    return getsizeof(data)


# по файлу вцелом. Способ №2
def file_getsizeof2(*args, storage=[]):
    file_memory = 0
    for array in args:
        file_memory += array_getsizeof2(array, storage)
    return file_memory


def array_getsizeof2(data, storage=[]):
    if id(data) in storage:
        return 0
    storage.append(id(data))
    if hasattr(data, '__iter__'):
        if hasattr(data, 'items'):
            return getsizeof(data) + sum(array_getsizeof2(k, storage) + array_getsizeof2(v, storage) for k, v in data.items())
        elif isinstance(data, str):
            return getsizeof(data)
        return getsizeof(data) + sum(array_getsizeof2(x, storage) for x in data)
    return getsizeof(data)



def first_way(array):
    first_min = array[0]
    second_min = array[1]
    if first_min > second_min:
        first_min, second_min = second_min, first_min
    for i in range(2, len(array)):
        if array[i] < first_min:
            second_min = first_min  # чтобы не потерять преднаименьшее число
            first_min = array[i]
        elif array[i] < second_min:
            second_min = array[i]
    # print(locals())
    print(f'Общие затраты памяти состваляют (способ 1): {file_getsizeof(locals(), storage=[])}')
    print(f'Общие затраты памяти состваляют (способ 2): {file_getsizeof2(locals(), storage=[])}')
    return f'первое минимальное число = {first_min}, второе минимальное число = {second_min}'

print('Первый вариант:')
print(first_way(array))
print('*'* 100)
# Общие затраты памяти состваляют (способ 1): 3973
# Общие затраты памяти состваляют (способ 2): 3973
# первое минимальное число = -100, второе минимальное число = -100



# 2 способ

def second_way(array):
    first_min = min(array)
    new_massive = array.copy()
    new_massive.pop(new_massive.index(first_min))
    second_min = min(new_massive)
    print(f'Общие затраты памяти состваляют (способ 1): {file_getsizeof(locals(), storage = [])}')
    print(f'Общие затраты памяти состваляют (способ 2): {file_getsizeof2(locals(), storage= [])}')
    return f'первое минимальное число = {first_min}, второе минимальное число = {second_min}'

print('Второй вариант:')
print(second_way(array))
print('*'* 100)
# Общие затраты памяти состваляют (способ 1): 4899
# Общие затраты памяти состваляют (способ 2): 4899
# первое минимальное число = -100, второе минимальное число = -100


# 3 способ

def third_way(array: list):
    first_min = MAX_ITEM
    second_min = MAX_ITEM
    for i in array:
        if i < first_min:
            first_min = i
    for i in range(len(array) - 1):
        if array[i] == first_min:
            spam = array.pop(i)
            break
    for i in array:
        if i == first_min:
            second_min = first_min
            break
        elif i < second_min:
            second_min = i
    print(f'Общие затраты памяти состваляют (способ 1): {file_getsizeof(locals(), storage=[])}')
    print(f'Общие затраты памяти состваляют (способ 2): {file_getsizeof2(locals(), storage=[])}')
    return f'первое минимальное число = {first_min}, второе минимальное число = {second_min}'

print('Третий вариант:')
print(third_way(array))
print('*'* 100)
# Общие затраты памяти состваляют (способ 1): 4054
# Общие затраты памяти состваляют (способ 2): 4054
# первое минимальное число = -100, второе минимальное число = -100

def check_way(array: list):  # использем сортировку для проверки правильности решений
    array.sort()
    print(f'Общие затраты памяти состваляют (способ 1): {file_getsizeof(locals(), storage=[])}')
    print(f'Общие затраты памяти состваляют (способ 2): {file_getsizeof2(locals(), storage=[])}')
    return f'первое минимальное число = {array[0]}, второе минимальное число = {array[1]}'

print('Четвертый вариант:')
print(check_way(array))
# Общие затраты памяти состваляют (способ 1): 3890
# Общие затраты памяти состваляют (способ 2): 3890
# первое минимальное число = -100, второе минимальное число = -100


'''Выводы:
Все способы заняли примерно равное количество памяти, вместе с тем second_way занял на 20-25% больше памяти
за счет копирования исходного массива.
PS так и не смог выяснить почему 1й способ не очищает переменную storage и если выполнять все функции одновременно,
то способ 2, 3 и check выдают неверные результаты, если вызывать функции поочередно то и 1 и 2 работают правильно '''
