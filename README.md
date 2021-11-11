# Lab 4 - Création d’une suite de tests Python

## Auteur

Laboratoire créé par Alan Brucher

## Installation

Ouvrez le fichier sur VS Code

**Verifiez que vous utilisez Python 3 et que les extensions Python sont instalées**

Utiliser la commande "pip install -r requirements.txt" pour installer les librairies nécésaires

Utiliser l'environement virtuel

Modifier le BEARER_TOKEN dans le fichier TwitterAPI.py si besoin

> :warning:	Les variables booléennes "save_tweets_succes" et "load_tweets_succes" simule le fonctionnement de la database

> De préférence, si vous voulez utiliser normalement le code, mettez les valeurs a True pour faire fonctionner la database

> Si vous voulez vérifier les tests unitaires de la database, mettez les valeurs a False pour simuler un disfonctionnement

## Utilisation normale

Lancer le ficher main.py

Utiliser ce lien : http://localhost:8080

Entrez un mot-clé dans la barre "Query" et appuyer sur "Send"

## Utilisation tests unitaires

Aller dans l'onglet "testing" à gauche

Et appuyer sur le boutons "Run tests" en haut

## Sources 

Intervalle max_results: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/paginate

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
