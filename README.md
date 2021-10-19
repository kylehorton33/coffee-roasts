# Set up for development:

- `git clone https://github.com/kylehorton33/coffee-roasts.git`
- `cd coffee-roasts/`
- Create and activate your virtual environment: e.g. `python3 -m venv venv`
- `pip install -r requirement.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `export DJANGO_SETTINGS_MODULE=coffee_roasts.settings`
- `python manage.py loaddata fixtures/db-` (complete with current db json file)
- `python manage.py runserver`
- ☕

## To create new db fixture:
- `python manage.py dumpdata coffee --indent 4 --foat json > fixtures/db-YYYYMMDD-hhmmss.json` (with current time)


## Future Ideas
- 'Useful Forms': Roasting Notes template, espresso shot notes, operating manuals
- `Extraction` model for logging brews with specific roasts