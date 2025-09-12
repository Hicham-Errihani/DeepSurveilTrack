# dashboard_list.py

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="DeepSurveilTrack – Liste des événements",
    layout="wide"
)

st.title("📋 DeepSurveilTrack – Liste des événements")

# 1) Choix du mode de chargement
use_csv = st.checkbox("Charger un CSV local", value=False)
if use_csv:
    uploaded = st.file_uploader("👉 Déposez votre fichier CSV ici", type="csv")
    if uploaded is None:
        st.info("Aucun CSV chargé, attendez ou décochez l'option.")
        st.stop()
    df = pd.read_csv(uploaded, parse_dates=["timestamp"])
else:
    # Génère quelques événements factices
    dates = pd.date_range(datetime.today(), periods=5, freq="T")
    df = pd.DataFrame({
        "timestamp": dates,
        "type":      ["Mouvement rapide détecté"] * len(dates),
        "camera":    [f"CAM_{i+1:02d}" for i in range(len(dates))],
        "score":     [round(50+50*i/len(dates),1) for i in range(len(dates))]
    })

# 2) Affiche la liste
st.subheader(f"{len(df)} événements chargés")
st.dataframe(df, use_container_width=True)

# 3) Optionnel : afficher chaque événement en détail avec un expander
for idx, row in df.iterrows():
    with st.expander(f"Événement #{idx+1} – {row['timestamp']}"):
        st.write({
            "Horodatage": row["timestamp"],
            "Type": row["type"],
            "Caméra": row["camera"],
            "Score": f"{row['score']} %"
        })
