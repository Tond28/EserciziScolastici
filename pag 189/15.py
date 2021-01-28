#Dato un elenco di nazioni con le rispettive capitali, 
#Inserito il nome di una nazione restituire la capitale
#Se non è presente la nazione dare un messaggio di errori
#Utilizzare 2 liste

nazioni=["Italia", "Spagna", "Germania", "Regno unito", "Portogallo"]
capitali=["Roma", "Madrid", "Berlino", "Londra", "Lisbona"]

while True:
    nazione=input("Inserire una nazione (inserire aaa per fermare il programma) \n")
    nazione=nazione.capitalize()
    if nazione=="Aaa":
        break
    elif nazione in nazioni:
        print("La capitale di", nazione, "è", capitali[nazioni.index(nazione)])
    else:
        #print("Nazione non presente")


        #aggiunta
        print("Inserire la capitale di", nazione)
        capitale=input()
        capitale=capitale.capitalize()
        nazioni.append(nazione)
        capitali.append(capitale)
        print("Nazione e Capitale aggiunta correttamente")
        