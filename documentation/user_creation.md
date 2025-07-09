# 🔐 Authentification dans votre API Django avec JWT

---

## 🔸 1. Qu’est-ce que l’authentification avec JWT ?

L’authentification permet de vérifier l’identité d’un utilisateur (comme une porte avec une clé).

Avec JWT (JSON Web Token), le système ne garde pas l’utilisateur “connecté” sur le serveur. Au lieu de ça :

* L’utilisateur **envoie ses identifiants (email + mot de passe)**.
* Le serveur **génère un "token" (clé temporaire)**.
* Ce token est utilisé dans chaque requête pour prouver que l’utilisateur est connecté.

---

## 🔄 2. Le cycle d’authentification JWT

### 🔹 Étapes :

1. **Connexion** – `POST /api/accounts/login/`

   * Envoie `email` + `password`
   * Reçoit :

     * `access_token` (valable 5 minutes)
     * `refresh_token` (valable 1 jour)

2. **Accès à une ressource protégée** – `GET /api/stocks/`

   * Envoie `Authorization: Bearer <access_token>`
   * Le serveur vérifie que le token est toujours valide.

3. **Renouvellement du token** – `POST /api/accounts/refresh-token/`

   * Envoie `refresh_token`
   * Reçoit un nouveau `access_token`.

4. **Déconnexion** – `POST /api/accounts/logout/`

   * Le `refresh_token` est invalidé (blacklisté).

---

## 🔐 Permissions

Dans votre projet, tous les endpoints sous `/api/` nécessitent une authentification sauf :

* `/register/` → création de compte
* `/login/` → connexion
* `/password-forgotten/` → réinitialisation de mot de passe

Les autres routes nécessitent un token JWT (`Bearer <token>` dans l’en-tête HTTP).

---

## 🛠️ Comment créer un utilisateur

### ➤ A. Par la console

```bash
python manage.py shell
```

Puis :

```python
from accounts.models import CustomUser, Role

# Crée un rôle "Visiteur" s'il n'existe pas
role, _ = Role.objects.get_or_create(name='Visiteur')

# Crée l’utilisateur
user = CustomUser.objects.create_user(
    email="dev@example.com",
    password="motdepasse123",
    first_name="Jean",
    last_name="Dupont",
    gender="H",
    role=role
)
```

### ➤ B. Par API (endpoint `POST /api/accounts/register/`)

```json
POST /api/accounts/register/
Content-Type: application/json

{
  "email": "dev@example.com",
  "password": "motdepasse123",
  "first_name": "Jean",
  "last_name": "Dupont",
  "gender": "H"
}
```

> Le backend associera automatiquement le rôle "Visiteur" par défaut s’il est configuré ainsi.

---

## ⚠️ Sécurité en production

* Ne laissez pas `DEBUG=True` en production.
* Ne donnez pas les mêmes tokens à tous les utilisateurs.
* Stockez les `refresh_token` de façon sécurisée (dans la base, ou en HttpOnly cookies).
* Expirez les sessions inactives après un certain temps.

---

## 📦 En résumé pour un développeur

| Étape               | Endpoint                       | Méthode | Auth requise |
| ------------------- | ------------------------------ | ------- | ------------ |
| S’enregistrer       | `/api/accounts/register/`      | POST    | ❌ Non        |
| Se connecter        | `/api/accounts/login/`         | POST    | ❌ Non        |
| Accéder aux données | `/api/stocks/`                 | GET     | ✅ Oui        |
| Rafraîchir token    | `/api/accounts/refresh-token/` | POST    | ❌ Non        |
| Se déconnecter      | `/api/accounts/logout/`        | POST    | ✅ Oui        |
