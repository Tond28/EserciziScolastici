stipendiototale=0
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
        stipendiototale+=stipendio
        counter+=1
print("La media degli stipendi è", stipendiototale/counter, "€")
    
    