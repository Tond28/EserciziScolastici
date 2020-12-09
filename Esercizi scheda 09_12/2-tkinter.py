from tkinter import *
from tkinter import ttk

def lunghezza_par(*args):
    parola=par.get()
    lun_par=len(parola)
    risultato.set(lun_par)


def reset(*args):
    clear = ""
    par.set(clear)
    risultato.set(clear)


root=Tk()
root.title("Lunghezza parola")
root.geometry("450x235")

par=StringVar()

risultato=StringVar()

parola_entry=Entry(root, width=10, textvariable=par, font=('verdana', 30))
parola_entry.place(height=60, x=5, y=90)

Label(root, text="Lunghezza parola", font=('verdana', 20)).pack(anchor=N)
Label(root, text="parola:", font=('verdana', 15)).place(height=30, x=5, y=60)

Label(root, textvariable=risultato, font=('verdana', 23)).place(height=30, x=202, y=161)
Label(root, text="I caratteri sono: ", font=('verdana', 17)).place(height=35, x=5, y=160)

Button(root, text="CALCOLA LUNGHEZZA PAROLA", command=lunghezza_par, font=('verdana', 15)).place(height=25, x=5, y=210)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=360, y=210)

root.bind('<Return>', lunghezza_par)
root.bind('<Return>', reset)

root.mainloop()