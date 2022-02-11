# Projet Python [Interface de connexion à un site web]

## Objectif du projet

Notre projet consiste à créer une interface de connexion + un site web en python. Dans ce projet, nous allons gérer : 
- L'ajout des nouveaux utilisateurs
- La suppression d'un utilisateur
- La mise à jour des données utilisateurs
- La connexion des utilisateurs à leur compte

## Technologie utilisée

### Dash
Dash est idéal pour créer et déployer des applications web avec des interfaces utilisateur personnalisées. Il est particulièrement adapté à tous ceux qui travaillent avec des données.
Il est construit sur des technologies matures et largement déployées :
 - Flask est un micro framework web Python
 - Plotly est une bibliothèque graphique basée sur D3.js
 - Reactjs est une bibliothèque JavaScript développée par Facebook spécialement fait pour les interfaces

Pour fonctionner, une application Dash à besoin de callback. Un callback s'écrit comme ceci : 
```@app.callback```.  
Il doit être situé avant une fonction. Cette fonction sera appelée chaque fois que la valeur du composant "input" (la zone de texte) change afin de mettre à jour les enfants du composant "output" sur la page (la div HTML).

Les callback vont modifier une autre partie de l'application qui s'appelle le layout. C'est tout le visuel de l'application, qui s'écrit en html.

## Installation des packages

Avant de lancer le projet, créer un environment python afin de faciliter la mise en production.  
En suite, il existe un fichier dans le projet nommé *package.txt* qui contient l'ensemble des packages python à installer.
Exécuter cette commande afin d'installer tout les packets :
```buildoutcfg
pip install -r package.txt
```
## Enregistrement des données
Nous avons deux fichiers enregistrant les données utilisateurs et système dans le dans dossier Data visible dans l'arborescence du projet.
- comptes.csv :  
  - Il s'agit d'un fichier enregistrant les données personnelles de l'utilisateur.
- loggs_file : 
  - Il s'agit du fichier enregistrant les loggs de connexion de l'utilisateur
  
## Composition du code

Le code est composé de deux parties essentielles :
- le front-end qui est assuré par Dash 
- le Back-end controlé par nos fonctions python

Le backend est composé par deux fichiers qui se trouvent dans apps/(Dossier contenant les modules qu'on a développés) : 
- Compte.py  
  - Ce fichier contient les fonctions gérant la gestion des comptes (insertion, suppression, etc.)
- connexion.py  
  - Ce fichier contient les fonctions gérant la connexion des utilisateurs et l'enregistrement des logg  dans le fichier
    loggs_file.csv

## Lancement du projet

Pour lancer le projet, exécuter le fichier *index.py*. Une instruction contenant un l'adresse de connexion vous sera communiquer et en cliquant dessus vous allez atterir sur la page de connexion.
```buildoutcfg
python index.py
```
