CARATTERI="aeiou:,;.!?òàùèì "
while True:
    parola_it=""
    parola=input("Inserire la parola in italiano (non inserire niente per fermare il programma) ")
    if parola=="":
        print("Grazie per aver utilizzato il programma")
        break
    else:
        for l in parola:
            if not l in CARATTERI:
                parola_it=parola_it+l+"o"+l

            else:
                parola_it=parola_it+l

        print(parola_it)