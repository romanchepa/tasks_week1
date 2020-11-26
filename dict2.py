"""1.Проверьте, есть ли в словаре ключ country"""

dict={"city": "Москва", "temperature": 20}

print(dict.get('country'))



"""2.Выведите значение по-умолчанию "Россия" для ключа country"""

print(dict.get('country', "Россия"))



"""3.Добавьте в словарь элемент date со значением "27.05.2019" """

dict["date"] = '27.05.2019'
print(len(dict))

