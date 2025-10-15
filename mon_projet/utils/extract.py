import pandas as pd
import requests
from urllib.parse import urlparse, parse_qs

def extract_boston_salary(url: str) -> pd.DataFrame:
    """
    Extrait l'ensemble des données sur les salaires depuis l'API Boston en gérant la pagination.

    Args:
        url: L'URL de base de l'API avec le resource_id.

    Returns:
        Un DataFrame pandas contenant toutes les données de salaires.
    """
    all_records = []

    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    resource_id = query_params.get('resource_id', [None])[0] 

    base_url = "https://data.boston.gov/api/3/action/datastore_search"

    # Paramètres pour la pagination
    offset = 0
    try:
        limit = int(query_params.get('limit', [5000])[0])
    except (ValueError, IndexError):
        limit = 5000 # Valeur par défaut si non spécifié ou invalide

    while True:
        params = {
            'resource_id': resource_id,
            'offset': offset,
            'limit': limit
        }
        print(f"Récupération des données... (offset={offset})")

        try:

            # Fait la requête à l'API
            response = requests.get(base_url, params=params)
            response.raise_for_status()

            data = response.json()
            
            # Vérifier que la requête a réussi
            if not data.get("success"):
                print("Erreur de l'API : La requête n'a pas réussi.")
                break

            records = data['result']['records']

            # S'il n'y a plus d'enregistrements renvoyés, on a fini
            if not records:
                print("Fin de la récupération.")
                break

            # Ajouter les enregistrements de cette page à notre liste globale
            all_records.extend(records)

            offset += limit

        except requests.exceptions.RequestException as e:
            print(f"Une erreur réseau est survenue : {e}")
            break
        except KeyError:
            print("Erreur : La structure de la réponse JSON est inattendue.")
            break

    if all_records:
        #créer le DataFrame
        df = pd.DataFrame(all_records)
        print(f"Extraction terminée. {len(df)} lignes récupérées.")
        return df
    else:
        print("Aucune donnée n'a été récupérée.")
        return pd.DataFrame()
