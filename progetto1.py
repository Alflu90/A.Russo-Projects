# Parte 1 - Variabili e tipi di dati

titolo:str = "Il Signore degli Anelli"
copie:int = 5
prezzo:float = 19.90
stato:bool = True

print(f"Titolo - {titolo}\nCopie - {copie}\nPrezzo - {prezzo:.2f}€\nDisponibile - {stato}")

# Parte 2 - Strutture dati

"""Crea una lista con almeno 5 titoli di libri"""
lista_libri = [
    "Frankenstein",
    "Cent'anni di solitudine",
    "Il potere delle abitudini",
    "1984",
    "Il gioane Holden"
]

"""Crea un dizionario che mappa il titolo del libro al numero di copie disponibili"""
copie_libri = {
    "Frankenstein": 4,
    "Cent'anni di solitudine": 6,
    "Il potere delle abitudini": 3,
    "1984": 5,
    "Il giovane Holden": 2
}

"""Crea un insieme (set) che contiene tutti gli utenti registrati alla biblioteca"""
registrati_biblioteca = {
    "Alfio",
    "Luana",
    "Diana",
    "Beatrice"
}

# Parte 3 - Classi e OOP

"""Crea una classe Libro"""
class Libro:
    def __init__(self, titolo, autore, anno, copie):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie = copie

    def info(self):
        """Aggiunge un metodo info() che restituisce una stringa descrittiva del libro"""
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nAnno: {self.anno}\nCopie disponibili: {self.copie}"
        
"""Crea una classe Utente"""
class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente
    
    def scheda(self):
        """Aggiunge un metodo scheda() che stampa i dati dell'utente"""
        return f"{self.nome}, {self.eta} anni - ID: {self.id_utente}"

"""Crea una classe Prestito"""
class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni
    
    def dettagli(self):
        """Aggiunge un metodo dettagli() che stampa tutte le informazioni sul prestito"""
        return (
            f"L'utente {self.utente.nome} ha preso in prestito il libro "
            f"'{self.libro.titolo}' per {self.giorni} giorni."
        )
    
# Parte 4 – Funzionalità

def presta_libro(utente, libro, giorni):
    """Verifica se il libro ha almeno 1 copia disponibile"""
    if libro.copie > 0:
        libro.copie -= 1  # riduce il numero di copie
        prestito = Prestito(utente, libro, giorni)
        print(f"'{libro.titolo}' è stato prestato a {utente.nome} con successo.")
        return prestito
    else:
        print(f"Il libro '{libro.titolo}' non è attualmente disponibile per il prestito!")
        return None


################################################# ESEMPI #################################################

if __name__ == "__main__":
# Esempio 1
    libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 2)
    utente1 = Utente("Alfio Russo", 34, "12345")

    prestito1 = presta_libro(utente1, libro1, 7)
    if prestito1:
        print(prestito1.dettagli())

    """Mostra copie aggiornate"""
    print("\nStato attuale del libro:")
    print(libro1.info())


# Esempio 2
    libro2 = Libro("Harry Potter", "J.K. Rowling", 1997, 0)
    utente2 = Utente("Luana Lucà", 35, "67890")

    prestito2 = presta_libro(utente2, libro2, 4)
    if prestito2:
        print(prestito2.dettagli())
    
    """Mostra copie aggiornate"""
    print("\nStato attuale del libro:")
    print(libro2.info())


# Esempio 3
    libro3 = Libro("Il trono di spade", "George R.R. Martin", 1996, 1)
    utente3 = Utente("Diana Russo", 3, "102938")

    prestito3 = presta_libro(utente3, libro3, 14)
    if prestito3:
        print(prestito3.dettagli())
    
    """Mostra copie aggiornate"""
    print("\nStato attuale del libro:")
    print(libro3.info())