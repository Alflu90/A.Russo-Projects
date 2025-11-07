#--------------------------------------------------------#
#  Progetto - Analisi di Vendite in una Catena di Negozi #
#--------------------------------------------------------#

"""
Una catena di negozi di elettronica vuole analizzare i dati delle vendite per migliorare la gestione e capire l'andamento del mercato.
I dati vengono raccolti giornalmente e comprendono informazioni su prodotti, quantità vendute, prezzo, incassi e negozi.

Si richiede di sviluppare un programma in Python che utilizzi:

- NumPy per elaborazioni numeriche veloci;
- Pandas per la gestione e analisi di dataset;
- Matplotlib per la visualizzazione dei dati in grafici.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm 


#---------------------------#
# Parte 1 - Dataset di base #
#---------------------------#

"""
Creare un file CSV chiamato vendite.csv con almeno 30 righe che contenga le seguenti colonne:

- Data (formato YYYY-MM-DD);
- Negozio (stringa: es. Milano, Roma, Napoli…);
- Prodotto (stringa: es. Smartphone, Laptop, TV…);
- Quantità (intero);
- Prezzo_unitario (float).
"""

n_righe = 30
date = pd.date_range(start="2025-11-01", periods=n_righe, freq="D").strftime("%Y-%m-%d") # 30 date consecutive (formato YYYY-MM-DD)
negozi = ["Milano", "Roma", "Napoli", "Torino", "Firenze", "Bologna", "Palermo"]
prodotti = ["Smartphone", "Laptop", "TV", "Tablet", "Cuffie", "Fotocamera", "Monitor"]

# DataFrame e salvataggio in un file .CSV

df = pd.DataFrame({
    "Data": date,
    "Negozio": np.random.choice(negozi, size=n_righe),
    "Prodotto": np.random.choice(prodotti, size=n_righe),
    "Quantità": np.random.randint(1, 20, size=n_righe),
    "Prezzo_unitario": np.random.uniform(100, 2000, size=n_righe).round(2)
})

df.to_csv("vendite.csv", index=False)


#-----------------------------------#
# Parte 2 - Importazione con Pandas #
#-----------------------------------#

"""
Importare il file CSV in un DataFrame Pandas e stampare:
- le prime 5 righe (head());
- il numero di righe e colonne (shape);
- le informazioni generali (info()).
"""

df = pd.read_csv("vendite.csv") # Importa il file .CSV appena creato

# Prime 5 righe del file

print("Prime 5 righe:")
print(df.head())
print("\n" + "-"*60)

# Numero di righe e colonne

print("\nDimensioni (righe, colonne):")
print(df.shape)
print("\n" + "-"*60)

# Informazioni generali del DataFrame

print("\nInformazioni generali:")
df.info()


#-----------------------------------#
# Parte 3 - Elaborazioni con Pandas #
#-----------------------------------#

"""
Aggiungere una colonna Incasso calcolata come Quantità * Prezzo_unitario.

Calcolare con Pandas:
- l'incasso totale di tutta la catena;
- l'incasso medio per negozio;
- i 3 prodotti più venduti (in termini di quantità totale);
- Raggruppare i dati per Negozio e Prodotto e mostrare l'incasso medio.
"""

df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"] # Nuova colonna "Incasso"

# Incasso totale di tutta la catena

incasso_totale = df["Incasso"].sum().round(2)
print("Incasso totale di tutta la catena:\n")
print(incasso_totale)

# Incasso medio per negozio

incasso_medio_negozio = df.groupby("Negozio")["Incasso"].mean()
print("\nIncasso medio per negozio:\n")
print(incasso_medio_negozio)

# 3 prodotti più venduti

top3_prodotti = df.groupby("Prodotto")["Quantità"].sum().sort_values(ascending=False).head(3)
print("\n3 prodotti più venduti (in termini di quantità totale):\n")
print(top3_prodotti)

# Incasso medio per negozio e prodotto

incasso_medio_negozio_prodotto = df.groupby(["Negozio", "Prodotto"])["Incasso"].mean()
print("\nIncasso medio per 'Negozio' e 'Prodotto':\n")
print(incasso_medio_negozio_prodotto)


#------------------------#
# Parte 4 - Uso di NumPy #
#------------------------#

"""
Estrarre la colonna Quantità come array NumPy e calcolare:

- media, minimo, massimo e deviazione standard;
- percentuale di vendite sopra la media.

Creare un array NumPy 2D che contenga solo Quantità e Prezzo_unitario e calcolare per ogni riga l'incasso.
Confrontare i risultati con la colonna Incasso del DataFrame per verificarne la correttezza.
"""

q = df["Quantità"].to_numpy() # Estrazione della colonna "Quantità" come array NumPy

# Calcolo dei dati

media = np.mean(q)
minimo = np.min(q)
massimo = np.max(q)
deviazione_standard = np.std(q)

percentuale_sopra_media = np.sum(q > media) / len(q) * 100

# Visualizzazione dei dati

print(f"\nMedia: {media:.2f}")
print(f"Minimo: {minimo}")
print(f"Massimo: {massimo}")
print(f"Deviazione standard: {deviazione_standard:.2f}")
print(f"Percentuale di vendite sopra la media: {percentuale_sopra_media:.2f}%\n")

# Array NumPy 2D che contiene solo "Quantità" e "Prezzo_unitario"

arr = df[["Quantità", "Prezzo_unitario"]].to_numpy()
incassi_np = arr[:, 0] * arr[:, 1] # Calcola l'incasso per ogni riga (Quantità * Prezzo_unitario)

incassi_df = df["Incasso"].to_numpy() # Nuovo array per il confronto con i dati originali

confronto = np.allclose(incassi_np, incassi_df) # Confronta con la colonna "Incasso" del DataFrame

# Verifichiamo la correttezza dei dati con un ritorno booleano (True o False)

print("I dati coincidono?\n")
print(confronto)


#------------------------------------------#
# Parte 5 - Visualizzazioni con Matplotlib #
#------------------------------------------#

"""
Creare i seguenti grafici:
- grafico a barre: incasso totale per ogni negozio;
- grafico a torta: percentuale di incassi per ciascun prodotto;
- grafico a linee: andamento giornaliero degli incassi totali della catena.
"""

###################### GRAFICO A BARRE ######################

incasso_negozio = df.groupby("Negozio")["Incasso"].sum()
colors = cm.get_cmap("plasma")(np.linspace(0, 1, len(incasso_negozio))).tolist() # Genera una scala di colori automatica

# Grafico a barre

plt.figure(figsize=(8,5))
bars = plt.bar(np.array(incasso_negozio.index), incasso_negozio.values, # type: ignore
        color=colors, edgecolor='black')

# Titoli e assi

plt.title("Incasso per ogni negozio", fontsize=14, fontweight="bold")
plt.xlabel("Negozi", fontsize=12)
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

# Visualizzazione del grafico

plt.tight_layout()
plt.show()

###################### GRAFICO A TORTA ######################

incassi_prodotto = df["Prodotto"].value_counts()

# Grafico a torta

plt.figure(figsize=(7,7))
plt.pie(
    incassi_prodotto.values, # type: ignore
    labels = incassi_prodotto.index.astype(str).tolist(),
    autopct="%1.1f%%",
    startangle=90,
    shadow=True,
    colors=cm.get_cmap("tab10")(np.linspace(0, 1, len(incassi_prodotto))).tolist()
)

# Titolo

plt.title("Percentuale di incassi per prodotto", fontsize=14, fontweight="bold")

# Mostra il grafico

plt.tight_layout()
plt.show()

###################### GRAFICO A LINEE ######################

incasso_giornaliero = df.groupby("Data")["Incasso"].sum()

# Grafico a linee

plt.figure(figsize=(10,5))
plt.plot(incasso_giornaliero.index.to_numpy(), incasso_giornaliero.values, # type: ignore
        marker='o', color='tab:blue', linewidth=2)

# Titoli e assi

plt.title("Incasso Totale della catena", fontsize=14, fontweight="bold")
plt.xlabel("Data", fontsize=12, fontweight="bold")
plt.ylabel("Incasso (€)", fontsize=12, fontweight="bold")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(incasso_giornaliero.index[::5])
plt.xticks(rotation=45)

# Mostra il grafico

plt.tight_layout()
plt.show()


#----------------------------#
# Parte 6 - Analisi Avanzata #
#----------------------------#

"""
Creare una nuova colonna Categoria che raggruppi i prodotti in grandi famiglie (es. Smartphone e Laptop → Informatica, TV → Elettrodomestici).

Calcolare per ogni categoria:

- incasso totale;
- quantità media venduta.

Salvare il DataFrame aggiornato con le nuove colonne in un nuovo file vendite_analizzate.csv.
"""

categorie = {
    "Smarphone": "Elettronica",
    "Laptop": "Informatica",
    "TV": "Elettronica",
    "Tablet": "Elettronica",
    "Cuffie": "Accessori",
    "Fotocamera": "Elettronica",
    "Monitor": "Informatica"
}

df["Categoria"] = df["Prodotto"].map(categorie)

# Calcoli

incasso_tot_categoria = df.groupby("Categoria")["Incasso"].sum()
quantita_media_venduta_categoria = df.groupby("Categoria")["Quantità"].mean()

# Visualizzazione risultati

print("--- ANALISI PER CATEGORIA ---")
print("\nIncasso totale per categoria (€):")
print(incasso_tot_categoria.round(2))

print("\nQuantità media venduta per categoria:")
print(quantita_media_venduta_categoria.round(2))

# Salvataggio in .CSV

df.to_csv("vendite_analizzate.csv", index=False, encoding="utf-8-sig")
print("\nFile 'vendite_analizzate.csv' salvato correttamente.")


#----------------------#
# Parte 7 - Estensioni #
#----------------------#

"""
Creare un grafico combinato: incasso medio per categoria (grafico a barre) + linea della quantità media venduta.
Creare una funzione top_n_prodotti(n) che restituisca i 'n' prodotti più venduti in termini di incasso totale.
"""

# Calcolo incasso medio e quantità media per categoria

analisi_categorie = df.groupby("Categoria").agg({
    "Incasso": "mean",
    "Quantità": "mean"
}).round(2)

# Creazione del grafico combinato

fig, ax1 = plt.subplots(figsize=(8, 5))

# --- Barre: incasso medio per categoria ---

ax1.bar(analisi_categorie.index, analisi_categorie["Incasso"], color="cornflowerblue", alpha=0.7, label="Incasso medio (€)")
ax1.set_xlabel("Categoria", fontsize=12, fontweight="bold")
ax1.set_ylabel("Incasso medio (€)", color="cornflowerblue", fontsize=12, fontweight="bold")
ax1.tick_params(axis="y", labelcolor="cornflowerblue")

# --- Linea: quantità media per categoria ---

ax2 = ax1.twinx()
ax2.plot(analisi_categorie.index, analisi_categorie["Quantità"], color="darkorange", marker="o", linewidth=2, label="Quantità media")
ax2.set_ylabel("Quantità media", color="darkorange", fontsize=12, fontweight="bold")
ax2.tick_params(axis="y", labelcolor="darkorange")

# Titolo e legenda

plt.title("Confronto 'Incasso medio' e 'Quantità media' per categoria", fontsize=14, fontweight="bold")

# Gestione legende doppio asse

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc="lower left")

# Mostra il grafico

plt.tight_layout()
plt.show()

# Funzione che restituisce i 'n' prodotti più venduti in termini di incasso totale

def top_n_prodotti(n):
    incasso_per_prodotto = df.groupby("Prodotto")["Incasso"].sum()
    top_prodotti = incasso_per_prodotto.sort_values(ascending=False).head(n)
    return top_prodotti

# Test

print("\nI prodotti più venduti sono:\n")
print(top_n_prodotti(5))
