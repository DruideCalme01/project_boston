import pandas as pd

def analyse(df: pd.DataFrame) -> dict:
    """
    Réalise des calculs statistiques globaux et par département sur les salaires.

    Args:
        df: Le DataFrame nettoyé contenant les données de salaires.

    Returns:
        Un dictionnaire contenant les statistiques globales et par département.
    """
    if not pd.api.types.is_numeric_dtype(df['TOTAL EARNINGS']):
        raise TypeError("La colonne 'TOTAL EARNINGS' doit être de type numérique.")

    # Calcul des statistiques globales
    stats_globales = df['TOTAL EARNINGS'].describe().to_dict()

    # Calcul des statistiques par département
    stats_par_departement_df = df.groupby('DEPARTMENT_NAME')['TOTAL EARNINGS'].describe()
    stats_par_departement = stats_par_departement_df.to_dict(orient='index')

    resultats = {
        'statistiques_globales': stats_globales,
        'statistiques_par_departement': stats_par_departement
    }
    
    return resultats