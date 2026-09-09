"""Contenu du portfolio.

Source unique de verite du site : editer ce fichier puis commiter pour
mettre a jour le contenu. Aucune base de donnees, aucun mode admin.
"""

profil = {
    "nom": "Etienne Girard",
    "titre": "Étudiant ingénieur — Majeure Data & IA",
    "accroche": "Data Scientist en alternance chez Décathlon — équipe Finance Data",
    "presentation": (
        "J'applique l'analyse exploratoire, la modélisation et le machine "
        "learning aux données financières et business de l'équipe Finance Data. "
        "Je travaille sur des sujets concrets, du nettoyage des données au "
        "modèle qui outille la décision. Élève ingénieur à l'EPF en Majeure "
        "Data & IA, mon parcours s'est aussi construit autour de projets menés "
        "en équipe pour des commanditaires réels et d'un semestre d'échange à "
        "Buenos Aires."
    ),
    "email": "etienne.p.girard@gmail.com",
    "telephone": "",
    "localisation": "Paris, France",
    "github": "https://github.com/etienneg92i",
    "linkedin": "https://www.linkedin.com/in/etienne-girard-207a95281",
}

faits = [
    {"libelle": "Poste", "valeur": "Data Scientist en alternance"},
    {"libelle": "Entreprise", "valeur": "Décathlon — Finance Data"},
    {"libelle": "École", "valeur": "EPF, Majeure Data & IA"},
    {"libelle": "International", "valeur": "Semestre à Buenos Aires"},
    {"libelle": "Base", "valeur": "Paris, France"},
]

competences = [
    {
        "categorie": "Programmation & Data",
        "items": [
            "Python (Pandas, NumPy, scikit-learn)",
            "Machine learning : régression, classification, clustering",
            "R / RStudio",
            "MySQL / SQL",
            "Databricks",
            "MATLAB",
            "VBA",
            "Bases en JavaScript",
        ],
    },
    {
        "categorie": "Outils & environnements",
        "items": [
            "Linux (ligne de commande, configuration d'environnement)",
            "Git & GitHub",
            "Microsoft Office",
        ],
    },
    {
        "categorie": "Savoir-être",
        "items": [
            "Travail en équipe transverse et communication",
            "Autonomie et capacité d'adaptation",
            "Esprit projet et méthodes agiles",
        ],
    },
]

langues = [
    {"langue": "Français", "niveau": "Langue maternelle"},
    {"langue": "Anglais", "niveau": "B2"},
    {"langue": "Espagnol", "niveau": "B2"},
]

interets = [
    "Football et tennis",
    "Voyages : Japon, États-Unis, Brésil, Tanzanie, Angleterre, Argentine, Canada",
]

projets = [
    {
        "titre": "RenovTaCana — outil d'aide à la décision",
        "cadre": "Projet industriel en équipe",
        "organisation": "Eau d'Azur",
        "periode": "2026 · 7 semaines",
        "description": (
            "Commande d'Eau d'Azur : automatiser la planification du "
            "renouvellement des canalisations d'eau potable. Travail d'équipe "
            "sur l'analyse des données réseau et la logique de priorisation, "
            "livré sous forme d'une application web qui cartographie les "
            "tronçons à renouveler et l'ordre d'intervention."
        ),
        "technos": ["Python", "R", "Analyse de données", "Optimisation"],
    },
    {
        "titre": "Borne d'arcade",
        "cadre": "Projet en équipe",
        "organisation": "",
        "periode": "2025 · 4 semaines",
        "description": (
            "Construction en équipe d'une borne d'arcade jouable, de la "
            "structure à l'électronique : assemblage, connectique et "
            "intégration du système. Livrable : une borne fonctionnelle."
        ),
        "technos": ["Électronique", "Hardware", "Intégration système"],
    },
]

experiences = [
    {
        "titre": "Data Scientist en apprentissage — Finance Data",
        "organisation": "Décathlon",
        "logo": "logos/decathlon.webp",
        "lieu": "",
        "periode": "depuis 2026",
        "description": (
            "Data science appliquée aux données financières et business de "
            "Décathlon : analyse exploratoire, préparation des données et "
            "modèles (régression, classification, clustering) pour outiller la "
            "décision. Travail en équipe transverse — data engineers, data "
            "analysts, product managers — en méthode agile. Stack Python/R, "
            "Pandas, scikit-learn, Databricks, SQL."
        ),
    },
    {
        "titre": "Événementiel — FFF Tour",
        "organisation": "Fédération Française de Football",
        "logo": "logos/fff.webp",
        "lieu": "France",
        "periode": "juil. – août 2024 · 2 mois",
        "description": (
            "Participation à la tournée estivale de la FFF sur les plages "
            "françaises. Première expérience de l'événementiel de terrain : "
            "logistique quotidienne et travail en équipe sur un format "
            "itinérant."
        ),
    },
    {
        "titre": "Chef de rang",
        "organisation": "Hyatt Paris Madeleine",
        "logo": "logos/hyatt.png",
        "lieu": "Paris",
        "periode": "sept. – déc. 2023 · 4 mois",
        "description": (
            "Service en salle dans un hôtel 5 étoiles. Exigence sur la qualité, "
            "gestion de la pression du service et coordination en équipe."
        ),
    },
    {
        "titre": "Stage associatif",
        "organisation": "Pic-Pic Environnement",
        "logo": "",
        "lieu": "Issy-les-Moulineaux",
        "periode": "2023 · 4 semaines",
        "description": (
            "Sensibilisation à l'environnement en milieu scolaire : animation "
            "d'ateliers pédagogiques auprès d'élèves."
        ),
    },
    {
        "titre": "Stage de découverte — ingénierie",
        "organisation": "Flying Whales",
        "logo": "",
        "lieu": "Suresnes",
        "periode": "2020 · 1 mois",
        "description": (
            "Stage d'observation : découverte du métier d'ingénieur et du "
            "secteur des dirigeables industriels."
        ),
    },
]

formations = [
    {
        "titre": "Diplôme d'ingénieur — Majeure Data & IA",
        "organisation": "EPF École d'ingénieurs",
        "logo": "logos/epf.png",
        "lieu": "Montpellier",
        "periode": "depuis 2021",
        "description": (
            "Cycle ingénieur généraliste, spécialisation Data et Intelligence "
            "Artificielle en dernière année."
        ),
    },
    {
        "titre": "Semestre d'échange — Facultad de Ingeniería",
        "organisation": "Universidad de Buenos Aires (UBA)",
        "logo": "logos/fiuba.png",
        "lieu": "Buenos Aires, Argentine",
        "periode": "août – déc. 2025",
        "description": (
            "Mobilité académique d'un semestre à la faculté d'ingénierie, en "
            "espagnol."
        ),
    },
    {
        "titre": "Baccalauréat général",
        "organisation": "Lycée Petit-Champs",
        "logo": "",
        "lieu": "Paris",
        "periode": "2021",
        "description": (
            "Spécialités mathématiques et physique-chimie. Option mathématiques "
            "expertes."
        ),
    },
]
