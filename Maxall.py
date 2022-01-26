
#Data una lista di interi stampa il più grande dei numeri inseriti

print(f"Inserisci una lista di interi e ti  dirò il più grande che hai inserito\n")

numeri=[]

print(f"Digitare una lettera qualsiasi quando finito\n")

while True:                                 #Riempio la lista

    try:
        
        numero=int(input(f"Inserisci un numero "))
        numeri.append(numero)
          
    except ValueError:

        break

numeri.sort()

print(f"Il più grande dei numeri inseriti è {numeri[-1]}\n")
print(f"{numeri}")
