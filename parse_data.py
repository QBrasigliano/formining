import requests
from bs4 import BeautifulSoup
import logging
import csv

# Configurer le logger
logging.basicConfig(filename='script.log', level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

# Liste des URLs à traiter
urls = [
    'https://www.f2pool.com/coin/kaspa',
    'https://www.f2pool.com/coin/bitcoin',
    'https://www.f2pool.com/coin/alephium'
]

# Ouvrir un fichier CSV pour écrire les données
with open('mining_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Écrire l'en-tête du CSV
    writer.writerow(['URL', 'Block Reward', 'Difficulty', 'Price'])

    for url in urls:
        logger.info(f"Traitement de l'URL : {url}")

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            block_reward_info = ""
            difficulty_info = ""
            price_info = ""

            block_reward_section = soup.find(string='Block Reward')
            if block_reward_section:
                parent = block_reward_section.find_parent()
                next_span = parent.find_next('span', class_='item')
                if next_span:
                    block_reward_info = next_span.get_text(strip=True)

            difficulty_section = soup.find(string='Difficulty')
            if difficulty_section:
                parent = difficulty_section.find_parent()
                next_span = parent.find_next('span', class_='format-num', attrs={'data-rule': 'formatHashrate'})
                if next_span:
                    difficulty_info = next_span['data-origin']

            price_section = soup.find(string='Price')
            if price_section:
                parent = price_section.find_parent()
                money_val_span = parent.find_next('span', class_='money-val', attrs={'data-rule': 'formatPrice'})
                if money_val_span:
                    price_info = money_val_span['data-usd']

            combined_info = f"{block_reward_info} {difficulty_info} {price_info}"
            logger.info(combined_info)

            # Écrire les données dans le fichier CSV
            writer.writerow([url, block_reward_info, difficulty_info, price_info])

        else:
            logger.error(f"Erreur lors de la récupération de la page : {response.status_code}")




"""
import requests
from bs4 import BeautifulSoup
import logging

# Configurer le logger
logging.basicConfig(filename='script.log', level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

# Étape 1 : Choisir l'URL
url = 'https://www.f2pool.com/coin/kaspa'

# Étape 2 : Récupérer le contenu de la page
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    logger.info(soup.prettify())  # Vérifier le contenu HTML

    # Étape 3 : Afficher tout le contenu récupéré
    elements = soup.find_all('script')  # Modifier cette ligne pour cibler les bons éléments
    logger.info(f"Nombre d'éléments trouvés : {len(elements)}")  # Vérifier le nombre d'éléments trouvés
    for item in elements:
        text = item.string
        if text:
            logger.info(text)  # Afficher tout le contenu récupéré

    logger.info("Données extraites et affichées avec succès !")
else:
    logger.error(f"Erreur lors de la récupération de la page : {response.status_code}")
"""