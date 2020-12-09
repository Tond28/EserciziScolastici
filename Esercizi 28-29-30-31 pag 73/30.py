lunghezza=int(input("Inserire la lunghezza del numero binario "))
valore_dec=0
valore_bin_int=""
for i in range(lunghezza):
    while True:
        try:
            valore_bin=int(input("Inserire uno dei valori binari partendo dal più piccolo "))
            break
        except ValueError:
            print("Valore errato, riinserire il valore numero", i)
            pass
    if valore_bin==1:
        valore_dec+=(2**i)
    else:
        pass
    valore_bin_int=valore_bin_int+str(valore_bin)
print("Il valore decimale di", valore_bin_int, "è:", valore_dec)