#  Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from functools import reduce
import random

n = int(input("Введите количество элементов в списке: ")) 
list1 = [random.randint(0, 10) for i in range(n)]
list2 = []
summ =0
print(f"Список чисел: {list1}")
print("На нечётных позициях элементы:")
for index, value in enumerate(list1, start=0):
    if index%2 != 0:
        summ += value
        print(value)
    else:
        continue
print(f'Сумма элементов = {summ}')
exit()




from functools import reduce
import random

n = int(input("Введите количество элементов в списке: ")) 
list1 = [random.randint(0, 10) for i in range(n)]
list2 = []
print(f"Список чисел: {list1}")
print("На нечётных позициях элементы:")
for i in range(len(list1)):
    if i%2!=0:
        list2.append(list1[i])
print(list2)
summa = reduce((lambda x, y: x + y), list2)
print(f'Сумма элементов = {summa}')