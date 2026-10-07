# Boîte à Idées — Campus Life

Plateforme collaborative permettant aux étudiants et membres du campus de proposer des idées d'amélioration, de voter pour les initiatives de la communauté et de suivre leur concrétisation.

Lien vers le GitHub Project : [Campus Life - Boîte à Idées](https://github.com/users/FamilyTsuki/projects/5)

---

## Objectif du produit (Product Goal)

> Permettre aux étudiants et membres du campus de proposer facilement des idées d'amélioration, de voter démocratiquement pour les meilleures initiatives et de suivre leur concrétisation en toute transparence.

Le but est de proposer un espace centralisé et interactif :
- Dépôt rapide d'idées avec catégorisation
- Système de vote Pour / Contre avec score visible
- Suivi transparent des statuts (Soumise, À l'étude, Retenue, En cours, Réalisée, Rejetée)
- Modération et gestion des propositions

---

## Product Backlog & User Stories

L'ensemble des fonctionnalités est découpé sous forme de User Stories, priorisées selon la méthode MoSCoW et estimées en Story Points (suite de Fibonacci).

| # | User Story | Priorité | Estimation | Sprint |
|---|------------|----------|:----------:|:------:|
| **US-01** | Création et soumission d'une idée | Must Have | 5 SP | Sprint 1 |
| **US-02** | Fil d'actualité et consultation des idées | Must Have | 3 SP | Sprint 1 |
| **US-03** | Consultation détaillée d'une idée | Must Have | 3 SP | Sprint 1 |
| **US-04** | Système de vote Pour / Contre | Must Have | 5 SP | Sprint 1 |
| **US-05** | Option de publication anonyme | Should Have | 3 SP | Backlog |
| **US-06** | Modération et gestion des statuts (Admin/Staff) | Should Have | 8 SP | Backlog |
| **US-07** | Filtrage par catégorie et tri par popularité | Should Have | 3 SP | Backlog |
| **US-08** | Espace d'échange et commentaires constructifs | Should Have | 5 SP | Backlog |
| **US-09** | Signalement d'une proposition inappropriée | Could Have | 2 SP | Backlog |
| **US-10** | Recherche textuelle par mots-clés | Could Have | 3 SP | Backlog |
| **US-11** | Notifications des mises à jour des idées soutenues | Could Have | 5 SP | Backlog |
| **US-12** | Tableau de bord des statistiques d'impact campus | Won't Have | 13 SP | Backlog |

---

## Sprint 1

- **Capacité de l'équipe** : 20 Story Points
- **Objectif du Sprint** : Mettre en place le parcours utilisateur principal permettant de soumettre, consulter et voter pour des idées.
- **Périmètre (16 SP)** :
  - **US-01** : Création et soumission d'une idée (5 SP)
  - **US-02** : Fil d'actualité et consultation des idées (3 SP)
  - **US-03** : Consultation détaillée d'une idée (3 SP)
  - **US-04** : Système de vote Pour / Contre (5 SP)

### Critères d'acceptation du Sprint 1

#### US-01 : Création et soumission d'une nouvelle idée
- [ ] Titre obligatoire (entre 5 et 100 caractères).
- [ ] Sélection d'une catégorie obligatoire (*Vie étudiante, Infrastructures, Restauration, Événements, Pédagogie, Autre*).
- [ ] Description détaillée d'au moins 30 caractères.
- [ ] Message de confirmation après soumission avec redirection vers la fiche.

#### US-02 : Fil d'actualité des idées
- [ ] Affichage des propositions sous forme de cartes synthétiques.
- [ ] Chaque carte affiche : titre, auteur (ou anonyme), date, catégorie et compteur de votes.
- [ ] Tri antéchronologique par défaut (plus récentes en premier).
- [ ] Clic sur une carte redirigeant vers le détail de l'idée.

#### US-03 : Consultation détaillée d'une idée
- [ ] Affichage complet de la proposition (titre, description, auteur, date).
- [ ] Statut visible (*Soumise, À l'étude, Retenue, En cours, Réalisée, Rejetée*).
- [ ] Distinction claire des votes Pour et Contre.
- [ ] Possibilité de copier le lien direct de l'idée.

#### US-04 : Système de vote Pour / Contre
- [ ] Deux boutons d'action : Soutenir (Pour) ou Défavorable (Contre).
- [ ] Un seul vote possible par utilisateur et par proposition (avec possibilité de modifier ou d'annuler son choix).
- [ ] Mise à jour du score en temps réel.
- [ ] État du vote de l'utilisateur visible.

---

## Definition of Done (DoD)

Une User Story est considérée comme terminée uniquement si :
1. Les critères d'acceptation sont tous validés.
2. Les tests fonctionnels sont passés (cas nominaux et cas d'erreur).
3. Le code a été revu et approuvé par un pair (Peer Review).
4. Le code est fusionné proprement sur la branche principale (`main`).
5. La documentation est à jour.
6. La fonctionnalité est démontrable.

---

## Structure du projet

```text
boite-a-idees/
├── code/                   # Maquette HTML/CSS de l'application
│   ├── index.html          # Accueil & fil d'actualité
│   ├── create.html         # Formulaire de soumission d'idée
│   ├── detail.html         # Fiche détaillée & vote
│   ├── login.html          # Page de connexion
│   ├── settings.html       # Paramètres du compte & thème
│   ├── admin.html          # Espace modération
│   ├── admin-register.html # Inscription staff
│   ├── css/                # Styles CSS
│   └── assets/             # Assets graphiques
├── scripts/                # Scripts d'automatisation
└── README.md
```

---

## Lancer la maquette

Pour tester la maquette en local :

1. Ouvrir directement `code/index.html` dans un navigateur.
2. Ou via un serveur local :
   ```bash
   cd code
   python3 -m http.server 8080
   ```
   Puis ouvrir `http://localhost:8080` dans le navigateur.
