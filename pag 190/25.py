

studenti_voti={}
voti_classe=[]
NUMERO_STUDENTI=5
for i in range(NUMERO_STUDENTI):
    print("Inserire la matricola dello studente numero", i+1)
    studente=input()
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
