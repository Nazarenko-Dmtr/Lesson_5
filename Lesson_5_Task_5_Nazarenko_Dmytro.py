slen = i
# LESSON 5 TASK 5

list = [0,5,2,4,7,1,3,19]
new_list = []
for i in list:
    if i % 2:
        new_list.append(i)
print ("sum of new_list", new_list, sum(new_list), sep = " : ")
