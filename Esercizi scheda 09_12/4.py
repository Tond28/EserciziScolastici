while True:
    scelta=input("Che area vuoi calcolare (scegliere tra triangolo,rettangolo, quadrato, cerchio; schiaccaire invio senza inserire nulla per fermare il programma) ")
    scelta=scelta.upper()
    if scelta=="":
        print("Grazie per aver utilizzato il programma")
        break
    if scelta=="TRIANGOLO":
        while True:
            try:
                base=float(input("Inserire il valore della base "))
                altezza=float(input("Inserire il valore dell'altezza "))
                break
            except ValueError:
                print("Valori inseriti in modo errato")
                pass
        area_triangolo=(base*altezza)/2
        print("L'area del triangolo con base", base, "e altezza", altezza, "è", area_triangolo)
    if scelta=="RETTANGOLO":
        while True:
            try:
                base=float(input("Inserire il valore della base "))
                altezza=float(input("Inserire il valore dell'altezza "))
                break
            except ValueError:
                print("Valori inseriti in modo errato")
                pass
        area_rettangolo=(base*altezza)
        print("L'area del rettangolo con base", base, "e altezza", altezza, "è", area_rettangolo)
    if scelta=="QUADRATO":
        while True:
            try:
                lato=float(input("Inserire il valore del lato "))
                break
            except ValueError:
                print("Valori inseriti in modo errato")
                pass
        area_quadrato=lato**2
        print("L'area del quadrato con lato", "è", area_quadrato)
    if scelta=="CERCHIO":
        while True:
            try:
                raggio=float(input("Inserire il valore del raggio "))
                break
            except ValueError:
                print("Valori inseriti in modo errato")
                pass
        area_cerchio=(raggio**2)*3.1415926535
        print("L'area del cerchio con raggio", raggio, "è", area_cerchio)
    else:
        print("Figura non trovata")


