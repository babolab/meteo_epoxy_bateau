# Scripts de Prévision Météorologique

Ce projet contient plusieurs scripts Python pour analyser les prévisions météorologiques à Cherbourg (49.6386°N, -1.6164°E) en utilisant l'API Open-Meteo.

## Scripts disponibles

### Détection de conditions spécifiques

- `temperature_5.py` : Détecte quand la température est de 5°C avec un point de rosée 3°C plus bas
- `script_temperature_0.py` : Détecte quand la température est de 0°C avec un point de rosée 3°C plus bas
- `script_temperature_10.py` : Détecte quand la température est de 10°C avec un point de rosée 3°C plus bas

### Visualisation des données

- `plot_temperature_conditions.py` : Génère un graphique des températures et points de rosée sur 15 jours en utilisant le modèle ECMWF
- `long_term_forecast.py` : Génère un graphique similaire mais sur 16 jours en utilisant le modèle GFS

## Fonctionnalités communes

Tous les scripts :
- Utilisent l'API Open-Meteo (ECMWF ou GFS)
- Récupèrent les données de température et point de rosée
- Utilisent pandas pour le traitement des données
- Incluent la gestion des erreurs de l'API

## Dépendances

- requests
- pandas
- matplotlib (pour les scripts de visualisation)

## Utilisation

Exécutez chaque script individuellement selon vos besoins d'analyse. Les scripts de détection afficheront les résultats dans la console, tandis que les scripts de visualisation généreront des graphiques.
