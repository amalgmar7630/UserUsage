# UserUsage


This project was generated with Django 3.1.7. These are steps to run the project:

I created Ubuntu 16.04 VM using Vagrant and installed requirements and made the database setup into it, you can use it by flowing these steps:

      -Set some customized environment variables in setting.py file, add new .env file under config folder and add:
      
              DATABASE_NAME=planetly
              DEBUG=on
              DATABASE_PASSWORD = postgres1
              DATABASE_USERNAME = postgres1
              
       
       - Then install VirtualBox and Vagrant.
       
       - Run vagrant up in console.
       
       - run vagrant ssh.
       
       - The features added using vagrants are installing ubuntu packages, install postgresql and setup database, install requirements and create super user with the credentials:username: admin, email:admin@example.com, pwd: adminpass
      
      
      
     
Otherwise you can make the previous features manually:


- Create a Virtual Environment with Python 3.9.1

- Install PostgreSQL and create new databse using pgAdmin if you are using windows 10.

- Install the backend requirements by running pip install -r requirememts.txt

- Set some customized environment variables in setting.py file, add new .env file under config folder and add:

                DATABASE_NAME=db_name
                DEBUG=on
                DATABASE_PASSWORD = password_db
                DATABASE_USERNAME = username_db

- Run python manage.py makemigrations to create new migrations based on the changes you have made to your models

- Run python manage.py migrate to apply migrations

- Create Super User by running python manage.py createsuperuser

- Run tests with running python manage.py test

- To use swagger,I made it public to view requests but you need to login to autorize requests so use auth/login and fill username and password or use auth/signup to register new user and then you will get a token and have access to API requests.

- The Test takes about 5 hours and the planning phase is the challenging part for me because I needed to think about the frontend how it should be the UI so as a user perspective I was thinking that there should be 2 seperate interfaces one for adding usage types and the other is to apply CRUD actions on usage:


       - user should signup and sign in to get a token and autorize requets using JWT.
       - user can add usage date and pick one option for the usage type from a select picker.
       - user can delete his usage from list of usages.
       - user can edit one usage by updating the usage date or picking another usage type.
       - user can consult his usages and filter by date range or sort by date.
