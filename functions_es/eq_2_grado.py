#Calcola un'equazione di secondo grado ax**2+bx+c=0
import math as mt


def eq_grado_uno(b, c):
    if b==0:
        if c==0:
            print("Equazione Indeterminata")
        else:
            print("Equazione Impossibile")
    else:
        print("Il risultato dell'equazione è x=", -c/b)

def delta_calc(a, b, c):
    return (b**2)-(4*a*c)

def eq_grado_due(a, b, c):
    delta=delta_calc(a, b, c)
    if delta<0:
        print("Non esistono soluzione reali")
    else:
        soluzione_1=(-b+mt.sqrt(delta))/(2*a)
        soluzione_2=(-b-mt.sqrt(delta))/(2*a)
        print("La prima soluzione è x=", soluzione_1, "\n"
            "La seconda soluzione è x=",soluzione_2)

print("Questo programma calcola le equazioni di secondo grado ax**2+bx+c=0")
while True:
    try:
        valore_a=float(input("Inserire il valore di a "))
        valore_b=float(input("Inserire il valore di b "))
        valore_c=float(input("Inserire il valore di c "))
    except ValueError:
        print("INSERIRE DEI VALORI VALIDI")
        continue
    break
if valore_a==0:
    eq_grado_uno(valore_b, valore_c)
else:
    eq_grado_due(valore_a, valore_b, valore_c)
