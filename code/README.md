# 🎓 Campus Life — Groupe RAMMSS

> **Product Goal :** Offrir à la communauté du campus une plateforme démocratique permettant de soumettre, de consulter et de valider des requêtes et des idées sous forme de sondage, afin d'améliorer la vie étudiante de manière collaborative.

Projet GitHub source : [Campus Life - Groupe RAMMSS (GitHub Project #2)](https://github.com/users/FamilyTsuki/projects/2)

---

## 🚀 Présentation de la Maquette (100% HTML & CSS)

Cette maquette interactive a été conçue **exclusivement en HTML5 sémantique et CSS3 moderne**, sans dépendance externe lourde ni framework JavaScript. Elle implémente fidèlement l'ensemble des 12 fonctionnalités et critères d'acceptation du backlog de gestion de projet.

### ✨ Points forts techniques :
- **100% Pur HTML & CSS** : Fonctionne de manière autonome dans n'importe quel navigateur moderne.
- **Design System responsive** : Grid CSS, Flexbox, typographie fluide avec `clamp()`, variables CSS (`--primary`, `--success`, etc.).
- **Mode Sombre / Clair** : Détection automatique via `prefers-color-scheme` et bascule dynamique pure CSS avec sélecteur `:has()`.
- **Composants interactifs CSS** :
  - Modal de décision administrative via `:target`
  - Dropdown des notifications via `:focus-within`
  - Bascule d'anonymat et formulaires interactifs
  - Jauges de ratio de vote tripartites (Pour / Neutre / Contre)
  - Stepper visuel du cycle de vie démocratique
- **Assets vectoriels intégrés** : Logo et icônes en SVG natifs garantissant légèreté et netteté retina.

---

## 📋 Matrice de Traçabilité des 12 User Stories

| # | User Story (Backlog GitHub) | Page / Composant | Critères d'acceptation & Réalisations |
|---|---|---|---|
| **1** | **Page de connexion (Login)** | [`login.html`](login.html) | Saisie identifiant & mot de passe, bouton de soumission avec redirection vers le fil d'actualité, et bloc d'alerte en cas d'erreur d'identifiants simulable via ancre CSS. |
| **2** | **Fil d'actualité des requêtes** | [`index.html`](index.html) | Flux sous forme de cartes affichant le titre, l'auteur (ou Anonyme), le nombre de votes, la jauge tripartite et le statut. Requêtes récentes et populaires mises en avant. |
| **3** | **Créer une nouvelle requête** | [`create.html`](create.html) | Formulaire avec champ titre, sélection de catégorie, description détaillée, impact estimé et bouton de soumission. |
| **4** | **Page des paramètres (Settings)** | [`settings.html`](settings.html) | Personnalisation du thème clair / sombre en temps réel, gestion des notifications et consultation des droits/informations du compte étudiant. |
| **5** | **Consultation détaillée d'une requête** | [`detail.html`](detail.html) | Affichage complet de l'idée, historique et arguments, répartition précise des votes, et espace d'avis/commentaires de la communauté. |
| **6** | **Page d'inscription Administrateur** | [`admin-register.html`](admin-register.html) | Formulaire dédié au staff, à la scolarité et aux membres du BDE avec clé secrète d'accréditation du campus et attribution de rôles administratifs. |
| **7** | **Espace de gestion des requêtes (Admin)** | [`admin.html`](admin.html) | Tableau de bord de modération avec compteurs KPIs, liste des requêtes à traiter, boutons pour approuver, rejeter ou valider officiellement. |
| **8** | **Anonymisation des requêtes** | [`create.html`](create.html), [`index.html`](index.html), [`detail.html`](detail.html) | Interrupteur dédié lors de la création d'une idée (« Publier de manière anonyme 🎭 ») et masquage public du nom sur les cartes et commentaires. |
| **9** | **Structure et validation d'une requête** | [`detail.html`](detail.html), [`index.html`](index.html), [`create.html`](create.html) | Stepper visuel horizontal détaillant les 5 étapes : Soumission ➔ Modération ➔ Seuil 100 votes ➔ Examen commission ➔ Validation officielle. |
| **10** | **Système de vote (Pour / Contre / Neutre)** | [`index.html`](index.html), [`detail.html`](detail.html) | Sondage avec 3 boutons d'action (👍 Pour / ⚖️ Neutre / 👎 Contre), barres de pourcentage colorées et décompte précis. |
| **11** | **Trier les requêtes par popularité** | [`index.html`](index.html) | Barre de filtres rapides (Plus populaires 🔥, Récentes ⏱️, Seuil franchi 🎯, Validées ✅) et sélecteur de tri par volume de votes. |
| **12** | **Notification lors de la validation d'une requête** | [`index.html`](index.html), [`admin.html`](admin.html), [`settings.html`](settings.html) | Bandeau toast en tête de page alertant l'auteur de la validation de sa requête, menu déroulant de notifications et déclencheur admin. |

---

## 🗂️ Arborescence des Fichiers

```text
RAMMSS/
├── index.html            # Fil d'actualité des requêtes (Accueil)
├── create.html           # Formulaire de proposition d'une nouvelle requête
├── detail.html           # Consultation détaillée d'une requête & Débats
├── login.html            # Page de connexion étudiante (avec simulation d'erreur)
├── settings.html         # Paramètres, thème clair/sombre & notifications
├── admin.html            # Dashboard de modération et décisions administratives
├── admin-register.html   # Inscription sécurisée des administrateurs & staff
├── README.md             # Documentation et spécifications du projet
├── css/
│   └── style.css         # Feuille de style principale (Design system, responsive, dark mode)
└── assets/
    └── logo.svg          # Logo vectoriel officiel Campus Life - RAMMSS
```

---

## 🖥️ Comment Visualiser la Maquette

Vous pouvez ouvrir directement les fichiers dans votre navigateur web préféré :

1. **Double-clic sur `index.html`** depuis votre explorateur de fichiers (ou clic droit > Ouvrir avec Google Chrome / Firefox).
2. **Ou via le terminal :**
   ```bash
   xdg-open /home/tsuki/Documents/coda/2026-2027/projet/RAMMSS/index.html
   ```
3. **Ou en lançant un serveur local léger :**
   ```bash
   python3 -m http.server 8080 --directory /home/tsuki/Documents/coda/2026-2027/projet/RAMMSS
   ```
   Puis ouvrez `http://localhost:8080` dans votre navigateur.

