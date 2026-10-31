# README - Effets du serrage du corset orthopédique pour la scoliose


## Table des matières

1. [Aperçu](#aperçu)
2. [Disponibilité des données](#disponibilité-des-données)
3. [Instructions pour les réplicateurs](#instructions-pour-les-réplicateurs)
4. [Liste des figures](#liste-des-figures)
5. [Requis](#requis)
6. [Description des codes](#description-des-codes)
7. [Structure des fichiers](#structure-des-fichiers)


## Aperçu

Ce répertoire inclut le code nécessaire pour télécharger les données brutes accessibles via un dépôt institutionnel, puis un code pour générer les graphiques. Ces deux codes doivent être exécutés l'un après l'autre. 

L'objectif de ce projet est d'établir la relation entre la tension de sangle d'un corset orthopédique, la pression exercée par le corset sur le tronc puis la correction de la colonne vertébrale. Pour plus de détails sur le projet, veuillez consulter le rapport, Rapport.md.

## Disponibilité des données


### Source des données

Les données brutes sont disponibles via un répertoire sur un dépôt institutionnel demo.borealis. Le dépôt s'intitule "Relation entre la tension, la pression, et la correction pour un patient atteint de la scoliose idiopathique de l'adolescent", publié par les auteurs Antoine Reid et Danika Duval.

Le code dans ce répertoire permet de télécharger automatiquement les données de ce dépôt. Néanmoins, voici des informations clés concernant les données:
- **Nom du fichier de données**: P2_donnees.csv
- **Source des données**: Guy A, Coulombe M, Labelle H, Rigo M, Wong MS, Beygi BH, Wynne J, Hresko MT, Ebermeyer E, Vedreine P, Liu XC, Thometz JG, Bissonnette B, Sapaly C, Barchi S, Aubin CÉ. Biomechanical Effects of Thoracolumbosacral Orthosis Design Features on 3D Correction in Adolescent Idiopathic Scoliosis: A Comprehensive Multicenter Study. Spine (Phila Pa 1976). 2022 Aug 1;47(15):1103-1110. doi: 10.1097/BRS.0000000000004353. Epub 2022 Mar 11. PMID: 35275852.doi: 10.1097/brs.0000000000004353
- **Date d'accès**: Septembre 2026
- **Nombre de variables**: 5
- **Nombre d'observations**: 7
- **Licence des données**: CC-BY-NC 4.0

###  Déclaration sur les droits

- [ ] Je certifie que les auteurs de ce répertoire ont un accès légitime et la permission d'utiliser les données pour ce projet.
- [ ] Je certifie que les auteurs de ce répertoire ont documenté les permissions associées avec ce répertoire pour la réplication du projet. Les permissions sont documentés dans le document LICENCE.txt. 

## Instructions pour les réplicateurs

Les nouveaux utilisateurs devraient suivre les étapes suivantes pour exécuter le package: 
- Le code suivant doit être téléchargé

    - `insérer_nom_du_code`
- Assurez-vous que les logiciels nécessaire sont installés tel qu'énuméré dans la section des [Requis](#requis)
- Exécuter `insérer_nom_du_code`. Ce code sert à télécharger les données à partir du dépôt sur demo.borealis.


## Liste des figures

Le code de ce répertoire reproduit:
- [ ] Tous les résultats numériques énoncés dans le rapport (Rapport.md)
- [ ] Toutes les figures présentées dans le rapport (Rapport.md)


| Nom de la figure | Nom du fichier de sortie | Script | Note |
|--------------|-----------------|--------|------|
| Figure 1     |  | | Trouvé dans Rapport.md/Résultats, Format de l'image: , Bits par pixel: , Couleur: , Dimensions: ,  |
| Figure 2     |  |  | Trouvé dans Rapport.md/Résultats, Format de l'image: , Bits par pixel: , Couleur: , Dimensions: ,  |

## Requis

### Requis informatiques

Ajouter les informations requises selon les recommendations suivantes:
*In this section, specify operating system requirements, software dependencies, environment setup instructions, and any other relevant information essential for replicating the results. Each of these factors plays an important role in ensuring successful replication.*

### Requis de logiciel

Ajouter les informations requises selon les recommendations suivantes: *List all software requirements, including versions, dependencies, libraries, environment setup, and packages installed. Using different versions of the same software could lead to variations in results. If multiple software are used, include details for all.*

*Example:*

- ***Stata version 15***

  - *estout*
  
  - *rdrobust*
  
- ***Python 3.6.4***

  - *pandas 0.24.2*
  
  - *numpy 1.16.4*

### Mémoire, temps de calcul et requis de stockage

Ajouter les informations requises selon les recommendations suivantes: *Provide consistent information about memory resources for reliable computation. Include runtime information for replicators to assess processing times and detect potential issues with the code. It would be best to describe how much storage is required in addition to the space visible in the typical repository, for instance, because data will be unzipped, data downloaded, or temporary files written.*

## Description des codes 

Si le temps le permet, ajouter les informations requises selon les recommendations suivantes:
*Give an overview of the program files and their purposes. Remove redundant or obsolete files from the replication archive. For example, main.do sets file paths, installs necessary ADO packages, and executes all other dofiles. Meanwhile, cleaning.do loads data, handles missing values, and analysis.do performs basic statistical analysis and generate visualizations.* 

*Make sure to also include any crucial information that replicators should be aware of to facilitate a one-click run of the code.*

## Structure des fichiers

Voici la structure des fichiers de ce répertoire:

```
Donnees
  ├── Brutes
  └── Traitees
Code
  ├── 
Resultats
  ├── Rapport
  │   └── Figures
```

## Références
Le modèle du README est basé sur le modèle de README de la Banque mondiale, au lien suivant: https://github.com/worldbank/wb-reproducible-research-repository/blob/main/resources/README_Template.md