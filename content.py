"""Contenu du portfolio.

Source unique de verite du site : editer ce fichier puis commiter pour
mettre a jour le contenu. Aucune base de donnees, aucun mode admin.
"""

profil = {
    "nom": "Etienne Girard",
    "titre": "Étudiant ingénieur — Majeure Data & IA",
    "accroche": "Alternant Data Finance chez Décathlon — en poste depuis 2026",
    "presentation": (
        "Étudiant ingénieur à l'EPF, spécialisé en Data et Intelligence "
        "Artificielle, actuellement en alternance dans le service Finance de "
        "Décathlon. Fort intérêt pour l'analyse de données, la programmation et "
        "les projets à impact concret. Sérieux, motivé et adaptable, je mets la "
        "data au service de la décision."
    ),
    "email": "etienne.p.girard@gmail.com",
    "telephone": "",
    "localisation": "Paris, France",
    "github": "https://github.com/etienneg92i",
    "linkedin": "",
}

competences = [
    {
        "categorie": "Programmation & Data",
        "items": [
            "Python (analyse de données, scripting)",
            "R / RStudio",
            "MATLAB",
            "MySQL",
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
            "Travail en équipe et communication",
            "Autonomie et capacité d'adaptation",
            "Esprit projet",
        ],
    },
]

langues = [
    {"langue": "Français", "niveau": "Langue maternelle"},
    {"langue": "Anglais", "niveau": "B2"},
    {"langue": "Espagnol", "niveau": "B2"},
]

interets = [
    "Football & tennis",
    "Voyages : Japon, États-Unis, Brésil, Tanzanie, Angleterre, Argentine, Canada",
    "Ouvert au réseau",
]

projets = [
    {
        "titre": "RenovTaCana — outil d'aide à la décision",
        "cadre": "Projet industriel en équipe",
        "organisation": "Eau d'Azur",
        "periode": "2026 · 7 semaines",
        "description": (
            "Outil d'aide à la décision pour automatiser la planification du "
            "renouvellement des réseaux d'eau potable : analyse de données, "
            "logique d'optimisation et application web de visualisation."
        ),
        "technos": ["Python", "R", "Analyse de données", "Optimisation"],
    },
    {
        "titre": "Borne d'arcade",
        "cadre": "Projet en équipe",
        "organisation": "",
        "periode": "2025 · 4 semaines",
        "description": (
            "Conception et construction d'une borne d'arcade fonctionnelle : "
            "assemblage matériel, connectique, connexions électroniques et "
            "intégration du système."
        ),
        "technos": ["Électronique", "Hardware", "Intégration système"],
    },
]

experiences = [
    {
        "titre": "Alternant Data — service Finance",
        "organisation": "Décathlon",
        "lieu": "",
        "periode": "depuis 2026",
        "description": (
            "Analyse et valorisation de données financières : automatisation de "
            "reportings, indicateurs de pilotage et outils d'aide à la décision "
            "pour les équipes Finance."
        ),
    },
    {
        "titre": "Événementiel — FFF Tour",
        "organisation": "Fédération Française de Football",
        "lieu": "France",
        "periode": "juil. – août 2024 · 2 mois",
        "description": (
            "Participation à la tournée estivale « FFF Tour » sur les plages "
            "françaises. Découverte de l'événementiel."
        ),
    },
    {
        "titre": "Chef de rang",
        "organisation": "Hyatt Paris Madeleine",
        "lieu": "Paris",
        "periode": "sept. – déc. 2023 · 4 mois",
        "description": (
            "Service en hôtel 5 étoiles. Sens du service client, travail en "
            "équipe et gestion d'un environnement exigeant."
        ),
    },
    {
        "titre": "Stage associatif",
        "organisation": "Pic-Pic Environnement",
        "lieu": "Issy-les-Moulineaux",
        "periode": "2023 · 4 semaines",
        "description": (
            "Sensibilisation à la protection de l'environnement et animation "
            "d'ateliers pédagogiques dans des écoles."
        ),
    },
    {
        "titre": "Stage de découverte — ingénierie",
        "organisation": "Flying Whales",
        "lieu": "Suresnes",
        "periode": "2020 · 1 mois",
        "description": (
            "Observation du travail d'ingénieurs et découverte du secteur des "
            "dirigeables industriels."
        ),
    },
]

formations = [
    {
        "titre": "Diplôme d'ingénieur — Majeure Data & IA",
        "organisation": "EPF École d'ingénieurs",
        "lieu": "Montpellier",
        "periode": "depuis 2021",
        "description": (
            "Formation d'ingénieur généraliste, spécialisation Data et "
            "Intelligence Artificielle."
        ),
    },
    {
        "titre": "Semestre d'échange — Facultad de Ingeniería",
        "organisation": "Universidad de Buenos Aires (UBA)",
        "lieu": "Buenos Aires, Argentine",
        "periode": "août – déc. 2025",
        "description": "Semestre international en école d'ingénieurs.",
    },
    {
        "titre": "Baccalauréat général",
        "organisation": "Lycée Petit-Champs",
        "lieu": "Paris",
        "periode": "2021",
        "description": (
            "Spécialités mathématiques et physique-chimie. Option mathématiques "
            "expertes."
        ),
    },
]
