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