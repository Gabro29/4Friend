
#Data una lista e un'oggetto capisce se l'oggetto è presente nella lista

def checkitem(lista, item):


##    print(f"\nInserisci una lista di oggetti\n")                #Si può far in modo che la lista venga presa da file
##
##    lista=[]
##
##    print(f"Digitare terminato quando finito\n")
##
##    while True:
##
##            oggetto=input(f"Inserici oggetto ")
##
##            if oggetto == "terminato":
##                break
##            else:
##                lista.append(oggetto)
##
##    item=input(f"\nInserire l'oggetto per vedere se è presente il lista ")

    if item in lista:
        print(f"La stringa inserita è presente nella lista")            #Si far in modo che stampi la posizione dell'oggetto nella lista
    else:
        print(f"La stringa inserita non è nella lista")

print(f"Richiamare la funzione checkitem e inserire come argomenti una lista e poi una parola da ricercare al suo interno\n")
