list1 = [8] * 3
list2 = [8] * 3

print(id(list1))
print(id(list2))

list2 = list1

print(id(list1))
print(id(list2))