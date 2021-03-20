# UserUsage


This project was generated with Django 3.1.7. These are steps to run the project:

- Create a Virtual Environment with Python 3.9.1

- Install PostgreSQL and create new databse using pgAdmin if you are using windows 10.

- Install the backend requirements by running pip install -r requirememts.txt

- Set some customized environment variables in setting.py file, add new .env file under config folder and add:

                DATABASE_NAME=planetly
                DEBUG=on
                DATABASE_PASSWORD = password_db
                DATABASE_USERNAME = username_db

- Run python manage.py makemigrations to create new migrations based on the changes you have made to your models

- Run python manage.py migrate to apply migrations

- Create Super User by running python manage.py createsuperuser
