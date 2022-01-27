# LESSON 5 TASK 6 VARIANT 2

from random import randint
list = [randint(1, 100) for i in range(4)]
new_list = []
for elem in list:
    new_list.append (elem*2)
list.extend(new_list)
print (list)
