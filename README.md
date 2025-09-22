---
title: "Deploy ML API"
emoji: "🚀"
colorFrom: "blue"
colorTo: "green"
sdk: "docker"
sdk_version: "latest"
app_file: "app.py"
pinned: false
---

# 🚀 Deploy Machine Learning API

API pour la prédiction attrition employé avec **FastAPI**, **SQLAlchemy** et **SQLite/PostgreSQL**.  
Elle permet de :

- 📊 **Lister** les modèles ML disponibles (`/`)
- 🤖 **Prédire** avec un modèle donné (`/predict`)
- 🗄️ **Sauvegarder** automatiquement les inputs et outputs en base
- 📚 **Documentation Swagger/OpenAPI** générée automatiquement

---

## 📦 Prérequis

- Python 3.12+
- [Poetry](gestion des dépendances)
- Docker (PostgreSQL local via Compose)

---

## Installation

### 1. Cloner le dépôt
~~~bash
git clone https://github.com/ton-compte/deploy-machine-learning.git
cd deploy-machine-learning
~~~


### 2. Créer un environnement virtuel avec Poetry
~~~bash
poetry install
~~~

### 3. Configurer l’environnement

Crée un fichier **.env** à la racine :

~~~env
# PostgreSQL
DATABASE_URL=postgresql+psycopg2://futu:futu_pass@localhost:5432/futurisys
# Hugging Face
HF_TOKEN= Token Hugging Face
~~~


## 4. Base de données (PostgreSQL)

### Démarrer la base
~~~bash
docker compose up -d db
~~~


### 5. Lancer l’API

~~~bash
poetry run uvicorn src.main:app --reload
~~~


### 🧹 Qualité de code

**Lint :**
~~~bash
poetry run ruff check .
~~~

### 🧪 Tests & Couverture

**Lancer les tests :**
```bash
poetry run pytest --maxfail=1 --disable-warnings -q
