import pandas as pd
import pytest  # pytest est utilisé implicitement mais l'importer est une bonne pratique
from mon_projet.utils.extract import extract_boston_salary 
from mon_projet.utils.transform import transform

# URL de l'API (peut être utilisée pour un test d'intégration léger)
URL = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"

# --- Test pour la fonction d'extraction (Extract) ---
def test_extract_returns_dataframe():
    """
    Vérifie que la fonction extract_boston_salary renvoie bien un DataFrame pandas.
    Note : Ce test fait un véritable appel API, mais ne récupère qu'une seule ligne
    pour être rapide et ne pas surcharger le serveur.
    """
    # Act : On appelle la fonction
    # Pour ne pas télécharger 24000 lignes, on ajoute un paramètre `limit` à l'URL
    df = extract_boston_salary(URL) 
    
    # Assert : On vérifie les résultats
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

# --- Test pour la fonction de transformation (Transform) ---
def test_transform_converts_total_earnings():
    """
    Vérifie que la fonction transform nettoie et convertit correctement
    la colonne 'TOTAL EARNINGS' en un type numérique (float).
    """
    # Arrange : On crée un DataFrame de test avec des données brutes typiques
    raw_data = {
        'TOTAL EARNINGS': ['$123,456.78', '$98,000.50', 'N/A']
    }
    raw_df = pd.DataFrame(raw_data)
    
    # Act : On applique la fonction de transformation
    transformed_df = transform(raw_df)
    
    # Assert : On vérifie que la colonne est maintenant de type numérique
    # pd.api.types.is_numeric_dtype est la manière la plus fiable de vérifier cela.
    assert pd.api.types.is_numeric_dtype(transformed_df['TOTAL EARNINGS'])
    
    # On peut aussi vérifier une valeur spécifique pour être sûr du calcul
    # Note : notre fonction transform remplace les N/A par 0
    assert transformed_df['TOTAL EARNINGS'][0] == 123456.78
    assert transformed_df['TOTAL EARNINGS'][2] == 0

# # --- Test pour la fonction d'analyse (Analyse) ---
# # Supposons que votre fonction `analyse` retourne un dictionnaire avec des indicateurs
# def test_analyse_returns_dict():
#     """
#     Vérifie que la fonction d'analyse retourne bien un dictionnaire
#     et que les clés attendues sont présentes.
#     """
#     # Arrange : On crée un DataFrame déjà nettoyé pour l'analyse
#     clean_data = {
#         'TOTAL EARNINGS': [100000.0, 50000.0, 150000.0],
#         'DEPARTMENT_NAME': ['Police', 'Fire', 'Police']
#     }
#     clean_df = pd.DataFrame(clean_data)
    
#     # Act : On appelle la fonction d'analyse
#     analysis_results = analyse(clean_df) # `analyse` doit être définie dans etl.py
    
#     # Assert : On vérifie le type de retour et la structure
#     assert isinstance(analysis_results, dict)
#     assert 'salaire_moyen_total' in analysis_results
#     assert 'salaire_max' in analysis_results
    
#     # On peut même vérifier le calcul
#     assert analysis_results['salaire_moyen_total'] == 100000.0