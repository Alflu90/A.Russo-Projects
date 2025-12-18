"""
Progetto #1 - Previsioni vendite

Traccia:
Lavorare su un dataset di vendite storiche per comprendere i dati, pulirli, trasformarli e produrre delle
previsioni di base usando metodi semplici e direttamente implementabili con Pandas e Python “puro”.

Dataset (esempio di struttura)

Data — data della vendita
Prodotto — nome o codice prodotto
Vendite — quantità venduta quel giorno
Prezzo — prezzo unitario (opzionale)

I dati possono contenere valori mancanti, duplicati o inconsistenze.

Consegna

Parte 1 - Caricamento e esplorazione dati

1. Leggere il dataset con Pandas.
2. Visualizzare le prime righe, la struttura (.info()), e statistiche descrittive (.describe()).

Parte 2 - Pulizia

3. Gestire valori mancanti (es. sostituire con 0 o media).
4. Rimuovere duplicati.
5. Verificare che i tipi di dato siano corretti (date come datetime, quantità come numeri, ecc.).

Parte 3 - Analisi esplorativa

6. Calcolare vendite totali per prodotto.
7. Individuare il prodotto più venduto e quello meno venduto.
8. Calcolare vendite medie giornaliere.
"""


import pandas as pd
import numpy as np

# Creazione di un Dataset con valori random, mancanti e con errori di caricamento.
df_ferrari = pd.DataFrame({
    "Data": pd.date_range(start="2025-01-01", periods=8),
    "Modello": ["296", "SF90", "roma", "  Purosangue", "12Cilindri", "sf90", "spider", "Roma"],
    "Vendite": np.random.randint(0, 5, size=8),
    "Prezzo": [395, np.nan, 219, 390, 320, 275, 250, np.nan]
})


#-------------------------------------------#
# Parte 1 - Caricamento e esplorazione dati #
#-------------------------------------------#

# Visualizzazione prime righe
print("Prime 5 righe del Dataset iniziale:")
print(df_ferrari.head())

# Informazioni del Dataset
print("\n" + "-"*60)
print("Informazioni:")
print(df_ferrari.info())

# Statistiche descrittive
print("\n" + "-"*60)
print("Statistiche descrittive:")
print(df_ferrari.describe())


#-------------------#
# Parte 2 - Pulizia #
#-------------------#

# Pulizia e uniformazione delle stringhe
df_ferrari["Modello_pulito"] = df_ferrari["Modello"].str.strip().str.title()

# Gestione valori mancanti
df_ferrari["Prezzo"] = df_ferrari["Prezzo"].fillna(df_ferrari["Prezzo"].mean().round(2)) # type: ignore

# Rimuozione duplicati
df_ferrari = df_ferrari.drop_duplicates(subset=["Modello_pulito"])

# Controllo tipi dati
df_ferrari["Data"] = pd.to_datetime(df_ferrari["Data"])
df_ferrari["Vendite"] = df_ferrari["Vendite"].astype(int)
df_ferrari["Prezzo"] = df_ferrari["Prezzo"].astype(float)

# Visualizzazione del Dataset intero dopo la pulizia
print("\n" + "-"*60)
print("Dataset pulito:")
print(df_ferrari)

# Informazioni del Dataset pulito
print("\n" + "-"*60)
print("Informazioni dopo la pulizia:")
print(df_ferrari.info())


#-------------------------------#
# Parte 3 - Analisi esplorativa #
#-------------------------------#

# Vendite totali per modello
totali_per_modello = df_ferrari.groupby("Modello_pulito")["Vendite"].sum()
print("\n" + "-"*60)
print(f"Vendite totali per modello:\n", totali_per_modello)

# Modello più venduto e quello meno venduto
print("\n" + "-"*60)
print("Modello più venduto:\n", totali_per_modello.idxmax())  # Velocizzare la produzione del modello in trend
print("\n" + "-"*60)
print("Modello meno venduto:\n", totali_per_modello.idxmin()) # Campagna di marketing mirata per incrementare le vendite

# Vendite medie giornaliere
print("\n" + "-"*60)
medie_giornaliere = df_ferrari.groupby("Data")["Vendite"].sum()
print(f"Vendite medie giornaliere:\n", medie_giornaliere)


#-----------------#
# EXTRA - Grafici #
#-----------------#

import matplotlib.pyplot as plt

# Creazione colonna "Incasso" = Vendite * Prezzo
df_ferrari["Incasso"] = df_ferrari["Vendite"] * df_ferrari["Prezzo"]

# Raggruppamento per Data
df_giornaliero = df_ferrari.groupby("Data").agg({
    "Vendite": "sum",
    "Incasso": "sum"
}).reset_index()

print("\n" + "-"*60)
print("Vendite e incassi giornalieri:")
print(df_giornaliero)

# Totali sull'intero periodo
tot_vendite = df_giornaliero["Vendite"].sum()
print("\n" + "-"*60)
print("Vendite totali:\n")
print(tot_vendite)

tot_incasso = df_giornaliero["Incasso"].sum()
print("\n" + "-"*60)
print("Incassi totali (M€):\n")
print(f"{tot_incasso / 1000:.2f}")
print("")

# Grafico combinato
fig, ax1 = plt.subplots(figsize=(12,6))

# Istogramma per le vendite
bar = ax1.bar(
    df_giornaliero["Data"],
    df_giornaliero["Vendite"],
    color='skyblue'
)
ax1.set_xlabel("Data", fontsize=12)
ax1.set_ylabel("Vendite", color='black', fontsize=12)
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_xticks(df_giornaliero["Data"])
ax1.set_xticklabels(df_giornaliero["Data"].dt.strftime('%d-%m'), rotation=45) # type: ignore

# Linea per l'incasso
ax2 = ax1.twinx()
line, = ax2.plot(
    df_giornaliero["Data"],
    df_giornaliero["Incasso"],
    color='orange',
    marker='o',
    linestyle='-'
)
ax2.set_ylabel("Incasso (k€)", color='orange', fontsize=12)
ax2.tick_params(axis='y', labelcolor='orange')

# Titolo e legenda
plt.title("Vendite e Incassi giornalieri - Ferrari Gennaio 2025", fontsize=14)
fig.tight_layout()
legend_labels = [
    f"Totale vendite: {tot_vendite} vetture",
    f"Totale incasso: {tot_incasso / 1000:.2f} M€"
]

ax1.legend(
    [bar, line],
    legend_labels,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.15),
    ncol=2,           # legenda su una riga
    frameon=False     # senza riquadro
)

plt.title(
    "Vendite e Incassi - Ferrari (1-8 Gennaio 2025)",
    fontsize=14
)

fig.tight_layout()
plt.show()
