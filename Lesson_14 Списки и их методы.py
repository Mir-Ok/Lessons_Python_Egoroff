# Вызов контекстной подсказки - после точки . нажимаем CTRL + пробел

a = [12, 43, 54, 65, 76, 3]

a.append(46)
print(a) # ----- [12, 43, 54, 65, 76, 3, 46] добавление одного элемента в конец списка

# Списки, в отличии от строк, изменяемы, поэтому обработка методами МЕНЯЕТ исходник, никакого
# дполонительного переприсвоения не нужно! Наоборот, переприсвоение опустошает список
a = a.append(48)
print(a) # ----- None

a = [12, 43, 54, 65, 76, 3]

a.clear() # ---- очищает список полностью
a = [12, 43, 54, 65, 76, 3]

a.copy() # --------- [12, 43, 54, 65, 76, 3] делает копию списка, аналогично a[:]

a.count(12) # ------ 1 считает, сколько раз аргумент встретился в списке? если ни разу, то выдаст 0

a.index(12) # ------ 0 ищет в списке указанное в аргументе значение и возвращает  индекс встреченного в первый раз,
            # ------ можно указать интервал для поиска

a.insert(2, 100) # - [12, 43, 100, 54, 65, 76, 3] на позицию с индексом 2 встало указаное число, остальные сдвигаются
                 # вправо, только по одному элементу. Похож на append, но есть возможность указать позицию

a.pop() # ---------- 3, вернет нам последнее значение в списке, убрав его из списка, теперь a == [12, 43, 100, 54, 65, 76]
a.pop(3) # --------- 54, вернет нам значение с указанным индексом, убрав его из списка, теперь a == [12, 43, 100, 65, 76]

a.remove(100) # ---- удаляет по значению (первое найденное, если их много), а не по индексу. Убрать много - циклом while
              # ---- Если попробуем удалить то, чего нет - сбой программы

a.reverse() # ------ [47, 65, 100, 43, 12], а было [12, 43, 100, 65, 76]. Метод развернул задом наперед

a.sorted() # ------- по умолчанию сортирует по возрастанию
a.sorted(reverse=True) # ------- сортирует по убыванию