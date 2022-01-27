# LESSON 5 TASK 6 VARIANT 1

from random import randint
list = [randint(1, 100) for i in range(4)]
new_list = [i * 2 for i in list]
list.extend(new_list)
print (list)
