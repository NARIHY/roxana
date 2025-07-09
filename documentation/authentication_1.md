# Documentation simple : Comment ajouter des rôles par défaut dans votre base de données avec Django

## Pourquoi faire ça ?

Dans votre application, vous avez besoin de créer automatiquement deux rôles importants, par exemple :

* **Visiteur** (pour les utilisateurs simples)
* **Admin** (pour les administrateurs qui ont tous les droits)

Pour ne pas avoir à créer ces rôles manuellement, on va demander au système de le faire automatiquement quand on installe ou met à jour l’application.

---

## Comment on fait ça ?

### 1. Écrire une petite fonction qui crée ces rôles

On écrit un bout de code qui va dire au système :

*“S’il n’y a pas encore de rôle nommé ‘Visiteur’, crée-le. Pareil pour ‘Admin’.”*

Cette fonction sera enregistrée dans un fichier spécial appelé **migration**.

---

### 2. Dire à Django d’exécuter cette fonction lors de la mise à jour

Dans ce fichier migration, on ne met pas juste la fonction toute seule, on l’emballe dans une instruction spéciale pour que Django sache qu’il doit la lancer automatiquement.

---

### 3. Pourquoi cette étape est importante ?

Si on oublie d’“emballer” la fonction correctement, Django essaiera de lire la fonction comme si c’était une pièce complète de travail, mais ce n’est pas le cas. Ça provoque une erreur difficile à comprendre.

---

### 4. Que se passe-t-il quand tout est bien fait ?

* Quand vous mettez à jour votre application (en lançant les commandes), Django lance cette fonction.
* Les rôles “Visiteur” et “Admin” sont créés dans la base de données.
* Vous n’avez rien à faire à la main.

---

## Résumé visuel

| Étape                 | Ce que vous écrivez dans le fichier migration           |
| --------------------- | ------------------------------------------------------- |
| 1. La fonction        | Créer ou trouver les rôles “Visiteur” et “Admin”        |
| 2. L’emballage        | Dire à Django d’exécuter cette fonction via `RunPython` |
| 3. Lancer la commande | `python manage.py migrate` (cela applique la migration) |

---

## En résumé

* **Fonction** = la recette pour créer les rôles.
* **Migration** = le moment où on dit au système de lancer cette recette.
* **RunPython** = la manière correcte d’indiquer à Django d’exécuter la recette.
* **Erreur courante** = ne pas utiliser `RunPython` et mettre juste la fonction, ce qui bloque tout.

