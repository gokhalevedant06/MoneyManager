release: python manage.py makemigrations --no-input
release: python manage.py migrate

web: daphne MoneyManager.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker --settings=MoneyManager.settings -v2