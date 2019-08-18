Project-
Django basics(including calculator basic app, HTML template importing, Database migration, Database fetching, Login and registration, admin panel(auto in django), contact form)

main project is "django_website"
rest there are apps-
travello(a website)
accounts(for login and logout)
templates(for storing HTML pages)
media(for saving uploaded images)
static(for keeping static contact like img, csss and js)
assests(created by django to store static content to enhance process)
csvDB_files- it contains 2 files in csv format


Database used-
postgres(with UI pgadmin)

INFO-
all main fiels are inside django_website directory as it is main project
urls.py- for all rotuing
settings.py- for all settings


running project-
create a virtual env for django(I named it test)
open cmd and goto project directory and type in cmd-
for working on virtual env- workon test
for running server-  python manage.py runserver

URLs-
home- http://localhost:8000/
contact- http://localhost:8000/contact
login- http://localhost:8000/login
register- http://localhost:8000/register

admin- http://localhost:8000/admin
user- admin
pass- 1234

postgres account-
user- postgres
pass- 1234

Migrations-
create a ModelClass in models.py with column description
open cmd and goto project directory and type in cmd-
for creating migration file- python manage.py makemigrations <app_name>
for migrating - python manage.py migrate


saving data in database-
http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php
youtube channel- Telusko(python videos)