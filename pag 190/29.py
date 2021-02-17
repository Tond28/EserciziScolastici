#Scrivi un programma che legga un reddito da tastiera e calcoli l'importo dell'imposta sul reddito e sull'imposta media
#Utilizza un dizionario

percentuale_tasse={
    15000:(15000, 23),
    28000:(13000, 27),
    55000:(27000 ,38),
    75000:(20000, 41),
    1000000000000:(0, 43)
}
tasse=0
while True:
    try:
        reddito=int(input("Inserire il reddito "))
        break
    except ValueError:
        print("INSERIRE UN VALORE VALIDO")
        continue

reddito_rid=reddito
for valore in percentuale_tasse:
    if reddito_rid>=valore:
        reddito_rid-=percentuale_tasse[valore][0]
        tasse+=(percentuale_tasse[valore][0]*percentuale_tasse[valore][1])/100
    else:
        tasse+=(reddito_rid*percentuale_tasse[valore][1])/100
        break
tasse=round(tasse, 2)
imp_media=round(tasse/reddito*100, 2)
print("Le tasse imposte sono {}\nCioè il {}% del reddito({})".format(tasse, imp_media, reddito))