

# classe persona
class Persona:
    def __init__ (self, nome, cognome, eta, citta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.citta = citta
        
    def stampa_info(self):
        print(f"nome: {self.nome}")
        print(f"cognome: {self.cognome}")
        print(f"eta: {self.eta}")
        print(f"citta: {self.citta}")
        
Persona1 = Persona("Laika", "Manis", 3 , "Oristano")
Persona1.stampa_info()
  
#classe libro
class Libro:
    def __init__ (self, titolo, anno):
        self.titolo = titolo
        self.anno = anno
    
    def libro_attuale(self, anno_attuale):
        anni_trascorsi = anno_attuale - self.anno
        return anni_trascorsi <= 10

Libro1 = Libro("sognare", 2000)

anno_attuale =2024

if Libro1.libro_attuale(anno_attuale):
    print("Il libro  e' recente")
    
else:
    print("Il libro non e' recente")    

# conto bancario
class Conto:
    def __init__(self, saldo_iniziale=0):
        self.saldo = saldo_iniziale

    def deposito(self, importo):
        self.saldo += importo
        print(f"Deposito di {importo} effettuato. Nuovo saldo: {self.saldo}")
    def prelievo(self, importo):
      if importo <= self.saldo:
            self.saldo -= importo
            print("Prelievo effettuato")
      else:
            print("Impossibile prelevare. Operazione annullata.")
            
conto1= Conto (500)
conto1.deposito (600)
conto1.prelievo (100)

# classe prodotto
class Prodotto:
    def __init__(self, nome, prezzo, quantita_disponibile):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita_disponibile = quantita_disponibile

    def calcola_costo_totale(self, quantita_disponibile):
        costo_totale = self.prezzo * quantita_disponibile
        return costo_totale

    def verifica_disponibilita(self, quantita_desiderata):
        return self.quantita_disponibile >= quantita_desiderata

prodotto1 = Prodotto("Pc", 1300, 10)

quantita_desiderata = 9
if prodotto1.verifica_disponibilita(quantita_desiderata):
    costo_totale = prodotto1.calcola_costo_totale(quantita_desiderata)
    print(f"Prodotto: {prodotto1.nome} quantita: {quantita_desiderata} Costo Totale: {costo_totale}")
else:
    print(f"Prodotto '{prodotto1.nome}' non disponibile nella quantita richiesta.")
    

