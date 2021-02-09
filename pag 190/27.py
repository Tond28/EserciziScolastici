nomi_numeri={
    "Rossi":"3993331234",
    "Pizzeria":"0555123456",
    "Verdi":"3341234567"
}

while True:
    contatto=input("Inserire il nome della persona della quale si vuole cercare (per fermare inserire aaa) ")
    contatto=contatto.capitalize()
    if contatto=="Aaa":
        break
    if contatto in nomi_numeri:
        print("Il numero di", contatto, "è", nomi_numeri[contatto], "\n")
    else:
        print("Contatto non trovato")
        aggiunta=input("Si vuole aggiungere il contatto?(y, n) ")
        if aggiunta=="y":
            print("Inserire il numero di", contatto)
            numero=input()
            nomi_numeri[contatto]=numero
            print("Numero aggiunto correttamente\n\n")
