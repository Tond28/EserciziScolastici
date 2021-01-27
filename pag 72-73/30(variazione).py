'''
Fornisci la rappresentazione in decimale di un numero binario
'''

valore_dec=0
contatore=0
numero_bin=input("Inserire il numero binario ")
numero_bin=numero_bin[::-1]
for i in numero_bin:
    if i=="1":
        valore_dec+=(2**contatore)
    else:
        pass
    contatore+=1
print("Il valore decimale di", numero_bin, "è:", valore_dec)