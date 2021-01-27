'''
Verifica se un numero è pari o disapri
'''
while True:
    try:
        numero=float(input("Inserire un numero "))
    except ValueError:
        print("Valore non valido, inserire un numero")
        continue
    break
if numero % 2 == 0:
    print(numero, "è un numero pari")
else:
    print(numero, "è un numero dispari")