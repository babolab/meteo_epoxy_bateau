# Prévisions Météorologiques - Cherbourg

Ce projet contient une collection de scripts Python pour analyser les prévisions météorologiques à Cherbourg (49.6386°N, -1.6164°E) en utilisant l'API Open-Meteo.

## Description

Le projet utilise deux modèles de prévision différents :
- ECMWF (European Centre for Medium-Range Weather Forecasts)
- GFS (Global Forecast System)

## Scripts disponibles

### Scripts de détection de conditions spécifiques

Ces scripts recherchent des créneaux horaires où la température et le point de rosée respectent des conditions particulières :
- `temperature_5.py` : Température ≥ 5°C avec point de rosée ≤ T°-3°C
- `script_temperature_0.py` : Température ≥ 0°C avec point de rosée ≤ T°-3°C
- `script_temperature_10.py` : Température ≥ 10°C avec point de rosée ≤ T°-3°C

Chaque script affiche les créneaux trouvés avec :
- La date
- L'heure de début et de fin
- Les températures et points de rosée correspondants

### Scripts de visualisation

- `plot_temperature_conditions.py` : Graphique sur 15 jours (modèle ECMWF)
- `long_term_forecast.py` : Graphique sur 16 jours (modèle GFS)

Les graphiques montrent l'évolution :
- De la température à 2m du sol
- Du point de rosée

## Installation

1. Cloner le repository
2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

Chaque script peut être exécuté individuellement :
```bash
python temperature_5.py
python long_term_forecast.py
```

Les scripts de détection affichent les résultats dans la console.
Les scripts de visualisation ouvrent une fenêtre avec le graphique généré.

## Dépendances

Voir le fichier `requirements.txt` pour la liste complète des dépendances et leurs versions.

## Notes techniques

- Utilisation de l'API gratuite Open-Meteo
- Données horaires de température et point de rosée
- Prévisions jusqu'à 16 jours
- Traitement des données avec pandas
- Visualisation avec matplotlib
