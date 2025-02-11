import requests
import pandas as pd
import matplotlib.pyplot as plt
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

    # Filtrer les conditions spécifiques pour 5°C et 10°C
    condition_5 = (df['temperature_2m'] == 5) & (df['dewpoint_2m'] == df['temperature_2m'] - 3)
    condition_10 = (df['temperature_2m'] == 10) & (df['dewpoint_2m'] == df['temperature_2m'] - 3)

    result_5 = df[condition_5]
    result_10 = df[condition_10]

    # Tracer les résultats
    plt.figure(figsize=(12, 6))
    if not result_5.empty:
        plt.plot(result_5['time'], result_5['temperature_2m'], 'o', label="Température 5°C")
    if not result_10.empty:
        plt.plot(result_10['time'], result_10['temperature_2m'], 'x', label="Température 10°C")

    # Ajouter des détails au graphique
    plt.title("Conditions de température et de point de rosée")
    plt.xlabel("Temps")
    plt.ylabel("Température (°C)")
    plt.legend()
    plt.grid()

    # Afficher le graphique
    plt.show()
else:
    print("Erreur lors de la récupération des données :", response.text)
