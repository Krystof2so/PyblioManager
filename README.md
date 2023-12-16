# Titre de l'application : PyblioManager
## Cahier des charges
### Objectifs :
Développer une application de gestion bibliographique utilisant Python pour faciliter la manipulation, la création, la modification et la suppression des références bibliographiques. L'application vise à fournir une interface conviviale pour les utilisateurs afin de gérer efficacement leurs bibliographies.

### Fonctionnalités attendues :
1. Saisie de nouvelles références :
   * Permettre à l'utilisateur d'ajouter de nouvelles références bibliographiques via une interface intuitive.
2. Modification des références existantes :
   * Offrir la possibilité de modifier les références déjà enregistrées dans la base de données de l'application.
3. Visualisation des références :
   * Afficher les références existantes de manière lisible et organisée pour une consultation aisée.
4. Suppression des références :
   * Permettre à l'utilisateur de supprimer des références de manière sécurisée.
5. Génération de fichiers .bib :
   * Offrir la fonctionnalité de générer des fichiers .bib à partir des références enregistrées.
6. Ouverture de fichiers .bib existants :
   * Permettre à l'utilisateur d'ouvrir et de charger des fichiers .bib existants dans l'application.
7. Affichage des répertoires et fichiers créés :
   * Afficher les répertoires et fichiers générés par l'application pour une gestion transparente des données.
8. Affichage de documentation :
   * Offrir un accès à la documentation pour guider les utilisateurs dans l'utilisation de l'application. 
9. Présentation de l'application (A propos...) :
   * Fournir des informations sur l'application, les développeurs, la version, etc.
10. Quitter l'application :
    * Permettre une sortie sécurisée de l'application.

### Architecture souhaitée :
* Utilisation de PySide6 pour l'interface graphique.
* Conception d'une interface utilisateur conviviale avec des menus dédiés à chaque fonctionnalité.
* Connexion des éléments de menu aux méthodes correspondantes pour déclencher les actions.
* Modularité et clarté du code pour faciliter les évolutions futures et la maintenance.

## Plan de développement
### Conception et mise en place de l'interface utilisateur
1. Choix de l'architecture :
   * Sélectionner la structure globale de l'interface (menus, zones d'affichage, etc.).
2. Interface des fonctionnalités de base :
   * Créer les interfaces pour la saisie, la modification, et la visualisation des références.
3. Menus et navigation :
   * Mettre en place les menus pour chaque fonctionnalité spécifique.

### Implémentation des fonctionnalités principales
1. Saisie de nouvelles références :
   * Créer la logique pour ajouter de nouvelles références dans la base de données de l'application.
2. Modification des références existantes :
   * Élaborer le processus permettant de modifier les références déjà enregistrées.
3. Visualisation des références :
   * Développer le système pour afficher de manière organisée les références existantes.
4. Suppression des références :
   * Mettre en place la fonctionnalité pour supprimer des références de la base de données.
5. Génération de fichiers .bib :
   * Implémenter le mécanisme pour générer des fichiers .bib à partir des références enregistrées.
6. Ouverture de fichiers .bib existants :
   * Élaborer la logique pour ouvrir et charger des fichiers .bib dans l'application. 

### Fonctionnalités supplémentaires et finalisation
1. Affichage des répertoires et fichiers créés :
   * Développer la fonction pour afficher les répertoires et fichiers générés par l'application.
2. Affichage de documentation :
   * Mettre en place une section pour afficher la documentation et les instructions d'utilisation.
3. Présentation de l'application (A propos...) :
   * Créer une section informant sur l'application, les développeurs, la version, etc.
4. Quitter l'application :
   * Finaliser la fonction pour permettre une sortie sécurisée de l'application.

### Tests et Débogage
1. Tests unitaires :
   * Tester chaque fonctionnalité pour s'assurer de son bon fonctionnement.
2. Tests d'intégration :
   * Tester l'ensemble de l'application pour vérifier la cohérence et l'interaction des fonctionnalités.
3. Débogage :
   * Corriger les erreurs et les bugs détectés lors des tests. 

### Documentation et évolution
1. Documentation :
   * Rédiger la documentation complète de l'application, incluant les guides d'utilisation.
2. Évolutions futures :
   * Envisager les futures améliorations ou fonctionnalités à ajouter.
