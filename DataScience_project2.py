"""
Progetto #2 — Analisi vendite realistica

Traccia:
Sei un data analyst in un'azienda di e-commerce. Ti vengono forniti:
- Un CSV con ordini clienti (ordini.csv) .
- Un JSON con informazioni prodotto (prodotti.json).
- Un CSV con dati clienti (clienti.csv).
Questo progetto simula una situazione reale in cui occorre integrare fonti dati multiple,
ottimizzare memoria, applicare filtri complessi, aggregazioni avanzate e serializzazione
efficiente, come capita quotidianamente in un contesto lavorativo di Data Analyst o
Business Intelligence.

Consegna

Parte 1 - Crea i seguenti DataSet

1. Ordini.csv: 100.000 righe con ClienteID, ProdottoID, Quantità e DataOrdine.
2. prodotti.json: 20 prodotti con Categoria e Fornitore.
3. clienti.csv: 5.000 clienti con Regione e Segmento.

Parte 2 - Creare un DataFrame unificato

4. Unisci ordini.
5. Unisci prodotti.
6. Unisci clienti

Parte 3 - Ottimizzazione

7. Ottimizzare i tipi di dato.
8. Ottimizzare l'uso della memoria.

Parte 4 - Creare colonne e filtra i dati

9. Crea una colonna calcolata (ValoreTotale = Prezzo * Quantità).
10. Filtrare ordini con ValoreTotale > 100 e clienti
"""

import pandas as pd
import numpy as np

# Seed per riproducibilità
np.random.seed(42)

#---------------------------------#
# PARTE 1 - Creazione dei DataSet #
#---------------------------------#

# Ordini.csv: 100.000 righe con ClienteID, ProdottoID, Quantità e DataOrdine
ordini = pd.DataFrame({
    "ordine_id": range(1, 100_001),
    "cliente_id": np.random.randint(1, 5001, 100_000),
    "prodotto_id": np.random.randint(1, 21, 100_000),
    "quantita": np.random.randint(1, 6, 100_000),
    "data_ordine": pd.to_datetime("2025-01-01") +
                   pd.to_timedelta(np.random.randint(0, 365, 100_000), unit="D")
})

ordini.to_csv("ordini.csv", index=False)

# prodotti.json: 20 prodotti con Categoria e Fornitore
prodotti = pd.DataFrame({
    "prodotto_id": range(1, 21),
    "categoria": np.random.choice(["Elettronica", "Casa", "Sport", "Moda"], 20),
    "fornitore": np.random.choice(["Fornitore_A", "Fornitore_B", "Fornitore_C"], 20),
    "prezzo": np.round(np.random.uniform(10, 500, 20), 2)
})

prodotti.to_json("prodotti.json", orient="records")

# clienti.csv: 5.000 clienti con Regione e Segmento
clienti = pd.DataFrame({
    "cliente_id": range(1, 5001),
    "regione": np.random.choice(["Nord", "Centro", "Sud"], 5000),
    "segmento": np.random.choice(["Premium", "Standard"], 5000)
})

clienti.to_csv("clienti.csv", index=False)

# Lettura dati
ordini = pd.read_csv("ordini.csv", parse_dates=["data_ordine"])
clienti = pd.read_csv("clienti.csv")
prodotti = pd.read_json("prodotti.json")


#-----------------------------------------------#
# PARTE 2 - Creazione di un DataFrame unificato #
#-----------------------------------------------#

# Merge multipli su: Ordini, Prodotti e Clienti
df = ordini.merge(clienti, on="cliente_id", how="left")
df = df.merge(prodotti, on="prodotto_id", how="left")



#--------------------------#
# PARTE 3 - Ottimizzazione #
#--------------------------#

df["ordine_id"] = df["ordine_id"].astype("int32")
df["cliente_id"] = df["cliente_id"].astype("int32")
df["prodotto_id"] = df["prodotto_id"].astype("int8")
df["quantita"] = df["quantita"].astype("int16")
df["prezzo"] = df["prezzo"].astype("float32")

for col in ["regione", "segmento", "categoria", "fornitore"]:
    df[col] = df[col].astype("category")

# Memoria utilizzata
print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")


#---------------------------------------------------#
# PARTE 4 - Creazione colonne e filtraggio dei dati #
#---------------------------------------------------#

# Nuova colonna calcolata "valore_totale"
df["valore_totale"] = df["prezzo"] * df["quantita"]

# Filtro: clienti Premium con valore_totale > 100
filtered = df[(df["segmento"] == "Premium") & (df["valore_totale"] > 100)]



#-------#
# EXTRA #
#-------#

# Aggregazioni avanzate
vendite_regione = (
    filtered
    .groupby(["categoria", "regione"])
    .agg(
        totale_vendite=("valore_totale", "sum"),
        prezzo_medio=("prezzo", "mean"),
        numero_ordini=("ordine_id", "count")
    )
    .reset_index()
    .sort_values(by="totale_vendite", ascending=False)
)

# Stampa del risultato
print(vendite_regione)

# Serializzazione efficiente con Parquet
filtered.to_parquet("vendite_premium.parquet", index=False)
print("Report filtrato salvato in Parquet")

# Salvataggio report finale CSV
vendite_regione.to_csv("vendite_regione_premium.csv", index=False)
print("Report aggregato salvato in CSV")
