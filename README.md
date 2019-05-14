# runner-backend
Python, Django, Postgresql

## Installation guide for MacOS

### Packages to be installed:
1. Python 3.7.2
2. Django 2.1.5
3. Postgresql 11

#### Steps:

1. Install homebrew
2. Install python3\
 `brew install python3`
3. Check python version:\
 `python3 -V`\
 should give python 3.7.2\
4. Install Django\
`pip3 install django`
5. Check django version:\
`python3 -m django --version`\
should give you 2.1.5
6. Install postgres\
`brew install postgresql`
7. Create runner database in postgres from command line\
`createdb djangorunner`\
This will create a database called `djangorunner` in postgres and we later connect to this db from our python project.
8. Now you are ready to clone the project from github. I use pycharm community version for coding and terminal for running django commands.
9. After cloning the project, open the project in pycharm. Go to `runner/settings.py` and find the following lines:\
DATABASES = {\
    'default': {\
        'ENGINE': 'django.db.backends.postgresql',\
        'NAME': 'djangorunner',\
        'USER': 'dimple',\
        'PASSWORD': '******',\
        'HOST': '127.0.0.1',\
        'PORT': '5432'\
    }\
}\
Change the user and password to your mac user and password.
10. Now go to the command line and cd into the project.
11. `pip3 install djangorestframework`
12. `pip3 install django-filter`
12. `python3 manage.py makemigrations`
13. `python3 manage.py migrate`
14. `python3 manage.py runserver`
15. On your browser go to `localhost:8000`. You should see rest framework
16. `localhost:8000/admin` will give you django administration.





   




