#Contare i caratteri di una parola

parole=[]
num_lettere=[]
lettere=0
while True:
    parola=input("Inserire la parola (inserire 000 per fermare) ")
    if parola == "000":
        break
    else:
        parole.append(parola)
for par in parole:
    lettere=len(par)
    
    num_lettere.append(lettere)
    lettere=0 
for i in range(len(parole)):
    print(parole[i-1], "è di", num_lettere[i-1], "lettere")
   