CARATTERI="aeiou:,;.!?òàùèì "
parola_it=""
parola=input("Inserire la parola in italiano ")
for l in parola:
    if not l in CARATTERI:
        parola_it=parola_it+l+"o"+l

    else:
        parola_it=parola_it+l
parola=""
controllo=0
for l in parola_it:
    if controllo==0:
        if not l in CARATTERI:
            parola=parola+l
            controllo=2
        else:
            parola=parola+l
    else:
        controllo-=1
print(parola)