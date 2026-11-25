# -*- coding: utf-8 -*-
# English translation (same slide order as content.py). Code stays identical.
from i18n_helpers import *

PROJECT = """
<p>Throughout the bootcamp you build <b>one single application</b>, end to end:
<b>LibraStock</b>, a stock management app for a bookshop and stationery store.</p>
<ul>
<li><b>Products</b>: books, notebooks, pens… with price, stock quantity and category.</li>
<li><b>Stock movements</b>: incoming (supplier delivery) and outgoing (sale).</li>
<li><b>Alerts</b>: list of products below their minimum level.</li>
<li><b>Users</b>: <code>VENDEUR</code> (seller) role and <code>ADMIN</code> role.</li>
</ul>
<p>Each module adds a building block: the database, then the Java/Spring API, then the React interface,
then the automated pipeline. At the end you have a real project to show in your portfolio.</p>
<p><small>Note: code examples keep French names (e.g. <code>Produit</code> = product, <code>vendre</code> = sell) so the code is identical in all three languages.</small></p>
"""

MODULES = [
M("Weeks 1 & 2", "Computer science basics",
  "Understand what happens behind a web application: the server, Git and the Java language.",
  "A public GitHub repository containing a small command-line Java program (managing an in-memory product list), with at least 5 clean commits.",
[
L("How a server works", [
 G(["Explain the client / server model", "Understand an HTTP request and response", "Know the role of DNS, IP addresses and ports", "Use basic terminal commands"]),
 TX("Client and server", """
<p>When you open a website, two programs talk to each other:</p>
<div class="flow"><span>🧑‍💻 Client<br><small>browser, mobile app</small></span><span class="arrow">→ request →</span><span>🖥️ Server<br><small>program that listens</small></span></div>
<div class="flow"><span>🧑‍💻 Client</span><span class="arrow">← response ←</span><span>🖥️ Server</span></div>
<p>A <b>server</b> is not necessarily a special machine: first of all it is a <b>program</b> that waits for requests
on a <b>port</b> and sends back responses. This program runs on a computer (physical or in the cloud).</p>
<p>In our project: the browser displays the <b>React</b> interface (client), which calls the <b>Spring Boot</b> API (server), which reads and writes to <b>MySQL</b> (database server).</p>
"""),
 TX("The journey of a request", """
<ol class="steps">
<li><b>You type</b> <code>https://librastock.com/produits</code>.</li>
<li><b>DNS</b>: the Internet's phone book translates <code>librastock.com</code> into an <b>IP</b> address (e.g. <code>51.15.20.4</code>).</li>
<li><b>Connection</b>: the browser contacts this IP on <b>port 443</b> (HTTPS). Port 80 = HTTP, 3306 = MySQL, 8080 = usually Spring Boot locally.</li>
<li><b>HTTP request</b>: <code>GET /produits</code>.</li>
<li><b>Processing</b>: the server runs code and queries the database.</li>
<li><b>HTTP response</b>: a <b>status code</b> (200, 404…) and content (HTML, JSON…).</li>
</ol>
"""),
 CO("Anatomy of an HTTP request and response", "HTTP verbs to know: <b>GET</b> (read), <b>POST</b> (create), <b>PUT</b> (update), <b>DELETE</b> (delete). Codes: <b>2xx</b> success, <b>4xx</b> client error, <b>5xx</b> server error."),
 CO("The terminal: your first commands", "Developers spend a lot of time in the terminal. On Mac: the <b>Terminal</b> app. On Windows: <b>Git Bash</b> or <b>WSL</b>."),
 QU("What does HTTP status code 404 mean?", ["The server crashed", "The requested resource does not exist", "The request succeeded", "You need to log in"], "404 = <i>Not Found</i>. A 5xx error indicates a server-side problem, 401/403 an authentication or permission problem."),
 QU("What is the role of DNS?", ["Encrypting the connection", "Storing web pages", "Translating a domain name into an IP address", "Running Java code"], "DNS is the Internet's phone book: it turns <code>librastock.com</code> into an IP address."),
 EX("Exercise: observe a real request", """
<ol><li>Open your browser, then the developer tools (<kbd>F12</kbd> or <kbd>Cmd+Option+I</kbd>), <b>Network</b> tab.</li>
<li>Reload any web page.</li>
<li>Click the first request and note: the method, the status code, the response <code>Content-Type</code>.</li>
<li>In the terminal, run <code>curl -i https://api.github.com/users/octocat</code> and find the same information.</li></ol>
""", """
Method: GET
Status code: 200 OK
Content-Type: text/html (web page) or application/json (API)
With curl -i, the headers are shown before the JSON body.
"""),
]),
L("What is Git?", [
 G(["Understand why we version code", "Master the add → commit → push cycle", "Work with branches", "Publish a project on GitHub"]),
 TX("Why Git?", """
<p><b>Git</b> is a <b>version control</b> system. It records the history of your code as
<b>commits</b> ("snapshots" of your project at a given moment).</p>
<ul>
<li>Go back in time if you break something.</li>
<li>Work as a team without overwriting each other's work.</li>
<li>Try an idea in a <b>branch</b> without touching the stable version.</li>
</ul>
<p><b>GitHub</b> is not Git: it is a <b>website</b> that hosts Git repositories online (and also offers GitHub Actions, which you'll see in week 13).</p>
"""),
 TX("The 3 areas of Git", """
<div class="flow"><span>📁 Working directory<br><small>your modified files</small></span><span class="arrow">git add →</span><span>📋 Staging area<br><small>staging</small></span><span class="arrow">git commit →</span><span>🗄️ Local repository<br><small>history</small></span></div>
<div class="flow"><span>🗄️ Local repository</span><span class="arrow">git push →</span><span>☁️ GitHub<br><small>remote repository</small></span></div>
"""),
 CO("The basic cycle"),
 CO("Branches", "Good practice: <b>one branch per feature</b>, and clear commit messages in the imperative: \"Add…\", \"Fix…\"."),
 CO("The .gitignore file"),
 QU("Which command sends your local commits to GitHub?", ["git commit", "git add", "git push", "git pull"], "<code>git commit</code> records locally, <code>git push</code> sends to the remote repository."),
 QU("What is a branch for?", ["Deleting history", "Developing a feature without touching the main version", "Compiling the code", "Logging in to GitHub"], "A branch is a parallel line of development. You merge it when the work is ready."),
 EX("Exercise: your first repository", """
<ol><li>Create a <code>librastock</code> folder and initialise a Git repository.</li>
<li>Create a <code>README.md</code> file with the project title and commit it.</li>
<li>Create a <code>docs/description</code> branch, add a project description to the README, commit.</li>
<li>Merge the branch into <code>main</code>, then publish the repository on GitHub.</li></ol>
"""),
]),
L("What is Java?", [
 G(["Understand JDK, JVM and compilation", "Write variables, conditions, loops and methods", "Run a first Java program"]),
 TX("Java in one slide", """
<p><b>Java</b> is an <b>object-oriented</b>, <b>statically typed</b> language widely used in companies (banks, insurers, public administrations…). Spring Boot, the framework you'll use in week 5, is written in Java.</p>
<div class="flow"><span>📄 Main.java<br><small>source code</small></span><span class="arrow">javac →</span><span>⚙️ Main.class<br><small>bytecode</small></span><span class="arrow">java →</span><span>☕ JVM<br><small>runs everywhere</small></span></div>
<ul>
<li><b>JDK</b>: the development kit (compiler + tools). Install an LTS version: <b>Java 21</b>.</li>
<li><b>JVM</b>: the virtual machine that runs the bytecode on Windows, Mac or Linux.</li>
<li>Recommended <b>IDE</b>: IntelliJ IDEA Community (free) or VS Code + Java extension.</li>
</ul>
"""),
 CO("Variables and types"),
 CO("Conditions and loops"),
 CO("Methods"),
 QU("What does the JVM do?", ["It compiles the source code", "It runs Java bytecode", "It hosts code on the Internet", "It manages the database"], "<code>javac</code> compiles to bytecode, the <b>JVM</b> runs that bytecode on any system."),
 QU("Which type should store a price like 2.50?", ["int", "boolean", "String", "double"], "<code>double</code> stores decimal numbers. In production, <code>BigDecimal</code> is preferred for money to avoid rounding errors."),
 EX("Exercise: restock calculator", """
<p>Write a method <code>quantiteACommander(int stock, int seuil, int stockCible)</code> that returns
the quantity to order: 0 if the stock is greater than or equal to the threshold, otherwise <code>stockCible - stock</code>.
Test it with (8, 10, 50) and (25, 10, 50).</p>
"""),
]),
L("Object-oriented Java", [
 G(["Create classes and objects", "Use encapsulation (private + getters)", "Work with lists using ArrayList", "Deliver the module 1 program"]),
 TX("Class and object", """
<p>A <b>class</b> is a blueprint (the mould). An <b>object</b> is a concrete instance created from that blueprint.</p>
<p>Class <code>Produit</code> → objects: "Cahier A4", "Stylo bleu", "Le Petit Prince"…</p>
<p>The 4 ideas of object-oriented programming: <b>encapsulation</b> (protecting data), <b>inheritance</b>, <b>polymorphism</b>, <b>abstraction</b>.
For Spring Boot, encapsulation and interfaces matter most.</p>
"""),
 CO("The Produit (product) class"),
 CO("Lists of objects"),
 QU("Why declare attributes as private?", ["To make the program faster", "To prevent the object's state from being changed arbitrarily", "Because Java requires it", "To hide them on GitHub"], "This is <b>encapsulation</b>: changes go through methods (like <code>vendre()</code>) that enforce the rules, e.g. never selling more than the stock."),
 EX("🎯 Module 1 deliverable", """
<p>Create a command-line Java program <b>LibraStock v0</b>:</p>
<ul><li>a <code>Produit</code> class (name, price, stock, minimum level);</li>
<li>an <code>Inventaire</code> class with a <code>List&lt;Produit&gt;</code> and the methods
<code>ajouter</code> (add), <code>vendre(nom, quantite)</code> (sell), <code>produitsEnAlerte()</code> (products on alert), <code>valeurTotaleDuStock()</code> (total stock value);</li>
<li>a <code>main</code> that demonstrates all the methods.</li></ul>
<p>Publish it on GitHub with at least 5 clear commits.</p>
"""),
]),
]),
M("Weeks 3 & 4", "Databases",
  "Store data durably with SQL and MySQL.",
  "A <code>schema.sql</code> script and a <code>data.sql</code> script that create and fill the LibraStock database (categories, products, movements), plus a <code>requetes.sql</code> file with 10 useful queries.",
[
L("Relational databases", [
 G(["Understand tables, rows and columns", "Know primary keys and foreign keys", "Model the LibraStock data"]),
 TX("Why a database?", """
<p>In module 1, products disappear when the program stops: they only live in memory.
A <b>database</b> stores data <b>durably</b>, lets you search it quickly and share it between several users.</p>
<p>A <b>relational</b> database (MySQL, PostgreSQL…) organises data in <b>tables</b> linked to each other. You query it with the <b>SQL</b> language.</p>
<table class="tbl"><tr><th>id</th><th>nom</th><th>prix</th><th>stock</th><th>categorie_id</th></tr>
<tr><td>1</td><td>Cahier A4</td><td>2.50</td><td>140</td><td>2</td></tr>
<tr><td>2</td><td>Le Petit Prince</td><td>7.90</td><td>12</td><td>1</td></tr></table>
<p><small>A table = one type of object · a row = one record · a column = one attribute</small></p>
"""),
 TX("Keys and relationships", """
<ul>
<li><b>Primary key (PRIMARY KEY)</b>: unique identifier of each row, often an auto-incremented <code>id</code>.</li>
<li><b>Foreign key (FOREIGN KEY)</b>: a column that points to the primary key of another table.</li>
</ul>
<p><b>Relationships in LibraStock:</b></p>
<div class="flow"><span>categorie</span><span class="arrow">1 ── N</span><span>produit</span><span class="arrow">1 ── N</span><span>mouvement_stock</span></div>
<p>A category contains several products; a product has several movements (in / out).
This is what an <b>entity-relationship diagram</b> shows.</p>
"""),
 QU("What is a foreign key for?", ["Encrypting data", "Linking a row to a row of another table", "Sorting results", "Speeding up the web server"], "The foreign key <code>categorie_id</code> in <code>produit</code> indicates which category each product belongs to."),
 EX("Exercise: draw your model", """
<p>On paper or with <a href="https://dbdiagram.io" target="_blank" rel="noopener">dbdiagram.io</a>, draw the tables
<code>categorie</code>, <code>produit</code>, <code>mouvement_stock</code> and <code>utilisateur</code> (user) with their columns, primary keys and foreign keys.</p>
"""),
]),
L("SQL: creating and handling data", [
 G(["Create tables with CREATE TABLE", "Do CRUD: INSERT, SELECT, UPDATE, DELETE", "Filter and sort with WHERE and ORDER BY"]),
 CO("Creating the tables"),
 CO("CRUD: Create, Read, Update, Delete", "⚠️ An <code>UPDATE</code> or <code>DELETE</code> without <code>WHERE</code> changes or deletes <b>every</b> row of the table."),
 QU("Which query shows the products whose stock is below the threshold?", ["SELECT * FROM produit ORDER BY stock", "SELECT nom FROM produit WHERE stock < seuil_minimum", "UPDATE produit SET stock = 0", "DELETE FROM produit WHERE stock < 5"], "<code>WHERE</code> filters rows according to a condition."),
 EX("Exercise: CRUD queries", """
<ol><li>Add 3 products of your choice.</li>
<li>Show all products of category 2 sorted by name.</li>
<li>Increase the price of books (category 1) by 10%.</li>
<li>Show the 3 most expensive products (hint: <code>LIMIT</code>).</li></ol>
"""),
]),
L("MySQL in practice: joins and aggregates", [
 G(["Install and start MySQL", "Combine tables with JOIN", "Calculate with COUNT, SUM, GROUP BY", "Deliver the module 2 scripts"]),
 CO("Start MySQL (with Docker, recommended)", "Without Docker: install MySQL Community Server + <b>MySQL Workbench</b> (graphical interface). DBeaver is also an excellent free tool for exploring the database."),
 CO("JOIN: combining several tables"),
 CO("Aggregates: counting and summing", "<code>WHERE</code> filters rows <i>before</i> grouping, <code>HAVING</code> filters groups <i>after</i>."),
 QU("Which clause groups rows to compute a total per category?", ["ORDER BY", "GROUP BY", "LIMIT", "JOIN"], "<code>GROUP BY</code> creates one group per value; <code>SUM</code>, <code>COUNT</code>, <code>AVG</code> compute on each group."),
 EX("🎯 Module 2 deliverable", """
<p>In your repository, create a <code>database/</code> folder with:</p>
<ul><li><code>schema.sql</code>: the 4 tables (categorie, produit, mouvement_stock, utilisateur);</li>
<li><code>data.sql</code>: at least 3 categories, 15 products and 20 movements;</li>
<li><code>requetes.sql</code>: 10 commented queries (alerts, revenue per month, top 5 sales…).</li></ul>
"""),
]),
]),
M("Weeks 5 to 8", "Frameworks: Spring",
  "Build a professional REST API with Spring Boot, connected to MySQL and secured.",
  "A working Spring Boot REST API (product CRUD, stock movements, alerts) connected to MySQL, with validation, error handling, tests and JWT authentication.",
[
L("Introduction to Spring Boot", [
 G(["Understand what a framework is", "Understand dependency injection", "Generate a project with Spring Initializr"]),
 TX("Why a framework?", """
<p>A <b>framework</b> is a ready-made structure: it handles the plumbing (web server, database connection, security…)
so you can focus on the <b>business logic</b>.</p>
<p><b>Spring</b> is the most widely used Java framework. <b>Spring Boot</b> makes it easy to start: auto-configuration and a built-in web server (Tomcat).</p>
<p><b>Dependency injection</b>: instead of writing <code>new ProduitService()</code> everywhere, Spring creates the objects (the <b>beans</b>) and "injects" them wherever you need them.</p>
"""),
 TX("Create the project", """
<ol class="steps">
<li>Go to <a href="https://start.spring.io" target="_blank" rel="noopener">start.spring.io</a>.</li>
<li>Project: <b>Maven</b> · Language: <b>Java</b> · Spring Boot: latest stable version · Java: <b>21</b>.</li>
<li>Group: <code>com.librastock</code> · Artifact: <code>api</code>.</li>
<li>Dependencies: <b>Spring Web</b>, <b>Spring Data JPA</b>, <b>MySQL Driver</b>, <b>Validation</b>, <b>Lombok</b> (optional).</li>
<li>Click <b>Generate</b>, unzip, open in IntelliJ.</li>
</ol>
"""),
 CO("Project structure"),
 CO("Hello Spring"),
 QU("What does dependency injection do?", ["It injects SQL into the database", "Spring creates objects and provides them to the classes that need them", "It installs Maven dependencies", "It encrypts passwords"], "Spring manages the lifecycle of <b>beans</b> (@Service, @Repository, @RestController…) and injects them via the constructor."),
]),
L("Building a REST API", [
 G(["Understand REST principles", "Create a CRUD controller", "Use the right HTTP codes", "Test with Postman or curl"]),
 TX("LibraStock routes", """
<table class="tbl">
<tr><th>Verb</th><th>URL</th><th>Action</th><th>Response</th></tr>
<tr><td>GET</td><td>/api/produits</td><td>List</td><td>200</td></tr>
<tr><td>GET</td><td>/api/produits/{id}</td><td>Detail</td><td>200 / 404</td></tr>
<tr><td>POST</td><td>/api/produits</td><td>Create</td><td>201</td></tr>
<tr><td>PUT</td><td>/api/produits/{id}</td><td>Update</td><td>200</td></tr>
<tr><td>DELETE</td><td>/api/produits/{id}</td><td>Delete</td><td>204</td></tr>
<tr><td>GET</td><td>/api/produits/alertes</td><td>Low stock</td><td>200</td></tr>
</table>
<p>REST: <b>resources</b> (plural nouns) + <b>HTTP verbs</b>. Data is exchanged as <b>JSON</b>.</p>
"""),
 CO("The controller"),
 CO("A DTO with validation", "A <b>DTO</b> (Data Transfer Object) defines what the API receives and returns. Database entities are not exposed directly."),
 CO("Testing the API"),
 QU("Which HTTP code should be returned after successfully creating a product?", ["200 OK", "201 Created", "204 No Content", "404 Not Found"], "<b>201 Created</b> indicates that a new resource was created."),
]),
L("Spring Data JPA and MySQL", [
 G(["Configure the MySQL connection", "Turn a class into a table with @Entity", "Use a repository without writing SQL", "Handle relationships between entities"]),
 CO("application.properties", "Never put a real password in the code: use an environment variable (<code>${DB_PASSWORD}</code>)."),
 CO("A JPA entity"),
 CO("A repository", "<code>JpaRepository</code> already provides <code>findAll()</code>, <code>findById()</code>, <code>save()</code>, <code>deleteById()</code>…"),
 CO("The service: business logic", "<code>@Transactional</code>: either everything succeeds (stock updated + movement saved), or nothing is saved."),
 QU("What does spring.jpa.hibernate.ddl-auto=update do?", ["It deletes the database on every start", "It updates the table schema to match the entities", "It updates Spring Boot", "It backs up the database"], "Handy in development. In production, versioned migrations with <b>Flyway</b> or <b>Liquibase</b> are preferred."),
]),
L("Quality: errors, tests and security", [
 G(["Return clean errors", "Write tests with JUnit and MockMvc", "Understand JWT authentication and roles", "Deliver the module 3 API"]),
 CO("Global error handling"),
 CO("An integration test", "Run the tests with <code>./mvnw test</code>. In week 13, GitHub Actions will run them automatically on every push."),
 TX("Security: JWT and roles", """
<ol class="steps">
<li>The user sends email + password to <code>POST /api/auth/login</code>.</li>
<li>The server checks the password (stored <b>hashed</b> with BCrypt, never in plain text).</li>
<li>It returns a signed <b>JWT token</b> containing the identifier and the role.</li>
<li>The client sends this token with every request: <code>Authorization: Bearer &lt;token&gt;</code>.</li>
<li><b>Spring Security</b> checks the token and permissions: a <code>VENDEUR</code> (seller) can sell, only an <code>ADMIN</code> can delete a product.</li>
</ol>
"""),
 CO("Access rules with Spring Security"),
 QU("How should passwords be stored?", ["In plain text in the database", "Encrypted with a key in the code", "Hashed with an algorithm like BCrypt", "In the JWT token"], "A hash is irreversible: even if the database leaks, passwords are not directly readable."),
 EX("🎯 Module 3 deliverable", """
<p>A Spring Boot API <code>librastock-api</code> with:</p>
<ul><li>full CRUD for <b>products</b> and <b>categories</b>;</li>
<li><code>POST /api/stock/entree</code> and <code>POST /api/stock/sortie</code> (with a recorded movement);</li>
<li><code>GET /api/produits/alertes</code>;</li>
<li>validation + clean JSON errors (400, 404, 409);</li>
<li>at least 8 passing tests;</li>
<li>JWT login with VENDEUR / ADMIN roles;</li>
<li>a README explaining how to run the project.</li></ul>
""", """
Self-assessment checklist:
[ ] ./mvnw test → BUILD SUCCESS
[ ] All routes tested in Postman (collection exported to the repo)
[ ] No password or secret in the code (environment variables)
[ ] A VENDEUR gets 403 on DELETE /api/produits/{id}
[ ] Selling more than the stock returns 409 and changes nothing
"""),
]),
]),
M("Weeks 9 to 12", "The front end",
  "Build the interface users see: HTML, CSS, then React connected to your API.",
  "A LibraStock React app: login, product list with search, add form, recording a sale and an alerts dashboard, connected to your Spring API.",
[
L("HTML: the structure", [
 G(["Understand the role of HTML", "Use semantic tags", "Create tables and forms"]),
 TX("The web trio", """
<ul>
<li><b>HTML</b>: the <b>structure</b> and content (headings, text, forms…).</li>
<li><b>CSS</b>: the <b>presentation</b> (colours, layout, responsive design).</li>
<li><b>JavaScript</b>: the <b>behaviour</b> (clicks, API calls…). React is a JavaScript library.</li>
</ul>
<p>An HTML document is a tree of <b>tags</b>: <code>&lt;tag attribute="value"&gt;content&lt;/tag&gt;</code>.</p>
"""),
 CO("A semantic page"),
 CO("A form", "Always associate a <code>&lt;label&gt;</code> with each field: it is essential for accessibility."),
 QU("Which tag should hold the main content of a page?", ["<div>", "<main>", "<span>", "<b>"], "<code>&lt;main&gt;</code> is a <b>semantic</b> tag: it gives meaning to the structure (useful for accessibility and SEO)."),
]),
L("CSS: styling", [
 G(["Target elements with selectors", "Understand the box model", "Lay out with Flexbox and Grid", "Make a page responsive"]),
 CO("Selectors and box model"),
 CO("Flexbox and Grid"),
 CO("Responsive", "Test your design in the browser developer tools (mobile device mode)."),
 QU("Which property turns a container into a grid?", ["display: flex", "display: grid", "position: absolute", "float: left"], "<code>display: grid</code> + <code>grid-template-columns</code> define the columns."),
 EX("Exercise: the catalogue page", """
<p>Create an HTML + CSS page that displays 6 products as cards (name, category, price, stock).
Cards with low stock get a red border (class <code>.alerte</code>). On mobile: 1 column; on desktop: 3 columns.</p>
"""),
]),
L("React: the basics", [
 G(["Create a React project with Vite", "Write components and use JSX", "Pass data with props", "Manage state with useState"]),
 CO("Create the project", "Prerequisite: <b>Node.js LTS</b> installed. Vite is today's recommended starter tool."),
 TX("Components and JSX", """
<p>With React, the interface is split into <b>components</b>: functions that return <b>JSX</b> (HTML inside JavaScript).</p>
<div class="flow"><span>App</span><span class="arrow">→</span><span>BarreRecherche</span><span class="arrow">+</span><span>ListeProduits</span><span class="arrow">→</span><span>CarteProduit ×N</span></div>
<p>Data flows down from parent to child via <b>props</b>. Each component can have its own <b>state</b> (<code>useState</code>): when the state changes, React updates the display automatically.</p>
"""),
 CO("Props and lists"),
 CO("State with useState"),
 QU("What happens when you call setTexte(...)?", ["Nothing, you must reload the page", "React updates the state and re-renders the component", "The value is sent to the server", "The component is removed"], "Changing state triggers a new render of the component."),
]),
L("React connected to the API", [
 G(["Load data with useEffect and fetch", "Send a form to the API", "Navigate between pages with React Router", "Deliver the module 4 front end"]),
 CO("Loading the products"),
 CO("Submitting a form", "On the Spring side, allow the front-end origin (CORS): <code>@CrossOrigin(\"http://localhost:5173\")</code> or a global configuration."),
 CO("Several pages with React Router"),
 QU("Why pass [] as the second argument of useEffect?", ["To never run the effect", "To run the effect only once on first render", "To clear the state", "To cancel fetch"], "An empty dependency array means: run the effect after the first render only."),
 EX("🎯 Module 4 deliverable", """
<p>The <code>librastock-web</code> app must have:</p>
<ul><li>a <b>Login</b> page that stores the JWT token;</li>
<li>a <b>Products</b> page with search and add (ADMIN);</li>
<li>recording a <b>sale</b> and a stock <b>delivery</b>;</li>
<li>an <b>Alerts</b> page;</li>
<li>a clean display on mobile;</li>
<li>loading and error handling.</li></ul>
""", """
Self-assessment checklist:
[ ] npm run build runs without errors
[ ] The API URL comes from an environment variable (VITE_API_URL)
[ ] A logged-out user is redirected to /login
[ ] After a sale, the list updates without reloading the page
[ ] Tested on a phone screen
"""),
]),
]),
M("Weeks 13 to 16", "Automation",
  "Automate tests, builds and deployment with GitHub Actions, then deliver the final project.",
  "A GitHub Actions pipeline that tests and builds the API and the front end on every push, an application deployed online and a polished portfolio repository (README, screenshots, architecture diagram).",
[
L("CI/CD and GitHub Actions", [
 G(["Understand continuous integration and deployment", "Know the vocabulary: workflow, job, step, runner", "Write a first workflow"]),
 TX("Why automate?", """
<ul>
<li><b>CI – Continuous Integration</b>: on every <code>push</code> or <i>pull request</i>, the code is automatically compiled and tested. A bug is caught within minutes, not in production.</li>
<li><b>CD – Continuous Deployment</b>: if everything is green, the application is automatically built and released.</li>
</ul>
<div class="flow"><span>git push</span><span class="arrow">→</span><span>✅ Tests</span><span class="arrow">→</span><span>📦 Build</span><span class="arrow">→</span><span>🚀 Deploy</span></div>
"""),
 TX("GitHub Actions vocabulary", """
<table class="tbl">
<tr><th>Term</th><th>Meaning</th></tr>
<tr><td><b>Workflow</b></td><td>A YAML file in <code>.github/workflows/</code></td></tr>
<tr><td><b>Event</b> (<code>on</code>)</td><td>What triggers the workflow: push, pull_request, schedule…</td></tr>
<tr><td><b>Job</b></td><td>A group of steps run on one machine</td></tr>
<tr><td><b>Runner</b></td><td>The virtual machine (e.g. <code>ubuntu-latest</code>)</td></tr>
<tr><td><b>Step</b></td><td>A command (<code>run</code>) or a reusable action (<code>uses</code>)</td></tr>
</table>
"""),
 CO(".github/workflows/hello.yml"),
 QU("Where must a GitHub Actions workflow file be located?", [".github/workflows/", "src/main/resources/", "workflows/ at the root", "node_modules/"], "GitHub automatically detects YAML files placed in <code>.github/workflows/</code>."),
]),
L("A pipeline for Java and React", [
 G(["Test and build the Spring API automatically", "Build the React front end automatically", "Use a MySQL database in CI", "Manage secrets"]),
 CO(".github/workflows/ci.yml"),
 TX("Secrets", """
<p>A password, a JWT signing key or a deployment token must <b>never</b> be written in the code.</p>
<ol class="steps">
<li>On GitHub: <b>Settings → Secrets and variables → Actions → New repository secret</b>.</li>
<li>Create e.g. <code>JWT_SECRET</code> or <code>DEPLOY_TOKEN</code>.</li>
<li>Use it in a workflow: <code>${{ secrets.JWT_SECRET }}</code>. GitHub masks it in the logs.</li>
</ol>
<p>Bonus: enable <b>branch protection on main</b> to block merging while CI is not green.</p>
"""),
 QU("How do you use a secret named DEPLOY_TOKEN in a workflow?", ["$DEPLOY_TOKEN", "${{ secrets.DEPLOY_TOKEN }}", "{{ DEPLOY_TOKEN }}", "process.env.DEPLOY_TOKEN"], "The GitHub Actions expression syntax is <code>${{ ... }}</code>, and secrets live in the <code>secrets</code> context."),
 EX("Exercise: break the CI on purpose", """
<ol><li>Add the <code>ci.yml</code> workflow to your project and push to main: check that everything is green in the <b>Actions</b> tab.</li>
<li>Create a branch, change a test so it fails, open a <i>pull request</i>.</li>
<li>Look at the red ❌ on the PR, read the logs to find the failing test.</li>
<li>Fix it, push again, see the ✅.</li></ol>
""", """
What to remember:
- Every push to the PR re-runs CI automatically.
- The logs of the "Tests et build" step show the name of the failing test and the line.
- With branch protection, the "Merge" button stays blocked while CI is red.
"""),
]),
L("Deployment and final project", [
 G(["Containerise the application with Docker", "Deploy automatically", "Prepare your portfolio and CV", "Deliver the final project"]),
 CO("API Dockerfile"),
 CO("docker-compose.yml: start everything with one command", "<code>docker compose up -d</code> starts the database and the API. The built React front end (<code>npm run build</code>) can be served by <b>Nginx</b> or hosted on a static hosting service."),
 TX("Where to deploy?", """
<table class="tbl">
<tr><th>Part</th><th>Simple options to start with</th></tr>
<tr><td>React front end</td><td>GitHub Pages, Netlify, Vercel</td></tr>
<tr><td>Spring API (Docker)</td><td>Render, Railway, Fly.io, or a small VPS with Nginx</td></tr>
<tr><td>MySQL</td><td>Managed database from the same host, or a container on the VPS</td></tr>
</table>
<p>Free tiers change often: check the current terms before choosing.
Most of these services can deploy automatically on every push to <code>main</code>, or via a deployment step in your workflow.</p>
"""),
 TX("Your portfolio", """
<p>A recruiter spends about one minute on your repository. Make it count:</p>
<ul>
<li><b>README</b>: one sentence explaining the project, a screenshot, the link to the live demo.</li>
<li><b>Architecture diagram</b>: React → Spring API → MySQL, with the CI/CD pipeline.</li>
<li><b>Tech stack</b> and <b>how to run the project</b> in 3 commands.</li>
<li>A green <b>CI badge</b> at the top of the README.</li>
<li>On your CV: "Built a fullstack application (Java 21, Spring Boot, MySQL, React, Docker, GitHub Actions)" + link.</li>
</ul>
"""),
 QU("What is the benefit of a two-stage (multi-stage) Dockerfile?", ["Compiling twice to be safe", "Getting a lighter final image without the build tools", "Running two applications", "Replacing GitHub Actions"], "The first stage contains Maven to compile, the second only the JRE and the .jar: the image is smaller and safer."),
 EX("🏁 Final project", """
<p>Your <code>librastock</code> repository contains:</p>
<ul><li><code>api/</code> (Spring Boot), <code>web/</code> (React), <code>database/</code> (SQL scripts);</li>
<li><code>docker-compose.yml</code> to run everything locally;</li>
<li>a green CI pipeline (tests + build) and an online deployment;</li>
<li>a portfolio README with screenshot, diagram and demo link.</li></ul>
<p>Present your project in 3 minutes as in a job interview: the problem, your solution, the stack, one difficulty you met and how you solved it.</p>
""", """
Final checklist:
[ ] git clone + docker compose up → the application works
[ ] Green CI badge in the README
[ ] Live demo accessible
[ ] No secret in the Git history
[ ] You can explain each layer: React → REST/JSON → Spring → JPA → MySQL
[ ] You can explain the pipeline: push → tests → build → deploy
"""),
]),
]),
]
