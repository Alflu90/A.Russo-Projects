# Introduzione

# L’obiettivo è lavorare su un dataset di vendite storiche per capire la struttura dei dati, 
# pulirli, analizzarli e realizzare previsioni semplici dei prossimi giorni usando Pandas e Python puro.

# Gli step principali:
# - Caricamento e esplorazione dati
# - Pulizia
# - Analisi esplorativa
# - Raggruppamenti e aggregazioni
# - Implementazione di due previsioni semplici
# - Confronto tra previsioni
# - Output richiesti

# Parte 1 – Caricamento e esplorazione dati
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulazione dataset vendite storiche
data = {
    "Data": pd.date_range(start="2024-01-01", periods=30),
    "Prodotto": ["A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C"],
    "Vendite": [10, 5, 2, 12, 6, 3, np.nan, 7, 4, 11, 5, 2, 13, 6, 3, 14, 7, 4, 12, 5, 2, 13, 6, 3, 10, 5, 2, 12, 6, 3],
    "Prezzo": [100, 150, 200, 100, 150, 200, 100, 150, 200, 100, 150, 200, 100, 150, 200, 100, 150, 200, 100, 150, 200, 100, 150, 200, 100, 150, 200, 100, 150, 200]
}

df = pd.DataFrame(data)

# Visualizzare prime righe
print(df.head())

# Informazioni sul dataset
print(df.info())

# Statistiche descrittive
print(df.describe())


# Spiegazione:

# head() mostra le prime righe per avere un’idea dei dati.
# info() verifica tipi e valori mancanti.
# describe() calcola medie, minimi, massimi, std delle colonne numeriche.


# Parte 2 – Pulizia dati

# Gestione valori mancanti
df["Vendite"] = df["Vendite"].fillna(df["Vendite"].mean())

# Rimuovere duplicati
df = df.drop_duplicates()

# Controllo tipi dati
df["Data"] = pd.to_datetime(df["Data"])
df["Vendite"] = df["Vendite"].astype(float)
df["Prezzo"] = df["Prezzo"].astype(float)

print(df.info())


# Spiegazione:

# Valori mancanti in “Vendite” sostituiti con media.
# Duplicati rimossi per evitare distorsioni.
# Assicurato che le date siano datetime e le quantità numeriche.


# Parte 3 – Analisi esplorativa

# Vendite totali per prodotto
totali_per_prodotto = df.groupby("Prodotto")["Vendite"].sum()
print(totali_per_prodotto)

# Prodotto più e meno venduto
print("Prodotto più venduto:", totali_per_prodotto.idxmax())
print("Prodotto meno venduto:", totali_per_prodotto.idxmin())

# Vendite medie giornaliere
medie_giornaliere = df.groupby("Data")["Vendite"].sum()
print(medie_giornaliere)


# Spiegazione:

# groupby aggrega le vendite per prodotto.
# idxmax() e idxmin() identificano i prodotti con vendite estreme.
# groupby("Data") calcola la media giornaliera delle vendite totali.


# Parte 4 – Raggruppamenti e aggregazioni

# Vendite mensili
df["Mese"] = df["Data"].dt.to_period("M")
vendite_mensili = df.groupby("Mese")["Vendite"].sum()
print(vendite_mensili)

# Visualizzare trend
vendite_mensili.plot(kind="bar", title="Vendite mensili totali")
plt.ylabel("Vendite")
plt.show()


# Spiegazione:

# Aggiunta colonna “Mese” per aggregare per mese.
# Grafico a barre semplice mostra trend mensile.


# Parte 5 – Previsioni di base

# Metodo 1: media storica
media_storica = df["Vendite"].mean()
print("Previsione media storica:", media_storica)

# Metodo 2: ultimo valore osservato
ultimo_valore = df["Vendite"].iloc[-1]
print("Previsione ultimo valore osservato:", ultimo_valore)

# Applicazione su 7 giorni futuri
future_days = pd.date_range(start=df["Data"].max() + pd.Timedelta(days=1), periods=7)

previsione_media = pd.DataFrame({
    "Data": future_days,
    "Vendite_Prev_Media": [media_storica]*7
})

previsione_ultimo = pd.DataFrame({
    "Data": future_days,
    "Vendite_Prev_Ultimo": [ultimo_valore]*7
})

print(previsione_media)
print(previsione_ultimo)


# Spiegazione:

# La previsione media storica assume che le vendite future siano simili alla media passata.
# La previsione ultimo valore osservato assume che le vendite rimangano costanti come nell’ultimo giorno.


# Parte 6 – Confronto previsioni

plt.figure(figsize=(10,6))
plt.plot(df["Data"], df["Vendite"], label="Storico")
plt.plot(previsione_media["Data"], previsione_media["Vendite_Prev_Media"], label="Previsione Media", linestyle="--")
plt.plot(previsione_ultimo["Data"], previsione_ultimo["Vendite_Prev_Ultimo"], label="Previsione Ultimo Valore", linestyle="--")
plt.title("Confronto previsioni vendite")
plt.xlabel("Data")
plt.ylabel("Vendite")
plt.legend()
plt.grid(True)
plt.show()


# Spiegazione:

# Visualizza vendite storiche e previsioni su 7 giorni futuri.
# Permette di confrontare i due metodi e capire quale è più coerente col trend osservato.


# Parte 7 – Output richiesti

# Notebook commentato: ogni cella con spiegazione.

# Tabelle: aggregazioni per prodotto, vendite giornaliere e mensili, previsioni.

# Grafici: trend storici e confronto previsioni.

# Breve relazione (max 1 pagina) con:

# - Descrizione dataset e pulizia
# - Logica delle previsioni
# - Riflessi sul confronto delle due metodologie
