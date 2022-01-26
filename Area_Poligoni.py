
#Calcola l'area di alcune figure geometriche

from math import *

poligoni={'cerchio': None, 'quadrato': None, 'triangolo': None, 'rettangolo': None}


print(f"Ciao sono in grado di calcolare l'area di una delle seguenti figure geometriche {list(poligoni.keys())}")
scelta=input(f"Digita il nome del poligono di cui vuoi calcolare l'area ")


if scelta == "cerchio":

    poligoni["cerchio"]=float(input(f"Inserisci il raggio "))
    print(f"L'area è {pow(poligoni.get(scelta), 2)*pi}")
elif scelta == "quadrato":

    poligoni["quadrato"]=float(input(f"Inserisci il lato "))
    print(f"L'area è {pow(poligoni.get(scelta), 2)}")
elif scelta == "triangolo":
    
    poligoni["triangolo"]=float(input(f"Inserisci la base "))
    poligoni["triangolo"]*=float(input(f"Inserisci l'altezza "))
    print(f"L'area è {poligoni.get(scelta)/2}")
elif scelta == "rettangolo":
    
    poligoni["rettangolo"]=float(input(f"Inserisci la base "))
    poligoni["rettangolo"]*=float(input(f"Inserisci l'altezza "))
    print(f"L'area è {poligoni.get(scelta)}")


