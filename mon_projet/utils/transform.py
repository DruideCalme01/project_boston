import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie et transforme les données de salaires, en particulier la colonne 'TOTAL EARNINGS'.

    Args:
        df: Le DataFrame brut contenant les données de salaires.

    Returns:
        Le DataFrame transformé avec les types de données corrigés.
    """
    print("🧹 Début du nettoyage des données...")
    #Faire une copie 
    df_transformed = df.copy()
    
    cleaned_series = pd.to_numeric(
        df_transformed['TOTAL EARNINGS'].str.replace('$', '', regex=False).str.replace(',', '', regex=False),
        errors='coerce'
    )

    # Gérer les valeurs manquantes (NaN) 
    df_transformed['TOTAL EARNINGS'] = cleaned_series.fillna(0)
    
    print("Nettoyage et typage de 'TOTAL EARNINGS' terminés.")

    return df_transformed