import subprocess
import time

REPO = "FamilyTsuki/boite-a-idees"
PROJECT_NUMBER = "5"
OWNER = "FamilyTsuki"

missing_items = [
    {
        "title": "US-04: Système de vote Pour / Contre",
        "labels": ["user-story", "Must Have", "Sprint 1"],
        "points": "5",
        "priority": "Must have",
        "sprint": "Sprint 1",
        "body": """## 📝 User Story
**En tant qu'** utilisateur,  
**Je veux** voter pour ou contre une proposition,  
**Afin d'** exprimer mon soutien ou mes réserves sur chaque initiative.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Deux boutons d'action sont disponibles : Pour (+1) et Contre (-1).
- [ ] Un utilisateur authentifié ne peut voter qu'une seule fois par idée (possibilité d'annuler ou d'inverser son vote).
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
        "points": "3",
        "priority": "Should have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant qu'** utilisateur souhaitant préserver sa confidentialité,  
**Je veux** cocher une option d'anonymat lors de la soumission de mon idée,  
**Afin de** m'exprimer librement sans craindre de jugement.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Une case à cocher 'Publier anonymement' est présente sur le formulaire.
- [ ] Si cochée, le nom affiché publiquement sur la carte et la fiche est 'Étudiant anonyme'.
- [ ] L'anonymat est préservé dans les flux publics et les exports.
- [ ] Seule l'administration conserve la traçabilité interne en cas d'abus avéré.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Should Have (P2)
- **Estimation** : 3 Story Points
- **Sprint cible** : Product Backlog
"""
    },
    {
        "title": "US-07: Filtrage par catégorie et tri par popularité",
        "labels": ["user-story", "Should Have"],
        "points": "3",
        "priority": "Should have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant qu'** utilisateur,  
**Je veux** filtrer les idées par thématique et les classer par nombre de votes,  
**Afin d'** identifier immédiatement les propositions les plus plébiscitées.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Filtres disponibles par catégorie (Vie étudiante, Restauration, Matériel, etc.).
- [ ] Options de tri : 'Plus populaires (Top votes)', 'Plus récentes'.
- [ ] L'URL reflète les filtres sélectionnés pour faciliter le partage d'une vue filtrée.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Should Have (P2)
- **Estimation** : 3 Story Points
- **Sprint cible** : Product Backlog
"""
    },
    {
        "title": "US-12: Tableau de bord des statistiques d'impact campus",
        "labels": ["user-story", "Won't Have"],
        "points": "8",
        "priority": "Won't have",
        "sprint": "Product Backlog",
        "body": """## 📝 User Story
**En tant que** direction du campus et équipe projet,  
**Je veux** consulter un tableau de bord analytique sur l'activité de la boîte à idées,  
**Afin de** mesurer le taux de participation et valoriser les idées concrétisées.

---

## 🎯 Critères d'Acceptation (Acceptance Criteria)
- [ ] Graphique du nombre d'idées soumises par mois et par catégorie.
- [ ] Compteur public des 'Idées réalisées grâce à vos votes'.
- [ ] Taux d'engagement global de la communauté.

---

## 📊 Informations Scrum
- **Priorité (MoSCoW)** : Won't Have (P4)
- **Estimation** : 8 Story Points
- **Sprint cible** : Product Backlog
"""
    }
]

def run_cmd(args):
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error running: {' '.join(args)}\nStderr: {res.stderr}")
    return res.stdout.strip()

for idx, item in enumerate(missing_items, 1):
    # Create issue
    cmd_issue = ["gh", "issue", "create", "-R", REPO, "--title", item["title"], "--body", item["body"], "--label", ",".join(item["labels"])]
    url = run_cmd(cmd_issue)
    print(f"[{idx}/4] Created Issue: {url}")
    time.sleep(1)

    # Add to project
    cmd_add = ["gh", "project", "item-add", PROJECT_NUMBER, "--owner", OWNER, "--url", url]
    run_cmd(cmd_add)
    time.sleep(1)

    # Edit Story Points
    cmd_points = ["gh", "project", "item-edit", PROJECT_NUMBER, "--owner", OWNER, "--url", url, "--field", "Story Points", "--number", item["points"]]
    run_cmd(cmd_points)

    # Edit Priority
    cmd_priority = ["gh", "project", "item-edit", PROJECT_NUMBER, "--owner", OWNER, "--url", url, "--field", "Priority", "--value", item["priority"]]
    run_cmd(cmd_priority)

    # Edit Sprint
    cmd_sprint = ["gh", "project", "item-edit", PROJECT_NUMBER, "--owner", OWNER, "--url", url, "--field", "Sprint", "--value", item["sprint"]]
    run_cmd(cmd_sprint)

    # Edit Status
    cmd_status = ["gh", "project", "item-edit", PROJECT_NUMBER, "--owner", OWNER, "--url", url, "--field", "Status", "--value", "Todo"]
    run_cmd(cmd_status)
    time.sleep(1)

print("Finished creating missing issues!")

