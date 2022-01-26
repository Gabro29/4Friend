
#Ogni quanto capita la stessa password

import random

caratteri=open("Caratteri_ascii.txt", "r").readlines()      #E' possibile aggiungere eventuali caratteri modificando il file
password=""
temp=""
alfanum=""
a=0
n=0

print(f"\nGenero una password e vedo dopo quanti cicli si ripete\n")

#for i in range(22,84):                                      #Commentando eventuali linee ed aggiustando le variabili
                                                            #si può generare una password di m caratteri ASCII o alfanumerici
    #alfanum+=caratteri[0][i]
        
while True:
    
    if n == 0:
        
        for i in range(0,3):

            #password+=random.choice(alfanum)
            a=random.randrange(93)
            password+=caratteri[0][a]
            
        temp=password
        n+=1
        
    else:
        
        password=""
        n+=1
         
        for i in range(0,3):

            a=random.randrange(93)
            password+=caratteri[0][a]
            #password+=random.choice(alfanum)

        if temp == password:

            print(f"Ho ottenuto due password uguali dopo {n} cicli, le password sono {temp} e {password}")

        elif n%10000 == 0:

            print(f"Ciclo {n}")
             
        else:
            continue
