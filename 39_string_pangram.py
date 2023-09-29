string_1="The quick brown fox jumps over the lazy dog"
string_1=string_1.replace(" ","")
string_1=string_1.lower()
alpha="abcdefghijklmnopqrstuvwxyz"
c=0
for i in alpha:
    if i in string_1:
        c=c+1
if(c==len(alpha)):
    print("The give string is a Pangram")
else:
    print("The given string is not a pangram")