# Parte 1 – Variabili e Tipi di Dati

"""
Definire le variabili necessarie per rappresentare:

- Nome, cognome e codice fiscale di un paziente (stringhe).
- Età e peso del paziente (interi e float).
- Lista delle analisi effettuate (lista di stringhe).
"""

# Paziente 1

nome1 = "Alfio"
cognome1 = "Russo"
codice_fiscale1 = "RSS*123"
eta1 = 34
peso1 = 73.5
analisi1 = ["emocromo", "glicemia", "colesterolo"]

# Paziente 2

nome2 = "Luana"
cognome2 = "Lucà"
codice_fiscale2 = "LCU*456"
eta2 = 35
peso2 = 58.2
analisi2 = ["ferro", "beta"]

# Paziente 3

nome3 = "Diana"
cognome3 = "Zappalà"
codice_fiscale3 = "ZPP*789"
eta3 = 64
peso3 = 55.7
analisi3 = ["emocromo", "glicemia", "trigliceridi"]

# Stampa dei dati per verifica

print("Paziente 1:\n", nome1, cognome1, codice_fiscale1, eta1, "anni", peso1, "kg\n",analisi1)
print("Paziente 2:\n", nome2, cognome2, codice_fiscale2, eta2, "anni", peso2, "kg\n",analisi2)
print("Paziente 3:\n", nome3, cognome3, codice_fiscale3, eta3, "anni", peso3, "kg\n",analisi3)



# Parte 2 – Classi e OOP

"""
Creare una classe Paziente con:
- Attributi: nome, cognome, codice_fiscale, eta, peso, analisi_effettuate.
- Metodo scheda_personale() che restituisca una stringa con i dati principali del paziente.

Creare una classe Medico con:
- Attributi: nome, cognome, specializzazione.
- Metodo visita_paziente(paziente) che stampi quale medico sta visitando quale paziente.

Creare una classe Analisi che contenga:
- Tipo di analisi (es. glicemia, colesterolo).
- Risultato numerico.
- Metodo valuta() che stabilisca se il valore è nella norma (criteri inventati da voi).
"""

import numpy as np
import random

# Classe Paziente

class Paziente():
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = None # modifica della classe Paziente per aggiungere un attributo (parte 4).
    
    def scheda_personale(self):
        """Metodo che restituisce una stringa con i dati principali del paziente."""
        return (f"Scheda Paziente:\n"
                f"Nome: {self.nome} {self.cognome}\n"
                f"Codice Fiscale: {self.codice_fiscale}\n"
                f"Età: {self.eta} anni\n"
                f"Peso: {self.peso} kg\n"
                f"Analisi effettuate: {', '.join(str(a) for a in self.analisi_effettuate)}")

# Classe Medico

class Medico():
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione
    
    def visita_paziente(self, paziente):
        """Metodo che stampa presso quale medico è in cura il paziente."""
        print(f"Il paziente {paziente.nome} {paziente.cognome} è sotto la cura del dottor {self.nome} {self.cognome} ({self.specializzazione}).")

# Classe Analisi

class Analisi():
    def __init__(self, tipo_analisi, risultati):
        self.tipo_analisi = tipo_analisi
        self.risultati = risultati

    def __str__(self):
        return f"{self.tipo_analisi} ({self.risultati})"
    
    def valuta(self):
        """Metodo che stabilisce se il valore è nella norma"""
        if self.tipo_analisi.lower() == "glicemia":
            if 70 <= self.risultati <= 100:
                return "Glicemia nella norma"
            else:
                return "***\nValore glicemia fuori norma"
        elif self.tipo_analisi.lower() == "colesterolo":
            if self.risultati < 200:
                return "Colesterolo nella norma"
            else:
                return "***\nValore colesterolo alto (> 200)"
        elif self.tipo_analisi.lower() == "emocromo":
            if 4.0 <= self.risultati <= 5.5:
                return "Emocromo nella norma"
            else:
                return "***\nValori emocromo fuori norma"
        else:
            return f"Nessun criterio definito per {self.tipo_analisi}"

# --- ESEMPIO DI UTILIZZO ---

# Creazione di alcune analisi

a1 = Analisi("emocromo", 5.1)
a2 = Analisi("glicemia", 95)
a3 = Analisi("colesterolo", 220)

# Creazione di un paziente

p1 = Paziente("Alfio", "Russo", "RSS*123", 34, 73.5, [a1, a2, a3])

# Creazione di un medico

m1 = Medico("Mario", "Rossi", "Medicina Interna")

# Esempio di utilizzo dei metodi

print(p1.scheda_personale())
print()
m1.visita_paziente(p1)
print()
for analisi in p1.analisi_effettuate:
    print(f"{analisi.tipo_analisi}: '{analisi.risultati}' - {analisi.valuta()}")



# Parte 3 – Uso di NumPy

"""
Supponiamo che il centro raccolga i risultati di un certo esame per 10 pazienti.
Rappresentare i valori in un array NumPy.
Calcolare con NumPy: media, valore massimo, valore minimo e deviazione standard.
"""

# Risultati generati in modo randomico per un certo esame (es: glicemia) per 10 ipotetici pazienti

risultati = np.random.randint(0, 200, size=10)

media = np.mean(risultati)      # Media
valore_max = np.max(risultati)  # Valore Massimo
valore_min = np.min(risultati)  # Valore Minimo
deviazione = np.std(risultati)  # Deviazione Standard

# Rappresentazione dei valori dell'array NumPy

print(f"I risultati degli esami della 'Glicemia' per i dieci pazienti sono:\n", risultati)
print(f"Media: {media}")
print(f"Valore Massimo: {valore_max}")
print(f"Valore Massimo: {valore_min}")
print(f"Deviazione Standard: {deviazione:.2f}")



# Parte 4 - Integrazione OOP + NumPy

"""
- Aggiornare la classe Paziente inserendo un attributo risultati_analisi che sia un array NumPy 
contenente i valori numerici delle analisi svolte.
- Creare un metodo statistiche_analisi() che calcoli:
- Media dei valori
- Minimo e massimo
- Deviazione standard
"""

class PazienteRisultati(Paziente):
    """Creazione di una sottoclasse per inserire un attributo alla classe Paziente"""
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate, risultati_analisi):
        super().__init__(nome, cognome, codice_fiscale, eta, peso, analisi_effettuate)
        self.risultati_analisi = np.array(risultati_analisi) # array NumPy che contiene i valori delle analisi svolte

    def statistiche_analisi(self):
        media = np.mean(self.risultati_analisi)     # Media dei valori
        minimo = np.min(self.risultati_analisi)     # Minimo
        massimo = np.max(self.risultati_analisi)    # Massimo
        deviazione = np.std(self.risultati_analisi) # Deviazione Standard

        return {
            "media": f"{round(media, 2)}",
            "minimo": f"{minimo}",
            "massimo": f"{massimo}",
            "deviazione standard": f"{round(deviazione, 2)}"
        }

# Creazione di un paziente di prova

paziente_risultati = PazienteRisultati("Alfio", "Russo", "RSS*123", 34, 73.5, 
                                       ["emocromo", "glicemia", "colesterolo"], 
                                       [95, 180, 150])

# Rappresentazione dei risultati per il paziente di riferimento

print(paziente_risultati.scheda_personale())
print("\nStatistiche analisi:", paziente_risultati.statistiche_analisi())

"""
Parte 5 - Applicazione completa

Creare un piccolo programma principale (main) che:

- Inserisca almeno 3 medici e 5 pazienti.
- Ogni paziente deve avere almeno 3 risultati di analisi.
- Stampi la scheda di ogni paziente.
- Mostri quale medico visita quale paziente.
- Stampi le statistiche delle analisi per ciascun paziente.
"""

if __name__ == "__main__":
    # Creazione di 3 medici
    medici = [
        Medico("Ippocrate", "di Kos", "Medicina Interna"),
        Medico("Andreas", "van Wesel", "Anatomopatologo"),
        Medico("Edward", "Jenner", "Immunologo")
    ]

    # Creazione di 5 pazienti con relativi risultati analisi
    pazienti = [
        PazienteRisultati("Albert", "Einstein", "NSTLRT", 65, 76.5,
                          ["emocromo", "glicemia", "colesterolo"], [5.2, 95, 210]),
        PazienteRisultati("Isaac", "Newton", "NWTSCI", 52, 70.3,
                          ["glicemia", "colesterolo", "vitamina D"], [89, 180, 45]),
        PazienteRisultati("Marie", "Curie", "CRUMRA", 48, 54.2,
                          ["creatinina", "glicemia", "colesterolo"], [1.0, 120, 250]),
        PazienteRisultati("Galileo", "Galilei", "GLLGLL", 47, 69.2,
                          ["emocromo", "colesterolo", "glicemia"], [4.9, 170, 100]),
        PazienteRisultati("Nikola", "Tesla", "TSLNKL", 50, 76.0,
                          ["glicemia", "colesterolo", "trigliceridi"], [85, 195, 130])
    ]

    # Rappresentazione schede pazienti e statistiche
    print("=== SCHEDA COMPLETA PAZIENTI ===\n")
    for paziente in pazienti:
        print(paziente.scheda_personale())
        print("Statistiche analisi:", paziente.statistiche_analisi())

        # Assegnazione casuale del medico
        medico_scelto = random.choice(medici)
        medico_scelto.visita_paziente(paziente)

        print("\n")
