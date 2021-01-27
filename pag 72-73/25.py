'''
A un concorso pubblico hanno partecipato due candidati di cui si conoscono 
i nomi e i punteggi conseguiti. 
Visualizza l'elenco dei due candidati prima in ordine alfabetico 
e poi in ordine decrescente di punteggio
'''

candidati=[]
cand1=input("Inseire il nome del primo candidato ")
cand1=cand1.upper()
candidati.append(cand1)
cand2=input("Inserire il nome del secondo candidato ")
cand2=cand2.upper()
candidati.append(cand2)
while True:
    try:
        punteggio1=int(input("Inserire i voti del primo "))
        punteggio2=int(input("Inserire il voti del secondo "))
        break
    except ValueError:
        print("\nERRORE\n")
        pass
candidati.sort()
print("Candidati in ordine alfabetico:", candidati)
if punteggio1==punteggio2:
    print("I candidati in ordine di punti sono: PAREGGIO")
elif punteggio1>punteggio2:
    print("I candidati in ordine di punti sono:", cand1, cand2)
else:
    print("I candidati in ordine di punti sono:", cand2, cand1)