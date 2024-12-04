import requests
from bs4 import BeautifulSoup
import logging
import csv

# Configurer le logger pour écraser le fichier à chaque exécution
logging.basicConfig(filename='script.log', level=logging.INFO, format='%(message)s', filemode='w')
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
    writer.writerow(['Coin', 'Block Reward', 'Difficulty', 'Price'])

    for url in urls:
        logger.info(f"Traitement de l'URL : {url}")

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            block_reward_info = ""
            difficulty_info = ""
            price_info = ""

            # Extraire le nom de la pièce de l'URL
            coin = url.split('/')[-1]

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
            writer.writerow([coin, block_reward_info, difficulty_info, price_info])

        else:
            logger.error(f"Erreur lors de la récupération de la page : {response.status_code}")