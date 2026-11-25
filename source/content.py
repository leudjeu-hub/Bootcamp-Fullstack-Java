# -*- coding: utf-8 -*-
# Contenu du cours "Bootcamp Fullstack Java en 16 semaines"

def T(title, html):
    return {"type": "text", "title": title, "html": html}

def C(title, lang, code, note=""):
    return {"type": "code", "title": title, "lang": lang, "code": code.strip("\n"), "note": note}

def Q(question, options, answer, explain):
    return {"type": "quiz", "title": "Quiz", "question": question, "options": options, "answer": answer, "explain": explain}

def E(title, task, solution, lang="text"):
    return {"type": "exercise", "title": title, "task": task, "solution": solution.strip("\n"), "lang": lang}

def OBJ(items):
    return T("Objectifs de la leçon", "<ul class='goals'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>")

PROJECT = """
<p>Tout au long du bootcamp, tu construis <b>une seule application</b>, de bout en bout :
<b>LibraStock</b>, une application de gestion de stock pour une librairie-papeterie.</p>
<ul>
<li><b>Produits</b> : livres, cahiers, stylos… avec prix, quantité en stock et catégorie.</li>
<li><b>Mouvements de stock</b> : entrées (livraison fournisseur) et sorties (vente).</li>
<li><b>Alertes</b> : liste des produits sous le seuil minimum.</li>
<li><b>Utilisateurs</b> : rôle <code>VENDEUR</code> et rôle <code>ADMIN</code>.</li>
</ul>
<p>Chaque module ajoute une brique : la base de données, puis l'API Java/Spring, puis l'interface React,
puis la pipeline automatique. À la fin, tu as un vrai projet à montrer dans ton portfolio.</p>
"""

MODULES = [
# ---------------------------------------------------------------- MODULE 1
{
"id": "m1", "weeks": "Semaines 1 & 2", "title": "Les bases de l'informatique",
"icon": "🖥️", "color": "#7CFC00",
"summary": "Comprendre ce qui se passe derrière une application web : le serveur, Git et le langage Java.",
"deliverable": "Un dépôt GitHub public contenant un petit programme Java en ligne de commande (gestion d'une liste de produits en mémoire), avec au moins 5 commits propres.",
"lessons": [
{
"title": "Le fonctionnement d'un serveur",
"slides": [
OBJ(["Expliquer le modèle client / serveur", "Comprendre une requête et une réponse HTTP", "Connaître le rôle du DNS, de l'IP et des ports", "Utiliser les commandes de base du terminal"]),
T("Client et serveur", """
<p>Quand tu ouvres un site web, deux programmes discutent :</p>
<div class="flow"><span>🧑‍💻 Client<br><small>navigateur, appli mobile</small></span><span class="arrow">→ requête →</span><span>🖥️ Serveur<br><small>programme qui écoute</small></span></div>
<div class="flow"><span>🧑‍💻 Client</span><span class="arrow">← réponse ←</span><span>🖥️ Serveur</span></div>
<p>Un <b>serveur</b> n'est pas forcément une machine spéciale : c'est d'abord un <b>programme</b> qui attend des requêtes
sur un <b>port</b> et renvoie des réponses. Ce programme tourne sur un ordinateur (physique ou dans le cloud).</p>
<p>Dans notre projet : le navigateur affiche l'interface <b>React</b> (client), qui appelle l'API <b>Spring Boot</b> (serveur), qui lit et écrit dans <b>MySQL</b> (serveur de base de données).</p>
"""),
T("Le voyage d'une requête", """
<ol class="steps">
<li><b>Tu tapes</b> <code>https://librastock.com/produits</code>.</li>
<li><b>DNS</b> : l'annuaire d'Internet traduit <code>librastock.com</code> en adresse <b>IP</b> (ex. <code>51.15.20.4</code>).</li>
<li><b>Connexion</b> : le navigateur contacte cette IP sur le <b>port 443</b> (HTTPS). Le port 80 = HTTP, 3306 = MySQL, 8080 = souvent Spring Boot en local.</li>
<li><b>Requête HTTP</b> : <code>GET /produits</code>.</li>
<li><b>Traitement</b> : le serveur exécute du code, interroge la base de données.</li>
<li><b>Réponse HTTP</b> : un <b>code statut</b> (200, 404…) et un contenu (HTML, JSON…).</li>
</ol>
"""),
C("Anatomie d'une requête et d'une réponse HTTP", "http", """
GET /api/produits/12 HTTP/1.1
Host: librastock.com
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json

{ "id": 12, "nom": "Cahier A4 96 pages", "prix": 2.50, "stock": 140 }
""", "Les verbes HTTP à connaître : <b>GET</b> (lire), <b>POST</b> (créer), <b>PUT</b> (modifier), <b>DELETE</b> (supprimer). Codes : <b>2xx</b> succès, <b>4xx</b> erreur du client, <b>5xx</b> erreur du serveur."),
C("Le terminal : tes premières commandes", "bash", """
pwd                 # où suis-je ?
ls -la              # lister les fichiers (même cachés)
cd projets          # entrer dans un dossier
cd ..               # remonter d'un niveau
mkdir librastock    # créer un dossier
touch notes.txt     # créer un fichier vide
cat notes.txt       # afficher un fichier
rm notes.txt        # supprimer un fichier (attention, pas de corbeille !)
curl https://api.github.com   # envoyer une requête HTTP depuis le terminal
""", "Un développeur passe beaucoup de temps dans le terminal. Sur Mac : application <b>Terminal</b>. Sur Windows : <b>Git Bash</b> ou <b>WSL</b>."),
Q("Que signifie un code de réponse HTTP 404 ?", ["Le serveur a planté", "La ressource demandée n'existe pas", "La requête a réussi", "Il faut se connecter"], 1, "404 = <i>Not Found</i>. Une erreur 5xx indique un problème côté serveur, 401/403 un problème d'authentification ou de droits."),
Q("Quel est le rôle du DNS ?", ["Chiffrer la connexion", "Stocker les pages web", "Traduire un nom de domaine en adresse IP", "Exécuter le code Java"], 2, "Le DNS est l'annuaire d'Internet : il transforme <code>librastock.com</code> en une adresse IP."),
E("Exercice : observe une vraie requête", """
<ol><li>Ouvre ton navigateur, puis les outils de développement (<kbd>F12</kbd> ou <kbd>Cmd+Option+I</kbd>), onglet <b>Réseau / Network</b>.</li>
<li>Recharge une page web au choix.</li>
<li>Clique sur la première requête et note : la méthode, le code statut, le <code>Content-Type</code> de la réponse.</li>
<li>Dans le terminal, lance <code>curl -i https://api.github.com/users/octocat</code> et repère les mêmes informations.</li></ol>
""", """
Méthode : GET
Code statut : 200 OK
Content-Type : text/html (page web) ou application/json (API)
Avec curl -i, les en-têtes (headers) s'affichent avant le corps JSON.
"""),
]},
{
"title": "C'est quoi Git ?",
"slides": [
OBJ(["Comprendre pourquoi on versionne son code", "Maîtriser le cycle add → commit → push", "Travailler avec des branches", "Publier un projet sur GitHub"]),
T("Pourquoi Git ?", """
<p><b>Git</b> est un logiciel de <b>gestion de versions</b>. Il enregistre l'historique de ton code sous forme de
<b>commits</b> (des « photos » de ton projet à un instant donné).</p>
<ul>
<li>Revenir en arrière si tu casses quelque chose.</li>
<li>Travailler à plusieurs sans écraser le travail des autres.</li>
<li>Tester une idée dans une <b>branche</b> sans toucher à la version stable.</li>
</ul>
<p><b>GitHub</b> n'est pas Git : c'est un <b>site</b> qui héberge des dépôts Git en ligne (et qui propose aussi GitHub Actions, que tu verras en semaine 13).</p>
"""),
T("Les 3 zones de Git", """
<div class="flow"><span>📁 Dossier de travail<br><small>tes fichiers modifiés</small></span><span class="arrow">git add →</span><span>📋 Zone de préparation<br><small>staging</small></span><span class="arrow">git commit →</span><span>🗄️ Dépôt local<br><small>historique</small></span></div>
<div class="flow"><span>🗄️ Dépôt local</span><span class="arrow">git push →</span><span>☁️ GitHub<br><small>dépôt distant</small></span></div>
"""),
C("Le cycle de base", "bash", """
git config --global user.name "Ton Nom"
git config --global user.email "toi@email.com"

git init                     # transformer un dossier en dépôt Git
git status                   # voir ce qui a changé
git add Main.java            # préparer un fichier (ou: git add .)
git commit -m "Ajoute la classe Main"
git log --oneline            # voir l'historique

git remote add origin https://github.com/TON-COMPTE/librastock.git
git push -u origin main      # envoyer sur GitHub
git pull                     # récupérer les changements distants
"""),
C("Les branches", "bash", """
git switch -c feature/alertes-stock   # créer une branche et y aller
# ... modifier du code, add, commit ...
git switch main                       # revenir sur main
git merge feature/alertes-stock       # fusionner la branche
git branch -d feature/alertes-stock   # supprimer la branche fusionnée
""", "Bonne pratique : <b>une branche par fonctionnalité</b>, et des messages de commit clairs à l'impératif : « Ajoute… », « Corrige… »."),
C("Le fichier .gitignore", "text", """
# Ne jamais versionner :
target/          # fichiers compilés Java (Maven)
node_modules/    # dépendances JavaScript
.env             # mots de passe et secrets !
.idea/
.DS_Store
"""),
Q("Quelle commande envoie tes commits locaux vers GitHub ?", ["git commit", "git add", "git push", "git pull"], 2, "<code>git commit</code> enregistre localement, <code>git push</code> envoie vers le dépôt distant."),
Q("À quoi sert une branche ?", ["À supprimer l'historique", "À développer une fonctionnalité sans toucher à la version principale", "À compiler le code", "À se connecter à GitHub"], 1, "Une branche est une ligne de développement parallèle. On la fusionne (merge) quand le travail est prêt."),
E("Exercice : ton premier dépôt", """
<ol><li>Crée un dossier <code>librastock</code> et initialise un dépôt Git.</li>
<li>Crée un fichier <code>README.md</code> avec le titre du projet et fais un commit.</li>
<li>Crée une branche <code>docs/description</code>, ajoute une description du projet dans le README, commit.</li>
<li>Fusionne la branche dans <code>main</code>, puis publie le dépôt sur GitHub.</li></ol>
""", """
mkdir librastock && cd librastock
git init
echo "# LibraStock" > README.md
git add README.md
git commit -m "Ajoute le README"
git switch -c docs/description
echo "Application de gestion de stock pour une librairie-papeterie." >> README.md
git commit -am "Décrit le projet"
git switch main
git merge docs/description
git remote add origin https://github.com/TON-COMPTE/librastock.git
git push -u origin main
""", "bash"),
]},
{
"title": "C'est quoi Java ?",
"slides": [
OBJ(["Comprendre JDK, JVM et compilation", "Écrire variables, conditions, boucles et méthodes", "Exécuter un premier programme Java"]),
T("Java en une slide", """
<p><b>Java</b> est un langage <b>orienté objet</b>, <b>typé</b> et très utilisé en entreprise (banques, assurances, administrations…). Spring Boot, le framework que tu utiliseras en semaine 5, est écrit en Java.</p>
<div class="flow"><span>📄 Main.java<br><small>code source</small></span><span class="arrow">javac →</span><span>⚙️ Main.class<br><small>bytecode</small></span><span class="arrow">java →</span><span>☕ JVM<br><small>exécute partout</small></span></div>
<ul>
<li><b>JDK</b> : le kit pour développer (compilateur + outils). Installe une version LTS : <b>Java 21</b>.</li>
<li><b>JVM</b> : la machine virtuelle qui exécute le bytecode, sur Windows, Mac ou Linux.</li>
<li><b>IDE</b> conseillé : IntelliJ IDEA Community (gratuit) ou VS Code + extension Java.</li>
</ul>
"""),
C("Variables et types", "java", """
public class Main {
    public static void main(String[] args) {
        String nom = "Cahier A4";      // texte
        int stock = 140;               // nombre entier
        double prix = 2.50;            // nombre décimal
        boolean disponible = stock > 0; // vrai / faux

        System.out.println(nom + " coûte " + prix + " €");
        System.out.println("Disponible : " + disponible);
    }
}
"""),
C("Conditions et boucles", "java", """
int stock = 8;
int seuilMinimum = 10;

if (stock == 0) {
    System.out.println("Rupture de stock !");
} else if (stock < seuilMinimum) {
    System.out.println("Stock faible, commander bientôt.");
} else {
    System.out.println("Stock OK");
}

// Boucle for : afficher 5 étiquettes
for (int i = 1; i <= 5; i++) {
    System.out.println("Étiquette n°" + i);
}

// Boucle while : vendre jusqu'à épuisement
while (stock > 0) {
    stock--;
}
"""),
C("Méthodes", "java", """
public class Caisse {

    // Une méthode reçoit des paramètres et renvoie un résultat
    static double calculerTotal(double prixUnitaire, int quantite) {
        return prixUnitaire * quantite;
    }

    static double appliquerRemise(double total, double pourcentage) {
        return total - total * pourcentage / 100;
    }

    public static void main(String[] args) {
        double total = calculerTotal(2.50, 12);
        double aPayer = appliquerRemise(total, 10);
        System.out.println("À payer : " + aPayer + " €"); // 27.0 €
    }
}
"""),
Q("Que fait la JVM ?", ["Elle compile le code source", "Elle exécute le bytecode Java", "Elle héberge le code sur Internet", "Elle gère la base de données"], 1, "<code>javac</code> compile en bytecode, la <b>JVM</b> exécute ce bytecode sur n'importe quel système."),
Q("Quel type utiliser pour stocker un prix comme 2.50 ?", ["int", "boolean", "String", "double"], 3, "<code>double</code> stocke les nombres décimaux. En production, on utilise plutôt <code>BigDecimal</code> pour l'argent afin d'éviter les erreurs d'arrondi."),
E("Exercice : calculateur de réapprovisionnement", """
<p>Écris une méthode <code>quantiteACommander(int stock, int seuil, int stockCible)</code> qui renvoie
la quantité à commander : 0 si le stock est supérieur ou égal au seuil, sinon <code>stockCible - stock</code>.
Teste-la avec (8, 10, 50) et (25, 10, 50).</p>
""", """
static int quantiteACommander(int stock, int seuil, int stockCible) {
    if (stock >= seuil) {
        return 0;
    }
    return stockCible - stock;
}

// quantiteACommander(8, 10, 50)  -> 42
// quantiteACommander(25, 10, 50) -> 0
""", "java"),
]},
{
"title": "Java orienté objet",
"slides": [
OBJ(["Créer des classes et des objets", "Utiliser l'encapsulation (private + getters)", "Manipuler des listes avec ArrayList", "Livrer le programme du module 1"]),
T("Classe et objet", """
<p>Une <b>classe</b> est un plan (le moule). Un <b>objet</b> est une instance concrète créée à partir de ce plan.</p>
<p>Classe <code>Produit</code> → objets : « Cahier A4 », « Stylo bleu », « Le Petit Prince »…</p>
<p>Les 4 idées de la programmation orientée objet : <b>encapsulation</b> (protéger les données), <b>héritage</b>, <b>polymorphisme</b>, <b>abstraction</b>.
Pour Spring Boot, l'encapsulation et les interfaces sont les plus importantes.</p>
"""),
C("La classe Produit", "java", """
public class Produit {
    private String nom;     // private = protégé, accessible seulement ici
    private double prix;
    private int stock;

    public Produit(String nom, double prix, int stock) {  // constructeur
        this.nom = nom;
        this.prix = prix;
        this.stock = stock;
    }

    public void vendre(int quantite) {
        if (quantite > stock) {
            throw new IllegalArgumentException("Stock insuffisant pour " + nom);
        }
        stock -= quantite;
    }

    public void reapprovisionner(int quantite) { stock += quantite; }

    public String getNom() { return nom; }
    public double getPrix() { return prix; }
    public int getStock() { return stock; }
}
"""),
C("Des listes d'objets", "java", """
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Produit> catalogue = new ArrayList<>();
        catalogue.add(new Produit("Cahier A4", 2.50, 140));
        catalogue.add(new Produit("Stylo bleu", 0.80, 6));

        catalogue.get(0).vendre(10);

        for (Produit p : catalogue) {
            if (p.getStock() < 10) {
                System.out.println("⚠ Stock faible : " + p.getNom());
            }
        }

        // Version moderne avec les streams
        catalogue.stream()
                 .filter(p -> p.getStock() < 10)
                 .forEach(p -> System.out.println(p.getNom()));
    }
}
"""),
Q("Pourquoi déclarer les attributs en private ?", ["Pour que le programme soit plus rapide", "Pour empêcher qu'on modifie l'état de l'objet n'importe comment", "Parce que Java l'impose", "Pour les cacher sur GitHub"], 1, "C'est l'<b>encapsulation</b> : on passe par des méthodes (comme <code>vendre()</code>) qui contrôlent les règles, par ex. ne pas vendre plus que le stock."),
E("🎯 Livrable du module 1", """
<p>Crée un programme Java en ligne de commande <b>LibraStock v0</b> :</p>
<ul><li>une classe <code>Produit</code> (nom, prix, stock, seuil minimum) ;</li>
<li>une classe <code>Inventaire</code> avec une <code>List&lt;Produit&gt;</code> et les méthodes
<code>ajouter</code>, <code>vendre(nom, quantite)</code>, <code>produitsEnAlerte()</code>, <code>valeurTotaleDuStock()</code> ;</li>
<li>un <code>main</code> qui démontre toutes les méthodes.</li></ul>
<p>Publie-le sur GitHub avec au moins 5 commits clairs.</p>
""", """
public class Inventaire {
    private final List<Produit> produits = new ArrayList<>();

    public void ajouter(Produit p) { produits.add(p); }

    public void vendre(String nom, int quantite) {
        trouver(nom).vendre(quantite);
    }

    public List<Produit> produitsEnAlerte() {
        return produits.stream()
                .filter(p -> p.getStock() < p.getSeuilMinimum())
                .toList();
    }

    public double valeurTotaleDuStock() {
        return produits.stream()
                .mapToDouble(p -> p.getPrix() * p.getStock())
                .sum();
    }

    private Produit trouver(String nom) {
        return produits.stream()
                .filter(p -> p.getNom().equalsIgnoreCase(nom))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Produit inconnu : " + nom));
    }
}
""", "java"),
]},
]},
# ---------------------------------------------------------------- MODULE 2
{
"id": "m2", "weeks": "Semaines 3 & 4", "title": "Les bases de données",
"icon": "🗄️", "color": "#00D1FF",
"summary": "Stocker les données de façon durable avec SQL et MySQL.",
"deliverable": "Un script <code>schema.sql</code> et un script <code>data.sql</code> qui créent et remplissent la base LibraStock (catégories, produits, mouvements), plus un fichier <code>requetes.sql</code> avec 10 requêtes utiles.",
"lessons": [
{
"title": "Les bases de données relationnelles",
"slides": [
OBJ(["Comprendre tables, lignes et colonnes", "Connaître clé primaire et clé étrangère", "Modéliser les données de LibraStock"]),
T("Pourquoi une base de données ?", """
<p>Dans le module 1, les produits disparaissent quand le programme s'arrête : ils sont seulement en mémoire.
Une <b>base de données</b> stocke les données <b>durablement</b>, permet de les chercher rapidement et de les partager entre plusieurs utilisateurs.</p>
<p>Une base <b>relationnelle</b> (MySQL, PostgreSQL…) organise les données en <b>tables</b> reliées entre elles. On l'interroge avec le langage <b>SQL</b>.</p>
<table class="tbl"><tr><th>id</th><th>nom</th><th>prix</th><th>stock</th><th>categorie_id</th></tr>
<tr><td>1</td><td>Cahier A4</td><td>2.50</td><td>140</td><td>2</td></tr>
<tr><td>2</td><td>Le Petit Prince</td><td>7.90</td><td>12</td><td>1</td></tr></table>
<p><small>Une table = un type d'objet · une ligne = un enregistrement · une colonne = un attribut</small></p>
"""),
T("Clés et relations", """
<ul>
<li><b>Clé primaire (PRIMARY KEY)</b> : identifiant unique de chaque ligne, souvent <code>id</code> auto-incrémenté.</li>
<li><b>Clé étrangère (FOREIGN KEY)</b> : colonne qui pointe vers la clé primaire d'une autre table.</li>
</ul>
<p><b>Relations dans LibraStock :</b></p>
<div class="flow"><span>categorie</span><span class="arrow">1 ── N</span><span>produit</span><span class="arrow">1 ── N</span><span>mouvement_stock</span></div>
<p>Une catégorie contient plusieurs produits ; un produit a plusieurs mouvements (entrées / sorties).
C'est ce qu'on dessine dans un <b>MCD</b> ou un schéma entité-relation.</p>
"""),
Q("À quoi sert une clé étrangère ?", ["À chiffrer les données", "À relier une ligne à une ligne d'une autre table", "À trier les résultats", "À accélérer le serveur web"], 1, "La clé étrangère <code>categorie_id</code> dans <code>produit</code> indique à quelle catégorie appartient chaque produit."),
E("Exercice : dessine ton modèle", """
<p>Sur papier ou avec <a href="https://dbdiagram.io" target="_blank" rel="noopener">dbdiagram.io</a>, dessine les tables
<code>categorie</code>, <code>produit</code>, <code>mouvement_stock</code> et <code>utilisateur</code> avec leurs colonnes, clés primaires et clés étrangères.</p>
""", """
categorie(id PK, nom)
produit(id PK, nom, prix, stock, seuil_minimum, categorie_id FK -> categorie.id)
mouvement_stock(id PK, produit_id FK -> produit.id, type ENTREE/SORTIE, quantite, date_mouvement)
utilisateur(id PK, email UNIQUE, mot_de_passe_hash, role VENDEUR/ADMIN)
"""),
]},
{
"title": "SQL : créer et manipuler les données",
"slides": [
OBJ(["Créer des tables avec CREATE TABLE", "Faire le CRUD : INSERT, SELECT, UPDATE, DELETE", "Filtrer et trier avec WHERE et ORDER BY"]),
C("Créer les tables", "sql", """
CREATE DATABASE librastock;
USE librastock;

CREATE TABLE categorie (
    id  INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE produit (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    nom           VARCHAR(150) NOT NULL,
    prix          DECIMAL(10,2) NOT NULL,
    stock         INT NOT NULL DEFAULT 0,
    seuil_minimum INT NOT NULL DEFAULT 5,
    categorie_id  INT,
    FOREIGN KEY (categorie_id) REFERENCES categorie(id)
);
"""),
C("CRUD : Create, Read, Update, Delete", "sql", """
-- CREATE
INSERT INTO categorie (nom) VALUES ('Livres'), ('Papeterie');
INSERT INTO produit (nom, prix, stock, seuil_minimum, categorie_id)
VALUES ('Cahier A4', 2.50, 140, 20, 2),
       ('Stylo bleu', 0.80, 6, 30, 2),
       ('Le Petit Prince', 7.90, 12, 5, 1);

-- READ
SELECT * FROM produit;
SELECT nom, prix FROM produit WHERE prix < 5 ORDER BY prix DESC;
SELECT nom FROM produit WHERE stock < seuil_minimum;   -- alertes !

-- UPDATE (toujours avec un WHERE !)
UPDATE produit SET stock = stock - 3 WHERE id = 1;

-- DELETE (toujours avec un WHERE !)
DELETE FROM produit WHERE id = 3;
""", "⚠️ Un <code>UPDATE</code> ou <code>DELETE</code> sans <code>WHERE</code> modifie ou supprime <b>toutes</b> les lignes de la table."),
Q("Quelle requête affiche les produits dont le stock est sous le seuil ?", ["SELECT * FROM produit ORDER BY stock", "SELECT nom FROM produit WHERE stock < seuil_minimum", "UPDATE produit SET stock = 0", "DELETE FROM produit WHERE stock < 5"], 1, "<code>WHERE</code> filtre les lignes selon une condition."),
E("Exercice : requêtes CRUD", """
<ol><li>Ajoute 3 produits de ton choix.</li>
<li>Affiche tous les produits de la catégorie 2 triés par nom.</li>
<li>Augmente de 10 % le prix des livres (catégorie 1).</li>
<li>Affiche les 3 produits les plus chers (indice : <code>LIMIT</code>).</li></ol>
""", """
INSERT INTO produit (nom, prix, stock, seuil_minimum, categorie_id)
VALUES ('Gomme', 0.50, 80, 20, 2), ('Règle 30 cm', 1.20, 40, 10, 2), ('L''Étranger', 6.50, 9, 5, 1);

SELECT * FROM produit WHERE categorie_id = 2 ORDER BY nom;

UPDATE produit SET prix = prix * 1.10 WHERE categorie_id = 1;

SELECT nom, prix FROM produit ORDER BY prix DESC LIMIT 3;
""", "sql"),
]},
{
"title": "MySQL en pratique : jointures et agrégats",
"slides": [
OBJ(["Installer et lancer MySQL", "Combiner des tables avec JOIN", "Calculer avec COUNT, SUM, GROUP BY", "Livrer les scripts du module 2"]),
C("Lancer MySQL (avec Docker, recommandé)", "bash", """
docker run --name mysql-librastock \\
  -e MYSQL_ROOT_PASSWORD=secret \\
  -e MYSQL_DATABASE=librastock \\
  -p 3306:3306 -d mysql:8

# Se connecter en ligne de commande
docker exec -it mysql-librastock mysql -u root -p
""", "Sans Docker : installe MySQL Community Server + <b>MySQL Workbench</b> (interface graphique). Pour explorer la base, DBeaver est aussi un excellent outil gratuit."),
C("JOIN : combiner plusieurs tables", "sql", """
-- Nom du produit + nom de sa catégorie
SELECT p.nom AS produit, c.nom AS categorie, p.stock
FROM produit p
JOIN categorie c ON p.categorie_id = c.id;

-- LEFT JOIN : garde aussi les catégories sans produit
SELECT c.nom, p.nom
FROM categorie c
LEFT JOIN produit p ON p.categorie_id = c.id;
"""),
C("Agrégats : compter et additionner", "sql", """
-- Nombre de produits et valeur du stock par catégorie
SELECT c.nom              AS categorie,
       COUNT(p.id)        AS nb_produits,
       SUM(p.prix * p.stock) AS valeur_stock
FROM categorie c
JOIN produit p ON p.categorie_id = c.id
GROUP BY c.nom
HAVING valeur_stock > 50
ORDER BY valeur_stock DESC;
""", "<code>WHERE</code> filtre les lignes <i>avant</i> le regroupement, <code>HAVING</code> filtre les groupes <i>après</i>."),
Q("Quelle clause regroupe les lignes pour calculer un total par catégorie ?", ["ORDER BY", "GROUP BY", "LIMIT", "JOIN"], 1, "<code>GROUP BY</code> crée un groupe par valeur ; <code>SUM</code>, <code>COUNT</code>, <code>AVG</code> calculent sur chaque groupe."),
E("🎯 Livrable du module 2", """
<p>Dans ton dépôt, crée un dossier <code>database/</code> avec :</p>
<ul><li><code>schema.sql</code> : les 4 tables (categorie, produit, mouvement_stock, utilisateur) ;</li>
<li><code>data.sql</code> : au moins 3 catégories, 15 produits et 20 mouvements ;</li>
<li><code>requetes.sql</code> : 10 requêtes commentées (alertes, chiffre d'affaires par mois, top 5 des ventes…).</li></ul>
""", """
CREATE TABLE mouvement_stock (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    produit_id     INT NOT NULL,
    type           ENUM('ENTREE','SORTIE') NOT NULL,
    quantite       INT NOT NULL CHECK (quantite > 0),
    date_mouvement DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produit_id) REFERENCES produit(id)
);

-- Top 5 des produits les plus vendus
SELECT p.nom, SUM(m.quantite) AS total_vendu
FROM mouvement_stock m
JOIN produit p ON p.id = m.produit_id
WHERE m.type = 'SORTIE'
GROUP BY p.nom
ORDER BY total_vendu DESC
LIMIT 5;
""", "sql"),
]},
]},
# ---------------------------------------------------------------- MODULE 3
{
"id": "m3", "weeks": "Semaines 5 à 8", "title": "Les frameworks : Spring",
"icon": "🌱", "color": "#6DB33F",
"summary": "Construire une API REST professionnelle avec Spring Boot, reliée à MySQL et sécurisée.",
"deliverable": "Une API REST Spring Boot fonctionnelle (CRUD produits, mouvements de stock, alertes) connectée à MySQL, avec validation, gestion d'erreurs, tests et authentification JWT.",
"lessons": [
{
"title": "Introduction à Spring Boot",
"slides": [
OBJ(["Comprendre ce qu'est un framework", "Comprendre l'injection de dépendances", "Générer un projet avec Spring Initializr"]),
T("Framework : pourquoi ?", """
<p>Un <b>framework</b> est une structure prête à l'emploi : il gère la plomberie (serveur web, connexion à la base, sécurité…)
pour que tu te concentres sur la <b>logique métier</b>.</p>
<p><b>Spring</b> est le framework Java le plus utilisé. <b>Spring Boot</b> le rend simple à démarrer : configuration automatique et serveur web (Tomcat) intégré.</p>
<p><b>Injection de dépendances</b> : au lieu d'écrire <code>new ProduitService()</code> partout, Spring crée les objets (les <b>beans</b>) et te les « injecte » là où tu en as besoin.</p>
"""),
T("Créer le projet", """
<ol class="steps">
<li>Va sur <a href="https://start.spring.io" target="_blank" rel="noopener">start.spring.io</a>.</li>
<li>Project : <b>Maven</b> · Language : <b>Java</b> · Spring Boot : dernière version stable · Java : <b>21</b>.</li>
<li>Group : <code>com.librastock</code> · Artifact : <code>api</code>.</li>
<li>Dépendances : <b>Spring Web</b>, <b>Spring Data JPA</b>, <b>MySQL Driver</b>, <b>Validation</b>, <b>Lombok</b> (optionnel).</li>
<li>Clique sur <b>Generate</b>, dézippe, ouvre dans IntelliJ.</li>
</ol>
"""),
C("Structure du projet", "text", """
api/
├── pom.xml                         ← dépendances Maven
└── src/
    ├── main/
    │   ├── java/com/librastock/api/
    │   │   ├── ApiApplication.java   ← point d'entrée
    │   │   ├── controller/           ← reçoit les requêtes HTTP
    │   │   ├── service/              ← logique métier
    │   │   ├── repository/           ← accès à la base de données
    │   │   ├── model/                ← entités (tables)
    │   │   └── dto/                  ← objets échangés avec le client
    │   └── resources/
    │       └── application.properties
    └── test/                         ← tests automatisés
"""),
C("Hello Spring", "java", """
@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "LibraStock API est en ligne !";
    }
}
// Lance l'application puis ouvre http://localhost:8080/hello
"""),
Q("Que fait l'injection de dépendances ?", ["Elle injecte du SQL dans la base", "Spring crée les objets et les fournit aux classes qui en ont besoin", "Elle installe les dépendances Maven", "Elle chiffre les mots de passe"], 1, "Spring gère le cycle de vie des <b>beans</b> (@Service, @Repository, @RestController…) et les injecte via le constructeur."),
]},
{
"title": "Construire une API REST",
"slides": [
OBJ(["Comprendre les principes REST", "Créer un contrôleur CRUD", "Utiliser les bons codes HTTP", "Tester avec Postman ou curl"]),
T("Les routes de LibraStock", """
<table class="tbl">
<tr><th>Verbe</th><th>URL</th><th>Action</th><th>Réponse</th></tr>
<tr><td>GET</td><td>/api/produits</td><td>Lister</td><td>200</td></tr>
<tr><td>GET</td><td>/api/produits/{id}</td><td>Détail</td><td>200 / 404</td></tr>
<tr><td>POST</td><td>/api/produits</td><td>Créer</td><td>201</td></tr>
<tr><td>PUT</td><td>/api/produits/{id}</td><td>Modifier</td><td>200</td></tr>
<tr><td>DELETE</td><td>/api/produits/{id}</td><td>Supprimer</td><td>204</td></tr>
<tr><td>GET</td><td>/api/produits/alertes</td><td>Stock faible</td><td>200</td></tr>
</table>
<p>REST : des <b>ressources</b> (noms au pluriel) + des <b>verbes HTTP</b>. On échange du <b>JSON</b>.</p>
"""),
C("Le contrôleur", "java", """
@RestController
@RequestMapping("/api/produits")
public class ProduitController {

    private final ProduitService service;

    public ProduitController(ProduitService service) { // injection par constructeur
        this.service = service;
    }

    @GetMapping
    public List<ProduitDto> lister() {
        return service.lister();
    }

    @GetMapping("/{id}")
    public ProduitDto detail(@PathVariable Long id) {
        return service.trouver(id);
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ProduitDto creer(@Valid @RequestBody ProduitDto dto) {
        return service.creer(dto);
    }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void supprimer(@PathVariable Long id) {
        service.supprimer(id);
    }
}
"""),
C("Un DTO avec validation", "java", """
public record ProduitDto(
        Long id,
        @NotBlank String nom,
        @NotNull @Positive BigDecimal prix,
        @PositiveOrZero int stock,
        @PositiveOrZero int seuilMinimum,
        Long categorieId
) {}
""", "Un <b>DTO</b> (Data Transfer Object) définit ce que l'API reçoit et renvoie. On n'expose pas directement les entités de la base."),
C("Tester l'API", "bash", """
curl http://localhost:8080/api/produits

curl -X POST http://localhost:8080/api/produits \\
  -H "Content-Type: application/json" \\
  -d '{"nom":"Classeur","prix":3.20,"stock":25,"seuilMinimum":5,"categorieId":2}'
"""),
Q("Quel code HTTP renvoyer après la création réussie d'un produit ?", ["200 OK", "201 Created", "204 No Content", "404 Not Found"], 1, "<b>201 Created</b> indique qu'une nouvelle ressource a été créée."),
]},
{
"title": "Spring Data JPA et MySQL",
"slides": [
OBJ(["Configurer la connexion à MySQL", "Transformer une classe en table avec @Entity", "Utiliser un repository sans écrire de SQL", "Gérer les relations entre entités"]),
C("application.properties", "properties", """
spring.datasource.url=jdbc:mysql://localhost:3306/librastock
spring.datasource.username=root
spring.datasource.password=${DB_PASSWORD}
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
""", "Ne mets jamais un vrai mot de passe dans le code : utilise une variable d'environnement (<code>${DB_PASSWORD}</code>)."),
C("Une entité JPA", "java", """
@Entity
@Table(name = "produit")
public class Produit {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String nom;

    private BigDecimal prix;
    private int stock;
    private int seuilMinimum;

    @ManyToOne
    @JoinColumn(name = "categorie_id")
    private Categorie categorie;

    // constructeurs, getters, setters...
}
"""),
C("Un repository", "java", """
public interface ProduitRepository extends JpaRepository<Produit, Long> {

    // Spring génère le SQL à partir du nom de la méthode !
    List<Produit> findByCategorieNom(String nom);

    List<Produit> findByNomContainingIgnoreCase(String texte);

    @Query("SELECT p FROM Produit p WHERE p.stock < p.seuilMinimum")
    List<Produit> findEnAlerte();
}
""", "<code>JpaRepository</code> fournit déjà <code>findAll()</code>, <code>findById()</code>, <code>save()</code>, <code>deleteById()</code>…"),
C("Le service : la logique métier", "java", """
@Service
public class StockService {

    private final ProduitRepository produits;
    private final MouvementRepository mouvements;

    public StockService(ProduitRepository produits, MouvementRepository mouvements) {
        this.produits = produits;
        this.mouvements = mouvements;
    }

    @Transactional
    public void vendre(Long produitId, int quantite) {
        Produit p = produits.findById(produitId)
                .orElseThrow(() -> new RessourceIntrouvableException("Produit " + produitId));
        if (p.getStock() < quantite) {
            throw new StockInsuffisantException(p.getNom());
        }
        p.setStock(p.getStock() - quantite);
        mouvements.save(new MouvementStock(p, TypeMouvement.SORTIE, quantite));
    }
}
""", "<code>@Transactional</code> : soit tout réussit (stock mis à jour + mouvement enregistré), soit rien n'est enregistré."),
Q("Que fait spring.jpa.hibernate.ddl-auto=update ?", ["Il supprime la base à chaque démarrage", "Il met à jour le schéma des tables selon les entités", "Il met à jour Spring Boot", "Il sauvegarde la base"], 1, "Pratique en développement. En production, on préfère des migrations versionnées avec <b>Flyway</b> ou <b>Liquibase</b>."),
]},
{
"title": "Qualité : erreurs, tests et sécurité",
"slides": [
OBJ(["Renvoyer des erreurs propres", "Écrire des tests avec JUnit et MockMvc", "Comprendre l'authentification par JWT et les rôles", "Livrer l'API du module 3"]),
C("Gestion globale des erreurs", "java", """
@RestControllerAdvice
public class GestionErreurs {

    @ExceptionHandler(RessourceIntrouvableException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public Map<String, String> introuvable(RessourceIntrouvableException e) {
        return Map.of("erreur", e.getMessage());
    }

    @ExceptionHandler(StockInsuffisantException.class)
    @ResponseStatus(HttpStatus.CONFLICT)
    public Map<String, String> stock(StockInsuffisantException e) {
        return Map.of("erreur", "Stock insuffisant : " + e.getMessage());
    }
}
"""),
C("Un test d'intégration", "java", """
@SpringBootTest
@AutoConfigureMockMvc
class ProduitControllerTest {

    @Autowired MockMvc mvc;

    @Test
    void produitInexistantRenvoie404() throws Exception {
        mvc.perform(get("/api/produits/9999"))
           .andExpect(status().isNotFound());
    }

    @Test
    void creationSansNomRenvoie400() throws Exception {
        mvc.perform(post("/api/produits")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\\"prix\\": 2.5}"))
           .andExpect(status().isBadRequest());
    }
}
""", "Lance les tests avec <code>./mvnw test</code>. En semaine 13, GitHub Actions les lancera automatiquement à chaque push."),
T("Sécurité : JWT et rôles", """
<ol class="steps">
<li>L'utilisateur envoie email + mot de passe à <code>POST /api/auth/login</code>.</li>
<li>Le serveur vérifie le mot de passe (stocké <b>haché</b> avec BCrypt, jamais en clair).</li>
<li>Il renvoie un <b>token JWT</b> signé, qui contient l'identifiant et le rôle.</li>
<li>Le client envoie ce token dans chaque requête : <code>Authorization: Bearer &lt;token&gt;</code>.</li>
<li><b>Spring Security</b> vérifie le token et les droits : un <code>VENDEUR</code> peut vendre, seul un <code>ADMIN</code> peut supprimer un produit.</li>
</ol>
"""),
C("Règles d'accès avec Spring Security", "java", """
@Bean
SecurityFilterChain securite(HttpSecurity http, JwtFilter jwtFilter) throws Exception {
    return http
        .csrf(csrf -> csrf.disable())
        .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
        .authorizeHttpRequests(auth -> auth
            .requestMatchers("/api/auth/**").permitAll()
            .requestMatchers(HttpMethod.DELETE, "/api/**").hasRole("ADMIN")
            .anyRequest().authenticated())
        .addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class)
        .build();
}
"""),
Q("Comment doit-on stocker les mots de passe ?", ["En clair dans la base", "Chiffrés avec une clé dans le code", "Hachés avec un algorithme comme BCrypt", "Dans le token JWT"], 2, "Un hachage est irréversible : même en cas de fuite de la base, les mots de passe ne sont pas lisibles directement."),
E("🎯 Livrable du module 3", """
<p>Une API Spring Boot <code>librastock-api</code> avec :</p>
<ul><li>CRUD complet pour <b>produits</b> et <b>catégories</b> ;</li>
<li><code>POST /api/stock/entree</code> et <code>POST /api/stock/sortie</code> (avec mouvement enregistré) ;</li>
<li><code>GET /api/produits/alertes</code> ;</li>
<li>validation + erreurs JSON propres (400, 404, 409) ;</li>
<li>au moins 8 tests qui passent ;</li>
<li>login JWT avec rôles VENDEUR / ADMIN ;</li>
<li>un README qui explique comment lancer le projet.</li></ul>
""", """
Checklist d'auto-évaluation :
[ ] ./mvnw test → BUILD SUCCESS
[ ] Toutes les routes testées dans Postman (collection exportée dans le dépôt)
[ ] Aucun mot de passe ni secret dans le code (variables d'environnement)
[ ] Un VENDEUR reçoit 403 sur DELETE /api/produits/{id}
[ ] Vendre plus que le stock renvoie 409 et ne modifie rien
"""),
]},
]},
# ---------------------------------------------------------------- MODULE 4
{
"id": "m4", "weeks": "Semaines 9 à 12", "title": "Le front-end",
"icon": "🎨", "color": "#61DAFB",
"summary": "Créer l'interface que les utilisateurs voient : HTML, CSS puis React connecté à ton API.",
"deliverable": "Une application React LibraStock : connexion, liste des produits avec recherche, formulaire d'ajout, enregistrement d'une vente et tableau de bord des alertes, connectée à ton API Spring.",
"lessons": [
{
"title": "HTML : la structure",
"slides": [
OBJ(["Comprendre le rôle de HTML", "Utiliser les balises sémantiques", "Créer des tableaux et des formulaires"]),
T("Le trio du web", """
<ul>
<li><b>HTML</b> : la <b>structure</b> et le contenu (titres, textes, formulaires…).</li>
<li><b>CSS</b> : la <b>présentation</b> (couleurs, mise en page, responsive).</li>
<li><b>JavaScript</b> : le <b>comportement</b> (clics, appels à l'API…). React est une bibliothèque JavaScript.</li>
</ul>
<p>Un document HTML est un arbre de <b>balises</b> : <code>&lt;balise attribut="valeur"&gt;contenu&lt;/balise&gt;</code>.</p>
"""),
C("Une page sémantique", "html", """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LibraStock</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>LibraStock</h1>
    <nav><a href="#produits">Produits</a> <a href="#alertes">Alertes</a></nav>
  </header>
  <main>
    <section id="produits">
      <h2>Produits</h2>
      <table>
        <thead><tr><th>Nom</th><th>Prix</th><th>Stock</th></tr></thead>
        <tbody><tr><td>Cahier A4</td><td>2,50 €</td><td>140</td></tr></tbody>
      </table>
    </section>
  </main>
  <footer>© 2026 LibraStock</footer>
</body>
</html>
"""),
C("Un formulaire", "html", """
<form>
  <label for="nom">Nom du produit</label>
  <input id="nom" name="nom" type="text" required>

  <label for="prix">Prix (€)</label>
  <input id="prix" name="prix" type="number" step="0.01" min="0" required>

  <label for="categorie">Catégorie</label>
  <select id="categorie" name="categorie">
    <option value="1">Livres</option>
    <option value="2">Papeterie</option>
  </select>

  <button type="submit">Ajouter</button>
</form>
""", "Associe toujours un <code>&lt;label&gt;</code> à chaque champ : c'est indispensable pour l'accessibilité."),
Q("Quelle balise utiliser pour le contenu principal d'une page ?", ["<div>", "<main>", "<span>", "<b>"], 1, "<code>&lt;main&gt;</code> est une balise <b>sémantique</b> : elle donne du sens à la structure (utile pour l'accessibilité et le référencement)."),
]},
{
"title": "CSS : la mise en forme",
"slides": [
OBJ(["Cibler des éléments avec des sélecteurs", "Comprendre le modèle de boîte", "Mettre en page avec Flexbox et Grid", "Rendre une page responsive"]),
C("Sélecteurs et modèle de boîte", "css", """
/* sélecteur de balise, de classe, d'id */
body { font-family: system-ui, sans-serif; margin: 0; color: #1d1d1f; }
.carte { background: white; border-radius: 12px; }
#alertes { border-left: 4px solid crimson; }

/* Modèle de boîte : contenu + padding + border + margin */
.carte {
  padding: 16px;          /* espace intérieur */
  border: 1px solid #ddd; /* bordure */
  margin: 8px;            /* espace extérieur */
  box-sizing: border-box; /* width inclut padding et border */
}
"""),
C("Flexbox et Grid", "css", """
/* Flexbox : aligner sur une ligne */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 24px;
}

/* Grid : une grille de cartes produits */
.grille-produits {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 16px;
}
"""),
C("Responsive", "css", """
/* Mobile d'abord, puis on adapte aux grands écrans */
nav a { display: block; }

@media (min-width: 768px) {
  nav a { display: inline-block; margin-left: 16px; }
}
""", "Teste ton design dans les outils de développement du navigateur (mode appareil mobile)."),
Q("Quelle propriété transforme un conteneur en grille ?", ["display: flex", "display: grid", "position: absolute", "float: left"], 1, "<code>display: grid</code> + <code>grid-template-columns</code> définissent les colonnes."),
E("Exercice : la page catalogue", """
<p>Crée une page HTML + CSS qui affiche 6 produits sous forme de cartes (nom, catégorie, prix, stock).
Les cartes dont le stock est faible ont une bordure rouge (classe <code>.alerte</code>). Sur mobile : 1 colonne ; sur ordinateur : 3 colonnes.</p>
""", """
.grille { display: grid; grid-template-columns: 1fr; gap: 16px; }
@media (min-width: 900px) { .grille { grid-template-columns: repeat(3, 1fr); } }
.carte { padding: 16px; border: 1px solid #ddd; border-radius: 12px; }
.carte.alerte { border: 2px solid crimson; }
""", "css"),
]},
{
"title": "React : les bases",
"slides": [
OBJ(["Créer un projet React avec Vite", "Écrire des composants et utiliser JSX", "Passer des données avec les props", "Gérer l'état avec useState"]),
C("Créer le projet", "bash", """
npm create vite@latest librastock-web -- --template react
cd librastock-web
npm install
npm run dev        # ouvre http://localhost:5173
""", "Prérequis : <b>Node.js LTS</b> installé. Vite est l'outil de démarrage recommandé aujourd'hui."),
T("Composants et JSX", """
<p>Avec React, l'interface est découpée en <b>composants</b> : des fonctions qui renvoient du <b>JSX</b> (du HTML dans du JavaScript).</p>
<div class="flow"><span>App</span><span class="arrow">→</span><span>BarreRecherche</span><span class="arrow">+</span><span>ListeProduits</span><span class="arrow">→</span><span>CarteProduit ×N</span></div>
<p>Les données descendent du parent vers l'enfant via les <b>props</b>. Chaque composant peut avoir son propre <b>état</b> (<code>useState</code>) : quand l'état change, React met l'affichage à jour automatiquement.</p>
"""),
C("Props et listes", "jsx", """
function CarteProduit({ produit }) {
  const enAlerte = produit.stock < produit.seuilMinimum;
  return (
    <div className={enAlerte ? "carte alerte" : "carte"}>
      <h3>{produit.nom}</h3>
      <p>{produit.prix.toFixed(2)} € · stock : {produit.stock}</p>
      {enAlerte && <strong>⚠ À commander</strong>}
    </div>
  );
}

function ListeProduits({ produits }) {
  return (
    <div className="grille">
      {produits.map(p => <CarteProduit key={p.id} produit={p} />)}
    </div>
  );
}
"""),
C("L'état avec useState", "jsx", """
import { useState } from "react";

function Recherche({ produits }) {
  const [texte, setTexte] = useState("");

  const filtres = produits.filter(p =>
    p.nom.toLowerCase().includes(texte.toLowerCase())
  );

  return (
    <>
      <input
        placeholder="Rechercher un produit…"
        value={texte}
        onChange={e => setTexte(e.target.value)}
      />
      <ListeProduits produits={filtres} />
    </>
  );
}
"""),
Q("Que se passe-t-il quand on appelle setTexte(...) ?", ["Rien, il faut recharger la page", "React met à jour l'état et ré-affiche le composant", "La valeur est envoyée au serveur", "Le composant est supprimé"], 1, "Changer l'état déclenche un nouveau rendu du composant."),
]},
{
"title": "React connecté à l'API",
"slides": [
OBJ(["Charger des données avec useEffect et fetch", "Envoyer un formulaire à l'API", "Naviguer entre les pages avec React Router", "Livrer le front-end du module 4"]),
C("Charger les produits", "jsx", """
import { useEffect, useState } from "react";

const API = import.meta.env.VITE_API_URL; // ex. http://localhost:8080

export default function PageProduits() {
  const [produits, setProduits] = useState([]);
  const [chargement, setChargement] = useState(true);
  const [erreur, setErreur] = useState(null);

  useEffect(() => {
    fetch(`${API}/api/produits`, {
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
    })
      .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(setProduits)
      .catch(e => setErreur(e.message))
      .finally(() => setChargement(false));
  }, []); // [] = une seule fois, au premier affichage

  if (chargement) return <p>Chargement…</p>;
  if (erreur) return <p>Erreur : {erreur}</p>;
  return <ListeProduits produits={produits} />;
}
"""),
C("Envoyer un formulaire", "jsx", """
function FormulaireVente({ produitId, onSucces }) {
  const [quantite, setQuantite] = useState(1);

  async function envoyer(e) {
    e.preventDefault();
    const r = await fetch(`${API}/api/stock/sortie`, {
      method: "POST",
      headers: { "Content-Type": "application/json",
                 Authorization: `Bearer ${localStorage.getItem("token")}` },
      body: JSON.stringify({ produitId, quantite }),
    });
    if (r.status === 409) return alert("Stock insuffisant");
    onSucces();
  }

  return (
    <form onSubmit={envoyer}>
      <input type="number" min="1" value={quantite}
             onChange={e => setQuantite(Number(e.target.value))} />
      <button>Enregistrer la vente</button>
    </form>
  );
}
""", "Côté Spring, autorise l'origine du front (CORS) : <code>@CrossOrigin(\"http://localhost:5173\")</code> ou une configuration globale."),
C("Plusieurs pages avec React Router", "jsx", """
// npm install react-router-dom
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

export default function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Produits</Link> · <Link to="/alertes">Alertes</Link>
      </nav>
      <Routes>
        <Route path="/" element={<PageProduits />} />
        <Route path="/alertes" element={<PageAlertes />} />
        <Route path="/login" element={<PageLogin />} />
      </Routes>
    </BrowserRouter>
  );
}
"""),
Q("Pourquoi passer [] comme second argument de useEffect ?", ["Pour ne jamais exécuter l'effet", "Pour exécuter l'effet une seule fois au premier affichage", "Pour vider l'état", "Pour annuler fetch"], 1, "Le tableau de dépendances vide signifie : exécuter l'effet après le premier rendu uniquement."),
E("🎯 Livrable du module 4", """
<p>L'application <code>librastock-web</code> doit avoir :</p>
<ul><li>une page <b>Connexion</b> qui stocke le token JWT ;</li>
<li>une page <b>Produits</b> avec recherche et ajout (ADMIN) ;</li>
<li>l'enregistrement d'une <b>vente</b> et d'une <b>entrée</b> de stock ;</li>
<li>une page <b>Alertes</b> ;</li>
<li>un affichage propre sur mobile ;</li>
<li>la gestion du chargement et des erreurs.</li></ul>
""", """
Checklist d'auto-évaluation :
[ ] npm run build fonctionne sans erreur
[ ] L'URL de l'API vient d'une variable d'environnement (VITE_API_URL)
[ ] Un utilisateur non connecté est redirigé vers /login
[ ] Après une vente, la liste se met à jour sans recharger la page
[ ] Testé sur un écran de téléphone
"""),
]},
]},
# ---------------------------------------------------------------- MODULE 5
{
"id": "m5", "weeks": "Semaines 13 à 16", "title": "L'automatisation",
"icon": "⚙️", "color": "#2088FF",
"summary": "Automatiser les tests, le build et le déploiement avec GitHub Actions, puis livrer le projet final.",
"deliverable": "Une pipeline GitHub Actions qui teste et construit l'API et le front à chaque push, une application déployée en ligne et un dépôt portfolio soigné (README, captures, schéma d'architecture).",
"lessons": [
{
"title": "CI/CD et GitHub Actions",
"slides": [
OBJ(["Comprendre l'intégration et le déploiement continus", "Connaître le vocabulaire : workflow, job, step, runner", "Écrire un premier workflow"]),
T("Pourquoi automatiser ?", """
<ul>
<li><b>CI – Intégration continue</b> : à chaque <code>push</code> ou <i>pull request</i>, le code est automatiquement compilé et testé. Un bug est détecté en quelques minutes, pas en production.</li>
<li><b>CD – Déploiement continu</b> : si tout est vert, l'application est automatiquement construite et mise en ligne.</li>
</ul>
<div class="flow"><span>git push</span><span class="arrow">→</span><span>✅ Tests</span><span class="arrow">→</span><span>📦 Build</span><span class="arrow">→</span><span>🚀 Déploiement</span></div>
"""),
T("Le vocabulaire GitHub Actions", """
<table class="tbl">
<tr><th>Terme</th><th>Signification</th></tr>
<tr><td><b>Workflow</b></td><td>Un fichier YAML dans <code>.github/workflows/</code></td></tr>
<tr><td><b>Event</b> (<code>on</code>)</td><td>Ce qui déclenche le workflow : push, pull_request, horaire…</td></tr>
<tr><td><b>Job</b></td><td>Un groupe d'étapes exécuté sur une machine</td></tr>
<tr><td><b>Runner</b></td><td>La machine virtuelle (ex. <code>ubuntu-latest</code>)</td></tr>
<tr><td><b>Step</b></td><td>Une commande (<code>run</code>) ou une action réutilisable (<code>uses</code>)</td></tr>
</table>
"""),
C(".github/workflows/hello.yml", "yaml", """
name: Hello CI

on:
  push:
    branches: [main]

jobs:
  bonjour:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Dire bonjour
        run: echo "Bonjour depuis GitHub Actions 👋"
      - name: Lister les fichiers
        run: ls -la
"""),
Q("Où doit se trouver un fichier de workflow GitHub Actions ?", [".github/workflows/", "src/main/resources/", "workflows/ à la racine", "node_modules/"], 0, "GitHub détecte automatiquement les fichiers YAML placés dans <code>.github/workflows/</code>."),
]},
{
"title": "Pipeline pour Java et React",
"slides": [
OBJ(["Tester et construire l'API Spring automatiquement", "Construire le front React automatiquement", "Utiliser une base MySQL dans la CI", "Gérer les secrets"]),
C(".github/workflows/ci.yml", "yaml", """
name: CI LibraStock

on:
  push:
    branches: [main]
  pull_request:

jobs:
  api:
    runs-on: ubuntu-latest
    services:
      mysql:
        image: mysql:8
        env:
          MYSQL_ROOT_PASSWORD: test
          MYSQL_DATABASE: librastock
        ports: ["3306:3306"]
        options: --health-cmd="mysqladmin ping" --health-interval=10s --health-retries=5
    defaults:
      run:
        working-directory: api
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: "21"
          cache: maven
      - name: Tests et build
        run: ./mvnw -B verify
        env:
          DB_PASSWORD: test

  web:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: web
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
          cache-dependency-path: web/package-lock.json
      - run: npm ci
      - run: npm run build
"""),
T("Les secrets", """
<p>Un mot de passe, une clé de signature JWT ou un token de déploiement ne doivent <b>jamais</b> être écrits dans le code.</p>
<ol class="steps">
<li>Sur GitHub : <b>Settings → Secrets and variables → Actions → New repository secret</b>.</li>
<li>Crée par ex. <code>JWT_SECRET</code> ou <code>DEPLOY_TOKEN</code>.</li>
<li>Utilise-le dans un workflow : <code>${{ secrets.JWT_SECRET }}</code>. GitHub le masque dans les logs.</li>
</ol>
<p>Bonus : active la <b>protection de la branche main</b> pour interdire un merge tant que la CI n'est pas verte.</p>
"""),
Q("Comment utiliser un secret nommé DEPLOY_TOKEN dans un workflow ?", ["$DEPLOY_TOKEN", "${{ secrets.DEPLOY_TOKEN }}", "{{ DEPLOY_TOKEN }}", "process.env.DEPLOY_TOKEN"], 1, "La syntaxe des expressions GitHub Actions est <code>${{ ... }}</code>, et les secrets sont dans le contexte <code>secrets</code>."),
E("Exercice : casse la CI exprès", """
<ol><li>Ajoute le workflow <code>ci.yml</code> à ton projet et pousse sur main : vérifie que tout est vert dans l'onglet <b>Actions</b>.</li>
<li>Crée une branche, modifie un test pour qu'il échoue, ouvre une <i>pull request</i>.</li>
<li>Observe le ❌ rouge sur la PR, lis les logs pour trouver le test en échec.</li>
<li>Corrige, pousse à nouveau, constate le ✅.</li></ol>
""", """
Ce que tu dois retenir :
- Chaque push sur la PR relance la CI automatiquement.
- Les logs de l'étape "Tests et build" indiquent le nom du test et la ligne en échec.
- Avec la protection de branche, le bouton "Merge" reste bloqué tant que la CI est rouge.
"""),
]},
{
"title": "Déploiement et projet final",
"slides": [
OBJ(["Conteneuriser l'application avec Docker", "Déployer automatiquement", "Préparer ton portfolio et ton CV", "Livrer le projet final"]),
C("Dockerfile de l'API", "dockerfile", """
# Étape 1 : construire le .jar
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY . .
RUN mvn -B package -DskipTests

# Étape 2 : image légère pour l'exécution
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
"""),
C("docker-compose.yml : tout lancer en une commande", "yaml", """
services:
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
      MYSQL_DATABASE: librastock
    volumes: [db-data:/var/lib/mysql]
  api:
    build: ./api
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/librastock
      DB_PASSWORD: ${DB_PASSWORD}
      JWT_SECRET: ${JWT_SECRET}
    ports: ["8080:8080"]
    depends_on: [db]
volumes:
  db-data:
""", "<code>docker compose up -d</code> démarre la base et l'API. Le front React construit (<code>npm run build</code>) peut être servi par <b>Nginx</b> ou hébergé sur un service statique."),
T("Où déployer ?", """
<table class="tbl">
<tr><th>Partie</th><th>Options simples pour débuter</th></tr>
<tr><td>Front React</td><td>GitHub Pages, Netlify, Vercel</td></tr>
<tr><td>API Spring (Docker)</td><td>Render, Railway, Fly.io, ou un petit serveur VPS avec Nginx</td></tr>
<tr><td>MySQL</td><td>Base managée du même hébergeur, ou conteneur sur le VPS</td></tr>
</table>
<p>Les offres gratuites changent souvent : vérifie les conditions actuelles avant de choisir.
La plupart de ces services peuvent déployer automatiquement à chaque push sur <code>main</code>, ou via une étape de déploiement dans ton workflow.</p>
"""),
T("Ton portfolio", """
<p>Un recruteur passe environ une minute sur ton dépôt. Rends-la efficace :</p>
<ul>
<li><b>README</b> : une phrase qui explique le projet, une capture d'écran, le lien vers la démo en ligne.</li>
<li><b>Schéma d'architecture</b> : React → API Spring → MySQL, avec la pipeline CI/CD.</li>
<li><b>Stack technique</b> et <b>comment lancer le projet</b> en 3 commandes.</li>
<li>Un <b>badge CI</b> vert en haut du README.</li>
<li>Sur ton CV : « Développement d'une application fullstack (Java 21, Spring Boot, MySQL, React, Docker, GitHub Actions) » + lien.</li>
</ul>
"""),
Q("Quel est l'intérêt d'un Dockerfile en deux étapes (multi-stage) ?", ["Compiler deux fois pour être sûr", "Obtenir une image finale plus légère, sans les outils de build", "Lancer deux applications", "Remplacer GitHub Actions"], 1, "La première étape contient Maven pour compiler, la seconde seulement le JRE et le .jar : l'image est plus petite et plus sûre."),
E("🏁 Projet final", """
<p>Ton dépôt <code>librastock</code> contient :</p>
<ul><li><code>api/</code> (Spring Boot), <code>web/</code> (React), <code>database/</code> (scripts SQL) ;</li>
<li><code>docker-compose.yml</code> pour tout lancer en local ;</li>
<li>une pipeline CI verte (tests + build) et un déploiement en ligne ;</li>
<li>un README de portfolio avec capture, schéma et lien de démo.</li></ul>
<p>Présente ton projet en 3 minutes comme dans un entretien : le problème, ta solution, la stack, une difficulté rencontrée et comment tu l'as résolue.</p>
""", """
Checklist finale :
[ ] git clone + docker compose up → l'application fonctionne
[ ] Badge CI vert dans le README
[ ] Démo en ligne accessible
[ ] Aucun secret dans l'historique Git
[ ] Tu sais expliquer chaque couche : React → REST/JSON → Spring → JPA → MySQL
[ ] Tu sais expliquer la pipeline : push → tests → build → déploiement
"""),
]},
]},
]
