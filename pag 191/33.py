# in un laboratorio di analisi i pazienti sono sottoposti ad esame
# secondo l'ordine di arrivo (usa una struttura di coda per memorizzare i nomi):
# scrivi il programma che registri i nomi dei pazienti man mano che arrivano.
# visualizza poi il primo paziente che deve essere sottoposto all'esame.

pazienti=[]
while True:
    paziente=input("Inserire il nome del paziente (inserire stop per fermare il programma) ")
    paziente=paziente.capitalize()
    if paziente=="Stop":
        break
    else: 
        pazienti.append(paziente)
primo=pazienti.pop(0)
print("Il primo paziente è", primo)
#Aggiunta
while len(pazienti)>0:
    input("Premere invio per il prossimo paziente ")
    paziente=pazienti.pop(0)
    print("il prossimo è", paziente)