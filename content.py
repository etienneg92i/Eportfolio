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


# ── Traduction (anglais) ────────────────────────────────────────────────────
# Miroir en anglais des textes ci-dessus, pour le bouton EN/FR (bascule cote
# client, sans rechargement, voir static/i18n.js). Cle `ui` : libelles fixes
# du gabarit (nav, boutons, titres de section). Cles suivantes : miroir des
# listes/dicts ci-dessus, meme ordre, memes index — `_valider` verifie la
# parite de structure entre le francais et l'anglais.
#
# Ce qui n'est PAS traduit ici (reste identique dans les deux langues, aucune
# entree requise) : noms propres (personnes, organisations, ecoles, villes),
# `profil.nom`, `profil.email`/`telephone`/`github`/`linkedin`, les `technos`
# qui sont deja des noms d'outils, `formation.logo`.

traduction_en = {
    "ui": {
        "skip_link": "Skip to content",
        "brand_role": "Data & AI",
        "nav_accueil": "Home",
        "nav_apropos": "About",
        "nav_parcours": "Education & projects",
        "nav_experience": "Experience",
        "nav_contact": "Contact",
        "hero_at_decathlon": "at Décathlon",
        "cta_projects": "View projects",
        "cta_contact": "Contact me",
        "skills_heading": "Skills",
        "about_eyebrow": "About",
        "about_title": "Profile",
        "languages_heading": "Languages",
        "interests_heading": "Interests",
        "contact_details_heading": "Contact details",
        "location_label": "Location",
        "email_label": "Email",
        "parcours_eyebrow": "Background",
        "parcours_title_1": "Education",
        "parcours_title_2": "projects",
        "formations_heading": "Education",
        "projects_heading": "Projects",
        "no_formation": "No education entries yet.",
        "no_project": "No projects yet.",
        "no_experience": "No experience entries yet.",
        "experience_title": "Experience",
        "contact_title_1": "Let's stay",
        "contact_title_2": "in touch",
        "contact_lead": (
            "Data Scientist on a work-study program at Décathlon, Finance "
            "Data team. A question, or just want to connect? Write to me."
        ),
        "back_home": "Back to home",
        "error_404_eyebrow": "Error 404",
        "error_404_title_1": "Page",
        "error_404_title_2": "not found",
        "error_404_text": (
            "This address leads nowhere — the page may have moved, or "
            "never existed."
        ),
        "lang_toggle_to_en": "Switch to English",
        "lang_toggle_to_fr": "Passer en français",
        # Titres composés (nom du profil + titre / suffixe), calcules cote
        # Python pour rester en phase avec `profil["nom"]`.
        "title_accueil": None,
        "title_404": None,
    },
    "profil": {
        "titre": "Engineering student — Data & AI major",
        "accroche": "Data Scientist on a work-study program at Décathlon — Finance Data team",
        "presentation": (
            "I apply exploratory analysis, modeling and machine learning to "
            "the Finance Data team's financial and business data. I work on "
            "concrete problems, from data cleaning to the model that "
            "supports the decision. An engineering student at EPF in the "
            "Data & AI major, my path has also been shaped by team projects "
            "for real-world clients and an exchange semester in Buenos "
            "Aires."
        ),
    },
    "faits": [
        {"libelle": "Role", "valeur": "Data Scientist (work-study)"},
        {"libelle": "Company", "valeur": "Décathlon — Finance Data"},
        {"libelle": "School", "valeur": "EPF, Data & AI major"},
        {"libelle": "Based in", "valeur": "Paris, France"},
    ],
    "competences": [
        {
            "categorie": "Programming & Data",
            "items": [
                "Python (Pandas, NumPy, scikit-learn)",
                "Machine learning: regression, classification, clustering",
                "R / RStudio",
                "MySQL / SQL",
                "Databricks",
                "MATLAB",
                "VBA",
                "JavaScript basics",
            ],
        },
        {
            "categorie": "Tools & environments",
            "items": [
                "Linux (command line, environment setup)",
                "Git & GitHub",
                "Microsoft Office",
            ],
        },
        {
            "categorie": "Soft skills",
            "items": [
                "Cross-functional teamwork and communication",
                "Autonomy and adaptability",
                "Project mindset and agile methods",
            ],
        },
    ],
    "langues": [
        {"langue": "French", "niveau": "Native language"},
        {"langue": "English", "niveau": "B2"},
        {"langue": "Spanish", "niveau": "B2"},
    ],
    "interets": [
        "Football and tennis",
        "Travel: Japan, USA, Brazil, Tanzania, England, Argentina, Canada",
    ],
    "projets": [
        {
            "titre": "RenovTaCana — decision support tool",
            "cadre": "Team industry project",
            "periode": "2026 · 7 weeks",
            "description": (
                "Commissioned by Eau d'Azur: automate the renewal planning "
                "of drinking-water pipes. Team work on network data "
                "analysis and prioritization logic, delivered as a web app "
                "that maps the pipe sections to renew and the order of "
                "intervention."
            ),
            "technos": ["Python", "R", "Data analysis", "Optimization"],
            "liens": [],
        },
        {
            "titre": "Arcade cabinet",
            "cadre": "Team project",
            "periode": "2025 · 4 weeks",
            "description": (
                "Team build of a playable arcade cabinet, from the frame to "
                "the electronics: assembly, wiring and system integration. "
                "Deliverable: a working cabinet."
            ),
            "technos": ["Electronics", "Hardware", "System integration"],
            "liens": [],
        },
    ],
    "experiences": [
        {
            "titre": "Data Scientist apprentice — Finance Data",
            "periode": "since 2026",
            "description": (
                "Applied data science on Décathlon's financial and business "
                "data: exploratory analysis, data preparation and models "
                "(regression, classification, clustering) to support "
                "decisions. Cross-functional teamwork — data engineers, "
                "data analysts, product managers — in an agile setup. "
                "Python/R stack, Pandas, scikit-learn, Databricks, SQL."
            ),
        },
        {
            "titre": "Event staff — FFF Tour",
            "lieu": "France",
            "periode": "Jul – Aug 2024 · 2 months",
            "description": (
                "Took part in the FFF's summer tour on French beaches. "
                "First experience of on-the-ground event work: daily "
                "logistics and teamwork on a traveling format."
            ),
        },
        {
            "titre": "Head waiter",
            "lieu": "Paris",
            "periode": "Sep – Dec 2023 · 4 months",
            "description": (
                "Floor service in a 5-star hotel. High standards on "
                "quality, handling service pressure and team coordination."
            ),
        },
        {
            "titre": "Nonprofit internship",
            "lieu": "Issy-les-Moulineaux",
            "periode": "2023 · 4 weeks",
            "description": (
                "Environmental awareness in schools: running educational "
                "workshops for students."
            ),
        },
        {
            "titre": "Discovery internship — engineering",
            "lieu": "Suresnes",
            "periode": "2020 · 1 month",
            "description": (
                "Observation internship: an introduction to the engineering "
                "profession and the industrial airship sector."
            ),
        },
    ],
    "formations": [
        {
            "titre": "Engineering degree — Data & AI major",
            "lieu": "Montpellier",
            "periode": "since 2021",
            "description": (
                "General engineering program, specializing in Data and "
                "Artificial Intelligence in the final year."
            ),
        },
        {
            "titre": "Exchange semester — Facultad de Ingeniería",
            "lieu": "Buenos Aires, Argentina",
            "periode": "Aug – Dec 2025",
            "description": (
                "One-semester academic exchange at the engineering school, "
                "taught in Spanish."
            ),
        },
        {
            "titre": "General baccalauréat",
            "lieu": "Paris",
            "periode": "2021",
            "description": (
                "Mathematics and physics-chemistry specialties. Advanced "
                "mathematics option."
            ),
        },
    ],
}


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


def _liste_parallele(nom_fr, rows_fr, rows_en, *, requis):
    """Verifie qu'une liste `traduction_en[...]` a la meme longueur que son
    pendant francais et que chaque entree porte les champs `requis`."""
    if not isinstance(rows_en, list) or len(rows_en) != len(rows_fr):
        attendu = len(rows_fr) if isinstance(rows_fr, list) else "?"
        return [f"doit avoir autant d'entrees que `{nom_fr}` ({attendu})"]
    problemes = []
    for i, row in enumerate(rows_en):
        if not isinstance(row, dict):
            problemes.append(f"[{i}] n'est pas un dict")
            continue
        for cle in requis:
            if not _texte(row.get(cle)):
                problemes.append(f"[{i}] champ requis manquant ou vide : {cle!r}")
    return problemes


CLES_UI_TRADUCTION = (
    "skip_link", "brand_role", "nav_accueil", "nav_apropos", "nav_parcours",
    "nav_experience", "nav_contact", "hero_at_decathlon", "cta_projects",
    "cta_contact", "skills_heading", "about_eyebrow", "about_title",
    "languages_heading", "interests_heading", "contact_details_heading",
    "location_label", "email_label", "parcours_eyebrow", "parcours_title_1",
    "parcours_title_2", "formations_heading", "projects_heading",
    "no_formation", "no_project", "no_experience", "experience_title",
    "contact_title_1", "contact_title_2", "contact_lead", "back_home",
    "error_404_eyebrow", "error_404_title_1", "error_404_title_2", "error_404_text",
    "lang_toggle_to_en", "lang_toggle_to_fr",
)
# Calculees a l'import par main.py (dependent de `profil["nom"]`) : absentes
# ici, `None` tant que non renseignees, jamais exigees non vides.
CLES_UI_CALCULEES = ("title_accueil", "title_404")


def _valider_traduction():
    """Parite de structure entre `traduction_en` et le contenu francais."""
    problemes = {}

    ui = traduction_en.get("ui") if isinstance(traduction_en, dict) else None
    if not isinstance(ui, dict):
        problemes["ui"] = ["doit etre un dict"]
    else:
        manquants = [c for c in CLES_UI_TRADUCTION if not _texte(ui.get(c))]
        if manquants:
            problemes["ui"] = [f"champ requis manquant ou vide : {c!r}" for c in manquants]
        inconnues = set(ui) - set(CLES_UI_TRADUCTION) - set(CLES_UI_CALCULEES)
        if inconnues:
            problemes.setdefault("ui", []).extend(
                f"champ inconnu : {c!r}" for c in sorted(inconnues)
            )

    profil_en = traduction_en.get("profil") if isinstance(traduction_en, dict) else None
    if not isinstance(profil_en, dict) or not all(
        _texte(profil_en.get(c)) for c in ("titre", "presentation")
    ):
        problemes["profil"] = ["`titre` et `presentation` sont requis et non vides"]

    for nom, rows_fr, requis in (
        ("faits", faits, ("libelle", "valeur")),
        ("langues", langues, ("langue", "niveau")),
        ("projets", projets, ("titre", "description")),
        ("experiences", experiences, ("titre", "description")),
        ("formations", formations, ("titre", "description")),
    ):
        rows_en = traduction_en.get(nom) if isinstance(traduction_en, dict) else None
        p = _liste_parallele(nom, rows_fr, rows_en, requis=requis)
        if p:
            problemes[nom] = p

    competences_en = traduction_en.get("competences") if isinstance(traduction_en, dict) else None
    p = _liste_parallele("competences", competences, competences_en, requis=("categorie",))
    if not p and isinstance(competences_en, list):
        for i, (groupe_fr, groupe_en) in enumerate(zip(competences, competences_en)):
            items_fr = groupe_fr.get("items", [])
            items_en = groupe_en.get("items") if isinstance(groupe_en, dict) else None
            if not isinstance(items_en, list) or len(items_en) != len(items_fr) or not all(
                _texte(x) for x in items_en
            ):
                p.append(f"[{i}] `items` doit avoir autant d'entrees non vides que en francais")
    if p:
        problemes["competences"] = p

    interets_en = traduction_en.get("interets") if isinstance(traduction_en, dict) else None
    if not isinstance(interets_en, list) or len(interets_en) != len(interets) or not all(
        _texte(x) for x in interets_en
    ):
        problemes["interets"] = ["doit avoir autant d'entrees non vides que `interets`"]

    return {f"traduction_en.{k}": v for k, v in problemes.items()}


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


def _valider_tout():
    """`_valider()` + parite de `traduction_en`.

    Separee de `_valider()` : les tests de `test_content.py` monkeypatchent
    une seule section (ex. `projets`) et appellent `_valider()` pour verifier
    l'isolement de cette section, sans avoir a mettre a jour `traduction_en`
    en meme temps. La parite FR/EN, elle, ne s'applique qu'au vrai contenu
    commite — verifiee ici, appelee a l'import et par son propre test.
    """
    _valider()
    problemes = _valider_traduction()
    if problemes:
        lignes = "\n".join(
            f"  {section} :\n" + "\n".join(f"    - {m}" for m in msgs)
            for section, msgs in problemes.items()
        )
        raise ValueError("content.py : traduction invalide\n" + lignes)


_valider_tout()
