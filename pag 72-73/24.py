'''
Alla fine della giornata di elezioni per il ballottaggio tra due candidati, 
si acquisiscono i voti ottenuti dai due candidati. 
Scrivi il programma che calcoli le percentuali ottenute da ciascun candidato 
e comunichi il nome del vincitore
'''

candidato_1=input("Inserire il nome del primo candidato ")
candidato_2=input("Inserire il nome del secondo candidato ")
while True:
    while True:
        try:
            totale=int(input("Inserire il numero totale dei voti "))
            num_cand_1=int(input("Inserire il numero di voti del primo candidato "))
            num_cand_2=int(input("Inserire il numero di voti del secondo candidato "))
            break
        except ValueError:
            print("\nERRORE\n")
            pass
    #controllo se la somma dei voti dei 2 partecipanti è congruente al numero totale dei voti
    if num_cand_1+num_cand_2==totale:
        perc_cand1=(num_cand_1/totale)*100
        perc_cand2=(num_cand_2/totale)*100
        break
    else:
        print("numero voti errato, rinserire i voti")
if num_cand_1==num_cand_2:
    print("Pareggio")
elif num_cand_1>num_cand_2:
    print("Il vincitore è", candidato_1, "con il", perc_cand1, "%")
else:
    print("Il vincitore è", candidato_2, "con il", perc_cand2, "%")