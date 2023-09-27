myset ={"apple","basket","center"}
print(myset)
"""  #unordered
#unchangeable
#duplicates not allowed
myset.add("apple")
print(myset)
myset.add("mango")
print(myset)

#update
list1={"python","java","HTML"}
myset.update("list1")
print(myset)
myset.remove("s")
print(myset)
"""
set1={"one","two","three"}
set2={"four","five","six"}
set3=set1.union(set2)
print(set3)