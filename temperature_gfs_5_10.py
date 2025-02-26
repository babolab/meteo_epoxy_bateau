import requests
import pandas as pd
from datetime import datetime
import sys

# Configuration de l'encodage pour la sortie console
sys.stdout.reconfigure(encoding='utf-8')

# Coordonnées géographiques (Cherbourg)
latitude = 49.6386
longitude = -1.6164

# URL de l'API Open-Meteo avec le modèle GFS
url = "https://api.open-meteo.com/v1/gfs"

# Paramètres de la requête
params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m,dewpoint_2m",
    "forecast_days": 16,  # GFS peut offrir des prévisions jusqu'à 16 jours
    "timezone": "auto"
}

# Récupérer les données
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # Convertir en DataFrame Pandas
    df = pd.DataFrame(data['hourly'])
    df['time'] = pd.to_datetime(df['time'])  # Conversion des dates

    # Filtrer les conditions pour 5°C
    condition_5 = (df['temperature_2m'] >= 5) & (df['dewpoint_2m'] == df['temperature_2m'] - 3)
    result_5 = df[condition_5]

    # Filtrer les conditions pour 10°C
    condition_10 = (df['temperature_2m'] >= 10) & (df['dewpoint_2m'] == df['temperature_2m'] - 3)
    result_10 = df[condition_10]

    # Afficher les résultats pour 5°C
    print("\nPrévisions GFS - Température 5°C:")
    print("================================")
    if not result_5.empty:
        print(result_5[['time', 'temperature_2m', 'dewpoint_2m']].to_string(index=False))
    else:
        print("Aucune correspondance trouvée pour 5°C avec GFS.")

    # Afficher les résultats pour 10°C
    print("\nPrévisions GFS - Température 10°C:")
    print("=================================")
    if not result_10.empty:
        print(result_10[['time', 'temperature_2m', 'dewpoint_2m']].to_string(index=False))
    else:
        print("Aucune correspondance trouvée pour 10°C avec GFS.")
else:
    print("Erreur lors de la récupération des données :", response.text)
