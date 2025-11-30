# API Concessionnaire Auto/Moto

API Django REST pour gérer des concessionnaires et leurs véhicules (auto / moto).

## Technologies

- Python 3
- Django
- Django REST Framework

---

## Installation et lancement

### 1. Cloner le dépôt

```bash
git clone <URL_DU_REPO>
cd dossier

Créer et activer l’environnement virtuel
python3 -m venv venv
source venv/bin/activate        # macOS

Installer les dépendances
pip install -r requirements.txt

Appliquer les migrations
python3 manage.py migrate

Lancer le serveur de développement
python3 manage.py runserver
