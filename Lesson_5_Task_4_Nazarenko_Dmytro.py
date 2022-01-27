slen = int(input("Enter the short side length: "))
llen = int(input("Enter the long side length: "))
print(slen*"*", ("\n" + slen*"*"), sep = ("\n" + "*" + (" " * (slen-2)) + "*")*(llen-2))
