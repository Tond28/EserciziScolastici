from tkinter import *
from tkinter import ttk


def voti_def(*args):
    candidati=[]
    candidato1=(cand1.get()).upper()
    candidato2=(cand2.get()).upper()
    candidati.append(candidato1)
    candidati.append(candidato2)

    try:
        voti1=float(vo1.get())
        voti2=float(vo2.get())
    except ValueError:
        num1.set("ERRORE")
        pass
    candidati.sort()
    print(candidati)
    alfa1.set(candidati[0])
    alfa2.set(candidati[1])
    if voti1==voti2:
        num1.set("Pareggio")
    elif voti1>voti2:
        num1.set(candidato1)
        num2.set(candidato2)
    else:
        num1.set(candidato2)
        num2.set(candidato1)



def reset(*args):                                                                           
    clear = ""
    cand1.set(clear)
    cand2.set(clear)
    vo1.set(clear)
    vo2.set(clear)
    alfa1.set(clear)
    alfa2.set(clear)
    num1.set(clear)
    num2.set(clear)


root=Tk()
root.title("Es. 25")
root.geometry("650x400")


cand1=StringVar()
cand2=StringVar()
vo1=StringVar()
vo2=StringVar()
alfa1=StringVar()
alfa2=StringVar()
num1=StringVar()
num2=StringVar()


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
Label(root, text="Es. 25", font=('verdana', 20)).place(height=30, x=210, y=5)

Label(root, text="Ordine Alfabetico:", font=('verdana', 17)).place(height=30, x=10, y=280)
Label(root, textvariable=alfa1, font=('verdana', 17), fg="red").place(height=30, x=50, y=310)
Label(root, text="1)", font=('verdana', 17), fg="red").place(height=30, x=20, y=310)
Label(root, textvariable=alfa2, font=('verdana', 17), fg="red").place(height=30, x=50, y=340)
Label(root, text="2)", font=('verdana', 17), fg="red").place(height=30, x=20, y=340)

Label(root, text="Ordine per voti:", font=('verdana', 17)).place(height=30, x=270, y=280)
Label(root, textvariable=num1, font=('verdana', 17), fg="red").place(height=30, x=310, y=310)
Label(root, text="1)", font=('verdana', 17), fg="red").place(height=30, x=280, y=310)
Label(root, textvariable=num2, font=('verdana', 17), fg="red").place(height=30, x=310, y=340)
Label(root, text="2)", font=('verdana', 17), fg="red").place(height=30, x=280, y=340)

Button(root, text="CALCOLA RISULTATI", command=voti_def, font=('verdana', 15)).place(height=25, x=5, y=370)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=550, y=365)


root.bind('<Return>', voti_def)

root.bind('<Return>', reset)


root.mainloop()