# 🚀 Projet : Pipeline ETL AGILE - Analyse des Données Publiques de Boston

Ce document sert de référence principale pour l'organisation, les objectifs et les rôles de l'équipe travaillant sur la construction du pipeline ETL (Extract-Transform-Load) de la ville de Boston.

---

## 🎯 Vision et Objectif du Produit

### Vision du Produit
**Avoir un pipeline ETL automatisé, testé et réutilisable pour analyser les données publiques de la ville de Boston.**

### Objectif Principal (Le *Product Goal*)
Mettre en œuvre un pipeline ETL (Extract, Transform, Load) complet pour analyser les écarts de salaires des employés municipaux de la ville de Boston sur l'année 2018.
L'objectif est d'extraire des données publiques, de les transformer pour les rendre exploitables, puis de calculer des statistiques par département (écarts de salaire, médiane, min, max, etc.).

---

## 🧩 Tâches à réaliser par l'Équipe

**Tâches :**
- Réaliser une extraction de données depuis une API
- Transformer les données extraites de façon claires et lisibles
- Enregistrer les données transformées dans un fichier final type CSV
- Réaliser des tests unitaires pour vérifier que les codes marchent de façon correctes
- Effectuer une analyse des données pour récupérer les données importantes
- Automatiser le pipeline ETL grâce à une automatisation CI/CD

**Lien vers les tâches :** https://github.com/DruideCalme01/project_boston/issues

---

## 🤝 Organisation de l'Équipe (Méthode Scrum)

L'équipe opère selon le cadre de travail **Scrum** pour garantir une livraison de valeur progressive et adaptative.

### Rôles Clés

| Rôle | Responsabilité Principale | Orientation | Personnes |
| :--- | :--- | :--- | :--- |
| **Product Owner (PO)** | Maximiser la valeur du produit. Gère et ordonne le Backlog Produit, est l'interface avec les parties prenantes et valide le travail réalisé. | **Le "QUOI"** | William BAAL |
| **Scrum Master (SM)** | Assurer la bonne application d'AGILE/Scrum. Facilite les rituels, élimine les obstacles (*impediments*) et protège l'équipe des interférences. | **Le "COMMENT nous nous organisons"** | Benjamin CHASSIER |
| **Équipe de Développement** | Produire l'incrément de valeur à chaque Sprint. Responsable de l'estimation, de la conception, de l'implémentation, des tests et du déploiement. | **Les Data Engineers** | William BAAL Benjamin CHASSIER Matthieu NOGUEIRA Ryan BONZANINI Philippe GONCALVES |

---

## 🗓️ Rituels Scrum (Cérémonies)

Les rituels sont le cœur de la collaboration de l'équipe et permettent l'inspection et l'adaptation du produit et du processus. (Basé sur un Sprint de 2 semaines).

| Rituel | Objectif | Fréquence | Participants Clés |
| :--- | :--- | :--- | :--- |
| **Planification de Sprint** | Déterminer l'**Objectif du Sprint** et sélectionner les items du Backlog Produit à réaliser. | Début de chaque Sprint (Max 4 heures) | PO, SM, Équipe de Développement |
| **Mêlée Quotidienne (*Daily Scrum*)** | Synchroniser l'équipe, inspecter la progression vers l'Objectif du Sprint et identifier les obstacles. | Tous les jours (Max 15 minutes) | Équipe de Développement (PO et SM peuvent écouter) |
| **Revue de Sprint (*Sprint Review*)** | **Inspecter le produit réalisé** (l'*Incrément*). L'équipe présente ce qui est "Fini" aux parties prenantes. | Fin de chaque Sprint (Max 2 heures) | PO, SM, Équipe de Développement, Parties Prenantes |
| **Rétrospective de Sprint** | **Inspecter l'équipe et le processus.** Déterminer ce qui s'est bien passé, ce qui peut être amélioré. | Fin de chaque Sprint (Max 1.5 heures) | SM, Équipe de Développement (le PO peut participer si le SM le juge pertinent) |
| **Raffinement du Backlog** | Clarifier, détailler et estimer les items du Backlog Produit pour les Sprints futurs. | Régulièrement pendant le Sprint (Ex: 1 à 2 fois / semaine) | PO, Équipe de Développement |

---

## 💻 Tech Stack & Dépendances

*(Cette section est à compléter avec les outils concrets : Python, Airflow/Prefect, Docker, AWS/GCP/Azure, PostgreSQL/Snowflake, etc.)*

---

## 📦 Backlog Produit

**Lien vers le Backlog :** https://github.com/users/DruideCalme01/projects/3
