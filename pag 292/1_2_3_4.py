#Crea una classe Atleta per rappresentare le informazioni su un giocatore. 
#La classe devve contenere un attributo booleano chiamato visita_medica
#Deve contenere un metodo per assegnare all'altleta il nome della suqadra dove gioca
#Aggiungi alla classe Atleta un metodo chiamato effettua_visita che ponga l'attributo visita_medica uguale a True
#Aggiungi alla classe un metodo per visuallizare i dati del giocatore

class Atleta:
    def __init__(self, nome, cognome, anni, squadra="non pervenuto", visita_medica=False):
        self.nome=nome
        self.cognome=cognome
        self.anni=anni
        self.squadra=squadra
        self.visita_medica=visita_medica

    def informazioni(self):
        print("Nome: {}\nCognome: {}\nEtà: {}\nSquadra: {}\nDeve effettuare una visita medica: {}\
        ".format(self.nome, self.cognome, self.anni, self.squadra, self.visita_medica))

    def add_squadra(self, nome_squadra):
        self.squadra=nome_squadra

    def effettua_visita(self):
        self.visita_medica=True

a1=Atleta("Paolo", "Verdi", 17)
a1.informazioni()
a1.add_squadra("Napoli")
a1.effettua_visita()
a1.informazioni()