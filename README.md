# ☕ Bootcamp Fullstack Java – 16 semaines

Cours **interactif et autonome** pour devenir développeur Fullstack Java en 16 semaines.
Un bloc de semaines, un outil, un livrable.

👉 **Suivre le cours en ligne : https://leudjeu-hub.github.io/Bootcamp-Fullstack-Java/**

## Le programme

| Semaines | Module | Contenu | Livrable |
|---|---|---|---|
| 1 – 2 | Les bases de l'informatique | Fonctionnement d'un serveur, terminal, Git, Java, programmation orientée objet | Programme Java en ligne de commande sur GitHub |
| 3 – 4 | Les bases de données | Modèle relationnel, SQL (CRUD), MySQL, jointures, agrégats | Scripts `schema.sql`, `data.sql`, `requetes.sql` |
| 5 – 8 | Les frameworks : Spring | Spring Boot, API REST, Spring Data JPA, validation, tests, Spring Security + JWT | API REST connectée à MySQL |
| 9 – 12 | Le front-end | HTML, CSS (Flexbox, Grid, responsive), React, appels à l'API, React Router | Application React connectée à l'API |
| 13 – 16 | L'automatisation | CI/CD, GitHub Actions, secrets, Docker, déploiement, portfolio | Pipeline CI verte + application en ligne |

## Le projet fil rouge : LibraStock

Une application de gestion de stock pour une librairie-papeterie : produits, catégories,
entrées et sorties de stock, alertes de réapprovisionnement, rôles `VENDEUR` / `ADMIN`.

**Stack :** Java 21 · Spring Boot · Spring Data JPA · MySQL · React (Vite) · GitHub Actions · Docker

## Fonctionnalités du cours

- 5 modules, 18 leçons, plus de 100 slides
- Quiz avec correction et explication
- Exercices avec solution cachée (« Voir une solution »)
- Progression enregistrée dans le navigateur
- Navigation au clavier (← →), adapté au mobile
- Un seul fichier `index.html`, sans dépendance

## Utiliser le cours en local

```bash
git clone https://github.com/leudjeu-hub/Bootcamp-Fullstack-Java.git
cd Bootcamp-Fullstack-Java
open index.html   # ou double-clic sur le fichier
```

## Modifier le contenu

Le contenu est écrit dans `source/content.py` et injecté dans `source/template.html` :

```bash
cd source
python3 build.py   # régénère ../index.html
```

## Licence

Contenu sous licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr) : libre de partager et d'adapter en citant l'auteur.
