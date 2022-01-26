
#He writes the Fibonacci series

print(f"\nWrites the Fibonacci series within a specific threshold\n")

limit=int(input(f"Enter the threshold "))
l=1
n=1
fibncc=""

while n <= limit:

    if fibncc == "":
        
        fibncc+=str(l)
        
    else:

        fibncc+=", "+str(n)
        n=n+l
        l=n-l
        
print(f"\nHere it is ----> {fibncc}\n")
