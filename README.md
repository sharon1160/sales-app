![Center](https://capacitacion.uc.cl/images/noticias/gestion-de-bodegas.jpg)

# RESTful API - SalesApp 👷

This is the official repository of the "SalesApp" distributor's backend application.
  
## Visión general

The backend application is a RESTful API based on a wholesale distributor that sells different brands of products to small companies in the Metropolitan City of Lima. This API will allow the distributor to integrate your website or mobile application; in addition to facilitating integration with other e-commerce platforms.

## Content

* [Tech Stack](#techstack) :computer:
* [Architecture](#architecture) :bank:
* [Code Structure](#code_structure) :card_file_box:
* [Requirements](#requirements) 📝
* [Dependencies](#dependencies) :books:
* [Environment Variables](#env) :sparkles:
* [Database Entity Model](#dbmodel) :sparkles:
* [Database Information](#dbinfo) :sparkles:
* Endpoints :sparkles:
* [Install and Run](#install_run) 🚀

<a name="techstack"></a>
## Tech Stack :computer:

<a name="architecture"></a>
## Architecture :bank:

<a name="code_structure"></a>
## Code Structure :card_file_box:

<a name="requirements"></a>
## Requirements 📝



<a name="dependencies"></a>
## Dependencies :books:

<a name="env"></a>
## Environment Variables :sparkles:

<a name="dbmodel"></a>
## Database Entity Model :sparkles:

<a name="dbinfo"></a>
## Database Information :sparkles:

* Number of records per table
* Size of each table
* Table: Product
* Table: Product Category
* Table: UnitMeasure
* Table: UnitMeasureCategory
* Table: Currency
* Table: Order
* Table: Order Item
* Table: Customer
* Table: User

## Endpoints :sparkles:


<a name="install_run"></a>
## Install and Run 🚀

### Create virtual environment

* We create the virtual environment for our project.

  ```bash 
  python -m venv venv
  ````
* We activate our virtual environment.

  ```bash
  source venv/bin/activate
  ````
### Install requirements

* We install requirements using requirements.txt file.

  ```bash
  pip install -r requirements.txt
  ````

### Connect to database

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
### Migrate

* Inside the `sales_admin/` folder, we create migration files.

  ```bash
  python manage.py makemigrations
  ````
* We execute the changes detected in the models.

  ```bash
  python manage.py migrate
  ````
### Create super user

* We create a super user account to access the Django Admin.

   ```bash
   python manage.py createsuperuser
   ````
* We can validate by querying the auth_user table in the database.

  ```sql
  select * from auth_user;
  ````
### Run

* We raise the development server. Default port 8000.

  ```bash
  python manage.py runserver 0.0.0.0:8080
  ````
