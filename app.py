import streamlit as st
import requests
import pandas as pd
from datetime import datetime

def get_weather_intervals(temperature_seuil):
    """Récupère les intervalles de temps où les conditions sont remplies"""
    # Coordonnées géographiques (Cherbourg)
    latitude = 49.6386
    longitude = -1.6164

    # URL de l'API Open-Meteo
    url = "https://api.open-meteo.com/v1/ecmwf"

    # Paramètres de la requête
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,dewpoint_2m",
        "forecast_days": 16,
        "timezone": "auto"
    }

    # Récupérer les données
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Convertir en DataFrame Pandas
        df = pd.DataFrame(data['hourly'])
        df['time'] = pd.to_datetime(df['time'])  # Conversion des dates

        # Filtrer les conditions spécifiques
        condition = (df['temperature_2m'] >= temperature_seuil) & (df['dewpoint_2m'] <= df['temperature_2m'] - 3)
        result = df[condition]

        if not result.empty:
            # Identifier les créneaux consécutifs
            result = result.reset_index(drop=True)
            breaks = result.index[result['time'].diff() > pd.Timedelta(hours=1)].tolist()
            start_idx = 0
            intervals = []
            
            for break_idx in breaks + [len(result)]:
                créneau = result.iloc[start_idx:break_idx]
                début = créneau.iloc[0]
                fin = créneau.iloc[-1]
                
                interval = {
                    'date': début['time'].strftime('%d/%m/%Y'),
                    'debut_heure': début['time'].strftime('%Hh%M'),
                    'debut_temp': début['temperature_2m'],
                    'debut_rosee': début['dewpoint_2m'],
                    'fin_heure': fin['time'].strftime('%Hh%M'),
                    'fin_temp': fin['temperature_2m'],
                    'fin_rosee': fin['dewpoint_2m']
                }
                intervals.append(interval)
                start_idx = break_idx
                
            return intervals
        else:
            return []
    else:
        st.error(f"Erreur lors de la récupération des données : {response.text}")
        return []

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Prévisions Météo Cherbourg",
    page_icon="🌡️",
    layout="wide"
)

# Titre de l'application
st.title("🌡️ Prévisions Météo - Cherbourg")
st.subheader("Détection des créneaux favorables")

# Sélection de la température
temperature = st.selectbox(
    "Choisissez la température minimale",
    options=[5, 10],
    format_func=lambda x: f"{x}°C"
)

# Bouton pour lancer l'analyse
if st.button("Analyser les prévisions"):
    with st.spinner("Récupération des données en cours..."):
        intervals = get_weather_intervals(temperature)
        
    if intervals:
        st.success(f"Créneaux trouvés où T° ≥ {temperature}°C et point de rosée ≤ T°-3°C")
        
        for interval in intervals:
            with st.expander(f"Créneau du {interval['date']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Début du créneau :")
                    st.write(f"🕒 {interval['debut_heure']}")
                    st.write(f"🌡️ {interval['debut_temp']:.1f}°C")
                    st.write(f"💧 {interval['debut_rosee']:.1f}°C")
                with col2:
                    st.write("Fin du créneau :")
                    st.write(f"🕒 {interval['fin_heure']}")
                    st.write(f"🌡️ {interval['fin_temp']:.1f}°C")
                    st.write(f"💧 {interval['fin_rosee']:.1f}°C")
    else:
        st.warning(f"Aucun créneau trouvé pour {temperature}°C")

# Informations complémentaires
with st.sidebar:
    st.info("""
    Cette application utilise :
    - L'API Open-Meteo (modèle ECMWF)
    - Les coordonnées de Cherbourg (49.6386°N, -1.6164°E)
    - Des prévisions sur 16 jours
    """)
