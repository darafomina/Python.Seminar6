# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a=int(input("Введите цифру, обозначающую день недели: "))
if 6 <= a <= 7:
    print("Выходной")
elif 0 < a < 6:
    print("Будний")
else:
    print("Число вне пределов 7 дней")