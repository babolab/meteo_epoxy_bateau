import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL de la page à scraper
url = "https://www.meteolafleche.com/previsionsmodeles"

# Effectuer la requête HTTP
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extraire les données pertinentes
# (Ceci est un exemple, l'extraction réelle dépendra de la structure HTML de la page)
# Supposons que les données de température et d'humidité soient dans des balises spécifiques
temperature_data = soup.find_all('span', class_='temperature')
humidity_data = soup.find_all('span', class_='humidity')

# Convertir les données en DataFrame
data = {
    'temperature': [float(temp.get_text()) for temp in temperature_data],
    'humidity': [float(hum.get_text()) for hum in humidity_data]
}
df = pd.DataFrame(data)

# Filtrer les conditions spécifiques
condition = (df['temperature'] == 10) & (df['humidity'] < 50)
result = df[condition]

# Afficher les résultats
if not result.empty:
    print("Périodes où la température est de 10°C avec une faible humidité :")
    print(result)
else:
    print("Aucune correspondance trouvée pour les conditions spécifiées.")
