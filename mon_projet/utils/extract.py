import pandas as pd
import requests

def extract_boston_salary(url: str):
    """
    Extrait l'ensemble des données sur les salaires depuis l'API Boston en gérant la pagination.

    Args:
        url: L'URL de base de l'API avec le resource_id.

    Returns:
        Un DataFrame pandas contenant toutes les données de salaires.
    """
    # Liste pour stocker les enregistrements de toutes les pages
    all_records = []
    
    # Paramètres pour la pagination
    offset = 0
    # On met une limite plus élevée pour réduire le nombre d'appels à l'API
    limit = 5000

    while True:
        print(f"Récupération des données... (offset={offset})")

        try:
            # Construction de l'URL avec les paramètres de pagination
            paginated_url = f"{url}&limit={limit}&offset={offset}"

            # Fait la requête à l'API
            response = requests.get(paginated_url)
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
