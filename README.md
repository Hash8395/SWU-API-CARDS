# Star Wars Unlimited API

## Description

L'API **Star Wars Unlimited** permet d'accéder aux informations des cartes du jeu de cartes Star Wars, issues de plusieurs sets (par exemple, SHD et SOR). Elle offre des points de terminaison permettant de récupérer les détails des cartes par numéro, par type, par coût, et plus encore.

L'API est construite avec **FastAPI**, un framework moderne et rapide pour créer des APIs RESTful en Python. Elle inclut une documentation interactive générée automatiquement grâce à **Swagger UI**.

## Fonctionnalités

- **Récupérer une carte par son numéro** : Permet de récupérer une carte spécifique d'un set donné en fonction de son numéro unique.
- **Récupérer toutes les cartes d'un set** : Récupère toutes les cartes d'un set donné.
- **Requêtes supplémentaires** : Des points de terminaison pour filtrer les cartes selon des critères spécifiques comme le type ou le coût.

## Points de terminaison

### 1. `/`

Retourne un message de bienvenue pour l'API.

- **Méthode** : `GET`
- **Réponse** : `{"message": "Bienvenue dans l'API Star Wars Unlimited"}`

### 2. `/cards/{set_name}/{card_number}`

Permet de récupérer les détails d'une carte spécifique d'un set.

- **Méthode** : `GET`
- **Paramètres** :
  - `set_name` : Le nom du set (par exemple, "SHD", "SOR").
  - `card_number` : Le numéro unique de la carte dans le set.
- **Réponse** : Détails de la carte, incluant son nom, son coût, ses traits, etc.

### 3. `/cards/{set_name}`

Retourne toutes les cartes d'un set spécifique.

- **Méthode** : `GET`
- **Paramètres** :
  - `set_name` : Le nom du set (par exemple, "SHD", "SOR").
- **Réponse** : Liste des cartes du set, avec leurs détails.

### 4. `/cards/type`

Permet de filtrer les cartes par type.

- **Méthode** : `GET`
- **Réponse** : Liste des cartes filtrées par type (ex. "Leader", "Trooper", etc.).

### 5. `/cards/cost`

Permet de filtrer les cartes par coût.

- **Méthode** : `GET`
- **Réponse** : Liste des cartes filtrées par coût (par exemple, toutes les cartes coûtant 5 ressources).

## Swagger UI

Une interface Swagger UI interactive est disponible à l'adresse suivante pour explorer et tester facilement l'API :

http://localhost:8000/docs


## Installation

### Prérequis

- **Python 3.7+**
- **Pip** pour installer les dépendances

### Étapes d'installation

1. Clonez ce repository :

    ```bash
    git clone https://votre-url-de-repository.git
    ```

2. Installez les dépendances via `pip` :

    ```bash
    pip install -r requirements.txt
    ```

3. Lancez le serveur FastAPI :

    ```bash
    uvicorn main:app --reload
    ```

4. L'API sera accessible sur `http://localhost:8000`.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer l'API, veuillez soumettre une pull request avec des explications sur vos changements. Vous pouvez aussi ouvrir une issue pour suggérer de nouvelles fonctionnalités.

## Licence

Ce projet est sous la licence MIT. Voir le fichier `LICENSE` pour plus d'informations.


