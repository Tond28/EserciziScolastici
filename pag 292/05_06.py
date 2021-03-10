# Elenca proprietà e metodi della classe Prodotto
# Definisci il metodo assegna_prezzo della classe prodotto

class Prodotto:
    def __init__(self, name, type_, deadline="Nessuna scadenza", price=0, notes="/"):
        self.name=name
        self.type_=type_
        self.deadline=deadline
        self.price=price
        self.notes=notes
    
    def assegna_prezzo(self, price):
        self.price=price
    def get_info(self):
        print("Descrizione prodotto\nNome: {}\nTipologia: {}\nPrezzo: {}€\nScadenza: {}\nNote particolari: {}".format(self.name, self.type_, self.price, self.deadline, self.notes))


p1=Prodotto("Mela", "Frutta", "20/03/2021")
p1.assegna_prezzo(3)
p1.get_info()

p2=Prodotto("Notebook", "pc", price=1300, notes="i7-9780u")
p2.get_info()