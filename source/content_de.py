# -*- coding: utf-8 -*-
# Deutsche Übersetzung (gleiche Folienreihenfolge wie content.py). Der Code bleibt identisch.
from i18n_helpers import *

PROJECT = """
<p>Während des gesamten Bootcamps baust du <b>eine einzige Anwendung</b> von Anfang bis Ende:
<b>LibraStock</b>, eine Lagerverwaltung für eine Buch- und Schreibwarenhandlung.</p>
<ul>
<li><b>Produkte</b>: Bücher, Hefte, Stifte … mit Preis, Lagerbestand und Kategorie.</li>
<li><b>Lagerbewegungen</b>: Eingänge (Lieferung) und Ausgänge (Verkauf).</li>
<li><b>Warnungen</b>: Liste der Produkte unter dem Mindestbestand.</li>
<li><b>Benutzer</b>: Rolle <code>VENDEUR</code> (Verkäufer) und Rolle <code>ADMIN</code>.</li>
</ul>
<p>Jedes Modul fügt einen Baustein hinzu: die Datenbank, dann die Java/Spring-API, dann die React-Oberfläche,
dann die automatische Pipeline. Am Ende hast du ein echtes Projekt für dein Portfolio.</p>
<p><small>Hinweis: Die Codebeispiele verwenden französische Namen (z. B. <code>Produit</code> = Produkt, <code>vendre</code> = verkaufen), damit der Code in allen drei Sprachen identisch ist.</small></p>
"""

MODULES = [
M("Woche 1 & 2", "Grundlagen der Informatik",
  "Verstehen, was hinter einer Webanwendung passiert: der Server, Git und die Programmiersprache Java.",
  "Ein öffentliches GitHub-Repository mit einem kleinen Java-Kommandozeilenprogramm (Produktliste im Arbeitsspeicher) und mindestens 5 sauberen Commits.",
[
L("Wie ein Server funktioniert", [
 G(["Das Client-Server-Modell erklären", "HTTP-Anfrage und -Antwort verstehen", "Die Rolle von DNS, IP-Adressen und Ports kennen", "Die wichtigsten Terminal-Befehle nutzen"]),
 TX("Client und Server", """
<p>Wenn du eine Website öffnest, unterhalten sich zwei Programme:</p>
<div class="flow"><span>🧑‍💻 Client<br><small>Browser, Handy-App</small></span><span class="arrow">→ Anfrage →</span><span>🖥️ Server<br><small>Programm, das wartet</small></span></div>
<div class="flow"><span>🧑‍💻 Client</span><span class="arrow">← Antwort ←</span><span>🖥️ Server</span></div>
<p>Ein <b>Server</b> ist nicht unbedingt eine besondere Maschine: Er ist zuerst ein <b>Programm</b>, das auf einem <b>Port</b>
auf Anfragen wartet und Antworten zurückschickt. Dieses Programm läuft auf einem Computer (physisch oder in der Cloud).</p>
<p>In unserem Projekt: Der Browser zeigt die <b>React</b>-Oberfläche (Client), die die <b>Spring-Boot</b>-API (Server) aufruft, die in <b>MySQL</b> (Datenbankserver) liest und schreibt.</p>
"""),
 TX("Die Reise einer Anfrage", """
<ol class="steps">
<li><b>Du tippst</b> <code>https://librastock.com/produits</code> ein.</li>
<li><b>DNS</b>: Das Telefonbuch des Internets übersetzt <code>librastock.com</code> in eine <b>IP</b>-Adresse (z. B. <code>51.15.20.4</code>).</li>
<li><b>Verbindung</b>: Der Browser kontaktiert diese IP auf <b>Port 443</b> (HTTPS). Port 80 = HTTP, 3306 = MySQL, 8080 = lokal meist Spring Boot.</li>
<li><b>HTTP-Anfrage</b>: <code>GET /produits</code>.</li>
<li><b>Verarbeitung</b>: Der Server führt Code aus und fragt die Datenbank ab.</li>
<li><b>HTTP-Antwort</b>: ein <b>Statuscode</b> (200, 404 …) und ein Inhalt (HTML, JSON …).</li>
</ol>
"""),
 CO("Aufbau einer HTTP-Anfrage und -Antwort", "Wichtige HTTP-Methoden: <b>GET</b> (lesen), <b>POST</b> (anlegen), <b>PUT</b> (ändern), <b>DELETE</b> (löschen). Codes: <b>2xx</b> Erfolg, <b>4xx</b> Fehler des Clients, <b>5xx</b> Fehler des Servers."),
 CO("Das Terminal: deine ersten Befehle", "Entwickler verbringen viel Zeit im Terminal. Auf dem Mac: die App <b>Terminal</b>. Unter Windows: <b>Git Bash</b> oder <b>WSL</b>."),
 QU("Was bedeutet der HTTP-Statuscode 404?", ["Der Server ist abgestürzt", "Die angefragte Ressource existiert nicht", "Die Anfrage war erfolgreich", "Man muss sich anmelden"], "404 = <i>Not Found</i>. Ein 5xx-Fehler zeigt ein Problem auf dem Server, 401/403 ein Problem mit Anmeldung oder Rechten."),
 QU("Welche Aufgabe hat das DNS?", ["Die Verbindung verschlüsseln", "Webseiten speichern", "Einen Domainnamen in eine IP-Adresse übersetzen", "Java-Code ausführen"], "Das DNS ist das Telefonbuch des Internets: Es macht aus <code>librastock.com</code> eine IP-Adresse."),
 EX("Übung: eine echte Anfrage beobachten", """
<ol><li>Öffne deinen Browser und die Entwicklertools (<kbd>F12</kbd> oder <kbd>Cmd+Option+I</kbd>), Tab <b>Netzwerk / Network</b>.</li>
<li>Lade eine beliebige Webseite neu.</li>
<li>Klicke auf die erste Anfrage und notiere: die Methode, den Statuscode, den <code>Content-Type</code> der Antwort.</li>
<li>Führe im Terminal <code>curl -i https://api.github.com/users/octocat</code> aus und finde dieselben Informationen.</li></ol>
""", """
Methode: GET
Statuscode: 200 OK
Content-Type: text/html (Webseite) oder application/json (API)
Mit curl -i werden die Header vor dem JSON-Inhalt angezeigt.
"""),
]),
L("Was ist Git?", [
 G(["Verstehen, warum man Code versioniert", "Den Ablauf add → commit → push beherrschen", "Mit Branches arbeiten", "Ein Projekt auf GitHub veröffentlichen"]),
 TX("Warum Git?", """
<p><b>Git</b> ist ein <b>Versionsverwaltungssystem</b>. Es speichert die Geschichte deines Codes als
<b>Commits</b> („Fotos“ deines Projekts zu einem bestimmten Zeitpunkt).</p>
<ul>
<li>Zurückgehen, wenn du etwas kaputt gemacht hast.</li>
<li>Im Team arbeiten, ohne die Arbeit anderer zu überschreiben.</li>
<li>Eine Idee in einem <b>Branch</b> ausprobieren, ohne die stabile Version anzufassen.</li>
</ul>
<p><b>GitHub</b> ist nicht Git: Es ist eine <b>Website</b>, die Git-Repositories online speichert (und außerdem GitHub Actions anbietet, das du in Woche 13 kennenlernst).</p>
"""),
 TX("Die 3 Bereiche von Git", """
<div class="flow"><span>📁 Arbeitsverzeichnis<br><small>deine geänderten Dateien</small></span><span class="arrow">git add →</span><span>📋 Staging-Bereich<br><small>vorgemerkt</small></span><span class="arrow">git commit →</span><span>🗄️ Lokales Repository<br><small>Historie</small></span></div>
<div class="flow"><span>🗄️ Lokales Repository</span><span class="arrow">git push →</span><span>☁️ GitHub<br><small>entferntes Repository</small></span></div>
"""),
 CO("Der Grundablauf"),
 CO("Branches", "Gute Praxis: <b>ein Branch pro Funktion</b> und klare Commit-Nachrichten im Imperativ: „Füge … hinzu“, „Behebe …“."),
 CO("Die Datei .gitignore"),
 QU("Welcher Befehl schickt deine lokalen Commits zu GitHub?", ["git commit", "git add", "git push", "git pull"], "<code>git commit</code> speichert lokal, <code>git push</code> sendet an das entfernte Repository."),
 QU("Wofür ist ein Branch da?", ["Um die Historie zu löschen", "Um eine Funktion zu entwickeln, ohne die Hauptversion anzufassen", "Um den Code zu kompilieren", "Um sich bei GitHub anzumelden"], "Ein Branch ist eine parallele Entwicklungslinie. Man führt ihn zusammen (merge), wenn die Arbeit fertig ist."),
 EX("Übung: dein erstes Repository", """
<ol><li>Erstelle einen Ordner <code>librastock</code> und initialisiere ein Git-Repository.</li>
<li>Erstelle eine Datei <code>README.md</code> mit dem Projekttitel und committe sie.</li>
<li>Erstelle einen Branch <code>docs/description</code>, ergänze eine Projektbeschreibung in der README, committe.</li>
<li>Führe den Branch in <code>main</code> zusammen und veröffentliche das Repository auf GitHub.</li></ol>
"""),
]),
L("Was ist Java?", [
 G(["JDK, JVM und Kompilierung verstehen", "Variablen, Bedingungen, Schleifen und Methoden schreiben", "Ein erstes Java-Programm ausführen"]),
 TX("Java auf einer Folie", """
<p><b>Java</b> ist eine <b>objektorientierte</b>, <b>statisch typisierte</b> Sprache, die in Unternehmen sehr verbreitet ist (Banken, Versicherungen, Behörden …). Spring Boot, das Framework aus Woche 5, ist in Java geschrieben.</p>
<div class="flow"><span>📄 Main.java<br><small>Quellcode</small></span><span class="arrow">javac →</span><span>⚙️ Main.class<br><small>Bytecode</small></span><span class="arrow">java →</span><span>☕ JVM<br><small>läuft überall</small></span></div>
<ul>
<li><b>JDK</b>: das Entwicklungspaket (Compiler + Werkzeuge). Installiere eine LTS-Version: <b>Java 21</b>.</li>
<li><b>JVM</b>: die virtuelle Maschine, die den Bytecode unter Windows, Mac oder Linux ausführt.</li>
<li>Empfohlene <b>IDE</b>: IntelliJ IDEA Community (kostenlos) oder VS Code + Java-Erweiterung.</li>
</ul>
"""),
 CO("Variablen und Datentypen"),
 CO("Bedingungen und Schleifen"),
 CO("Methoden"),
 QU("Was macht die JVM?", ["Sie kompiliert den Quellcode", "Sie führt Java-Bytecode aus", "Sie hostet Code im Internet", "Sie verwaltet die Datenbank"], "<code>javac</code> kompiliert in Bytecode, die <b>JVM</b> führt diesen Bytecode auf jedem System aus."),
 QU("Welchen Datentyp nimmst du für einen Preis wie 2.50?", ["int", "boolean", "String", "double"], "<code>double</code> speichert Dezimalzahlen. In der Praxis nimmt man für Geld eher <code>BigDecimal</code>, um Rundungsfehler zu vermeiden."),
 EX("Übung: Nachbestell-Rechner", """
<p>Schreibe eine Methode <code>quantiteACommander(int stock, int seuil, int stockCible)</code>, die
die Bestellmenge zurückgibt: 0, wenn der Bestand größer oder gleich der Schwelle ist, sonst <code>stockCible - stock</code>.
Teste sie mit (8, 10, 50) und (25, 10, 50).</p>
"""),
]),
L("Objektorientiertes Java", [
 G(["Klassen und Objekte erstellen", "Kapselung nutzen (private + Getter)", "Mit Listen (ArrayList) arbeiten", "Das Ergebnis von Modul 1 abgeben"]),
 TX("Klasse und Objekt", """
<p>Eine <b>Klasse</b> ist ein Bauplan (die Form). Ein <b>Objekt</b> ist eine konkrete Instanz, die aus diesem Bauplan entsteht.</p>
<p>Klasse <code>Produit</code> → Objekte: „Cahier A4“, „Stylo bleu“, „Le Petit Prince“ …</p>
<p>Die 4 Ideen der objektorientierten Programmierung: <b>Kapselung</b> (Daten schützen), <b>Vererbung</b>, <b>Polymorphie</b>, <b>Abstraktion</b>.
Für Spring Boot sind Kapselung und Interfaces am wichtigsten.</p>
"""),
 CO("Die Klasse Produit (Produkt)"),
 CO("Listen von Objekten"),
 QU("Warum deklariert man Attribute als private?", ["Damit das Programm schneller läuft", "Damit der Zustand des Objekts nicht beliebig verändert werden kann", "Weil Java es vorschreibt", "Um sie auf GitHub zu verstecken"], "Das ist <b>Kapselung</b>: Änderungen laufen über Methoden (wie <code>vendre()</code>), die die Regeln prüfen, z. B. nicht mehr verkaufen als vorhanden."),
 EX("🎯 Ergebnis Modul 1", """
<p>Erstelle ein Java-Kommandozeilenprogramm <b>LibraStock v0</b>:</p>
<ul><li>eine Klasse <code>Produit</code> (Name, Preis, Bestand, Mindestbestand);</li>
<li>eine Klasse <code>Inventaire</code> (Inventar) mit einer <code>List&lt;Produit&gt;</code> und den Methoden
<code>ajouter</code> (hinzufügen), <code>vendre(nom, quantite)</code> (verkaufen), <code>produitsEnAlerte()</code> (Produkte mit Warnung), <code>valeurTotaleDuStock()</code> (Gesamtwert des Lagers);</li>
<li>eine <code>main</code>-Methode, die alle Methoden vorführt.</li></ul>
<p>Veröffentliche es auf GitHub mit mindestens 5 klaren Commits.</p>
"""),
]),
]),
M("Woche 3 & 4", "Datenbanken",
  "Daten dauerhaft speichern mit SQL und MySQL.",
  "Ein Skript <code>schema.sql</code> und ein Skript <code>data.sql</code>, die die LibraStock-Datenbank anlegen und befüllen (Kategorien, Produkte, Bewegungen), plus eine Datei <code>requetes.sql</code> mit 10 nützlichen Abfragen.",
[
L("Relationale Datenbanken", [
 G(["Tabellen, Zeilen und Spalten verstehen", "Primärschlüssel und Fremdschlüssel kennen", "Die Daten von LibraStock modellieren"]),
 TX("Warum eine Datenbank?", """
<p>In Modul 1 verschwinden die Produkte, sobald das Programm endet: Sie liegen nur im Arbeitsspeicher.
Eine <b>Datenbank</b> speichert Daten <b>dauerhaft</b>, ermöglicht schnelles Suchen und das Teilen zwischen mehreren Benutzern.</p>
<p>Eine <b>relationale</b> Datenbank (MySQL, PostgreSQL …) organisiert Daten in <b>Tabellen</b>, die miteinander verknüpft sind. Abgefragt wird sie mit der Sprache <b>SQL</b>.</p>
<table class="tbl"><tr><th>id</th><th>nom</th><th>prix</th><th>stock</th><th>categorie_id</th></tr>
<tr><td>1</td><td>Cahier A4</td><td>2.50</td><td>140</td><td>2</td></tr>
<tr><td>2</td><td>Le Petit Prince</td><td>7.90</td><td>12</td><td>1</td></tr></table>
<p><small>Eine Tabelle = eine Objektart · eine Zeile = ein Datensatz · eine Spalte = ein Attribut</small></p>
"""),
 TX("Schlüssel und Beziehungen", """
<ul>
<li><b>Primärschlüssel (PRIMARY KEY)</b>: eindeutige Kennung jeder Zeile, oft eine automatisch hochgezählte <code>id</code>.</li>
<li><b>Fremdschlüssel (FOREIGN KEY)</b>: eine Spalte, die auf den Primärschlüssel einer anderen Tabelle zeigt.</li>
</ul>
<p><b>Beziehungen in LibraStock:</b></p>
<div class="flow"><span>categorie</span><span class="arrow">1 ── N</span><span>produit</span><span class="arrow">1 ── N</span><span>mouvement_stock</span></div>
<p>Eine Kategorie enthält mehrere Produkte; ein Produkt hat mehrere Bewegungen (Ein- und Ausgänge).
Das zeichnet man in einem <b>Entity-Relationship-Diagramm</b>.</p>
"""),
 QU("Wofür ist ein Fremdschlüssel da?", ["Um Daten zu verschlüsseln", "Um eine Zeile mit einer Zeile einer anderen Tabelle zu verknüpfen", "Um Ergebnisse zu sortieren", "Um den Webserver zu beschleunigen"], "Der Fremdschlüssel <code>categorie_id</code> in <code>produit</code> gibt an, zu welcher Kategorie ein Produkt gehört."),
 EX("Übung: zeichne dein Modell", """
<p>Zeichne auf Papier oder mit <a href="https://dbdiagram.io" target="_blank" rel="noopener">dbdiagram.io</a> die Tabellen
<code>categorie</code>, <code>produit</code>, <code>mouvement_stock</code> und <code>utilisateur</code> (Benutzer) mit Spalten, Primär- und Fremdschlüsseln.</p>
"""),
]),
L("SQL: Daten anlegen und bearbeiten", [
 G(["Tabellen mit CREATE TABLE anlegen", "CRUD: INSERT, SELECT, UPDATE, DELETE", "Mit WHERE und ORDER BY filtern und sortieren"]),
 CO("Die Tabellen anlegen"),
 CO("CRUD: Create, Read, Update, Delete", "⚠️ Ein <code>UPDATE</code> oder <code>DELETE</code> ohne <code>WHERE</code> ändert oder löscht <b>alle</b> Zeilen der Tabelle."),
 QU("Welche Abfrage zeigt die Produkte, deren Bestand unter der Schwelle liegt?", ["SELECT * FROM produit ORDER BY stock", "SELECT nom FROM produit WHERE stock < seuil_minimum", "UPDATE produit SET stock = 0", "DELETE FROM produit WHERE stock < 5"], "<code>WHERE</code> filtert Zeilen nach einer Bedingung."),
 EX("Übung: CRUD-Abfragen", """
<ol><li>Füge 3 Produkte deiner Wahl hinzu.</li>
<li>Zeige alle Produkte der Kategorie 2, sortiert nach Name.</li>
<li>Erhöhe den Preis der Bücher (Kategorie 1) um 10 %.</li>
<li>Zeige die 3 teuersten Produkte (Tipp: <code>LIMIT</code>).</li></ol>
"""),
]),
L("MySQL in der Praxis: Joins und Aggregate", [
 G(["MySQL installieren und starten", "Tabellen mit JOIN kombinieren", "Mit COUNT, SUM, GROUP BY rechnen", "Die Skripte von Modul 2 abgeben"]),
 CO("MySQL starten (mit Docker, empfohlen)", "Ohne Docker: MySQL Community Server + <b>MySQL Workbench</b> (grafische Oberfläche) installieren. Auch DBeaver ist ein sehr gutes kostenloses Werkzeug, um die Datenbank zu erkunden."),
 CO("JOIN: mehrere Tabellen kombinieren"),
 CO("Aggregate: zählen und summieren", "<code>WHERE</code> filtert Zeilen <i>vor</i> der Gruppierung, <code>HAVING</code> filtert Gruppen <i>danach</i>."),
 QU("Welche Klausel gruppiert Zeilen, um eine Summe pro Kategorie zu berechnen?", ["ORDER BY", "GROUP BY", "LIMIT", "JOIN"], "<code>GROUP BY</code> bildet eine Gruppe pro Wert; <code>SUM</code>, <code>COUNT</code>, <code>AVG</code> rechnen auf jeder Gruppe."),
 EX("🎯 Ergebnis Modul 2", """
<p>Lege in deinem Repository einen Ordner <code>database/</code> an mit:</p>
<ul><li><code>schema.sql</code>: die 4 Tabellen (categorie, produit, mouvement_stock, utilisateur);</li>
<li><code>data.sql</code>: mindestens 3 Kategorien, 15 Produkte und 20 Bewegungen;</li>
<li><code>requetes.sql</code>: 10 kommentierte Abfragen (Warnungen, Umsatz pro Monat, Top 5 Verkäufe …).</li></ul>
"""),
]),
]),
M("Woche 5 bis 8", "Frameworks: Spring",
  "Eine professionelle REST-API mit Spring Boot bauen, mit MySQL verbunden und abgesichert.",
  "Eine funktionierende Spring-Boot-REST-API (CRUD für Produkte, Lagerbewegungen, Warnungen), verbunden mit MySQL, mit Validierung, Fehlerbehandlung, Tests und JWT-Anmeldung.",
[
L("Einführung in Spring Boot", [
 G(["Verstehen, was ein Framework ist", "Dependency Injection verstehen", "Ein Projekt mit Spring Initializr erzeugen"]),
 TX("Warum ein Framework?", """
<p>Ein <b>Framework</b> ist ein fertiges Grundgerüst: Es kümmert sich um die Technik im Hintergrund (Webserver, Datenbankverbindung, Sicherheit …),
damit du dich auf die <b>Geschäftslogik</b> konzentrierst.</p>
<p><b>Spring</b> ist das meistgenutzte Java-Framework. <b>Spring Boot</b> macht den Einstieg einfach: automatische Konfiguration und eingebauter Webserver (Tomcat).</p>
<p><b>Dependency Injection</b>: Statt überall <code>new ProduitService()</code> zu schreiben, erzeugt Spring die Objekte (die <b>Beans</b>) und „injiziert“ sie dort, wo du sie brauchst.</p>
"""),
 TX("Das Projekt anlegen", """
<ol class="steps">
<li>Gehe auf <a href="https://start.spring.io" target="_blank" rel="noopener">start.spring.io</a>.</li>
<li>Project: <b>Maven</b> · Language: <b>Java</b> · Spring Boot: neueste stabile Version · Java: <b>21</b>.</li>
<li>Group: <code>com.librastock</code> · Artifact: <code>api</code>.</li>
<li>Abhängigkeiten: <b>Spring Web</b>, <b>Spring Data JPA</b>, <b>MySQL Driver</b>, <b>Validation</b>, <b>Lombok</b> (optional).</li>
<li>Auf <b>Generate</b> klicken, entpacken, in IntelliJ öffnen.</li>
</ol>
"""),
 CO("Projektstruktur"),
 CO("Hallo Spring"),
 QU("Was macht Dependency Injection?", ["Sie schleust SQL in die Datenbank ein", "Spring erzeugt Objekte und stellt sie den Klassen bereit, die sie brauchen", "Sie installiert Maven-Abhängigkeiten", "Sie verschlüsselt Passwörter"], "Spring verwaltet den Lebenszyklus der <b>Beans</b> (@Service, @Repository, @RestController …) und injiziert sie über den Konstruktor."),
]),
L("Eine REST-API bauen", [
 G(["Die REST-Prinzipien verstehen", "Einen CRUD-Controller erstellen", "Die richtigen HTTP-Codes verwenden", "Mit Postman oder curl testen"]),
 TX("Die Routen von LibraStock", """
<table class="tbl">
<tr><th>Methode</th><th>URL</th><th>Aktion</th><th>Antwort</th></tr>
<tr><td>GET</td><td>/api/produits</td><td>Auflisten</td><td>200</td></tr>
<tr><td>GET</td><td>/api/produits/{id}</td><td>Details</td><td>200 / 404</td></tr>
<tr><td>POST</td><td>/api/produits</td><td>Anlegen</td><td>201</td></tr>
<tr><td>PUT</td><td>/api/produits/{id}</td><td>Ändern</td><td>200</td></tr>
<tr><td>DELETE</td><td>/api/produits/{id}</td><td>Löschen</td><td>204</td></tr>
<tr><td>GET</td><td>/api/produits/alertes</td><td>Niedriger Bestand</td><td>200</td></tr>
</table>
<p>REST: <b>Ressourcen</b> (Substantive im Plural) + <b>HTTP-Methoden</b>. Ausgetauscht wird <b>JSON</b>.</p>
"""),
 CO("Der Controller"),
 CO("Ein DTO mit Validierung", "Ein <b>DTO</b> (Data Transfer Object) legt fest, was die API empfängt und zurückgibt. Die Datenbank-Entitäten werden nicht direkt nach außen gegeben."),
 CO("Die API testen"),
 QU("Welchen HTTP-Code gibt man nach dem erfolgreichen Anlegen eines Produkts zurück?", ["200 OK", "201 Created", "204 No Content", "404 Not Found"], "<b>201 Created</b> zeigt an, dass eine neue Ressource angelegt wurde."),
]),
L("Spring Data JPA und MySQL", [
 G(["Die Verbindung zu MySQL konfigurieren", "Eine Klasse mit @Entity zur Tabelle machen", "Ein Repository ohne SQL nutzen", "Beziehungen zwischen Entitäten abbilden"]),
 CO("application.properties", "Schreibe nie ein echtes Passwort in den Code: Nutze eine Umgebungsvariable (<code>${DB_PASSWORD}</code>)."),
 CO("Eine JPA-Entität"),
 CO("Ein Repository", "<code>JpaRepository</code> liefert schon <code>findAll()</code>, <code>findById()</code>, <code>save()</code>, <code>deleteById()</code> …"),
 CO("Der Service: die Geschäftslogik", "<code>@Transactional</code>: Entweder klappt alles (Bestand aktualisiert + Bewegung gespeichert) oder nichts wird gespeichert."),
 QU("Was bewirkt spring.jpa.hibernate.ddl-auto=update?", ["Es löscht die Datenbank bei jedem Start", "Es passt das Tabellenschema an die Entitäten an", "Es aktualisiert Spring Boot", "Es sichert die Datenbank"], "Praktisch in der Entwicklung. In Produktion nutzt man besser versionierte Migrationen mit <b>Flyway</b> oder <b>Liquibase</b>."),
]),
L("Qualität: Fehler, Tests und Sicherheit", [
 G(["Saubere Fehlermeldungen zurückgeben", "Tests mit JUnit und MockMvc schreiben", "Anmeldung per JWT und Rollen verstehen", "Die API von Modul 3 abgeben"]),
 CO("Zentrale Fehlerbehandlung"),
 CO("Ein Integrationstest", "Starte die Tests mit <code>./mvnw test</code>. Ab Woche 13 führt GitHub Actions sie bei jedem Push automatisch aus."),
 TX("Sicherheit: JWT und Rollen", """
<ol class="steps">
<li>Der Benutzer schickt E-Mail + Passwort an <code>POST /api/auth/login</code>.</li>
<li>Der Server prüft das Passwort (mit BCrypt <b>gehasht</b> gespeichert, nie im Klartext).</li>
<li>Er gibt ein signiertes <b>JWT-Token</b> zurück, das Kennung und Rolle enthält.</li>
<li>Der Client schickt dieses Token bei jeder Anfrage mit: <code>Authorization: Bearer &lt;token&gt;</code>.</li>
<li><b>Spring Security</b> prüft Token und Rechte: Ein <code>VENDEUR</code> (Verkäufer) darf verkaufen, nur ein <code>ADMIN</code> darf ein Produkt löschen.</li>
</ol>
"""),
 CO("Zugriffsregeln mit Spring Security"),
 QU("Wie sollten Passwörter gespeichert werden?", ["Im Klartext in der Datenbank", "Mit einem Schlüssel im Code verschlüsselt", "Mit einem Verfahren wie BCrypt gehasht", "Im JWT-Token"], "Ein Hash ist nicht umkehrbar: Selbst wenn die Datenbank abfließt, sind die Passwörter nicht direkt lesbar."),
 EX("🎯 Ergebnis Modul 3", """
<p>Eine Spring-Boot-API <code>librastock-api</code> mit:</p>
<ul><li>vollständigem CRUD für <b>Produkte</b> und <b>Kategorien</b>;</li>
<li><code>POST /api/stock/entree</code> und <code>POST /api/stock/sortie</code> (mit gespeicherter Bewegung);</li>
<li><code>GET /api/produits/alertes</code>;</li>
<li>Validierung + saubere JSON-Fehler (400, 404, 409);</li>
<li>mindestens 8 erfolgreichen Tests;</li>
<li>JWT-Login mit den Rollen VENDEUR / ADMIN;</li>
<li>einer README, die erklärt, wie man das Projekt startet.</li></ul>
""", """
Checkliste zur Selbstkontrolle:
[ ] ./mvnw test → BUILD SUCCESS
[ ] Alle Routen in Postman getestet (Collection im Repo exportiert)
[ ] Kein Passwort und kein Geheimnis im Code (Umgebungsvariablen)
[ ] Ein VENDEUR bekommt 403 bei DELETE /api/produits/{id}
[ ] Mehr verkaufen als vorhanden liefert 409 und ändert nichts
"""),
]),
]),
M("Woche 9 bis 12", "Das Frontend",
  "Die Oberfläche bauen, die Benutzer sehen: HTML, CSS und dann React, verbunden mit deiner API.",
  "Eine React-App LibraStock: Anmeldung, Produktliste mit Suche, Formular zum Anlegen, Verkauf erfassen und Übersicht der Warnungen, verbunden mit deiner Spring-API.",
[
L("HTML: die Struktur", [
 G(["Die Rolle von HTML verstehen", "Semantische Tags verwenden", "Tabellen und Formulare erstellen"]),
 TX("Das Web-Trio", """
<ul>
<li><b>HTML</b>: die <b>Struktur</b> und der Inhalt (Überschriften, Texte, Formulare …).</li>
<li><b>CSS</b>: die <b>Darstellung</b> (Farben, Layout, Responsive Design).</li>
<li><b>JavaScript</b>: das <b>Verhalten</b> (Klicks, API-Aufrufe …). React ist eine JavaScript-Bibliothek.</li>
</ul>
<p>Ein HTML-Dokument ist ein Baum aus <b>Tags</b>: <code>&lt;tag attribut="wert"&gt;Inhalt&lt;/tag&gt;</code>.</p>
"""),
 CO("Eine semantische Seite"),
 CO("Ein Formular", "Verknüpfe jedes Feld mit einem <code>&lt;label&gt;</code>: Das ist für die Barrierefreiheit unverzichtbar."),
 QU("Welches Tag nimmst du für den Hauptinhalt einer Seite?", ["<div>", "<main>", "<span>", "<b>"], "<code>&lt;main&gt;</code> ist ein <b>semantisches</b> Tag: Es gibt der Struktur Bedeutung (wichtig für Barrierefreiheit und Suchmaschinen)."),
]),
L("CSS: die Gestaltung", [
 G(["Elemente mit Selektoren ansprechen", "Das Box-Modell verstehen", "Mit Flexbox und Grid gestalten", "Eine Seite responsive machen"]),
 CO("Selektoren und Box-Modell"),
 CO("Flexbox und Grid"),
 CO("Responsive", "Teste dein Design in den Entwicklertools des Browsers (Mobilgeräte-Ansicht)."),
 QU("Welche Eigenschaft macht aus einem Container ein Raster?", ["display: flex", "display: grid", "position: absolute", "float: left"], "<code>display: grid</code> + <code>grid-template-columns</code> legen die Spalten fest."),
 EX("Übung: die Katalogseite", """
<p>Erstelle eine HTML- und CSS-Seite, die 6 Produkte als Karten anzeigt (Name, Kategorie, Preis, Bestand).
Karten mit niedrigem Bestand bekommen einen roten Rahmen (Klasse <code>.alerte</code>). Auf dem Handy: 1 Spalte; am Computer: 3 Spalten.</p>
"""),
]),
L("React: die Grundlagen", [
 G(["Ein React-Projekt mit Vite anlegen", "Komponenten schreiben und JSX nutzen", "Daten mit Props weitergeben", "Zustand mit useState verwalten"]),
 CO("Das Projekt anlegen", "Voraussetzung: <b>Node.js LTS</b> ist installiert. Vite ist heute das empfohlene Startwerkzeug."),
 TX("Komponenten und JSX", """
<p>Mit React wird die Oberfläche in <b>Komponenten</b> zerlegt: Funktionen, die <b>JSX</b> zurückgeben (HTML in JavaScript).</p>
<div class="flow"><span>App</span><span class="arrow">→</span><span>BarreRecherche</span><span class="arrow">+</span><span>ListeProduits</span><span class="arrow">→</span><span>CarteProduit ×N</span></div>
<p>Daten fließen über <b>Props</b> von der Eltern- zur Kindkomponente. Jede Komponente kann ihren eigenen <b>Zustand</b> haben (<code>useState</code>): Ändert sich der Zustand, aktualisiert React die Anzeige automatisch.</p>
"""),
 CO("Props und Listen"),
 CO("Zustand mit useState"),
 QU("Was passiert, wenn man setTexte(...) aufruft?", ["Nichts, man muss die Seite neu laden", "React aktualisiert den Zustand und zeichnet die Komponente neu", "Der Wert wird an den Server geschickt", "Die Komponente wird entfernt"], "Eine Zustandsänderung löst ein neues Rendern der Komponente aus."),
]),
L("React mit der API verbinden", [
 G(["Daten mit useEffect und fetch laden", "Ein Formular an die API senden", "Mit React Router zwischen Seiten wechseln", "Das Frontend von Modul 4 abgeben"]),
 CO("Die Produkte laden"),
 CO("Ein Formular absenden", "Erlaube auf der Spring-Seite die Herkunft des Frontends (CORS): <code>@CrossOrigin(\"http://localhost:5173\")</code> oder eine globale Konfiguration."),
 CO("Mehrere Seiten mit React Router"),
 QU("Warum übergibt man [] als zweites Argument von useEffect?", ["Damit der Effekt nie läuft", "Damit der Effekt nur einmal beim ersten Anzeigen läuft", "Um den Zustand zu leeren", "Um fetch abzubrechen"], "Ein leeres Abhängigkeits-Array bedeutet: Effekt nur nach dem ersten Rendern ausführen."),
 EX("🎯 Ergebnis Modul 4", """
<p>Die App <code>librastock-web</code> braucht:</p>
<ul><li>eine Seite <b>Anmeldung</b>, die das JWT-Token speichert;</li>
<li>eine Seite <b>Produkte</b> mit Suche und Anlegen (ADMIN);</li>
<li>das Erfassen eines <b>Verkaufs</b> und eines <b>Wareneingangs</b>;</li>
<li>eine Seite <b>Warnungen</b>;</li>
<li>eine saubere Darstellung auf dem Handy;</li>
<li>Anzeige von Ladezustand und Fehlern.</li></ul>
""", """
Checkliste zur Selbstkontrolle:
[ ] npm run build läuft ohne Fehler
[ ] Die API-URL kommt aus einer Umgebungsvariable (VITE_API_URL)
[ ] Ein nicht angemeldeter Benutzer wird auf /login umgeleitet
[ ] Nach einem Verkauf aktualisiert sich die Liste ohne Neuladen
[ ] Auf einem Handy-Bildschirm getestet
"""),
]),
]),
M("Woche 13 bis 16", "Die Automatisierung",
  "Tests, Build und Deployment mit GitHub Actions automatisieren und das Abschlussprojekt abgeben.",
  "Eine GitHub-Actions-Pipeline, die API und Frontend bei jedem Push testet und baut, eine online laufende Anwendung und ein gepflegtes Portfolio-Repository (README, Screenshots, Architekturdiagramm).",
[
L("CI/CD und GitHub Actions", [
 G(["Continuous Integration und Deployment verstehen", "Die Begriffe kennen: Workflow, Job, Step, Runner", "Einen ersten Workflow schreiben"]),
 TX("Warum automatisieren?", """
<ul>
<li><b>CI – Continuous Integration</b>: Bei jedem <code>push</code> oder <i>Pull Request</i> wird der Code automatisch kompiliert und getestet. Ein Fehler fällt nach Minuten auf, nicht erst in Produktion.</li>
<li><b>CD – Continuous Deployment</b>: Wenn alles grün ist, wird die Anwendung automatisch gebaut und veröffentlicht.</li>
</ul>
<div class="flow"><span>git push</span><span class="arrow">→</span><span>✅ Tests</span><span class="arrow">→</span><span>📦 Build</span><span class="arrow">→</span><span>🚀 Deployment</span></div>
"""),
 TX("Die Begriffe von GitHub Actions", """
<table class="tbl">
<tr><th>Begriff</th><th>Bedeutung</th></tr>
<tr><td><b>Workflow</b></td><td>Eine YAML-Datei in <code>.github/workflows/</code></td></tr>
<tr><td><b>Event</b> (<code>on</code>)</td><td>Was den Workflow auslöst: push, pull_request, Zeitplan …</td></tr>
<tr><td><b>Job</b></td><td>Eine Gruppe von Schritten auf einer Maschine</td></tr>
<tr><td><b>Runner</b></td><td>Die virtuelle Maschine (z. B. <code>ubuntu-latest</code>)</td></tr>
<tr><td><b>Step</b></td><td>Ein Befehl (<code>run</code>) oder eine wiederverwendbare Action (<code>uses</code>)</td></tr>
</table>
"""),
 CO(".github/workflows/hello.yml"),
 QU("Wo muss eine Workflow-Datei für GitHub Actions liegen?", [".github/workflows/", "src/main/resources/", "workflows/ im Hauptordner", "node_modules/"], "GitHub erkennt YAML-Dateien in <code>.github/workflows/</code> automatisch."),
]),
L("Pipeline für Java und React", [
 G(["Die Spring-API automatisch testen und bauen", "Das React-Frontend automatisch bauen", "Eine MySQL-Datenbank in der CI nutzen", "Geheimnisse (Secrets) verwalten"]),
 CO(".github/workflows/ci.yml"),
 TX("Secrets", """
<p>Ein Passwort, ein JWT-Signaturschlüssel oder ein Deployment-Token gehören <b>nie</b> in den Code.</p>
<ol class="steps">
<li>Auf GitHub: <b>Settings → Secrets and variables → Actions → New repository secret</b>.</li>
<li>Lege z. B. <code>JWT_SECRET</code> oder <code>DEPLOY_TOKEN</code> an.</li>
<li>Nutze es im Workflow: <code>${{ secrets.JWT_SECRET }}</code>. GitHub blendet es in den Logs aus.</li>
</ol>
<p>Bonus: Aktiviere den <b>Schutz des Branches main</b>, damit nicht zusammengeführt werden kann, solange die CI nicht grün ist.</p>
"""),
 QU("Wie nutzt man ein Secret namens DEPLOY_TOKEN in einem Workflow?", ["$DEPLOY_TOKEN", "${{ secrets.DEPLOY_TOKEN }}", "{{ DEPLOY_TOKEN }}", "process.env.DEPLOY_TOKEN"], "Die Ausdruckssyntax von GitHub Actions ist <code>${{ ... }}</code>, und Secrets liegen im Kontext <code>secrets</code>."),
 EX("Übung: die CI absichtlich kaputt machen", """
<ol><li>Füge den Workflow <code>ci.yml</code> deinem Projekt hinzu und pushe auf main: Prüfe im Tab <b>Actions</b>, dass alles grün ist.</li>
<li>Erstelle einen Branch, ändere einen Test so, dass er fehlschlägt, und öffne einen <i>Pull Request</i>.</li>
<li>Schau dir das rote ❌ am PR an und finde in den Logs den fehlgeschlagenen Test.</li>
<li>Korrigiere, pushe erneut und sieh das ✅.</li></ol>
""", """
Was du dir merken solltest:
- Jeder Push auf den PR startet die CI automatisch neu.
- Die Logs des Schritts "Tests et build" zeigen den Namen des fehlgeschlagenen Tests und die Zeile.
- Mit Branch-Schutz bleibt der Button "Merge" gesperrt, solange die CI rot ist.
"""),
]),
L("Deployment und Abschlussprojekt", [
 G(["Die Anwendung mit Docker in Container packen", "Automatisch deployen", "Portfolio und Lebenslauf vorbereiten", "Das Abschlussprojekt abgeben"]),
 CO("Dockerfile der API"),
 CO("docker-compose.yml: alles mit einem Befehl starten", "<code>docker compose up -d</code> startet Datenbank und API. Das gebaute React-Frontend (<code>npm run build</code>) kann von <b>Nginx</b> ausgeliefert oder bei einem Static-Hosting-Dienst gehostet werden."),
 TX("Wo deployen?", """
<table class="tbl">
<tr><th>Teil</th><th>Einfache Optionen für den Anfang</th></tr>
<tr><td>React-Frontend</td><td>GitHub Pages, Netlify, Vercel</td></tr>
<tr><td>Spring-API (Docker)</td><td>Render, Railway, Fly.io oder ein kleiner VPS mit Nginx</td></tr>
<tr><td>MySQL</td><td>Verwaltete Datenbank beim selben Anbieter oder Container auf dem VPS</td></tr>
</table>
<p>Kostenlose Angebote ändern sich oft: Prüfe die aktuellen Bedingungen, bevor du dich entscheidest.
Die meisten dieser Dienste können bei jedem Push auf <code>main</code> automatisch deployen, oder über einen Deployment-Schritt in deinem Workflow.</p>
"""),
 TX("Dein Portfolio", """
<p>Ein Recruiter schaut sich dein Repository etwa eine Minute an. Nutze sie:</p>
<ul>
<li><b>README</b>: ein Satz, der das Projekt erklärt, ein Screenshot, der Link zur Live-Demo.</li>
<li><b>Architekturdiagramm</b>: React → Spring-API → MySQL, mit der CI/CD-Pipeline.</li>
<li><b>Tech-Stack</b> und <b>wie man das Projekt startet</b> in 3 Befehlen.</li>
<li>Ein grünes <b>CI-Badge</b> oben in der README.</li>
<li>Im Lebenslauf: „Entwicklung einer Fullstack-Anwendung (Java 21, Spring Boot, MySQL, React, Docker, GitHub Actions)“ + Link.</li>
</ul>
"""),
 QU("Was bringt ein Dockerfile in zwei Stufen (Multi-Stage)?", ["Zweimal kompilieren, um sicherzugehen", "Ein kleineres Endabbild ohne Build-Werkzeuge", "Zwei Anwendungen starten", "GitHub Actions ersetzen"], "Die erste Stufe enthält Maven zum Kompilieren, die zweite nur die JRE und die .jar: Das Abbild ist kleiner und sicherer."),
 EX("🏁 Abschlussprojekt", """
<p>Dein Repository <code>librastock</code> enthält:</p>
<ul><li><code>api/</code> (Spring Boot), <code>web/</code> (React), <code>database/</code> (SQL-Skripte);</li>
<li><code>docker-compose.yml</code>, um alles lokal zu starten;</li>
<li>eine grüne CI-Pipeline (Tests + Build) und ein Online-Deployment;</li>
<li>eine Portfolio-README mit Screenshot, Diagramm und Demo-Link.</li></ul>
<p>Stelle dein Projekt in 3 Minuten vor wie im Vorstellungsgespräch: das Problem, deine Lösung, der Stack, eine Schwierigkeit und wie du sie gelöst hast.</p>
""", """
Abschluss-Checkliste:
[ ] git clone + docker compose up → die Anwendung läuft
[ ] Grünes CI-Badge in der README
[ ] Live-Demo erreichbar
[ ] Kein Geheimnis in der Git-Historie
[ ] Du kannst jede Schicht erklären: React → REST/JSON → Spring → JPA → MySQL
[ ] Du kannst die Pipeline erklären: push → Tests → Build → Deployment
"""),
]),
]),
]
