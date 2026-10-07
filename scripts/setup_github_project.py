import subprocess
import json
import time

REPO = "FamilyTsuki/boite-a-idees"
PROJECT_NUMBER = "5"
OWNER = "FamilyTsuki"

items = [
    {
        "title": "US-01: Création et soumission d'une nouvelle idée",
        "labels": ["user-story", "Must Have", "Sprint 1"],
        "points": 5,
        "priority": "Must have",
        "sprint": "Sprint 1",
        "body": """## 📝 User Story
**En tant qu'** étudiant ou collaborateur du campus,  
**Je veux** pouvoir déposer une idée avec un titre, une thématique et une description détaillée,  
**Afin de** proposer une amélioration concrète pour la vie sur le campus.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Le formulaire comporte un champ Titre obligatoire (5 à 100 caractères).
- [ ] La sélection d'une catégorie est obligatoire (*Vie étudiante, Infrastructures, Restauration, Événements, Pédagogie, Autre*).
- [ ] Le champ description exige au minimum 30 caractères pour expliciter clairement le besoin.
- [ ] Un message de confirmation s'affiche après l'envoi avec redirection vers la fiche de l'idée créée.
- [ ] L'idée apparaît immédiatement dans le fil d'actualité avec le statut par défaut "Soumise".

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Must Have (P1)
- **Estimation** : 5 Story Points
- **Sprint cible** : Sprint 1
"""
    },
    {
        "title": "US-02: Fil d'actualité et consultation des idées",
        "labels": ["user-story", "Must Have", "Sprint 1"],
        "points": 3,
        "priority": "Must have",
        "sprint": "Sprint 1",
        "body": """## 📝 User Story
**En tant qu'** utilisateur,  
**Je veux** consulter la liste des idées soumises sous forme de cartes synthétiques,  
**Afin de** découvrir rapidement les propositions de la communauté.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Les idées sont affichées sous forme de cartes claires et lisibles.
- [ ] Chaque carte affiche le titre, l'auteur (ou "Anonyme"), la catégorie, la date de publication et le score de votes.
- [ ] Le tri initial est chronologique (idées les plus récentes en tête de liste).
- [ ] Le clic sur une carte ouvre la consultation détaillée de la proposition.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Must Have (P1)
- **Estimation** : 3 Story Points
- **Sprint cible** : Sprint 1
"""
    },
    {
        "title": "US-03: Consultation détaillée d'une idée",
        "labels": ["user-story", "Must Have", "Sprint 1"],
        "points": 3,
        "priority": "Must have",
        "sprint": "Sprint 1",
        "body": """## 📝 User Story
**En tant qu'** utilisateur,  
**Je veux** afficher la fiche détaillée d'une idée avec son statut et son historique,  
**Afin de** comprendre précisément l'initiative et ses objectifs.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] La fiche présente la totalité du texte de la proposition, son auteur et sa date.
- [ ] Le badge de statut actuel est bien visible (*Soumise, À l'étude, Retenue, En cours, Réalisée, Rejetée*).
- [ ] Les compteurs de votes favorables et défavorables sont distincts et lisibles.
- [ ] Un lien de partage unique permet de diffuser directement l'idée.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Must Have (P1)
- **Estimation** : 3 Story Points
- **Sprint cible** : Sprint 1
"""
    },
    {
        "title": "US-04: Système de vote Pour / Contre",
        "labels": ["user-story", "Must Have", "Sprint 1"],
        "points": 5,
        "priority": "Must have",
        "sprint": "Sprint 1",
        "body": """## 📝 User Story
**En tant qu'** utilisateur,  
**Je veux** voter pour ou contre une proposition,  
**Afin d'** exprimer mon soutien ou mes réserves sur chaque initiative.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Deux boutons d'action sont disponibles : "Pour (+1)" et "Contre (-1)".
- [ ] Un utilisateur authentifié ne peut voter qu'une seule fois par idée (il peut annuler ou inverser son vote).
- [ ] Le total des votes est réactualisé instantanément après l'interaction.
- [ ] L'état du vote personnel de l'utilisateur est visible (bouton en surbrillance).

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Must Have (P1)
- **Estimation** : 5 Story Points
- **Sprint cible** : Sprint 1
"""
    },
    {
        "title": "US-05: Option de publication anonyme",
        "labels": ["user-story", "Should Have"],
        "points": 3,
        "priority": "Should have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant qu'** utilisateur souhaitant préserver sa confidentialité,  
**Je veux** cocher une option d'anonymat lors de la soumission de mon idée,  
**Afin de** m'exprimer librement sans craindre de jugement.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Une case à cocher "Publier anonymement" est présente sur le formulaire.
- [ ] Si cochée, le nom affiché publiquement sur la carte et la fiche est "Étudiant anonyme".
- [ ] L'anonymat est préservé dans les flux publics et les exports.
- [ ] Seule l'administration conserve la traçabilité interne en cas d'abus.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Should Have (P2)
- **Estimation** : 3 Story Points
- **Sprint cible** : Product Backlog
"""
    },
    {
        "title": "US-06: Espace de modération et gestion des statuts (Admin/Staff)",
        "labels": ["user-story", "Should Have"],
        "points": 8,
        "priority": "Should have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant que** responsable ou modérateur du campus,  
**Je veux** faire évoluer le statut d'une idée et ajouter une note explicative officielle,  
**Afin d'** informer la communauté des décisions prises sur les projets proposés.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] L'interface admin permet de sélectionner un statut (*À l'étude, Retenue, En cours, Réalisée, Rejetée*).
- [ ] L'admin peut rédiger une justification officielle obligatoire lors de la décision.
- [ ] La réponse officielle apparaît en encadré mis en valeur sur la fiche de l'idée.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Should Have (P2)
- **Estimation** : 8 Story Points
- **Sprint cible** : Product Backlog
"""
    },
    {
        "title": "US-07: Filtrage par catégorie et tri par popularité",
        "labels": ["user-story", "Should Have"],
        "points": 3,
        "priority": "Should have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant qu'** utilisateur,  
**Je veux** filtrer les idées par thématique et les classer par nombre de votes,  
**Afin d'** identifier immédiatement les propositions les plus plébiscitées.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Filtres disponibles par catégorie (*Vie étudiante, Restauration, Matériel, etc.*).
- [ ] Options de tri : "Plus populaires (Top votes)", "Plus récentes".
- [ ] L'URL reflète les filtres sélectionnés pour faciliter le partage.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Should Have (P2)
- **Estimation** : 3 Story Points
- **Sprint cible** : Product Backlog
"""
    },
    {
        "title": "US-08: Espace d'échange et commentaires constructifs",
        "labels": ["user-story", "Should Have"],
        "points": 5,
        "priority": "Should have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant qu'** utilisateur,  
**Je veux** poster un commentaire sous une idée,  
**Afin d'** apporter des suggestions complémentaires et débattre de sa faisabilité.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Zone de saisie d'un commentaire sous la fiche de l'idée.
- [ ] Affichage de l'auteur, de la date et du message dans un fil de discussion.
- [ ] Possibilité pour l'admin d'épingler une contribution pertinente.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Should Have (P2)
- **Estimation** : 5 Story Points
- **Sprint cible** : Product Backlog
"""
    },
    {
        "title": "US-09: Signalement d'une proposition inappropriée",
        "labels": ["user-story", "Could Have"],
        "points": 2,
        "priority": "Could have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant qu'** utilisateur responsable,  
**Je veux** pouvoir signaler une idée ou un commentaire injurieux ou déplacé,  
**Afin de** garantir un espace d'échange respectueux et bienveillant.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Bouton "Signaler" accessible sur chaque idée et commentaire.
- [ ] Modal demandant le motif (*Propos haineux, Spam, Hors-sujet, Autre*).
- [ ] Les éléments recevant plus de 3 signalements sont masqués pour revue admin.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Could Have (P3)
- **Estimation** : 2 Story Points
- **Sprint cible** : Product Backlog
"""
    },
    {
        "title": "US-10: Recherche textuelle par mots-clés",
        "labels": ["user-story", "Could Have"],
        "points": 3,
        "priority": "Could have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant qu'** utilisateur,  
**Je veux** rechercher des idées via un champ de recherche textuel,  
**Afin de** vérifier si une suggestion similaire n'a pas déjà été soumise.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Champ de recherche dynamique avec auto-complétion dès 3 caractères.
- [ ] Recherche dans les titres et descriptions des idées.
- [ ] Suggestion des idées similaires directement lors de la rédaction d'une idée.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Could Have (P3)
- **Estimation** : 3 Story Points
- **Sprint cible** : Product Backlog
"""
    },
    {
        "title": "US-11: Notifications des mises à jour des idées soutenues",
        "labels": ["user-story", "Could Have"],
        "points": 5,
        "priority": "Could have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant qu'** utilisateur ayant soutenu une idée,  
**Je veux** recevoir une notification lorsque le statut de celle-ci évolue,  
**Afin d'** être tenu au courant de sa concrétisation réelle.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Notification in-app ou mail lors d'un passage au statut "Retenue" ou "Réalisée".
- [ ] Centre de notifications avec historique des alertes récentes.
- [ ] Préférence dans le profil pour activer/désactiver les notifications.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Could Have (P3)
- **Estimation** : 5 Story Points
- **Sprint cible** : Product Backlog
"""
    },
    {
        "title": "US-12: Tableau de bord des statistiques d'impact campus",
        "labels": ["user-story", "Won't Have"],
        "points": 8,
        "priority": "Won't have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant que** direction du campus et équipe projet,  
**Je veux** consulter un tableau de bord analytique sur l'activité de la boîte à idées,  
**Afin de** mesurer le taux de participation et valoriser les idées concrétisées.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Graphique du nombre d'idées soumises par mois et par catégorie.
- [ ] Compteur public des "Idées réalisées grâce à vos votes".
- [ ] Taux d'engagement global de la communauté.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Won't Have (P4)
- **Estimation** : 8 Story Points
- **Sprint cible** : Product Backlog
"""
    }
]

def run_cmd(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error running: {cmd}\nStderr: {res.stderr}")
    return res.stdout.strip()

print(f"Starting creation of {len(items)} issues...")

for idx, item in enumerate(items, 1):
    # 1. Create issue
    labels_flag = ",".join(item["labels"])
    cmd_issue = f'gh issue create -R "{REPO}" --title "{item["title"]}" --body "{item["body"]}" --label "{labels_flag}"'
    url = run_cmd(cmd_issue)
    print(f"[{idx}/{len(items)}] Created Issue: {url}")
    
    # 2. Add to project
    cmd_add = f'gh project item-add {PROJECT_NUMBER} --owner "{OWNER}" --url "{url}" --format json'
    add_out = run_cmd(cmd_add)
    time.sleep(0.5)

    # 3. Set Story Points
    cmd_points = f'gh project item-edit {PROJECT_NUMBER} --owner "{OWNER}" --url "{url}" --field "Story Points" --number {item["points"]}'
    run_cmd(cmd_points)

    # 4. Set Priority
    cmd_priority = f'gh project item-edit {PROJECT_NUMBER} --owner "{OWNER}" --url "{url}" --field "Priority" --value "{item["priority"]}"'
    run_cmd(cmd_priority)

    # 5. Set Sprint
    cmd_sprint = f'gh project item-edit {PROJECT_NUMBER} --owner "{OWNER}" --url "{url}" --field "Sprint" --value "{item["sprint"]}"'
    run_cmd(cmd_sprint)

    # 6. Set Status to Todo
    cmd_status = f'gh project item-edit {PROJECT_NUMBER} --owner "{OWNER}" --url "{url}" --field "Status" --value "Todo"'
    run_cmd(cmd_status)
    time.sleep(0.5)

print("✅ All items created and added to GitHub Project successfully!")

