# 💡 Boîte à Idées — Campus Life

Projet fil rouge de gestion agile Scrum développé dans le cadre du module **Agilité & Scrum**.

🔗 **Espace de travail GitHub Project (Backlog & Sprint 1)** :  
👉 **[Accéder au GitHub Project #5 : Boîte à Idées](https://github.com/users/FamilyTsuki/projects/5)**

---

## 🎯 1. Product Goal (TP4)

> **« Permettre aux étudiants et membres du campus de proposer facilement des idées d'amélioration, de voter démocratiquement pour les meilleures initiatives et de suivre leur concrétisation en toute transparence. »**

Ce Product Goal vise à transformer la boîte à idées physique/traditionnelle en une expérience numérique dynamique, participative et engageante, renforçant le sentiment de communauté et la vie sur le campus.

---

## 📋 2. Product Backlog & Matrice des 12 User Stories

Conformément aux exigences pédagogiques, l'ensemble des éléments du backlog est découpé sous forme de **User Stories** (`En tant que... Je veux... Afin de...`), priorisé selon la méthode **MoSCoW (TP5)** et estimé en **Story Points (TP6)** selon la suite de Fibonacci (`1, 2, 3, 5, 8, 13`).

| # | User Story (Backlog Item) | Priorité (MoSCoW) | Story Points | Sprint |
|---|---------------------------|-------------------|:------------:|:------:|
| **US-01** | **Création et soumission d'une idée** | 🔴 Must have (P1) | 5 | Sprint 1 |
| **US-02** | **Fil d'actualité et consultation des idées** | 🔴 Must have (P1) | 3 | Sprint 1 |
| **US-03** | **Consultation détaillée d'une idée** | 🔴 Must have (P1) | 3 | Sprint 1 |
| **US-04** | **Système de vote Pour / Contre** | 🔴 Must have (P1) | 5 | Sprint 1 |
| **US-05** | **Option de publication anonyme** | 🟡 Should have (P2) | 3 | Backlog |
| **US-06** | **Modération et gestion des statuts (Admin/Staff)** | 🟡 Should have (P2) | 8 | Backlog |
| **US-07** | **Filtrage par catégorie et tri par popularité** | 🟡 Should have (P2) | 3 | Backlog |
| **US-08** | **Espace d'échange et commentaires constructifs** | 🟡 Should have (P2) | 5 | Backlog |
| **US-09** | **Signalement d'une proposition inappropriée** | 🟢 Could have (P3) | 2 | Backlog |
| **US-10** | **Recherche textuelle par mots-clés** | 🟢 Could have (P3) | 3 | Backlog |
| **US-11** | **Notifications des mises à jour des idées soutenues**| 🟢 Could have (P3) | 5 | Backlog |
| **US-12** | **Tableau de bord des statistiques d'impact campus** | ⚪ Won't have (P4) | 8 | Backlog |

- **Total Backlog** : 53 Story Points
- **Sélection prioritaire (~25-30% du backlog - TP5)** : Les 4 User Stories fondamentales (US-01 à US-04) constituent le cœur du produit.

---

## 🔍 3. Critères d'Acceptation des 4 Stories Principales (TP4)

### US-01 : Création et soumission d'une nouvelle idée (5 SP)
- [ ] Le formulaire requiert un titre (entre 5 et 100 caractères).
- [ ] L'utilisateur doit obligatoirement sélectionner une thématique parmi les catégories prédéfinies (*Vie étudiante, Infrastructures, Restauration, Événements, Pédagogie, Autre*).
- [ ] La description doit faire au minimum 30 caractères pour expliciter le besoin.
- [ ] Un message de succès confirme le bon dépôt de l'idée avec un lien direct vers sa fiche.

### US-02 : Fil d'actualité des idées (3 SP)
- [ ] Les idées sont présentées sous forme de cartes synthétiques lisibles.
- [ ] Chaque carte indique le titre, l'auteur (ou *Anonyme*), la date relative, la catégorie et le compteur de votes.
- [ ] L'affichage par défaut présente les propositions les plus récentes en premier.
- [ ] Un clic sur une carte redirige vers la vue détaillée de l'idée.

### US-03 : Consultation détaillée d'une idée (3 SP)
- [ ] La page affiche l'intégralité de la proposition (titre, description complète, auteur, date).
- [ ] Le badge de statut actuel de l'idée est mis en avant (*Soumise, À l'étude, Retenue, En cours, Réalisée, Rejetée*).
- [ ] Les compteurs de votes "Pour" et "Contre" sont clairement distingués.
- [ ] Un bouton de partage de l'idée (lien direct) est présent.

### US-04 : Système de vote Pour / Contre (5 SP)
- [ ] Deux boutons d'action permettent de voter : *Soutenir (Pour)* ou *Défavorable (Contre)*.
- [ ] Un utilisateur ne peut voter qu'une seule fois par proposition (possibilité d'annuler ou de changer son vote).
- [ ] Le score global est mis à jour en temps réel sans rechargement de page.
- [ ] L'état du vote personnel de l'utilisateur reste mémorisé et visible.

---

## 🏃 4. Sprint 1 Planning (TP7)

- **Capacité de l'équipe** : 20 Story Points maximum.
- **Sprint Goal** :
  > **« Offrir aux étudiants le parcours utilisateur fondamental permettant de soumettre, découvrir et voter pour des idées afin de valider l'intérêt et la participation active de la communauté. »**
- **Périmètre du Sprint 1** :
  - US-01 : Création et soumission d'une idée (5 SP)
  - US-02 : Fil d'actualité et consultation des idées (3 SP)
  - US-03 : Consultation détaillée d'une idée (3 SP)
  - US-04 : Système de vote Pour / Contre (5 SP)
- **Total engagé** : **16 Story Points** (parfaitement conforme à la capacité maximale de 20 SP).

---

## ✅ 5. Definition of Done - DoD (TP8)

Une User Story est formellement déclarée **Done** uniquement si l'ensemble des critères suivants est vérifié :
1. **Critères d'acceptation validés** : Tous les critères d'acceptation définis dans la User Story sont testés et validés avec le Product Owner.
2. **Qualité & Tests fonctionnels** : Les tests du parcours nominal et des cas d'erreur sont concluants, sans régression ni bug bloquant/majeur.
3. **Revue par les pairs (Peer Review)** : Le travail a été relu et approuvé par au moins un autre membre de l'équipe de développement.
4. **Intégration** : L'ensemble est synchronisé et intégré proprement sur la branche principale (`main`).
5. **Documentation** : La documentation utilisateur et les notes de version sont à jour.
6. **Démontrable** : La fonctionnalité est présentable en direct aux parties prenantes lors de la Sprint Review (TP9).

