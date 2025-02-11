import requests
import pandas as pd
from datetime import datetime

# Coordonnées géographiques (La Mare)
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
    # Afficher le résultat brut de la requête API
    print("Résultat brut de la requête API :")
    print(data)
else:
    print("Erreur lors de la récupération des données :", response.text)
