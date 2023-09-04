str_1="rare"
str_2="care"
str_1=str_1.lower()
str_2=str_2.lower()
if(len(str_1)==len(str_2)):
    sorted_str1=sorted(str_1)
    sorted_str2=sorted(str_2)
    if(sorted_str1 == sorted_str2):
        print(str_1 + "and" +  str_2 + "are anagram")
    else:
        print(str_1 +  "and" + str_2 +  "are not Anagaram")
else:
    print(str_1 +  "and" + str_2 +  "are not Anagaram")