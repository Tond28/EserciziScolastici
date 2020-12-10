from tkinter import *
from tkinter import ttk

def calcoloarea(*args):
 try:
        altezza=float(h.get())
        base=float(b.get())
        risultato.set((base*altezza))


 except ValueError:
     risultato.set("ERRORE")
     pass

def reset(*args):
    clear = ""
    h.set(clear)
    b.set(clear)
    risultato.set(clear)

root=Tk()
root.title("Calcolatrice Area Rettangolo")
root.geometry("350x445")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)

h=StringVar()
b=StringVar()
risultato=StringVar()

b_entry=Entry(root, width=3, textvariable=b, font=('verdana', 50))
b_entry.place(height=100, x=5, y=100)

h_entry=Entry(root, width=3, textvariable=h, font=('verdana', 50))
h_entry.place(height=100, x=5, y=260)

Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=5, y=390)
Label(root, text="Calcolo area rettangolo", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Base:", font=('verdana', 20)).place(height=50, x=5, y=50)
Label(root, text="altezza:", font=('verdana', 20)).place(height=50, x=5, y=210)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=150, y=390)
Button(root, text="CALCOLA", command=calcoloarea, font=('verdana', 15)).place(height=25, x=5, y=420)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=215, y=420)

root.bind('<Return>', calcoloarea)
root.bind('<Return>', reset)

root.mainloop()