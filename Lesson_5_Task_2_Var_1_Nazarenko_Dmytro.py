# LESSON 5 TASK 2 VARIANT 1

from random import randint
number = randint (5, 16)
x = number
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(x, factorial, sep = ", ")
