import requests
import pandas as pd
from datetime import datetime

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
    condition = (df['temperature_2m'] >= 10) & (df['dewpoint_2m'] == df['temperature_2m'] - 3)
    result = df[condition]

    # Afficher les résultats
    if not result.empty:
        print("Jours et heures où la température est de 10°C et le point de rosée est de 3°C de moins :")
        print(result[['time', 'temperature_2m', 'dewpoint_2m']])
    else:
        print("Aucune correspondance trouvée pour les conditions spécifiées.")
else:
    print("Erreur lors de la récupération des données :", response.text)