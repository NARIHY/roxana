# 🚀 Démarrage du projet ROXANA (avec JWT & Swagger)

---

## ✅ 1. Prérequis

Avant tout, assure-toi d’avoir :

* **Python ≥ 3.10** installé
* **pip** (le gestionnaire de paquets Python)
* (Facultatif mais recommandé) : **virtualenv**

---

## 📦 2. Création d’un environnement virtuel

```bash
# Dans le dossier de ton choix
python -m venv env
env\Scripts\activate  # Windows
# ou
source env/bin/activate  # Mac/Linux
```

---

## ⚙️ 3. Installer les dépendances

Crée (ou utilise) un fichier `requirements.txt` :

```txt
Django>=5.2
djangorestframework
djangorestframework-simplejwt
drf-spectacular
```

Puis installe tout :

```bash
pip install -r requirements.txt
```

---

## 🏗️ 4. Créer ou cloner le projet

Si tu **crées un nouveau projet** :

```bash
django-admin startproject narix .
python manage.py startapp accounts
python manage.py startapp stocks
python manage.py startapp contacts
```

Sinon, si tu as déjà un projet :

```bash
git clone <lien_du_projet>
cd narix
pip install -r requirements.txt
```

---

## ⚙️ 5. Configuration de base (`settings.py`)

### A. Activer les apps :

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'drf_spectacular',
    'accounts',
    'stocks',
    'contacts',
]
```

### B. Authentification personnalisée

```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

### C. REST + JWT + Spectacular

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

---

## 🗂️ 6. Créer les tables et données

```bash
# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate
```

> 💡 Cela inclura aussi les rôles "Visiteur" et "Admin" si tu as bien mis la migration personnalisée.

---

## 👤 7. Créer un superutilisateur (admin)

```bash
python manage.py createsuperuser
```

---

## 📂 8. Lancer le serveur

```bash
python manage.py runserver
```

Visite ensuite :

* `http://127.0.0.1:8000/api/docs/swagger/` (interface Swagger)
* `http://127.0.0.1:8000/admin/` (admin Django)

---

## 🔐 9. Authentification avec JWT

Utilise ces routes API :

| Action            | URL                                 | Méthode |
| ----------------- | ----------------------------------- | ------- |
| Créer compte      | `/api/accounts/register/`           | POST    |
| Connexion         | `/api/accounts/login/`              | POST    |
| Rafraîchir token  | `/api/accounts/refresh-token/`      | POST    |
| Déconnexion       | `/api/accounts/logout/`             | POST    |
| Réinitialiser mdp | `/api/accounts/password-forgotten/` | POST    |

---

## 🧪 10. Tester

Tu peux utiliser :

* **Postman**
* **curl**
* **Swagger UI** (via `/api/docs/swagger/`)

---

## 🧼 11. Nettoyage (facultatif)

Pour une base propre de test :

```bash
# Supprimer la base SQLite
rm db.sqlite3
# Supprimer les fichiers de migration
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

Puis :

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🧠 En résumé

```bash
# Initialisation rapide
python -m venv env
source env/bin/activate  # ou env\Scripts\activate sous Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

