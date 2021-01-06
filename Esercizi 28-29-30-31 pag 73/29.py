'''
Dato un elenco di città, con specificato nome, temperatura massima e temperatura minima di ognuna
Trovare il numero di città che superato il valore dell'escursione termica inserita dall'utente
'''

città=[]
temp_max=[]
temp_min=[]
contatore=0
città_fin=[]
while True:
    citta_sing=input("Inserire il nome della città (Inserire aaa per fermare l'inserimento delle città) ")
    if citta_sing=="aaa":
        break
    else:
        while True:
            try:
                print("Inserire la temperatura massima a", citta_sing)
                temp_max_sing=int(input())
                print("Inserire la temperatura minima a", citta_sing)
                temp_min_sing=int(input())
                break
            except ValueError:
                print("VALORI ERRATI")
        città.append(citta_sing)
        temp_max.append(temp_max_sing)
        temp_min.append(temp_min_sing)

escursione_termica=int(input("Inserire valore escursione termica minima richiesta "))
for i in range(len(città)):
    if temp_max[i]-temp_min[i]>escursione_termica:
        contatore+=1
        città_fin.append(città[i])
print("Le città con escursione termica maggiore di", escursione_termica, "sono", contatore, "e sono queste città\n", città_fin)

