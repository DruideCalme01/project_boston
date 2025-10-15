import pandas as pd
import os # Utile pour gérer les chemins de fichiers

def load(df: pd.DataFrame, filename: str = "boston_salaries_clean.csv"):
    """
    Enregistre les données nettoyées d'un DataFrame dans un fichier CSV.

    Args:
        df: Le DataFrame pandas à enregistrer.
        filename: Le nom du fichier de sortie.
    """
    try:
        
        # On appelle la méthode to_csv sur le DataFrame.
        df.to_csv(
            filename,          
            index=False,       
            encoding='utf-8',  
            sep=','            
        )
        
        print(f"Fichier enregistré avec succès sous : {os.path.abspath(filename)}")

    except Exception as e:
        print(f"Une erreur est survenue lors de l'enregistrement du fichier : {e}")

