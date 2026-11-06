# Effets du serrage du corset orthopédique pour la scoliose


## Table des matières

1. [Aperçu](#aperçu)
2. [Disponibilité des données](#disponibilité-des-données)
3. [Instructions pour les réplicateurs](#instructions-pour-les-réplicateurs)
4. [Liste des figures et des résultats](#liste-des-figures-et-des-résultats)
5. [Requis](#requis)
6. [Description des codes](#description-des-codes)
7. [Structure des fichiers](#structure-des-fichiers)
8. [Intégration continue](#intégration-continue)
9. [Contribution](#contribution)
10. [Support](#support)
11. [Références](#références)


## Aperçu

Ce répertoire contient le code nécessaire pour télécharger les données brutes, les préparer pour l'analyse et générer les résultats ainsi que les figures du projet. Les trois étapes doivent être exécutées dans l'ordre : téléchargement, prétraitement, puis analyse.

L'objectif du projet est d'établir la relation entre la tension de sangle d'un corset orthopédique, la pression exercée par le corset sur le tronc et la correction de la colonne vertébrale, mesurée par les angles de Cobb. L'analyse porte sur le patient P2 et compare les régions thoracique et lombaire à l'aide de régressions linéaires. Pour plus de détails, consultez le rapport [Rapport.md](./Rapport.md).


## Disponibilité des données

### Source des données

Les données brutes sont disponibles dans le dépôt institutionnel Demo Borealis, sous le titre « Relation entre la tension, la pression, et la correction pour un patient atteint de la scoliose idiopathique de l'adolescent », publié par Antoine Reid et Danika Duval.

Le script `download-data` télécharge automatiquement les fichiers de ce dépôt à l'aide de son API. Les informations clés sont les suivantes :

- **Nom du fichier de données** : `P2_donnees.tab`
- **Dépôt Borealis** : [doi:10.80240/FK2/HLKYWD](https://demo.borealisdata.ca/dataset.xhtml?persistentId=doi:10.80240/FK2/HLKYWD)
- **Source primaire** : Guy A, Coulombe M, Labelle H, Rigo M, Wong MS, Beygi BH, et al. *Biomechanical Effects of Thoracolumbosacral Orthosis Design Features on 3D Correction in Adolescent Idiopathic Scoliosis: A Comprehensive Multicenter Study*. Spine (Phila Pa 1976). 2022;47(15):1103-1110. [doi:10.1097/BRS.0000000000004353](https://doi.org/10.1097/BRS.0000000000004353)
- **Date d'accès** : octobre 2026
- **Nombre de variables** : 5
- **Nombre d'observations** : 7
- **Licence des données** : CC BY-NC 4.0

### Variables

| Variable | Description | Unité |
|---|---|---|
| `Tension` | Tension de serrage du corset | N |
| `Pression_thor` | Pression appliquée au niveau thoracique | kPa |
| `Pression_lomb` | Pression appliquée au niveau lombaire | kPa |
| `Angle_Cobb_thor` | Angle de Cobb thoracique | ° |
| `Angle_Cobb_lomb` | Angle de Cobb lombaire | ° |

### Déclaration sur les droits

Les données sont utilisées conformément à leur licence CC BY-NC 4.0. Elles proviennent du dépôt Borealis identifié ci-dessus et doivent être citées avec la référence de Guy et al. (2022). Les données brutes ne sont pas versionnées dans ce répertoire; elles sont téléchargées par le script prévu à cet effet.


## Instructions pour les réplicateurs

### Préparation de l'environnement

1. Cloner le répertoire et se placer à sa racine :

   ```bash
   git clone https://github.com/Antetokounpo/corset-correction.git
   cd corset-correction
   ```

2. Installer [uv](https://docs.astral.sh/uv/) si ce n'est pas déjà fait, puis synchroniser l'environnement Python :

   ```bash
   uv sync
   ```

   Cette commande crée l'environnement virtuel et installe les versions de dépendances enregistrées dans `uv.lock`.

### Exécution du pipeline

Exécuter les commandes suivantes depuis la racine du projet :

```bash
# 1. Télécharger les données brutes dans data/raw/
uv run download-data

# 2. Copier les données brutes dans data/processed/
uv run preprocess-data

# 3. Effectuer les régressions et générer les figures et les résultats
uv run analyze-data
```

Les résultats numériques sont écrits dans `results/regression_results.csv` et les figures dans `figures/`.


## Liste des figures et des résultats

Le code de ce répertoire reproduit :

- [x] Tous les résultats numériques énoncés dans le rapport (`Rapport.md`)
- [x] Toutes les figures présentées dans le rapport (`Rapport.md`)

| Nom de la figure | Nom du fichier de sortie | Script | Note |
|---|---|---|---|
| Figure 1 — Pression en fonction de la tension | `figures/pression_vs_tension.png` | `uv run analyze-data` | PNG, 2100 × 1350 px, 300 dpi. Pression thoracique et lombaire observée et ajustée. |
| Figure 2 — Angles de Cobb en fonction de la tension | `figures/cobb_vs_tension.png` | `uv run analyze-data` | PNG, 2100 × 1350 px, 300 dpi. Angles thoracique et lombaire observés et ajustés. |

Le fichier `results/regression_results.csv` contient, pour chaque variable dépendante, la pente, l'ordonnée à l'origine, le coefficient de détermination \(R^2\), la statistique \(t\), la valeur \(p\) du test bilatéral et le nombre d'observations.


## Requis

### Requis informatiques

- Python 3.14 (version indiquée dans `.python-version`)
- [uv](https://docs.astral.sh/uv/) pour la gestion de l'environnement et des dépendances
- Un système d'exploitation compatible avec Python 3.14 (Linux, macOS ou Windows)
- Une connexion Internet pour télécharger les données depuis Borealis

Les figures sont générées avec le backend non interactif `Agg` de Matplotlib; aucun affichage graphique n'est requis.

### Requis de logiciel

Les dépendances Python sont déclarées dans `pyproject.toml` et verrouillées dans `uv.lock`.

### Mémoire, temps de calcul et stockage

Le jeu de données contient 7 observations et 5 variables. L'analyse est donc très légère et ne nécessite pas d'ordinateur très puissant.

## Description des codes

Le code est organisé comme un package Python dans `src/corset_correction/`. Les commandes sont exposées dans `pyproject.toml` et s'exécutent avec `uv run`.

| Commande | Module | Rôle |
|---|---|---|
| `uv run download-data` | `src/corset_correction/download_data.py` | Interroge l'API de Borealis à partir du DOI du jeu de données et télécharge tous les fichiers de la version courante dans `data/raw/`. |
| `uv run preprocess-data` | `src/corset_correction/preprocess.py` | Copie le contenu de `data/raw/` vers `data/processed/` afin de séparer les données brutes des données utilisées pour l'analyse. |
| `uv run analyze-data` | `src/corset_correction/analyze.py` | Lit `data/processed/P2_donnees.tab`, ajuste quatre régressions linéaires de la pression et des angles de Cobb en fonction de la tension, puis calcule les métriques et génère les figures. |

Le script d'analyse effectue les opérations suivantes :

1. Lecture du fichier tabulé avec gestion de l'encodage UTF-8 avec BOM.
2. Conversion des colonnes en valeurs numériques.
3. Ajustement d'une régression linéaire pour `Pression_thor`, `Pression_lomb`, `Angle_Cobb_thor` et `Angle_Cobb_lomb` en fonction de `Tension`.
4. Calcul de la pente, de l'ordonnée à l'origine, de \(R^2\), de la statistique \(t\), de la valeur \(p\) bilatérale et du nombre d'observations.
5. Écriture des résultats dans `results/regression_results.csv` et des figures dans `figures/`.


## Structure des fichiers

```text
corset-correction/
├── README.md
├── Rapport.md
├── CODE_DE_CONDUITE.md
├── CONTRIBUTIONS.md
├── AI_prompts.md
├── LICENSE.md
├── .gitignore
├── pyproject.toml
├── uv.lock
├── .python-version
├── data/
│   ├── raw/              # Données téléchargées, non versionnées
│   └── processed/        # Données préparées pour l'analyse, non versionnées
├── img/                  # Figures versionnées utilisées dans Rapport.md
│   ├── cobb_vs_tension.png
│   └── pression_vs_tension.png
├── figures/              # Figures générées par l'analyse, non versionnées
├── results/              # Résultats numériques générés, non versionnés
├── src/
│   └── corset_correction/
│       ├── __init__.py
│       ├── download_data.py
│       ├── preprocess.py
│       └── analyze.py
└── .github/
    └── workflows/
        ├── ci.yml
        └── pr_dependency.yml
```

Les répertoires `data/`, `figures/` et `results/` sont générés par le pipeline et exclus du contrôle de version. Le répertoire `img/` contient les figures versionnées utilisées dans `Rapport.md`.

## Intégration continue

Deux workflows GitHub Actions sont définis dans `.github/workflows/` :

- `ci.yml` s'exécute à l'ouverture ou à la mise à jour d'une pull request vers `main`, ainsi qu'après un push sur `main`. Il installe Python avec `uv`, crée l'environnement avec `uv sync --locked`, vérifie l'importation des dépendances, puis exécute successivement `download-data`, `preprocess-data` et `analyze-data`. Il vérifie finalement que le fichier de résultats et les deux figures ont bien été générés.
- `pr_dependency.yml` s'exécute lors des événements `pull_request_target` et utilise `gregsdennis/dependencies-action` afin de vérifier les dépendances déclarées entre les pull requests.

## Contribution

Les contributions sont encadrées par le guide [CONTRIBUTIONS.md](./CONTRIBUTIONS.md) et le [Code de conduite](./CODE_DE_CONDUITE.md). Les modifications doivent être proposées dans une branche dédiée et soumises par pull request.

## Support

Pour obtenir de l'aide technique concernant l'installation ou l'utilisation du projet, ou pour poser des questions générales sur le projet, veuillez ouvrir un problème GitHub ("issue") afin d'encourager le partage d'informations avec les futurs réplicateurs. Veuillez décrire clairement votre question et fournir les informations pertinentes pour faciliter la réponse des modérateurs.

Si vous n'obtenez pas de réponse d'ici 48 h, veuillez envoyer un courriel aux modérateurs, Danika Duval (danika.duval@etud.polymtl.ca) et/ou Antoine Reid (antoine-2.reid@etud.polymtl.ca).

Pour signaler un bogue ou suggérer une modification, consultez les instructions du fichier [CONTRIBUTIONS.md](./CONTRIBUTIONS.md).

## Références

- Duval, D. et Reid, A. « Relation entre la tension, la pression, et la correction pour un patient atteint de la scoliose idiopathique de l'adolescent », Demo Borealis, doi:10.80240/FK2/HLKYWD. https://demo.borealisdata.ca/dataset.xhtml?persistentId=doi:10.80240/FK2/HLKYWD
- Guy, A., Coulombe, M., Labelle, H., Rigo, M., Wong, M.-S., Beygi, B. H., et al. (2022). Biomechanical Effects of Thoracolumbosacral Orthosis Design Features on 3D Correction in Adolescent Idiopathic Scoliosis: A Comprehensive Multicenter Study. *Spine*, 47(15), 1103-1110. https://doi.org/10.1097/BRS.0000000000004353

Le modèle du README est basé sur le [modèle de README de la Banque mondiale](https://github.com/worldbank/wb-reproducible-research-repository/blob/main/resources/README_Template.md).
