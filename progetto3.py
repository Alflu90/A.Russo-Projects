# |------------------------------------|
# | Parte 1 – Variabili e Tipi di Dati |
# |------------------------------------|

"""
Definisci variabili per rappresentare le seguenti informazioni di un cliente:

- nome (stringa),
- età (intero),
- saldo conto (float),
- stato VIP (booleano).✅ Esempio: nome = "Mario Rossi", eta = 34, saldo = 2500.75, vip = True
- Crea una lista di destinazioni disponibili (almeno 5 città).
- Definisci un dizionario che associa ogni destinazione a un prezzo medio del viaggio.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm       # Per poter personalizzare meglio i grafici

# Variabili per rappresentare le informazioni di un cliente

nome = "Mario Rossi"
eta = 34
saldo = 2500.75
vip = True

# Lista di destinazioni disponibili

destinazioni = ["Londra", "Parigi", "Roma", "Barcelona", "Praga"]

# Dizionario che associa ogni destinazione a un prezzo medio del viaggio

prezzo_viaggio = {
    "Londra": 200,
    "Parigi": 150,
    "Roma": 50,
    "Barcelona": 80,
    "Praga": 130
}


# |-------------------------------------------|
# | Parte 2 – Programmazione ad Oggetti (OOP) | 
# |-------------------------------------------|

"""
- Crea una classe Cliente con attributi: nome, età, vip.
- Aggiungi un metodo per stampare le informazioni.
- Crea una classe Viaggio con attributi: destinazione, prezzo, durata in giorni.
- Crea una classe Prenotazione che colleghi un cliente a un viaggio.
- Deve calcolare l'importo finale, con sconto del 10% se il cliente è VIP.
- Aggiungi un metodo dettagli() che stampa le informazioni complete.
"""

class Cliente:
    def __init__(self, nome:str, eta:int, vip:bool):
        self.nome = nome
        self.eta = eta
        self.vip = vip
    
    def informazioni_cliente(self):
        print(f"Nome: {self.nome}")
        print(f"Età: {self.eta}")
        print(f"Cliente VIP: {'Sì' if self.vip else 'No'}")
    
class Viaggio:
    def __init__(self, destinazione, prezzo, durata):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata = durata
    
class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio

# Metodo che calcola l'importo finale (con sconto se il cliente è VIP)

    def importo_finale(self):
        if self.cliente.vip == True:
            return self.viaggio.prezzo * 0.9 # Sconto del 10% se il cliente è VIP
        else:
            return self.viaggio.prezzo

# Metodo che stampa le informazioni complete

    def dettagli(self):
        print("--- DETTAGLI PRENOTAZIONE ---\n")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Destinazione: {self.viaggio.destinazione}")
        print(f"Durata (giorni): {self.viaggio.durata}")
        print(f"Importo: {self.importo_finale():.2f}\n")

#################### ESEMPI ####################

cliente1 = Cliente("Alfio Russo", 34, vip=True)
viaggio1 = Viaggio("Tokyo", 2000, 15)
prenotazione1 = Prenotazione(cliente1, viaggio1)

cliente2 = Cliente("Luana Lucà", 35, vip=False)
viaggio2 = Viaggio("New York", 1500, 10)
prenotazione2 = Prenotazione(cliente2, viaggio2)

prenotazione1.dettagli()
prenotazione2.dettagli()


# |-----------------|
# | Parte 3 – NumPy |
# |-----------------|

"""
Genera un array NumPy di 100 prenotazioni simulate, con prezzi casuali fra 200 e 2000 €.

Calcola e stampa:
- prezzo medio,
- prezzo minimo e massimo,
- deviazione standard,
- percentuale di prenotazioni sopra la media.
"""

# Array NumPy di 100 prenotazioni simulate con prezzi simulati

prezzi = np.random.uniform(200, 2000, size=100)

prezzo_medio = np.mean(prezzi)       # Prezzo medio
prezzo_minimo = np.min(prezzi)       # Prezzo minimo
prezzo_massimo = np.max(prezzi)      # Prezzo massimo
deviazione_standard = np.std(prezzi) # Deviazione standard

# Percentuale di prenotazioni sopra la media

percentuale_sopra_media = np.sum(prezzi > prezzo_medio) / len(prezzi) * 100

#################### RISULTATI ####################

print("--- STATISTICHE PRENOTAZIONI ---\n")
print(f"Prezzo medio: {prezzo_medio:.2f}€")
print(f"Prezzo minimo: {prezzo_minimo:.2f}€")
print(f"Prezzo massimo: {prezzo_massimo:.2f}€")
print(f"Deviazione standard: {deviazione_standard:.2f}")
print(f"Percentuale di prenotazioni sopra la media: {percentuale_sopra_media:.2f}%")


# |------------------|
# | Parte 4 – Pandas |
# |------------------|

"""
Crea un DataFrame Pandas con colonne: Cliente, Destinazione, Prezzo, Giorno_Partenza, Durata, Incasso.

Calcola con Pandas:
- incasso totale dell'agenzia,
- incasso medio per destinazione,
- top 3 destinazioni più vendute.
"""

# Creazione di dati simulati

np.random.seed(42) # Seme per riproducibilità

# Creazione 100 clienti unici

clienti = [f"Cliente {i}" for i in range(1, 101)]

# Numero casuale di prenotazioni assegnate a ciascun cliente (la maggioranza prenota 1 volta, alcuni 2, pochi 3)

numero_prenotazioni = np.random.choice([1, 1, 1, 2, 2, 3], size=len(clienti))

# Lista effettiva di clienti (ripetendo i nomi)

clienti_effettivi = []
for nome, n in zip(clienti, numero_prenotazioni):
    clienti_effettivi.extend([nome] * n)

# Numero totale di prenotazioni

n_prenotazioni = len(clienti_effettivi)
print(f"Totale prenotazioni generate: {n_prenotazioni}")

# Dati casuali per ogni prenotazione

destinazioni = np.random.choice(["Parigi", "New York", "Tokyo", "Roma", "Londra"], n_prenotazioni)
prezzi = np.random.uniform(200, 2000, n_prenotazioni)
giorni_partenza = pd.date_range(start="2025-01-01", periods=n_prenotazioni, freq="D")
durate = np.random.randint(3, 15, n_prenotazioni)
incassi = prezzi * 0.15 # Commissione (stimata al 15%) da parte dell'agenzia di viaggio

# Creazione del DataFrame

df = pd.DataFrame({
    "Cliente": clienti_effettivi,
    "Destinazione": destinazioni,
    "Prezzo": prezzi,
    "Giorno_Partenza": giorni_partenza,
    "Durata": durate,
    "Incasso": incassi
})

# Test DataFrame

print("--- ANTEPRIMA DATI ---\n")
print(df.head())
print(f"Righe del DataFrame: {len(df)} (dovrebbero essere {n_prenotazioni})")

# Calcoli

incasso_totale = df["Incasso"].sum()                                          # Incasso totale dell’agenzia
incasso_medio_per_destinazione = df.groupby("Destinazione")["Incasso"].mean() # Incasso medio per destinazione
top3_destinazioni = df["Destinazione"].value_counts().head(3)                 # Top 3 destinazioni più vendute

#################### RISULTATI ####################

print("\n--- STATISTICHE AGENZIA ---\n")
print(f"Incasso totale dell'agenzia: {incasso_totale:.2f}€")
print("\nIncasso medio (€) per destinazione:")
print(incasso_medio_per_destinazione)
print("\nTop 3 destinazioni più vendute:")
print(top3_destinazioni)


# |----------------------|
# | Parte 5 – Matplotlib |
# |----------------------|

"""
- Crea un grafico a barre che mostri l'incasso per ogni destinazione.
- Crea un grafico a linee che mostri l'andamento giornaliero degli incassi.
- Crea un grafico a torta che mostri la percentuale di vendite per ciascuna destinazione.
"""

# --- Grafico a barre ---
# Calcolo incasso per destinazione

incasso_destinazione = df.groupby("Destinazione")["Incasso"].sum()

# Genera una scala di colori automatica

colors = cm.get_cmap("viridis")(np.linspace(0, 1, len(incasso_destinazione))).tolist()

# Crea il grafico a barre

plt.figure(figsize=(8,5))
bars = plt.bar(np.array(incasso_destinazione.index), incasso_destinazione.values, # type: ignore
        color=colors, edgecolor='black')

# Titoli e assi

plt.title("Incasso per ogni destinazione", fontsize=14, fontweight="bold")
plt.xlabel("Destinazioni", fontsize=12)
plt.ylabel("Incasso (€)", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Etichette sopra ogni barra

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,  # posizione orizzontale (centro barra)
        yval + (yval * 0.01),             # leggermente sopra la barra
        f"€{yval:,.0f}",                  # testo formattato
        ha='center', va='bottom',
        fontsize=10, fontweight="bold"
    )

# Mostra il grafico

plt.tight_layout()
plt.show()

# --- Grafico a linee ---
# Andamento giornaliero degli incassi

incasso_giornaliero = df.groupby("Giorno_Partenza")["Incasso"].sum()
plt.figure(figsize=(10,5))
plt.plot(incasso_giornaliero.index.to_numpy(), incasso_giornaliero.values, # type: ignore
        marker='o', color='tab:blue', linewidth=2)

# Titoli e assi

plt.title("Incasso Totale per Destinazione", fontsize=14, fontweight="bold")
plt.xlabel("Destinazione", fontsize=12)
plt.ylabel("Incasso (€)", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Mostra il grafico

plt.tight_layout()
plt.show()

# --- Grafico a torta ---
# Percentuale di vendite per ciascuna destinazione

vendite_per_destinazione = df["Destinazione"].value_counts()
plt.figure(figsize=(7,7))

# Crea il grafico a torta

plt.pie(
    vendite_per_destinazione.values, # type: ignore
    labels = vendite_per_destinazione.index.astype(str).tolist(),
    autopct="%1.1f%%",
    startangle=90,
    shadow=True,
    colors=cm.get_cmap("viridis")(np.linspace(0, 1, len(vendite_per_destinazione))).tolist()
)

# Titolo

plt.title("Percentuale di Vendite per Destinazione", fontsize=14, fontweight="bold")

# Mostra il grafico

plt.tight_layout()
plt.show()


# |----------------------------|
# | Parte 6 – Analisi Avanzata | 
# |----------------------------|

"""
Raggruppa i viaggi in categorie:

"Europa", "Asia", "America", "Africa" (puoi usare un dizionario che associa ogni destinazione a una categoria).

Calcola con Pandas:
- incasso totale per categoria,
- durata media dei viaggi per categoria.

Salva il DataFrame aggiornato in un CSV chiamato prenotazioni_analizzate.csv.
"""

# Dizionario di categorizzazione

categorie = {
    "Parigi": "Europa",
    "Roma": "Europa",
    "Londra": "Europa",
    "Tokyo": "Asia",
    "New York": "America",
}

# Aggiunta colonna "Categoria"

df["Categoria"] = df["Destinazione"].map(categorie)

# --- Controllo: alcuni clienti devono comparire più volte ---

print("\nNumero prenotazioni per i primi 10 clienti:")
print(df["Cliente"].value_counts().head(10))

# Calcoli

incasso_per_categoria = df.groupby("Categoria")["Incasso"].sum()      # Incasso totale per categoria
durata_media_per_categoria = df.groupby("Categoria")["Durata"].mean() # Durata media per categoria

#################### RISULTATI ####################

print("--- ANALISI PER CATEGORIA ---")
print("\nIncasso totale per categoria (€):")
print(incasso_per_categoria.round(2))

print("\nDurata media dei viaggi per categoria (giorni):")
print(durata_media_per_categoria.round(2))

# Salvataggio in .CSV

df.to_csv("prenotazioni_analizzate.csv", index=False, encoding="utf-8-sig")
print("\nFile 'prenotazioni_analizzate.csv' salvato correttamente.")


# |----------------------|
# | Parte 7 – Estensioni | 
# |----------------------|

"""
Crea una funzione che restituisce i N clienti con più prenotazioni.
Realizza un grafico combinato (barre + linea) che mostri:
- barre = incasso medio per categoria,
- linea = durata media per categoria.
"""

def top_clienti(df: pd.DataFrame, n: int = 5) -> pd.Series: # N clienti con il maggior numero di prenotazioni
    return df["Cliente"].value_counts().head(n)

#################### ESEMPI ####################

print("Top 5 clienti con più prenotazioni:")
print(top_clienti(df, 5))
print()

# --- Grafico combinato (Barre + Linee) ---
# Calcolo incasso medio e durata media per categoria

analisi_cat = df.groupby("Categoria").agg({
    "Incasso": "mean",
    "Durata": "mean"
}).round(2)

# Creazione del grafico combinato

fig, ax1 = plt.subplots(figsize=(8, 5))

# Barre: incasso medio per categoria

ax1.bar(analisi_cat.index, analisi_cat["Incasso"], color="cornflowerblue", alpha=0.7, label="Incasso medio (€)")
ax1.set_xlabel("Categoria", fontsize=12)
ax1.set_ylabel("Incasso medio (€)", color="cornflowerblue", fontsize=12)
ax1.tick_params(axis="y", labelcolor="cornflowerblue")

# Linea: durata media per categoria

ax2 = ax1.twinx()
ax2.plot(analisi_cat.index, analisi_cat["Durata"], color="darkorange", marker="o", linewidth=2, label="Durata media (giorni)")
ax2.set_ylabel("Durata media (giorni)", color="darkorange", fontsize=12)
ax2.tick_params(axis="y", labelcolor="darkorange")

# Titolo e legenda

plt.title("Confronto 'incasso medio' e 'durata media' per Categoria", fontsize=14, fontweight="bold")

# Gestione legende doppio asse

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc="lower left")

# Mostra il grafico

plt.tight_layout()
plt.show()
