
#Data una stringa restitisce quante volte un carattere si ripete al suo interno

text=input(f"\nInserisci una stringa di caratteri qualsiasi e ti dirò quante volte si ripete ciascuna lettera ")
mydizio={}

for carattere in text:

    vediamo = carattere in mydizio
    
    if vediamo == False:

        mydizio.setdefault(carattere,int(1))

    elif vediamo == True:

        mydizio[carattere]=int(mydizio.get(carattere))+1

print(f"Ecco un quante volte si ripetono i caratteri inseriti {mydizio}")
    
