# Invisible_immobilier
Projet commun Licence 3 MIAGE à Paris-Panthéon-Sorbonne


## Contexte

On sait qu’à Paris le prix de l'immobilier peut fluctuer selon ses arrondissements :

* Mais alors quels sont critères qui influent le prix au m2?
* Quelle pourrait être l’évolution de ces prix dans le temps ?

## Problématique

Comment les nouvelles technologies et l’analyse des données nous permettent de découvrir les critères et les corrélations qui influent sur le prix de l'immobilier dans les arrondissements parisiens ?


## Enjeu

Découvrir / confirmer les critères et les corrélations qui influent sur le prix de prix immobilier. 

## Objectifs

* Définir des critères objectifs et subjectifs dans la recherche d’un bien chez une personne

* Collecter des données et les transformer en jeu de donnée 

* Afficher différentes données sur un tableau du bord selon différents arrondissements

* Calculer les corrélations entre le prix de l'immobilier et les critères sélectionnés


## Environnement

![image](modelisation/diagramme_sequence_environnement.png)

Les documents dans 8 collections sont transférés vers ElasticSearch. Pour une connexion entre MongoDB et ElasticSearch, le plugin Monstache est utilisé. 

Monstache est un processus exécuté en arrière-plan de synchronisation écrit en Go qui indexe en continu les collections MongoDB dans Elasticsearch. Monstache donne la possibilité d'utiliser Elasticsearch pour effectuer des recherches et des agrégations complexes des données MongoDB et créer facilement des visualisations et des tableaux de bord Kibana en temps réel. 


Avant de transférer les données vers Elasticsearch, il faut vérifier si les données sont bien indexées et si leurs types sont bien corrects par mapping. Le mapping est le processus de définir la manière dont un document et les champs qu'il contient sont stockés et indexés.

Elasticsearch envoie des données à Kibana pour une visualisation des critères intéressants pour chaque arrondissement. Avec les dashboards, il est possible de transformer des données d'un ou plusieurs modèles d'index en un ensemble de panneaux qui clarifient les données, racontent une histoire sur les données et permettent de se concentrer uniquement sur les données qui sont importantes. Les données triées et rangées sur les dashboards sont téléchargeables en fichier CSV.


## Fonctionnalité

![image](modelisation/diagramme_sequence_utilisateur.png)

L’utilisateur doit tout d’abord se connecter à l’interface Kibana pour consulter le dashboard. L’interface Kibana envoie ensuite une demande au système pour établir une connexion avec la base de données. Le système charge les données qui charge les données en base et les envoie à l’interface Nous utilisons ainsi la technologie ElasticSearch pour cette étape d’importation des données. L’interface effectue la mise à jour avec les données reçues et publie ces données sur le dashboard.
 
L’utilisateur peut filtrer pour trier des données par arrondissement. Lorsque l’utilisateur choisit un arrondissement et clique sur le bouton “Apply the change”, l’interface applique les changements des données par rapport aux filtres appliqués et retourne la visualisation calculée.
