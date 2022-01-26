
#Stampa del più grande tra due numeri

def max(a, b, c):
    if a < b and c < b:
        print(f"Il numero più grande è {b}")
    elif a < c and b < c:
        print(f"Il Numero più grande è {c}")
    else:
        print(f"Il numero più grande è {a}")
