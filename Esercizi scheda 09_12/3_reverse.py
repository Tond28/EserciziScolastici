CARATTERI="aeiou:,;.!?òàùèì "
while True:
    parola_it=""
    controllo=0
    parola=input("Inserire la parola criptata (non inserire niente per fermare il programma) ")
    if parola=="":
        print("Grazie per aver utilizzato il programma")
        break
    else:
        for l in parola:
            if controllo==0:
                if not l in CARATTERI:
                    parola_it=parola_it+l
                    controllo=2
                else:
                    parola_it=parola_it+l
            else:
                controllo-=1
        print(parola_it)
