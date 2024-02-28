# Tests d'API avec Pytest

Ce projet contient les tests d'API pour __PROJECT_NAME__.

## Exécution des tests

pytest -s -v


## Structure du projet

* `README.md`: Ce fichier.
* `config`: Contient les fichiers de configuration pour différents environnements.
* `test`: Contient les fichiers de test.
* `utils`: Contient des modules utilitaires.

## Configuration

Le fichier `test.ini` contient la structure de base pour les paramètres de l'application, tels que l'API, la base de données et le SMTP. Vous pouvez adapter la structure et les valeurs en fonction de vos besoins.

## Tests

Le fichier `api_tests.py` contient des exemples de tests pour l'API. Vous pouvez ajouter d'autres tests et utiliser les marqueurs `slow` et `integration` pour les catégoriser.

## Remarques

* Assurez-vous de remplacer les valeurs par défaut dans les fichiers `.ini` avec les informations de votre application.
* Vous pouvez adapter le code et la configuration en fonction de vos besoins spécifiques.

## Ressources supplémentaires

* Documentation de Pytest: [https://pytest.org/](https://pytest.org/)