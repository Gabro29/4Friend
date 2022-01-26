
#Calcola il fattoriale

n=int(input(f"\nInserisci il numero di cui vuoi calcolare il fattoriale "))
fatt=1

for i in range(n, 0,-1):

    fatt*=i
    
print(f"Il fattoriale è {fatt}")
