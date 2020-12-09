from tkinter import *
from tkinter import ttk
giorni=0
veicoli_tot=0

#RIMOSSO CHE CON 0 SI FERMA IL PROGRAMMA IN QUANTO POCO UTILE IN QUESTO METODO GRAFICO

def transito_def(*args):
    global giorni, veicoli_tot
    giorni+=1
    try:
        veicoli1=int(vlc.get())
    except ValueError:
        risultato.set("ERRORE")
        pass
        vlc.set("")
    veicoli_tot+=veicoli1
    veicoli_totale=veicoli_tot
    veicoli_media=int(veicoli_tot/giorni)
    risultato.set(veicoli_totale)
    risultato2.set(veicoli_media)
    vlc.set("")


def reset(*args):
    global giorni, veicoli_tot                                                         
    clear = ""
    vlc.set(clear)
    risultato.set(clear)
    risultato2.set(clear)
    giorni=0
    veicoli_tot=0


root=Tk()
root.title("Es. 27")
root.geometry("650x296")


vlc=StringVar()

risultato=StringVar()
risultato2=StringVar()


stipendio_entry=Entry(root, width=10, textvariable=vlc, font=('verdana', 30))
stipendio_entry.place(height=60, x=5, y=90)

Label(root, text="Es. 27", font=('verdana', 20)).place(height=30, x=210, y=5)
Label(root, text="Numero veicoli giornalieri:", font=('verdana', 15)).place(height=30, x=5, y=60)
Label(root, text="Veicoli transitati totali:", font=('verdana', 15)).place(height=30, x=5, y=160)
Label(root, textvariable=risultato, font=('verdana', 15), fg="red").place(height=30, x=245, y=160)
Label(root, text="Media veicoli transitati giornalmente:", font=('verdana', 15)).place(height=30, x=5, y=200)
Label(root, textvariable=risultato2, font=('verdana', 15), fg="red").place(height=30, x=388, y=200)


Button(root, text="CALCOLA RISULTATI", command=transito_def, font=('verdana', 15)).place(height=25, x=5, y=270)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=550, y=270)


root.bind('<Return>', transito_def)

root.bind('<Return>', reset)


root.mainloop()