
#Which triangle is it ?

while True:

    from math import *
    

    print('''
    Welcome, lets see data please input the edges
    ''')

    a = float(input('Input the first one '))
    b = float(input('Input the second one '))
    c = float(input('Input the third one '))


    if a == b and a == c:

            print('The sides inserted are those of an equilateral triangle')
            

    if a < b and c < b:

        somma_dei_quadrati = pow(( (a*a) + (c*c) ), 0.5)

        if somma_dei_quadrati == b:
    
            print('Il lati inseriti sono quelli di un triangolo rettangolo')

            if a == c:

                print('Il triangolo è anche isoscele')

        else:

            print('The sides entered are those of a right triangle')
    
    elif a < c and b < c:

        somma_dei_quadrati = pow(( (a*a) + (b*b) ), 0.5)

        if somma_dei_quadrati == c:
    
                print('Il lati inseriti sono quelli di un triangolo rettangolo')

                if a == b:

                    print('Il triangolo è anche isoscele')

        else:

            print('I lati inserii non sono quelli di un triangolo rettangolo')

    elif b < a and c < a:
        
        somma_dei_quadrati = pow(( (b*b) + (c*c) ), 0.5)

        if somma_dei_quadrati == a:

            print('Il lati inseriti sono quelli di un triangolo rettangolo')

            if b == c:

                print('Il triangolo è anche isoscele')

        else:

            print('I lati inserii non sono quelli di un triangolo rettangolo')

    print('\nDesideri verificare altri possibili triangoli?')

    loop = input('Digita S/N per continuare/confermare --->')

    if loop == "S":

        continue
    else:
        break

    
   
