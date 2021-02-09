studenti_voti={}
NUMERO_STUDENTI=5
somma=0
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
    somma+=voto
    studenti_voti[studente]=voto

media=somma/NUMERO_STUDENTI

for studenti in studenti_voti:
    if studenti_voti[studenti]>media:
        print(studenti, "ha superato la media di voti della classe")
