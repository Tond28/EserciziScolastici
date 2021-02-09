#Con riferimento al dizionario del problema precedente, 
#elenca i numeri di matricola degli studenti che hanno ottenuto 
#una valutazione superiore alla media di tutte le valutazioni.

studenti_voti={}
NUMERO_STUDENTI=30
somma=0
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
    somma+=voto
    studenti_voti[studente]=voto

media=somma/NUMERO_STUDENTI

for studenti in studenti_voti:
    if studenti_voti[studenti]>media:
        print(studenti, "ha superato la media di voti della classe")
