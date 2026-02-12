"""
TITOLO PROGETTO
---------------
Analisi delle Vendite e della Profittabilità con Visualizzazione Geospaziale (Italia)

AUTORE
------
Alfio Russo

DESCRIZIONE
-----------
Questo progetto mostra un flusso completo di Data Analysis, partendo dalla gestione dei dati grezzi 
fino alla visualizzazione avanzata.
L'obiettivo è analizzare vendite e profitti di un negozio online e rappresentare i risultati 
sia con grafici tradizionali sia con una mappa interattiva delle regioni italiane.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pathlib import Path
import json
import urllib.request

# Impostazione stile grafici statici
sns.set(style="whitegrid")

# Pathlib, per evitare errori di percorso
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "sales_data_italy.csv"
GEOJSON_PATH = BASE_DIR / "italy_regions.geojson"

# URL pubblico del file GeoJSON con i confini delle regioni italiane
GEOJSON_URL = (
    "https://raw.githubusercontent.com/openpolis/"
    "geojson-italy/master/geojson/limits_IT_regions.geojson"
)


# ======================= #
# 1) CARICAMENTO DEI DATI #
# ======================= #

"""
Il progetto supporta due casi:
1. Dataset reale disponibile (CSV)
2. Dataset non disponibile → generazione dati simulati realistici.
"""

try:
    df = pd.read_csv(DATA_PATH)
    print("Dataset reale caricato correttamente.")

except FileNotFoundError:
    print("Dataset non trovato. Generazione di dati simulati.")

    np.random.seed(42)

    regioni = [
        "Lombardia", "Lazio", "Veneto", "Campania", "Sicilia",
        "Piemonte", "Emilia-Romagna", "Toscana", "Puglia", "Calabria"
    ]

    date = pd.date_range("2021-01-01", "2023-12-31", freq="D")

    df = pd.DataFrame({
        "Order Date": np.random.choice(date, 800),
        "Ship Date": np.random.choice(date, 800),
        "Category": np.random.choice(["Furniture", "Office Supplies", "Technology"], 800),
        "Sub-Category": np.random.choice(["Chairs", "Tables", "Phones", "Binders", "Accessories"], 800),
        "Sales": np.random.uniform(50, 1500, 800),
        "Profit": np.random.uniform(-150, 500, 800),
        "Region": np.random.choice(regioni, 800),
        "Quantity": np.random.randint(1, 10, 800)
    })


# ========================================= #
# 2) PULIZIA DEI DATI E FEATURE ENGINEERING #
# ========================================= #

"""
In questa fase:
- convertiamo le colonne temporali
- rimuoviamo eventuali duplicati
- creiamo nuove variabili utili all'analisi
"""

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Rimozione duplicati per evitare conteggi errati
df = df.drop_duplicates()

# Estrazione dell'anno per analisi temporali
df["Year"] = df["Order Date"].dt.year

# Controllo qualità dati
print("\nAnteprima del dataset:")
print(df.head())

print("\nValori mancanti per colonna:")
print(df.isnull().sum())


# ===================================== #
# 3) ANALISI ESPLORATIVA DEI DATI (EDA) #
# ===================================== #

"""
L'EDA serve a comprendere l'andamento generale del business:
- performance nel tempo
- categorie più rilevanti
"""

# ------------------------------- #
# 3.1 Vendite e Profitti per Anno #
# ------------------------------- #

annual = (df.groupby("Year")[["Sales", "Profit"]].sum().reset_index())

plt.figure(figsize=(9,5))
sns.barplot(data=annual, x="Year", y="Sales", color="steelblue", label="Vendite")
sns.barplot(data=annual, x="Year", y="Profit", color="darkorange", label="Profitto")
plt.title("Vendite e Profitti Totali per Anno")
plt.ylabel("€")
plt.legend()
plt.tight_layout()
plt.show()

# ------------------------------------ #
# 3.2 Top 5 Sottocategorie per Vendite #
# ------------------------------------ #

top5 = (df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(5))

plt.figure(figsize=(8,5))
sns.barplot(x=top5.values, y=top5.index, hue=top5.index, palette="viridis", legend=False)
plt.title("Top 5 Sottocategorie per Vendite")
plt.xlabel("Vendite (€)")
plt.ylabel("Sottocategoria")
plt.tight_layout()
plt.show()


# ============================ #
# 4) GESTIONE DEL FILE GEOJSON #
# ============================ #

"""
Plotly non supporta nativamente le regioni italiane.
Per questo utilizziamo un file GeoJSON esterno, soluzione standard nelle visualizzazioni geospaziali professionali.
"""

if not GEOJSON_PATH.exists():
    print("File GeoJSON non trovato. Download in corso...")
    urllib.request.urlretrieve(GEOJSON_URL, GEOJSON_PATH)
    print("Download completato.")

with open(GEOJSON_PATH, "r", encoding="utf-8") as f:
    italy_geojson = json.load(f)


# ============================== #
# 5) VISUALIZZAZIONE GEOSPAZIALE #
# ============================== #

"""
La mappa permette di confrontare rapidamente le performance di vendita tra le diverse regioni italiane.
"""

region_sales = (df.groupby("Region")[["Sales", "Profit"]].sum().reset_index())

fig = px.choropleth(
    region_sales,
    geojson=italy_geojson,
    locations="Region",
    featureidkey="properties.reg_name",
    color="Sales",
    color_continuous_scale="Viridis",
    labels={"Sales": "Vendite (€)"},
    title="Vendite Totali per Regione - Italia"
)

fig.update_geos(fitbounds="locations",visible=False)
fig.update_layout(margin=dict(l=0, r=0, t=50, b=0))
fig.show()


# ============== #
# 6) CONCLUSIONI #
# ============== #

"""
Conclusioni:
- Il progetto mostra un flusso completo di analisi dei dati.
- Combina grafici statici e interattivi.
- L'uso del GeoJSON garantisce precisione geografica.
- Il codice è modulare, leggibile ed estendibile.

Possibili estensioni future:
- dashboard interattiva con Streamlit
- analisi di trend stagionali
- previsione delle vendite
"""

