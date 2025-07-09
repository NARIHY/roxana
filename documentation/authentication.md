# Documentation : Création de données par défaut via migration Django

## Objectif

Créer des rôles par défaut (`Visiteur` et `Admin`) dans la table `Role` de l’application `accounts` automatiquement lors d’une migration.

---

## Étape 1 : Créer une fonction Python qui insère les données

Dans le fichier de migration (exemple : `accounts/migrations/0002_create_default_roles.py`), définissez une fonction :

```python
from django.db import migrations

def create_default_roles(apps, schema_editor):
    Role = apps.get_model('accounts', 'Role')
    Role.objects.get_or_create(name='Visiteur')
    Role.objects.get_or_create(name='Admin')
```

---

## Étape 2 : Ajouter l’opération `RunPython` dans la migration

Le fichier de migration complet doit ressembler à ceci :

```python
from django.db import migrations

def create_default_roles(apps, schema_editor):
    Role = apps.get_model('accounts', 'Role')
    Role.objects.get_or_create(name='Visiteur')
    Role.objects.get_or_create(name='Admin')

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_roles),
    ]
```

---

## Étape 3 : Explication de l’erreur courante

### Erreur rencontrée

```
AttributeError: 'function' object has no attribute 'state_forwards'
```

### Cause

Dans `operations`, la fonction Python est passée **directement** au lieu d’être enveloppée par `migrations.RunPython`. Django attend une instance d’opération, pas une fonction brute.

---

## Étape 4 : Correction de l’erreur

* Toujours utiliser `migrations.RunPython` pour appeler une fonction d’opération personnalisée.

---

## Étape 5 : Appliquer la migration

Lancez la commande Django pour créer et appliquer la migration :

```bash
python manage.py makemigrations accounts
python manage.py migrate
```

---

## Résumé rapide

| Étape                         | Exemple                                              |
| ----------------------------- | ---------------------------------------------------- |
| Fonction pour insérer données | `def create_default_roles(apps, schema_editor): ...` |
| Ajouter dans `operations`     | `migrations.RunPython(create_default_roles)`         |
| Commandes terminal            | `makemigrations` puis `migrate`                      |

---

## Conseils

* Utilisez `apps.get_model()` dans les migrations pour récupérer les modèles.
* Ne modifiez pas directement vos modèles dans la fonction de migration.
* Toujours envelopper vos fonctions dans `migrations.RunPython()` dans la liste `operations`.


