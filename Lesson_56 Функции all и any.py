# Функция all() принимает на вход коллекцию, преобразует каждый элемент в исниту / ложь согласно стандартной логике
# и выдает True, если ВСЕ элементы равны истине

a = ['hello', 'hi', 'world']
print(all(a))  # --> True

a = ['hello', '', 'world']
print(all(a))  # --> False

# Функция all() принимает на вход коллекцию, преобразует каждый элемент в исниту / ложь согласно стандартной логике
# и выдает True, если ХОТЯ БЫ ОДИН элемент равен истине

a = ['hello', '', 'world']
print(any(a))  # --> True

a = ['hello', '', '']
print(any(a))  # --> True

a = ['', '', '']
print(any(a))  # --> False


''' Полезно использовать при проверке множества условий, но их описание должно быть списком, 
кортежем, иначе функция не примет в работу'''

a = 100
condition_1 = a%2 == 0
condition_2 = a > 50
condition_3 = a < 100

print(any([condition_1, condition_2, condition_3]))  # --> True список
print(all((condition_1, condition_2, condition_3)))  # --> True кортеж

a = 100
condition_1 = a%2 == 0
condition_2 = a > 50
condition_3 = a < 99

print(any([condition_1, condition_2, condition_3]))  # --> True список
print(all((condition_1, condition_2, condition_3)))  # --> False кортеж