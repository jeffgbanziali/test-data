import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Constantes
NB_RESIDENCES = 27
NB_LITS_TOTAL = 5000
NB_ECOLES = 900
DATE_DEBUT = datetime(2024, 5, 1)
DATE_FIN = datetime(2024, 12, 31)
TYPES_ECOLES = ['Université', 'École de Commerce', 'École Spécialisée', 'IUT', 'BTS']
TYPES_LOGEMENT = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']
PERIODE_ARRIVEES = pd.date_range(start=DATE_DEBUT, end=DATE_FIN, freq='D')
PERIODE_DEPARTS = pd.date_range(start=DATE_DEBUT, end=DATE_FIN, freq='D')

# Génération des données sur les résidences
residences = []
for i in range(NB_RESIDENCES):
    residence = {
        'ID_Residence': f'Residence_{i+1}',
        'Taux_Occupation': round(random.uniform(0.6, 0.95), 2),
        'Revenu_Mensuel': round(random.uniform(50000, 150000), 2),
        'Nb_Lits': random.randint(50, 300)
    }
    residences.append(residence)

# Génération des données sur les écoles
ecoles = []
for _ in range(NB_ECOLES):
    ecole = {
        'ID_Ecole': f'Ecole_{_+1}',
        'Type_Ecole': random.choice(TYPES_ECOLES)
    }
    ecoles.append(ecole)

# Génération des données sur les arrivées et départs
arrivees = []
departs = []
for date in PERIODE_ARRIVEES:
    for _ in range(random.randint(10, 30)):
        arrivees.append({'Date_Arrivee': date, 'ID_Residence': random.choice(residences)['ID_Residence']})
for date in PERIODE_DEPARTS:
    for _ in range(random.randint(5, 20)):
        departs.append({'Date_Depart': date, 'ID_Residence': random.choice(residences)['ID_Residence']})

# Création des DataFrames
df_residences = pd.DataFrame(residences)
df_ecoles = pd.DataFrame(ecoles)
df_arrivees = pd.DataFrame(arrivees)
df_departs = pd.DataFrame(departs)

# Sauvegarde des données dans des fichiers CSV
df_residences.to_csv('../DataGenerate/donnees_residences.csv', index=False)
df_ecoles.to_csv('../DataGenerate/donnees_ecoles.csv', index=False)
df_arrivees.to_csv('../DataGenerate/donnees_arrivees.csv', index=False)
df_departs.to_csv('../DataGenerate/donnees_departs.csv', index=False)
