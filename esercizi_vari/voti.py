#Si definisca una funzione che preso un dizionario di studenti e voti, 
#restituisca un dizionario con gli studenti suddivisi per intervalli di media di voto: 
#k1(18,23), k2(24,26) e k3(27,30).
#Nel calcolo della media la lode permette di arrotondare all’intero successivo,
#nel caso in cui nella lista dei voti non sia presente una lode l’arrotondamento è per difetto.
import math
studenti={}
divisione_voti={
    (18, 23):"",
    (24, 27):"",
    (28,30):""
}
def media_divisione(dizionario_input, dizionario_output, prima_fascia=[], seconda_fascia=[], terza_fascia=[]):
    for st in dizionario_input:
        voti_studente=dizionario_input[st]
        somma=0
        for v in range(len(voti_studente)-1):
            somma+=voti_studente[v]
        media=somma/(len(voti_studente)-1)
        if voti_studente[len(voti_studente)-1]:
            round(media, 0)
        else:
            media=math.trunc(media)
        
        if media<=23:
            prima_fascia.append(st)
        elif media<=27:
            seconda_fascia.append(st)
        else:
            terza_fascia.append(st)
    dizionario_output[(18,23)]=prima_fascia
    dizionario_output[(24, 27)]=seconda_fascia
    dizionario_output[(28, 30)]=terza_fascia
    return dizionario_output

while True:
    studente=input("Inserire il nome dello studente (inserire stop per fermare l'inserimento degli studenti)\n")
    studente=studente.capitalize()
    voti=[]
    if studente=="Stop":
        break
    else:
        while True:
            try:
                print("Inserire un voto di", studente, "(Inserire 100 per fermare l'inserimento dei voti) ")
                voto=int(input())
            except ValueError:
                print("INSERIRE DEI VALORI VALIDI")
            if voto==100:
                break
            elif voto>=18 and voto<=30:
                voti.append(voto)
            else:
                print("INSERIRE DEI VOTI COMPRESI TRA 18 E 30\n")
        lode=input("Lo studente ha una lode? (y, n) ")
        if lode =="y":
            voti.append(True)
        else:
            voti.append(False)
        studenti[studente]=voti

studenti_divisi=media_divisione(studenti, divisione_voti)
for elements in studenti_divisi:
    print("Gli studenti con voti da", elements[0], "a", elements[1], "sono", ",".join(studenti_divisi[elements]))


