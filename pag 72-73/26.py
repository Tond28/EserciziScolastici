'''
Calcola la media degli stipendi dei dipendenti di un'azienda, 
acquisiti con una ripetizione fino a quando si inserisce -1 
per segnalare la fine dell'input dei dati
'''
stipendio_totale=0
counter=0
while True:
    try:
        stipendio=float(input("Inserire il valore dello stipendio   "))
    except ValueError:
        pass
        print("\nErrore\n")
    if stipendio==-1:
        break
    else:
        stipendio_totale+=stipendio
        counter+=1
print("La media degli stipendi è", stipendio_totale/counter, "€")
    
    