import requests
import pandas as pd
from datetime import datetime
import sys

# Configuration de l'encodage pour la sortie console
sys.stdout.reconfigure(encoding='utf-8')

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
    condition = (df['temperature_2m'] >= 5) & (df['dewpoint_2m'] <= df['temperature_2m'] - 3)
    result = df[condition]

    # Afficher les résultats
    if not result.empty:
        print("\nPrévisions ECMWF - Créneaux où T° ≥ 5°C et point de rosée ≤ T°-3°C")
        print("================================================================")
        
        # Identifier les créneaux consécutifs
        result = result.reset_index(drop=True)
        breaks = result.index[result['time'].diff() > pd.Timedelta(hours=1)].tolist()
        start_idx = 0
        
        for break_idx in breaks + [len(result)]:
            créneau = result.iloc[start_idx:break_idx]
            début = créneau.iloc[0]
            fin = créneau.iloc[-1]
            
            print(f"\nCréneau du {début['time'].strftime('%d/%m/%Y')}:")
            print(f"  De  {début['time'].strftime('%Hh%M')} : {début['temperature_2m']:4.1f}°C (rosée: {début['dewpoint_2m']:4.1f}°C)")
            print(f"  À   {fin['time'].strftime('%Hh%M')} : {fin['temperature_2m']:4.1f}°C (rosée: {fin['dewpoint_2m']:4.1f}°C)")
            
            start_idx = break_idx
    else:
        print("\nAucune correspondance trouvée pour 5°C avec ECMWF.")
else:
    print("Erreur lors de la récupération des données :", response.text)
