#Un'azienda vende prodotti in tutta Italia, e la rete di vendità è suddivisa in Nord, Centro, Sud, Isole. Dopo aver acquisito in un array il fatturato
#della quattro zone, calola: il totale del fatturato, i valori eprcentuali delle vendite nelle quattro zone rispetto al totale

zone={
    "nord":0,
    "centro":0,
    "sud":0,
    "isole":0 
}
totale=0

for z in zone:
    while True:
        try:
            print("Inserire fatturato del", z)
            fatturato=int(input())
            break
        except ValueError:
            print("INSERIRE UN VALORE VALIDO")
            continue
    totale+=fatturato
    zone[z]=fatturato

print("Il totale del fatturato è", totale)

for e in zone:
    percentuale=round((zone[e]/totale)*100, 2)
    print("Il fatturato del {} è il {}% del totale ".format(e, percentuale))
    
    