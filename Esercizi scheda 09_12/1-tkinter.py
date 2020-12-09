from tkinter import *
from tkinter import ttk

def palindromo(*args):
    parola=par.get()
    parola_reverse=parola[::-1]
    if parola==parola_reverse:
        risultato.set("PAROLA PALINDROMA")
    else:
        risultato.set("PAROLA NON PALINDROMA")



def reset(*args):
    clear = ""
    par.set(clear)
    risultato.set(clear)


root=Tk()
root.title("Parola palindroma")
root.geometry("450x235")

par=StringVar()

risultato=StringVar()

parola_entry=Entry(root, width=10, textvariable=par, font=('verdana', 30))
parola_entry.place(height=60, x=5, y=90)

Label(root, text="Parola palindroma", font=('verdana', 20)).pack(anchor=N)
Label(root, text="parola da controllare:", font=('verdana', 15)).place(height=30, x=5, y=60)

Label(root, textvariable=risultato, font=('verdana', 23), fg="red").place(height=30, x=5, y=160)

Button(root, text="CALCOLA PALINDROMO", command=palindromo, font=('verdana', 15)).place(height=25, x=5, y=210)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=360, y=210)

root.bind('<Return>', palindromo)
root.bind('<Return>', reset)

root.mainloop()