from tkinter import *
from tkinter import ttk
stipendi=0
stipendio_tot=0.0

#RIMOSSO CHE CON -1 SI FERMA IL PROGRAMMA IN QUANTO POCO UTILE IN QUESTO METODO GRAFICO

def stipendi_def(*args):
    global stipendi, stipendio_tot
    stipendi+=1
    try:
        stipendio1=float(stp.get())
    except ValueError:
        risultato.set("ERRORE")
        stp.set("")
        pass
    stipendio_tot+=stipendio1
    stipendio_media=(stipendio_tot/stipendi)
    stipendio_totale=("%.2f" % stipendio_tot)
    stipendio_media=("%.2f" % stipendio_media)
    risultato.set(stipendio_totale)
    risultato2.set(stipendio_media)
    stp.set("")


def reset(*args):
    global stipendi, stipendio_tot                                                         
    clear = ""
    stp.set(clear)
    risultato.set(clear)
    risultato2.set(clear)
    stipendi=0
    stipendio_tot=0


root=Tk()
root.title("Es. 26")
root.geometry("650x296")


stp=StringVar()

risultato=StringVar()
risultato2=StringVar()


stipendio_entry=Entry(root, width=10, textvariable=stp, font=('verdana', 30))
stipendio_entry.place(height=60, x=5, y=90)

Label(root, text="Es. 26", font=('verdana', 20)).place(height=30, x=210, y=5)
Label(root, text="Stipendio in €:", font=('verdana', 15)).place(height=30, x=5, y=60)
Label(root, text="Stipendio totate in €:", font=('verdana', 15)).place(height=30, x=5, y=160)
Label(root, textvariable=risultato, font=('verdana', 15), fg="red").place(height=30, x=255, y=160)
Label(root, text="Media stipendio in €:", font=('verdana', 15)).place(height=30, x=5, y=200)
Label(root, textvariable=risultato2, font=('verdana', 15), fg="red").place(height=30, x=255, y=200)


Button(root, text="CALCOLA RISULTATI", command=stipendi_def, font=('verdana', 15)).place(height=25, x=5, y=270)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=550, y=270)


root.bind('<Return>', stipendi_def)

root.bind('<Return>', reset)


root.mainloop()