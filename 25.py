candidati=[]
cand1=input("Inseire il nome del primo candidato ")
cand1=cand1.upper()
candidati.append(cand1)
cand2=input("Inserire il nome del secondo candidato ")
cand2=cand2.upper()
candidati.append(cand2)
punteggio1=int(input("Inserire i voti del primo "))
punteggio2=int(input("Inserire il voti del secondo "))
candidati.sort
print("Candidati in ordine alfabetico:", candidati)
if punteggio1==punteggio2:
    print(candidati)
elif punteggio1>punteggio2:
    print("I candidati in ordine di punti sono:", cand1, cand2)
else:
    print("I candidati in ordine di punti sono:", cand2, cand1)