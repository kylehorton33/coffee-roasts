# Set up for development:

- `git clone https://github.com/kylehorton33/coffee-roasts.git`
- `pip install -r requirement.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `export DJANGO_SETTINGS_MODULE=coffee_roasts.settings`
- `python manage.py loaddata fixtures/db-` (complete with current db json file)
- `python manage.py runserver`
- ☕