#Dato un elenco di nazioni con le rispettive capitali, 
#Inserito il nome di una nazione restituire la capitale
#Se non è presente la nazione dare un messaggio di errori
#Utilizza una dictionary

nazioni_capitali={
    "Italia":"Roma",
    "Francia":"Parigi",
    "Spagna":"Madrid",
    "Germania":"Berlino",
    "Regno unito":"Londra",
    "Portogallo":"Lisbona"
}

while True:
    nazione=input("Inserire una nazione (inserire aaa per fermare il programma) \n")
    nazione=nazione.capitalize()
    if nazione=="Aaa":
        break
    elif nazione in nazioni_capitali:
        print("La capitale di", nazione, "è", nazioni_capitali[nazione])
    else:
        #print("Nazione non presente")


        #aggiunta
        print("Inserire la capitale di", nazione)
        capitale=input()
        capitale=capitale.capitalize()
        nazioni_capitali[nazione]=capitale
        print("Nazione e Capitale aggiunta correttamente")
    