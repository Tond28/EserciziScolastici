#I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario 
#che ha per chiave la matricola, mentre il valore associato è il voto. 
#Elenca i risultati in ordine crescente di voto 
#e successivamente visualizza quali voti diversi tra loro sono stati assegnati, riducendo a uno i voti uguali.

studenti_voti={}
voti_classe=[]
NUMERO_STUDENTI=30
for i in range(NUMERO_STUDENTI):
    print("Inserire la matricola dello studente numero", i+1)
    studente=input()
    studente=studente.capitalize()
    while True:
        try:
            print("Inserire il voto di", studente)
            voto=float(input())
            break
        except ValueError:
            print("INSERIRE UN VALORE VALIDO\n\n")
            continue
    studenti_voti[studente]=voto

elenco_crescente=(sorted(studenti_voti.items(), key=lambda voto:voto[1]))
#Viene creata una lista con valori delle tuple contenenti (studente, voto)
#Viene messo il parametro opzionale key perchè devono essere ordinati i values (valore 1 della tupla)
#e non le chiavi (valore 0 della tupla)


for v in elenco_crescente:
    voto_studente=v[1]
    if not voto_studente in voti_classe:
        voti_classe.append(voto_studente)

for studenti in elenco_crescente:
    print(studenti[0], "ha preso", studenti[1])

print("\n\nIn classe ci sono stati i seguenti voti")
for e in voti_classe:
    print(e, end="| ")
