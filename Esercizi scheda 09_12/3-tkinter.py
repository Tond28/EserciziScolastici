from tkinter import *
from tkinter import ttk

def traduzione(*args):
    parola_it=""
    parola=par.get()
    for l in parola:
        if not l in "aeiou:,;.!?òàùèì ":
            parola_it=parola_it+l+"o"+l
        elif l in "aeiou:,;.!?òàùèì ":
            parola_it=parola_it+l
    risultato.set(parola_it)


def reset(*args):
    clear = ""
    par.set(clear)
    risultato.set(clear)


root=Tk()
root.title("Linguaggio dei furfanti")
root.geometry("550x235")

par=StringVar()

risultato=StringVar()

parola_entry=Entry(root, width=20, textvariable=par, font=('verdana', 30))
parola_entry.place(height=60, x=5, y=90)

Label(root, text="Linguaggio dei furfanti", font=('verdana', 20)).pack(anchor=N)
Label(root, text="parola in italiano:", font=('verdana', 15)).place(height=30, x=5, y=60)

Label(root, textvariable=risultato, font=('verdana', 20)).place(height=35, x=160, y=161)
Label(root, text="Traduzione: ", font=('verdana', 17)).place(height=35, x=5, y=160)

Button(root, text="TRADUCI", command=traduzione, font=('verdana', 15)).place(height=25, x=5, y=210)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=360, y=210)

root.bind('<Return>', traduzione)
root.bind('<Return>', reset)

root.mainloop()