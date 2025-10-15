# main.py
from mon_projet.utils.extract import extract_boston_salary
from mon_projet.utils.transform import transform
from mon_projet.utils.analyse import analyse
from mon_projet.utils.load import load

API_URL = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"
OUTPUT_FILENAME = "boston_salaries_clean.csv"

def main():
    """
    Fonction principale qui orchestre l'exécution du pipeline ETL.
    """
    print("--- Démarrage du pipeline ETL pour les salaires de Boston ---")

    # Étape 1 : EXTRACTION
    print("\n[E] Extraction des données depuis l'API...")
    raw_df = extract_boston_salary(API_URL)

    if raw_df.empty:
        print("L'extraction n'a renvoyé aucune donnée. Arrêt du pipeline.")
        return

    # Étape 2 : TRANSFORMATION
    print("\n[T] Nettoyage et transformation des données...")
    cleaned_df = transform(raw_df)
    
    # Étape 3 : ANALYSE
    print("\n[A] Analyse statistique des données nettoyées...")
    analysis_results = analyse(cleaned_df)
    
    # Affichage des résultats de l'analyse
    print("\n--- RÉSULTATS DE L'ANALYSE ---")
    print("\n--- Résumé des statistiques globales ---")
    stats_globales = analysis_results['statistiques_globales']
    print(f"Nombre d'employés : {int(stats_globales['count'])}")
    print(f"Salaire moyen : ${stats_globales['mean']:.2f}")
    print(f"Salaire médian : ${stats_globales['50%']:.2f}")
    print(f"Salaire maximum : ${stats_globales['max']:.2f}")
    print(f"Salaire minimum : ${stats_globales['min']:.2f}")
    print(f"Écart-type des salaires : ${stats_globales['std']:.2f}")

    print("\n--- Statistiques par département ---")
    stats_par_departement = analysis_results['statistiques_par_departement']
    for dept, stats in stats_par_departement.items(): # Parcourt chaque département et ses stats 
        print(f"\nDépartement : {dept}")
        print(f"  Nombre d'employés : {int(stats['count'])}")
        print(f"  Salaire moyen : ${stats['mean']:.2f}")
        print(f"  Salaire médian : ${stats['50%']:.2f}")
        print(f"  Salaire maximum : ${stats['max']:.2f}")
        print(f"  Salaire minimum : ${stats['min']:.2f}")
        print(f"  Écart-type des salaires : ${stats['std']:.2f}")
    
    # Étape 4 : CHARGEMENT (LOAD)
    print("\n[L] Enregistrement des données nettoyées...")
    load(cleaned_df, OUTPUT_FILENAME)
    
    print("\n--- Pipeline ETL terminé avec succès ! ---")



if __name__ == "__main__":
    main()

