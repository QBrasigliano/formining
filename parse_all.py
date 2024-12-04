import requests
from bs4 import BeautifulSoup
import logging

# Configurer le logger
logging.basicConfig(filename='script.log', level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

# Étape 1 : Choisir l'URL
url = 'https://www.asicminervalue.com/'

# Étape 2 : Récupérer le contenu de la page
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    logger.info(soup.prettify())  # Vérifier le contenu HTML

    # Étape 3 : Afficher tout le contenu récupéré
    # On cible le tag 'body' pour récupérer tout le contenu visible de la page
    body = soup.find('body')  
    if body:
        logger.info(body.text)  # Afficher tout le contenu du body

    logger.info("Données extraites et affichées avec succès !")
else:
    logger.error(f"Erreur lors de la récupération de la page : {response.status_code}")