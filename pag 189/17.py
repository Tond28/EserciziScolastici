#Costruisci un dizionario ottenuto da quello dell'esercizio precedente (16) invertendo il ruolo di chiave e valore.
#Usa il nuovo dizionario per trovare il nome della nazione, noto il nome della capitale

nazioni_capitali={
    "Italia":"Roma",
    "Francia":"Parigi",
    "Spagna":"Madrid",
    "Germania":"Berlino",
    "Regno unito":"Londra",
    "Portogallo":"Lisbona"
}
capitali_nazioni={capitali: nazioni for nazioni, capitali in nazioni_capitali.items()}
while True:
    capitale=input("Inserire una capitale (inserire aaa per fermare il programma) \n")
    capitale=capitale.capitalize()
    if capitale=="Aaa":
        break
    elif capitale in capitali_nazioni:
        print(capitale, "è in", capitali_nazioni[capitale])
    else:
        #print("Nazione non presente")


        #aggiunta
        print("Inserire la nazione di", capitale)
        nazione=input()
        nazione=nazione.capitalize()
        capitali_nazioni[capitale]=nazione
        print("Nazione e Capitale aggiunta correttamente")
