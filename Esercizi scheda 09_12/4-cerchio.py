from tkinter import *
from tkinter import ttk

def calcoloarea(*args):
 try:
        raggio=float(r.get())
        risultato.set((raggio**2)*3.1415926535)


 except ValueError:
        risultato.set("ERRORE")
        pass

def reset(*args):
    clear = ""
    r.set(clear)
    risultato.set(clear)

root=Tk()
root.title("Calcolatrice Area cerchio")
root.geometry("350x280")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)

r=StringVar()
risultato=StringVar()

l_entry=Entry(root, width=3, textvariable=r, font=('verdana', 50))
l_entry.place(height=100, x=5, y=100)

Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=5, y=220)
Label(root, text="Calcolo area cerchio", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Raggio:", font=('verdana', 20)).place(height=50, x=5, y=50)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=150, y=220)
Button(root, text="CALCOLA", command=calcoloarea, font=('verdana', 15)).place(height=25, x=5, y=250)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=215, y=250)

root.bind('<Return>', calcoloarea)
root.bind('<Return>', reset)

root.mainloop()