import csv
import subprocess

subprocess.run(['python3', '../parse_data.py'])

# Variables pour stocker les données spécifiques à l'URL "https://www.f2pool.com/coin/kaspa"
difficulte_reseau = 0.0
cours_crypto = 0.0
recompense_bloc = 0.0

# Lire les valeurs du fichier CSV pour l'URL spécifique
def lire_valeurs_csv():
    global difficulte_reseau, cours_crypto, recompense_bloc
    with open('../mining_data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['URL'] == 'https://www.f2pool.com/coin/kaspa':
                try:
                    difficulte_reseau = float(row['Difficulty'])
                    cours_crypto = float(row['Price'])
                    recompense_bloc = float(row['Block Reward'])
                except ValueError as e:
                    print(f"Erreur de conversion des données : {e}")
                break

# Appeler la fonction pour lire les valeurs du CSV
lire_valeurs_csv()

def calculer_rentabilite(hashrate, consommation_electrique, cout_machine, difficulte_reseau,
                         recompense_bloc, cours_crypto, cout_electricite):

    # Calcul du revenu quotidien
    hashrate_hs = hashrate * 1e14
    revenu_quotidien_btc = (hashrate_hs / difficulte_reseau) * recompense_bloc
    revenu_quotidien = (revenu_quotidien_btc * cours_crypto) * (90/100)

    # Calcul des coûts quotidiens
    consommation_quotidienne_kwh = (consommation_electrique * 24) / 1000
    couts_quotidiens = consommation_quotidienne_kwh * cout_electricite

    # Calcul du profit quotidien
    profit_quotidien = revenu_quotidien - couts_quotidiens

    # Calcul du retour sur investissement (en jours)
    retour_investissement = cout_machine / profit_quotidien if profit_quotidien > 0 else float('inf')

    return revenu_quotidien, couts_quotidiens, profit_quotidien, retour_investissement

# Données de votre machine (à compléter)
hashrate = 8000  # mH/s
consommation_electrique = 3200  # W
cout_machine = 2300 # €
cout_electricite = 0.1  # €/kWh

# Conversion du cours de $ à € (taux de change approximatif)
cours_crypto_euros = cours_crypto * 0.95

revenu_quotidien, couts_quotidiens, profit_quotidien, retour_investissement = calculer_rentabilite(
    hashrate, consommation_electrique, cout_machine, difficulte_reseau,
    recompense_bloc, cours_crypto_euros, cout_electricite
)

# Affichage des résultats
print(f"Revenu quotidien: {revenu_quotidien:.2f} €")
print(f"Coûts quotidiens: {couts_quotidiens:.2f} €")
print(f"Profit quotidien: {profit_quotidien:.2f} €")
print(f"Retour sur investissement: {retour_investissement:.2f} jours")
