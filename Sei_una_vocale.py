
#Capisce se il carattere inserito è una vocale 

print(f"Richiamare la funzione vocale e scrivere tra virgolette il carattere")

def vocale(lettera):
    vocali = ["a", "e", "i", "o" ,"u", "A", "E", "I", "O", "O", "U"]
    count=0

    for i in vocali:
        if i == lettera:
            print(f"Il carattere inserito è una vocale")
            
        elif count > 4 and i != lettera:
            print(f"Il carattere inserito non è una vocale")
            count +=1
