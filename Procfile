release: python manage.py makemigrations --no-input
release: python manage.py migrate
web: gunicorn MoneyManager.asgi --timeout 15 --keep-alive 5 --log-level debug