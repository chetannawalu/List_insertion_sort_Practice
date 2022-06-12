list1 = [11,1,1,2,2,5,0,3,4,9,8]
list2 = [] # Crete Empty List.
a = len(list1) # Assign length of list1 to variable.
for i in range(a):
    list2.append(min(list1)) # append minimum from list1 to list2.
    list1.remove(min(list1)) # After appending, Remove that item from list1.
# After sorting, list1 is now empty and list2 have all sorted values.
list1=list2 # list2 is now assign to list1 or Print list2 directly.
#print(list2)
print(list1) # print the list1.
