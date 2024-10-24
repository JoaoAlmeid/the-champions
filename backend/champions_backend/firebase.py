import firebase_admin
from firebase_admin import credentials
from pathlib import Path
import os

# Define o caminho base como o local onde está o manage.py
BASE_DIR = Path(__file__).resolve().parent.parent

# Caminho absoluto para o arquivo de credenciais
cred = credentials.Certificate(os.path.join(BASE_DIR, 'firebase_credentials.json'))

firebase_admin.initialize_app(cred)
