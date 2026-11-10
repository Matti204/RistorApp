# App Ristoranti

Progetto Django con registrazione e accesso tramite email.

```powershell
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py runserver
```

Apri http://127.0.0.1:8000/. Per un ambiente di produzione imposta `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0` e `DJANGO_ALLOWED_HOSTS`, e configura HTTPS.
