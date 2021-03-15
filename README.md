# Hackathon backend (DroidFactory)
Server application for android app: https://github.com/GoToHero/DroidFactory
More information: docs/description.txt

## Project structure

```
hackaton_back/
├── docs
│   ├── db_schema.txt
│   └── description.txt
├── LICENSE
├── manage.py
├── memeface
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── yasg.py
├── memeface_api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Procfile
├── README.md
├── requirements.txt
└── runtime.txt
```

## Installation

```
$ git clone https://github.com/aderny-twc/hackaton_back.git
$ cd hackaton_back
$ python -m venv venv
$ . venv/bin/activate
(venv) pip install -r requirements.txt
```

#### Migrations and server starting

```
(venv) python manage.py makemigrations
(venv) python manage.py migrate
(venv) python manage.py runserver
```

#### Superuser creating

```
(venv) python manage.py createsuperuser
# .. create your user
```

## Using the app

- http://127.0.0.1:8000/ - server address
- http://127.0.0.1:8000/admin/ - admin page
- http://127.0.0.1:8000/swagger/ - documentation
- http://127.0.0.1:8000/api/v1/ - api link

### Heroku

*You can test the application at the link:*

https://deez-nuts-back.herokuapp.com/

*Documentation:*

https://deez-nuts-back.herokuapp.com/swagger/

**The application is fully prepared for deployment on Heroku.**

For deployment you need Heroku CLI

```
$ heroku create <app_name>
$ git push heroku master
$ heroku run python manage.py makemigrations
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
# ..create your user
```

