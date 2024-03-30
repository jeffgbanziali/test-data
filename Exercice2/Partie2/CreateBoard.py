from numpy import fix
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Chargement des données
df_residences = pd.read_csv('../DataGenerate/donnees_residences.csv')
df_ecoles = pd.read_csv('../DataGenerate/donnees_ecoles.csv')
df_arrivees = pd.read_csv('../DataGenerate/donnees_arrivees.csv')
df_departs = pd.read_csv('../DataGenerate/donnees_departs.csv')

# Création des visualisations
fig_occupation = go.Bar(x=df_residences['ID_Residence'], y=df_residences['Taux_Occupation'], name='Taux d\'occupation')
fig_revenu = go.Bar(x=df_residences['ID_Residence'], y=df_residences['Revenu_Mensuel'], name='Revenu mensuel')
fig_lits = go.Bar(x=df_residences['ID_Residence'], y=df_residences['Nb_Lits'], name='Nombre de lits')

ecoles_counts = df_ecoles['Type_Ecole'].value_counts()
fig_ecoles = go.Bar(x=ecoles_counts.index, y=ecoles_counts.values, name='Nombre d\'écoles', marker=dict(color='orange'))

arrivees_counts = df_arrivees['Date_Arrivee'].value_counts().sort_index()
departs_counts = df_departs['Date_Depart'].value_counts().sort_index()

# Création des traces Scatter pour les arrivées et les départs
fig_arrivees = go.Scatter(x=arrivees_counts.index, y=arrivees_counts.values, mode='lines', name='Arrivées', line=dict(color='blue'))
fig_departs = go.Scatter(x=departs_counts.index, y=departs_counts.values, mode='lines', name='Départs', line=dict(color='red'))

# Création du tableau de bord
fig = make_subplots(rows=3, cols=2, subplot_titles=('Taux d\'occupation des résidences', 'Revenu mensuel des résidences', 'Nombre de lits par résidence', 'Nombre d\'écoles par type', 'Arrivées par jour', 'Départs par jour'), vertical_spacing=0.3, horizontal_spacing=0.2)

# Ajout des traces aux sous-graphiques
fig.add_trace(fig_occupation, row=1, col=1)
fig.add_trace(fig_revenu, row=1, col=2)
fig.add_trace(fig_lits, row=2, col=1)
fig.add_trace(fig_ecoles, row=2, col=2)
fig.add_trace(fig_arrivees, row=3, col=1)
fig.add_trace(fig_departs, row=3, col=2)  # Ajout du graphique des départs au subplot séparé

# Mise en forme du titre et des axes
fig.update_layout(title='Tableau de Bord de l\'activité des résidences KLEY', showlegend=True)

fig.update_xaxes(title_text='Résidence', row=1, col=1)
fig.update_yaxes(title_text='Taux d\'occupation', row=1, col=1)

fig.update_xaxes(title_text='Résidence', row=1, col=2)
fig.update_yaxes(title_text='Revenu mensuel', row=1, col=2)

fig.update_xaxes(title_text='Résidence', row=2, col=1)
fig.update_yaxes(title_text='Nombre de lits', row=2, col=1)

fig.update_xaxes(title_text='Type d\'école', row=2, col=2)
fig.update_yaxes(title_text='Nombre d\'écoles', row=2, col=2)

fig.update_xaxes(title_text='Date', row=3, col=1)
fig.update_yaxes(title_text='Nombre Arrivées', row=3, col=1)

fig.update_xaxes(title_text='Date', row=3, col=2)
fig.update_yaxes(title_text='Nombre Départs', row=3, col=2)

# Affichage du tableau de bord
fig.show()

