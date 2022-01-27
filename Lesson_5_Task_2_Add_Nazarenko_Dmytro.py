# LESSON 5 TASK 2 ADD (UPPER HALF OF HOURGLASS ONLY:( )

base_length = int (input("Print odd number: "))
indent = - 1
while not base_length % 2:
    print ("Print ODD number!")
    base_length = int (input("Print odd number: "))
while base_length + 1:
    indent += 1
    print (" "*indent + base_length*"*")
    base_length -= 2
