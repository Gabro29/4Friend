
#String reverser

string=input("Type any string ")
Len=int(len(string)-1)
reverse=""

for char in range(Len, -1,-1):
    reverse+=string[char]
print(f"The reverse string is {reverse}")
