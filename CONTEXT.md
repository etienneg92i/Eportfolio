# ePortfolio

Site vitrine personnel d'Étienne Girard : une page statique qui présente son
profil, ses compétences, son parcours et ses projets à des recruteurs. Le
contenu vit dans `content.py`.

## Audience

**Recruteur** :
Le lecteur cible du site — un futur employeur ou recruteur pour un poste en
Data/IA après l'alternance. Le contenu est trié selon ce qu'un Recruteur
jugerait pertinent.
_Éviter_ : visiteur, client

## Identité

**Profil** :
Le bloc d'identité d'Étienne : nom, Titre, Accroche, Présentation et
coordonnées. Seul objet singleton du contenu ; tout le reste est une liste.

**Titre** :
L'identité de fond : formation et spécialité. Stable sur plusieurs années.
_Éviter_ : poste, rôle

**Accroche** :
La situation du moment, mise en avant en bandeau. Change au gré de l'actualité.
_Éviter_ : slogan, tagline

**Présentation** :
Le paragraphe de synthèse qui relie le Titre et l'Accroche en un récit.
_Éviter_ : bio, à propos

## Parcours

**Expérience** :
Un poste ou une mission exercé au sein d'une Organisation dans un cadre
contractuel ou conventionné (alternance, CDD, job étudiant, stage), défini par
un rôle et une période. N'a pas de Livrable : elle a des missions.
_Éviter_ : job, emploi, mission

**Formation** :
Un cursus visant un diplôme ou des crédits académiques (école, baccalauréat,
semestre d'échange). Une Expérience ne délivre jamais de diplôme ; une Formation
toujours.
_Éviter_ : études, diplôme, cursus

**Projet** :
Une réalisation concrète (académique ou personnelle) définie par un Livrable et
des Technos, pas par un contrat de travail. Un stage est une Expérience ; si son
Livrable mérite d'être montré, il devient aussi un Projet distinct.
_Éviter_ : réalisation, travail

**Livrable** :
Le résultat concret et identifiable que produit un Projet — un outil, une
application, un objet physique. C'est ce qui rend un Projet montrable.
_Éviter_ : résultat, output, produit

**Organisation** :
L'entité rattachée à une Expérience, une Formation ou un Projet : entreprise,
école, association, fédération, commanditaire. Facultative. Ne contient que le
nom de l'entité, pas la nature de l'élément.
_Éviter_ : entreprise, employeur, école, client

## Savoir-faire

**Compétence** :
Un savoir-faire technique ou humain qu'Étienne revendique au niveau de son
Profil.
_Éviter_ : skill, aptitude

**Catégorie de compétences** :
Un regroupement d'affichage des Compétences, non normatif : une Compétence n'a
pas à tomber dans une liste figée.
_Éviter_ : famille, type

**Techno** :
Un outil ou une méthode mobilisé par un Projet précis. Point de vue local
(« ce projet a utilisé X »), là où la Compétence est une revendication de profil
(« je sais faire X »). Les deux ne coïncident pas toujours.
_Éviter_ : technologie, stack, compétence
