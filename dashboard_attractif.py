import os
import streamlit as st
import pandas as pd
import altair as alt

# --- Configuration de la page ---
st.set_page_config(
    page_title="DeepSurveilTrack Dashboard", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Titre principal ---
st.title("📋 DeepSurveilTrack – Liste et analyses des événements")

# --- Sidebar pour les filtres ---
st.sidebar.header("🔧 Filtres")
use_local = st.sidebar.checkbox("Charger un CSV local", value=True)
uploaded_file = None
if use_local:
    uploaded_file = st.sidebar.file_uploader(
        "Déposez votre CSV (timestamp,type,description,camera)", 
        type=["csv"]
    )

max_lines = st.sidebar.slider("Lignes max à afficher", 10, 1000, 100)
start_date = st.sidebar.date_input("Date début")
end_date   = st.sidebar.date_input("Date fin")

if st.sidebar.button("▶️ Charger"):
    # -- Lecture du CSV (uploadé ou fallback local) --
    if use_local and uploaded_file is not None:
        df = pd.read_csv(uploaded_file, parse_dates=["timestamp"])
    elif os.path.exists("events.csv"):
        df = pd.read_csv("events.csv", parse_dates=["timestamp"])
        st.info("ℹ️ Chargé `events.csv` depuis le dossier courant")
    else:
        st.error("🚨 Aucun CSV sélectionné ni trouvé en local (events.csv).")
        st.stop()

    # -- Filtrage par date et nombre de lignes --
    mask = (
        (df["timestamp"].dt.date >= start_date) &
        (df["timestamp"].dt.date <= end_date)
    )
    df = df.loc[mask].head(max_lines)

    if df.empty:
        st.warning("⚠️ Aucun événement trouvé pour ces critères.")
        st.stop()

    # -- Affichage de la liste --
    st.success(f"✅ {len(df)} événements de `{start_date}` à `{end_date}`")
    st.dataframe(df, use_container_width=True)

    # -- Préparation des dates/heures pour les graphiques --
    df["hour"] = df["timestamp"].dt.floor("H")

    # -- Section Analyses visuelles sur une seule page --
    st.markdown("## 📊 Analyses visuelles")
    col1, col2, col3 = st.columns(3)

    # 1) Répartition par type
    types = df["type"].unique().tolist()
    color_scale1 = alt.Scale(domain=types,
                             range=["#E74C3C","#3498DB","#F1C40F","#2ECC71"][:len(types)])
    chart1 = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("type:N", sort="-y", title="Type d'événement"),
            y=alt.Y("count()", title="Nombre"),
            color=alt.Color("type:N", scale=color_scale1, legend=None),
            tooltip=["type","count()"]
        )
        .properties(title="Répartition par type", height=300)
    )
    col1.altair_chart(chart1, use_container_width=True)

    # 2) Événements par caméra
    cams = df["camera"].unique().tolist()
    color_scale2 = alt.Scale(domain=cams,
                             range=["#F1948A","#3498DB","#E74C3C","#85C1E9","#2ECC71"][:len(cams)])
    chart2 = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("camera:N", sort="-y", title="Caméra"),
            y=alt.Y("count()", title="Nombre"),
            color=alt.Color("camera:N", scale=color_scale2, legend=None),
            tooltip=["camera","count()"]
        )
        .properties(title="Événements par caméra", height=300)
    )
    col2.altair_chart(chart2, use_container_width=True)

    # 3) Évolution horaire
    chart3 = (
        alt.Chart(df)
        .mark_line(point=True, strokeWidth=2)
        .encode(
            x=alt.X("hour:T", title="Heure"),
            y=alt.Y("count()", title="Nombre"),
            tooltip=[alt.Tooltip("hour:T", title="Heure"), alt.Tooltip("count()", title="Nombre")]
        )
        .properties(title="Évolution horaire", height=300)
    )
    col3.altair_chart(chart3, use_container_width=True)

    # -- Bouton d’export CSV --
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Exporter CSV",
        data=csv,
        file_name="events_export.csv",
        mime="text/csv"
    )
