# leankit_api/services.py

import os
import requests
import urllib3

# ⚠️ En dev uniquement : désactive l’avertissement SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Variables d’environnement (dans .env ou dans Windows)
API_TOKEN     = os.getenv('LEANKIT_TOKEN')      # ton token AgilePlace/LeanKit
ORGANIZATION  = os.getenv('LEANKIT_ORG')        # ex. "polybois4502"
# URL par défaut si tu utilises encore leankit.com
DEFAULT_BASE_URL = f"https://{ORGANIZATION}.leankit.com/io"
# Tu peux le remplacer via .env : LEANKIT_BASE_URL="https://polybois4502.agileplace.com/io"
BASE_URL      = os.getenv('LEANKIT_BASE_URL', DEFAULT_BASE_URL)

HEADERS = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json',
}


def get_boards():
    """
    Récupère la liste des boards LeanKit/AgilePlace.
    Retourne une liste de dicts JSON.
    """
    url  = f"{BASE_URL}/board"
    resp = requests.get(url, headers=HEADERS, verify=False)
    resp.raise_for_status()
    data = resp.json()
    # on renvoie la liste sous la clé 'boards'
    return data.get('boards', [])


def get_cards(board_id):
    """
    Récupère **toutes** les cartes d'un board donné, en paginant.
    """
    all_cards = []
    limit  = 200
    offset = 0

    while True:
        url = f"{BASE_URL}/board/{board_id}/card?limit={limit}&offset={offset}"
        resp = requests.get(url, headers=HEADERS, verify=False)
        resp.raise_for_status()
        data = resp.json()
        cards = data.get('cards', [])
        all_cards.extend(cards)

        # pageMeta indique combien il y a en tout
        meta = data.get('pageMeta', {})
        total = meta.get('totalRecords', 0)

        # si on a atteint ou dépassé le total, on arrête
        if len(all_cards) >= total:
            break

        # sinon, on décale l’offset
        offset += limit

    return all_cards

