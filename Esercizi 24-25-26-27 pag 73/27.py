veicoli_tot=0
giorni=0
while True:
    try:
        veicoli=int(input("Inserire il numero di veicoli transitati al giorno   "))
    except ValueError:
        pass
    if veicoli==0:
        break
    else:
        veicoli_tot+=veicoli
        giorni+=1
print("Il numero totale di veicoli transitati in", giorni, "giorni, è:", veicoli_tot)
