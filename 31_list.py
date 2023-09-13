#list[start:end:step]
#Access same as string
list_1=["chennai",2,3,4,5,"salem"]
print(list_1[:2])
print(list_1[::2])
list_1.append("erode")
print(list_1)
list_1.append("Karur")
print(list_1)
list_1.insert(3,78)
print(list_1)
list_1.pop(2)
print(list_1)
list_1.remove("salem")
print(list_1)
# print(sorted(list_1))
cities=[1,2,5,3,21,9,8,100,321,0]
print(sorted(cities))