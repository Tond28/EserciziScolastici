from tkinter import *
from tkinter import ttk


def voti_def(*args):
    candidato1=cand1.get()
    candidato2=cand2.get()
    try:
        voti1=float(vo1.get())
        voti2=float(vo2.get())
    except ValueError:
        risultato.set("ERRORE")
        pass
    perc1=(voti1/(voti1+voti2))*100
    perc2=(voti2/(voti1+voti2))*100
    percentuale1=("%.2f" % perc1)
    percentuale2=("%.2f" % perc2)
    if voti1==voti2:
        risultato.set("Pareggio")
    elif voti1>voti2:
        risultato.set(candidato1)
        risultato2.set(percentuale1)
    else:
        risultato.set(candidato2)
        risultato2.set(percentuale2)



def reset(*args):                                                                           
    clear = ""
    cand1.set(clear)
    cand2.set(clear)
    vo1.set(clear)
    vo2.set(clear)
    risultato.set(clear)
    risultato2.set(clear)


root=Tk()
root.title("Es. 24")
root.geometry("650x400")


cand1=StringVar()
cand2=StringVar()
vo1=StringVar()
vo2=StringVar()
risultato=StringVar()
risultato2=StringVar()


cand1_entry=Entry(root, width=10, textvariable=cand1, font=('verdana', 30))
cand1_entry.place(height=60, x=5, y=90)


cand2_entry=Entry(root, width=10, textvariable=cand2, font=('verdana', 30))
cand2_entry.place(height=60, x=275, y=90)


vo1_entry=Entry(root, width=10, textvariable=vo1, font=('verdana', 30))
vo1_entry.place(height=60, x=5, y=210)


vo2_entry=Entry(root, width=10, textvariable=vo2, font=('verdana', 30))
vo2_entry.place(height=60, x=275, y=210)


Label(root, text="Nome primo candidato:", font=('verdana', 15)).place(height=30, x=5, y=60)
Label(root, text="Nome secondo candidato:", font=('verdana', 15)).place(height=30, x=270, y=60)

Label(root, text="Voti primo candidato:", font=('verdana', 15)).place(height=30, x=5, y=180)
Label(root, text="Voti secondo candidato:", font=('verdana', 15)).place(height=30, x=275, y=180)
Label(root, text="Es. 24", font=('verdana', 20)).place(height=30, x=210, y=5)

Label(root, text="Il vincitore è:", font=('verdana', 17)).place(height=30, x=30, y=300)
Label(root, textvariable=risultato, font=('verdana', 17), fg="red").place(height=30, x=190, y=300)
Label(root, text="Con il", font=('verdana', 17)).place(height=30, x=30, y=330)
Label(root, textvariable=risultato2, font=('verdana', 17), fg="red").place(height=30, x=100, y=330)
Label(root, text="%", font=('verdana', 17), fg="red").place(height=30, x=180, y=330)

Button(root, text="CALCOLA RISULTATI", command=voti_def, font=('verdana', 15)).place(height=25, x=5, y=370)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=550, y=365)


root.bind('<Return>', voti_def)

root.bind('<Return>', reset)


root.mainloop()