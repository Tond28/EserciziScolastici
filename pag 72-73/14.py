'''
Cra un programma che scriva la differenza di due numeri a e b se il loro prodotto è maggiore a 10
Oppure la loro somma se il loro prodotto è minore o uguale a 10
'''
while True:
    try:
        numero_a=float(input("Inserire il primo numero "))
        numero_b=float(input("Inserire il secondo numero "))
    except ValueError:
        print("Inserire valori validi")
        continue
    break
if numero_a*numero_b>10:
    risulato=numero_a-numero_b
    print("La differenza tra", numero_a, "e", numero_b, "è", risulato)
else:
    risulato=numero_a+numero_b
    print("La somma tra", numero_a, "e", numero_b, "è", risulato)