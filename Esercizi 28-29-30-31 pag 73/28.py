studenti_nome=[]
studenti_lancio=[]
numero_studenti=int(input("Inserire il numero degli studenti "))
for i in range(numero_studenti):
    nome=input("Inserire il nome dello studente ")
    try:
        lancio=int(input("Inserire il valore del lancio "))
        print("\n")
    except ValueError:
        lancio=0
        print("VALORE IMPOSTATO A ZERO\n")
        pass
    studenti_nome.append(nome)
    studenti_lancio.append(lancio)

risultato=studenti_lancio.index(max(studenti_lancio))
print("Il migliore è", studenti_nome[risultato], "con", studenti_lancio[risultato])