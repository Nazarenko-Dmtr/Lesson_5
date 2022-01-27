# LESSON 5 TASK 1 ADD

for i in range (1, 100):
    n = 2
    while n < i:
        if not i % n:
            break
        n += 1
    else:
        print(i, end = "   ")
