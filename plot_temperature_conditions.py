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

    # Tracer les températures et le point de rosée
    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df['temperature_2m'], label="Température (°C)")
    plt.plot(df['time'], df['dewpoint_2m'], label="Point de rosée (°C)")

    # Ajouter des détails au graphique
    plt.title("Températures et point de rosée sur les 15 prochains jours")
    plt.xlabel("Temps")
    plt.ylabel("Température (°C)")
    plt.legend()
    plt.grid()

    # Afficher le graphique
    plt.show()
else:
    print("Erreur lors de la récupération des données :", response.text)
