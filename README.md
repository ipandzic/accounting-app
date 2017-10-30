# Accounting

Simple accounting app.

### Quickstart

Get the source from GitHub:

    git clone https://github.com/Pandza11/accounting-app.git

Create Python3 virtual environment:

    mkvirtualenv --python=/usr/bin/python3 accounting

Install required files:

    pip install -r requirements.txt

Create '/accounting-app/.env' file to define environment variables
showed in .env.sample, for example:

    DEBUG=true

Migrate the database:

    python manage.py migrate

Create super user:

    python manage.py createsuperuser

Run development server:

    python manage.py runserver

Point your browser to http://127.0.0.1:8000/admin and login

Running tests:

    python manage.py test