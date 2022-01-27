# LESSON 5 TASK 2 VARIANT 2

from random import randint
number = randint (5, 16)
factorial = 1
for i in range(2, number + 1):
    factorial *= i
print(number, factorial, sep = ", ")

