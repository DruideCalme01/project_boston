import pandas as pd
import pytest  # pytest est utilisé implicitement mais l'importer est une bonne pratique
from mon_projet.utils.extract import extract_boston_salary 
from mon_projet.utils.transform import transform
from mon_projet.utils.analyse import analyse

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

# --- Test pour la fonction d'analyse (Analyse) ---

# Dans test_etl.py, vous pourriez ajouter cette vérification :
def test_analyse_returns_dict():
    
    """
    Vérifie que la fonction analyse renvoie un dictionnaire avec les statistiques attendues.
    """ 
    # Arrange : On crée un DataFrame de test avec des données nettoyées
    cleaned_data = {
        'TOTAL EARNINGS': [120000.0, 80000.0, 100000.0],
        'DEPARTMENT_NAME': ['Dept A', 'Dept B', 'Dept A']
    }

    cleaned_df = pd.DataFrame(cleaned_data)
    
    analysis_results = analyse(cleaned_df)
    assert isinstance(analysis_results, dict)
    assert 'statistiques_globales' in analysis_results
    assert 'statistiques_par_departement' in analysis_results 
    assert 'Dept A' in analysis_results['statistiques_par_departement']
    assert 'Dept B' in analysis_results['statistiques_par_departement']
    assert analysis_results['statistiques_par_departement']['Dept A']['count'] == 2
    assert analysis_results['statistiques_par_departement']['Dept B']['count'] == 1
    assert analysis_results['statistiques_globales']['mean'] == 100000.0
    assert analysis_results['statistiques_globales']['min'] == 80000.0
    assert analysis_results['statistiques_globales']['max'] == 120000.0