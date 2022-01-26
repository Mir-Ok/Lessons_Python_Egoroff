''' Вызываемый объект это тот, к которому можно применить оператор вызова ().
 К переменным, например, нельзя.  А к чему можно? Проверяем через оператор callable()
 1. Встроенные функции len(), abs(), int() ...
 2. Встроенные методы объектов
 3. Самописные функции '
 4. Класс
 5. Объекты класса (настраиваемо)
 6. Методы класса
 7. Функции - генераторы  '''

a = 10
# print(a())  # --> 'int' object is not callable нельзя к строке применить оператор вызова
print(callable(a))  # -->   False

# 1. Встроенные функции ----------
print(callable(len))  # -->   True
print(callable(int))  # -->   True

# 2. Встроенные методы ----------

b = [1, 2, 3, 1]
print(callable(b.sort))  # -->   True вызываем вместе с переменной без скобок

# 3. Самописные функции ----------

def f():
    print('hello world')
print(callable(f))  # -->   True

# 4. Классы ----------

class Cat:
    pass
bob = Cat()
print(bob)  # --> <__main__.Cat object at 0x00000234D5D17640> экземпляр класса изначально не вызываемый
print(callable(Cat))  # -->   True
print(callable(bob))  # -->   False

# 5. Объект класса (настраиваемо) ----------

class Cat:
    def __call__(self, *args, **kwargs):
        print('may')

bob = Cat()
print(bob)  # --> <__main__.Cat object at 0x00000234D5D17640> экземпляр класса изначально не вызываемый
print(callable(Cat))  # -->   True
print(callable(bob))  # -->   True


# 6. Методы класса ----------

class Cat:
    def __call__(self, *args, **kwargs):
        print('may')

    def say_hello(self):
        print('hello')

bob = Cat()
print(callable(Cat))  # -->   True
print(callable(bob))  # -->   True
print(callable(bob.say_hello))  # -->   True

# 7. Функции - генераторы ----------

def g():
    n = 0
    while True:
        yield n
        n +=1

print(callable(g)) # -->   True


