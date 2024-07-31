urban-simulator/
├── data/
│   ├── raw/                 # Données brutes d'entrée
│   ├── processed/           # Données traitées et prêtes pour la simulation
│   └── outputs/             # Résultats de la simulation (fichiers KML, JSON, etc.)
├── docs/                    # Documentation du projet
│   ├── requirements.md      # Spécifications et exigences
│   ├── architecture.md      # Architecture du système
│   └── usage.md             # Guide d'utilisation
├── notebooks/               # Notebooks Jupyter pour l'analyse exploratoire
├── src/                     # Code source principal
│   ├── __init__.py
│   ├── main.py              # Point d'entrée principal de l'application
│   ├── simulation/          # Modules de simulation
│   │   ├── __init__.py
│   │   ├── agent.py         # Définition des agents
│   │   ├── environment.py   # Environnement de simulation
│   │   └── model.py         # Modèle de simulation
│   ├── data_processing/     # Scripts de traitement des données
│   │   ├── __init__.py
│   │   ├── load_data.py     # Chargement des données
│   │   └── preprocess.py    # Prétraitement des données
│   ├── utils/               # Utilitaires divers
│   │   ├── __init__.py
│   │   └── helpers.py       # Fonctions d'aide
│   └── visualization/       # Scripts de visualisation
│       ├── __init__.py
│       └── plot_data.py     # Visualisation des données
├── tests/                   # Tests unitaires et d'intégration
│   ├── __init__.py
│   ├── test_simulation.py   # Tests pour les modules de simulation
│   └── test_data_processing.py # Tests pour le traitement des données
├── .gitignore               # Fichiers et dossiers à ignorer par Git
├── README.md                # Description du projet
├── requirements.txt         # Dépendances du projet
└── setup.py                 # Script d'installation


