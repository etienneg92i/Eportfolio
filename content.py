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
        # "liens" : liste de {libelle, url}, vide si aucun. Le libelle nomme le
        # Livrable ou sa source ("Application web", "Code source", "Démo"),
        # jamais une Techno.
        "liens": [],
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
        "liens": [],
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


# ── Garde-fou de contenu ────────────────────────────────────────────────────
# Une entree mal formee (cle `titre` oubliee, `items` absent d'une categorie de
# competences...) passe le hook de commit mais casse ou defigure le rendu. On
# verifie ici la forme au moment de l'import : l'app refuse de demarrer, le test
# `test_content` echoue, avec un message qui pointe l'entree fautive.

def _texte(v):
    return isinstance(v, str) and v.strip() != ""


def _liste_de_dicts(rows, *, requis, optionnels=()):
    """Retourne la liste des problemes pour une liste d'entrees `dict`."""
    connus = set(requis) | set(optionnels)
    problemes = []
    if not isinstance(rows, list) or not rows:
        return ["doit etre une liste non vide"]
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            problemes.append(f"[{i}] n'est pas un dict")
            continue
        for cle in requis:
            if not _texte(row.get(cle)):
                problemes.append(f"[{i}] champ requis manquant ou vide : {cle!r}")
        for cle in set(row) - connus:
            problemes.append(f"[{i}] champ inconnu : {cle!r}")
    return problemes


def _valider():
    erreurs = {}

    manque = [c for c in ("nom", "titre", "presentation") if not _texte(profil.get(c))]
    if manque:
        erreurs["profil"] = [f"champ requis manquant ou vide : {c!r}" for c in manque]

    for nom, rows, requis, opt in (
        ("faits", faits, ("libelle", "valeur"), ()),
        ("langues", langues, ("langue", "niveau"), ()),
        ("projets", projets, ("titre", "description"),
         ("cadre", "organisation", "periode", "technos", "liens")),
        ("experiences", experiences, ("titre", "description"),
         ("organisation", "logo", "lieu", "periode")),
        ("formations", formations, ("titre", "description"),
         ("organisation", "logo", "lieu", "periode")),
    ):
        p = _liste_de_dicts(rows, requis=requis, optionnels=opt)
        if p:
            erreurs[nom] = p

    p = _liste_de_dicts(competences, requis=("categorie",), optionnels=("items",))
    for i, groupe in enumerate(competences if isinstance(competences, list) else []):
        items = groupe.get("items") if isinstance(groupe, dict) else None
        if not isinstance(items, list) or not items or not all(_texte(x) for x in items):
            p.append(f"[{i}] `items` doit etre une liste non vide de chaines")
    if p:
        erreurs["competences"] = p

    if not isinstance(interets, list) or not all(_texte(x) for x in interets):
        erreurs["interets"] = ["doit etre une liste de chaines non vides"]

    for nom, rows in (("projets", projets), ("experiences", experiences),
                      ("formations", formations)):
        for i, row in enumerate(rows if isinstance(rows, list) else []):
            technos = row.get("technos") if isinstance(row, dict) else None
            if technos is not None and (
                not isinstance(technos, list) or not all(_texte(x) for x in technos)
            ):
                erreurs.setdefault(nom, []).append(
                    f"[{i}] `technos`, si present, est une liste de chaines non vides"
                )

    for i, row in enumerate(projets if isinstance(projets, list) else []):
        liens = row.get("liens") if isinstance(row, dict) else None
        if liens is not None and not (
            isinstance(liens, list)
            and all(
                isinstance(x, dict) and _texte(x.get("libelle")) and _texte(x.get("url"))
                for x in liens
            )
        ):
            erreurs.setdefault("projets", []).append(
                f"[{i}] `liens`, si present, est une liste de {{libelle, url}} non vides"
            )

    if erreurs:
        lignes = "\n".join(
            f"  {section} :\n" + "\n".join(f"    - {m}" for m in msgs)
            for section, msgs in erreurs.items()
        )
        raise ValueError("content.py : contenu invalide\n" + lignes)


_valider()
