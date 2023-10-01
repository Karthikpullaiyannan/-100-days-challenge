string_1=input("Enter the string:")
string_1=string_1.lower()
string_2=reversed(string_1)
if(list(string_1)==list(string_2)):
    print("The given string is palindrome")
else:
    print("The string is not palindrome")