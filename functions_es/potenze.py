#calcolare una potenza
def potenza(base, esponente):
    return base**esponente

while True:
    try:
        base=float(input("Inserire il valore della base "))
        esponente=float(input("Inserire il valore dell'esponente "))
    except ValueError:
        print("INSERIRE DEI VALORI VALIDI")
        continue
    break
print(potenza(base, esponente))