# Sales App 

Sales application for a product distributor.

## Team

- Diego Anchillo Sanchez
- Cristian Quispe Quispe
- Sharon Chullunquia Rosas

## 1. Create virtual environment

* We create the virtual environment for our project.

  ```bash 
  python -m venv venv
  ````
* We activate our virtual environment.

  ```bash
  source venv/bin/activate
  ````
## 2. Install requirements

* We install requirements using requirements.txt file.

  ```bash
  pip install -r requirements.txt
  ````

## 3. Connect to database

* We change the file my.cnf for the connection to the database.

  ```bash
  # my.cnf
  [client]
  database = <database-name>
  user = <username>
  password = <password>
  host = 127.0.0.1
  port = 3306
  default-character-set = utf8
  ````
## 4. Migrate

* Inside the `sales_admin/` folder, we create migration files.

  ```bash
  python manage.py makemigrations
  ````
* We execute the changes detected in the models.

  ```bash
  python manage.py migrate
  ````
## 5. Create super user

* We create a super user account to access the Django Admin.

   ```bash
   python manage.py createsuperuser
   ````
* We can validate by querying the auth_user table in the database.

  ```sql
  select * from auth_user;
  ````
## 6. Run

* We raise the development server. Default port 8000.

  ```bash
  python manage.py runserver 0.0.0.0:8080
  ````
