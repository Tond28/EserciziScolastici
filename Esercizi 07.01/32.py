'''
Implementa l'algoritmo per il caldolo di un'equazione di primo grado ax + b = 0
'''
while True:
    try:
        numero_a=float(input("Inserire il valore di a "))
        numero_b=float(input("Inserire il valore di b "))
    except ValueError:
        print("INSERIRE VALORI VALIDI")
        continue
    break
if numero_a==0:
    if numero_b==0:
        print("L'equazione è indeterminata")
    else:
        print("L'equazione è impossibile")
elif numero_b==0:
    print("Il risultato è x = 0")
else:
    risulato=(numero_b/numero_a)*-1
    print("Il risultato è x =", risulato)