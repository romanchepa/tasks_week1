""" 1.Создайте список из чисел 3, 5, 7, 9 и 10.5 """
a = [3,5,7,9,10.5]

"""2.Выведите содержимое списка на экран"""

print(a)

"""3. Добавьте в конец списка строку "Python" """

a.append('Python')
print(a)

"""4.Выведите длину списка на экран"""

print(len(a))

"""Выведите на экран начальный элемент списка"""

print(a[0])

"""Выведите на экран последний элемент списка"""

print(a[5])

""" Напечатайте элементы списка со второго по четвертый включительно"""

print(a[1:4])


"""Удалите из списка строку "Python" """
del a[5]
print(a)