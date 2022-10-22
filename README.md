![Center](https://capacitacion.uc.cl/images/noticias/gestion-de-bodegas.jpg)

# RESTful API - SalesApp 👷

This is the official repository of the "SalesApp" distributor's backend application.

## Overview

The backend application is a RESTful API based on a wholesale distributor that sells different brands of products to small companies in the Metropolitan City of Lima. This API will allow the distributor to integrate your website or mobile application; in addition to facilitating integration with other e-commerce platforms.

## Content

- [Tech Stack](#techstack) :computer:
- [Architecture](#architecture) :bank:
- [Code Structure](#code_structure) :card_file_box:
- [Requirements](#requirements) 📝
- [Dependencies](#dependencies) :books:
- [Environment Variables](#env) :sparkles:
- [Database Entity Model](#dbmodel) :sparkles:
- [Database Information](#dbinfo) :sparkles:
- [Endpoints](#endpoints) :sparkles:

  - [API Sales Home](#endpointHomeSales)
  - [API Order List Filter with Pagination](#endpointOrderList)
  - [API Get Order with Token](#endpointOrderToken)
  - [API Order List by Order number](#endpointOrderNumber)
  - [API Order List by Order date](#endpointOrderDate)
  - [API Order List by Delivery date](#endpointOrderDelivery)
  - [API Customer List](#endpointCustomerList)
  - [API Customer List by RUC](#endpointCustomerListRuc)
  - [API Customer List by Category](#endpointCustomerListCategory)

- [Install and Run](#install_run) 🚀

<a name="techstack"></a>

## Tech Stack :computer:

- **Django:** Django is an open source web development framework, written in Python, that adheres to the model–view–controller design pattern.
- **Transactional Database:** MySQL Server version 8.0.29.
- **Server:** Localhost.
- **Postman:** API platform for developers to design, build, test, and iterate on their APIs.

<a name="architecture"></a>

## Architecture :bank:

![image Model Database](https://github.com/sharon1160/sales-app/blob/main/imgs/arquitecture_diagram.PNG)

<a name="code_structure"></a>

## Code Structure :card_file_box:

![image Model Database](https://github.com/sharon1160/sales-app/blob/main/imgs/code_structure.PNG)

<a name="requirements"></a>

## Requirements 📝

- Python 3.10.4
- Django 4.1.1
- Docker 20.10.16
- MySQL 8.0.30
- MySQL Workbench 8.0.30

<a name="dependencies"></a>

## Dependencies :books:

- "django-cors-headers": "3.13.0"
- "rest_framework.authtoken": "2.1.4"
- "django-filter": "22.1"
- "djangorestframework": "3.14.0"
- "mysqlclient": "2.1.1"

<a name="env"></a>

## Environment Variables :sparkles:

```bash
database = dbstore
user = ' '
password = ' '
host = 127.0.0.1
port = 3306
default-character-set = utf8
```

<a name="dbmodel"></a>

## Database Entity Model :sparkles:

Based on the requirements, a basic entity model of a relational database was defined to cover the scope of the project: develop an API that allows creating orders.

![image Model Database](https://github.com/sharon1160/sales-app/blob/main/imgs/db_diagram.png)

<a name="dbinfo"></a>

## Database Information :sparkles:

- Number of records per table

  ![records](https://github.com/sharon1160/sales-app/blob/main/imgs/records.jpg)

- Table: Product

  ![product](https://github.com/sharon1160/sales-app/blob/main/imgs/product.jpg)

- Table: Product Category

  ![product category](https://github.com/sharon1160/sales-app/blob/main/imgs/product_category.jpg)

- Table: UnitMeasure

  ![unit measure](https://github.com/sharon1160/sales-app/blob/main/imgs/unit_measure.jpg)

- Table: UnitMeasureCategory

  ![unit measure category](https://github.com/sharon1160/sales-app/blob/main/imgs/unit_measure_category.jpg)

- Table: Currency

  ![currency](https://github.com/sharon1160/sales-app/blob/main/imgs/currency.jpg)

- Table: Order

  ![order](https://github.com/sharon1160/sales-app/blob/main/imgs/order.jpg)

- Table: OrderItem

  ![order item](https://github.com/sharon1160/sales-app/blob/main/imgs/order_item.jpg)

- Table: Customer

  ![customer](https://github.com/sharon1160/sales-app/blob/main/imgs/customer.jpg)

- Table: User

  ![user](https://github.com/sharon1160/sales-app/blob/main/imgs/user.jpg)

<a name="endpoints"></a>

## Endpoints :sparkles:

<a name="endpointHomeSales"></a>

### Endpoint: Sales Home

```
GET /
```

Example Response:

```json
{
  "orders": "http://0.0.0.0:8000/api/sales/orders/",
  "order-items": "http://0.0.0.0:8000/api/sales/order-items/",
  "customers": "http://0.0.0.0:8000/api/sales/customers/"
}
```

<a name="endpointOrderList"></a>

### Endpoint: Order List Filter with Pagination

```
GET / api/sales/orders/
```

Example Response:

```json
{
  "count": 6,
  "next": "http://0.0.0.0:8000/api/sales/orders/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "number": "202200001",
      "date": "2022-10-05",
      "business_name": "Cinco Tenedores",
      "delivery_date": "2022-10-08",
      "subtotal": "4548.40",
      "igv": "818.71",
      "total": "5367.11",
      "discount_total": "224.00"
    },
    {
      "id": 4,
      "number": "202200002",
      "date": "2022-10-21",
      "business_name": "Okashi Restaurant",
      "delivery_date": "2022-10-23",
      "subtotal": "975.00",
      "igv": "175.50",
      "total": "1150.50",
      "discount_total": "0.00"
    },
    {
      "id": 5,
      "number": "202200003",
      "date": "2022-10-21",
      "business_name": "Hotel Palermo",
      "delivery_date": "2022-10-23",
      "subtotal": "159.30",
      "igv": "28.67",
      "total": "187.97",
      "discount_total": "0.56"
    },
    {
      "id": 6,
      "number": "202200004",
      "date": "2022-10-21",
      "business_name": "Mini Market San Blas",
      "delivery_date": "2022-10-23",
      "subtotal": "98.00",
      "igv": "17.64",
      "total": "115.64",
      "discount_total": "0.00"
    },
    {
      "id": 7,
      "number": "202200005",
      "date": "2022-10-21",
      "business_name": "Okashi Restaurant",
      "delivery_date": "2022-10-23",
      "subtotal": "139.50",
      "igv": "25.11",
      "total": "164.61",
      "discount_total": "0.00"
    }
  ]
}
```

<a name="endpointOrderToken"></a>

### Endpoint: Get Order with Token

```
GET / api/sales/order/1/
```

Example Response:

```json
{
  "order": {
    "id": 1,
    "number": "202200001",
    "date": "2022-10-05",
    "business_name": "Cinco Tenedores",
    "delivery_date": "2022-10-08",
    "subtotal": "4548.40",
    "igv": "818.71",
    "total": "5367.11",
    "discount_total": "224.00"
  },
  "have_permission": true
}
```

<a name="endpointOrderNumber"></a>

### Endpoint: Order List by Order number

```
GET / api/sales/orders/?number=202200004
```

Example Response:

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 6,
      "number": "202200004",
      "date": "2022-10-21",
      "business_name": "Mini Market San Blas",
      "delivery_date": "2022-10-23",
      "subtotal": "98.00",
      "igv": "17.64",
      "total": "115.64",
      "discount_total": "0.00"
    }
  ]
}
```

<a name="endpointOrderDate"></a>

### Endpoint: Order List by Order date

```
GET / api/sales/orders/?date=2022-10-21
```

Example Response:

```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 4,
      "number": "202200002",
      "date": "2022-10-21",
      "business_name": "Okashi Restaurant",
      "delivery_date": "2022-10-23",
      "subtotal": "975.00",
      "igv": "175.50",
      "total": "1150.50",
      "discount_total": "0.00"
    },
    {
      "id": 5,
      "number": "202200003",
      "date": "2022-10-21",
      "business_name": "Hotel Palermo",
      "delivery_date": "2022-10-23",
      "subtotal": "159.30",
      "igv": "28.67",
      "total": "187.97",
      "discount_total": "0.56"
    },
    {
      "id": 6,
      "number": "202200004",
      "date": "2022-10-21",
      "business_name": "Mini Market San Blas",
      "delivery_date": "2022-10-23",
      "subtotal": "98.00",
      "igv": "17.64",
      "total": "115.64",
      "discount_total": "0.00"
    },
    {
      "id": 7,
      "number": "202200005",
      "date": "2022-10-21",
      "business_name": "Okashi Restaurant",
      "delivery_date": "2022-10-23",
      "subtotal": "139.50",
      "igv": "25.11",
      "total": "164.61",
      "discount_total": "0.00"
    },
    {
      "id": 8,
      "number": "202200006",
      "date": "2022-10-21",
      "business_name": "Hotel Palermo",
      "delivery_date": "2022-10-23",
      "subtotal": "268.00",
      "igv": "48.24",
      "total": "316.24",
      "discount_total": "0.00"
    }
  ]
}
```

<a name="endpointOrderDelivery"></a>

### Endpoint: Order List by Delivery date

```
GET / api/sales/orders/?delivery_date=2022-10-23
```

Example Response:

```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 4,
      "number": "202200002",
      "date": "2022-10-21",
      "business_name": "Okashi Restaurant",
      "delivery_date": "2022-10-23",
      "subtotal": "975.00",
      "igv": "175.50",
      "total": "1150.50",
      "discount_total": "0.00"
    },
    {
      "id": 5,
      "number": "202200003",
      "date": "2022-10-21",
      "business_name": "Hotel Palermo",
      "delivery_date": "2022-10-23",
      "subtotal": "159.30",
      "igv": "28.67",
      "total": "187.97",
      "discount_total": "0.56"
    },
    {
      "id": 6,
      "number": "202200004",
      "date": "2022-10-21",
      "business_name": "Mini Market San Blas",
      "delivery_date": "2022-10-23",
      "subtotal": "98.00",
      "igv": "17.64",
      "total": "115.64",
      "discount_total": "0.00"
    },
    {
      "id": 7,
      "number": "202200005",
      "date": "2022-10-21",
      "business_name": "Okashi Restaurant",
      "delivery_date": "2022-10-23",
      "subtotal": "139.50",
      "igv": "25.11",
      "total": "164.61",
      "discount_total": "0.00"
    },
    {
      "id": 8,
      "number": "202200006",
      "date": "2022-10-21",
      "business_name": "Hotel Palermo",
      "delivery_date": "2022-10-23",
      "subtotal": "268.00",
      "igv": "48.24",
      "total": "316.24",
      "discount_total": "0.00"
    }
  ]
}
```

<a name="endpointCustomerList"></a>

### Endpoint: Customer List

```
GET / api/sales/customers/
```

Example Response:

```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "code": "100",
      "business_name": "Cinco Tenedores",
      "district": "San Isidro",
      "category": "Restaurantes",
      "ruc": "20601145852",
      "created_at": "2022-10-21T10:29:58-05:00",
      "updated_at": "2022-10-21T10:29:58-05:00"
    },
    {
      "id": 2,
      "code": "101",
      "business_name": "Okashi Restaurant",
      "district": "Miraflores",
      "category": "Restaurantes",
      "ruc": "20664585121",
      "created_at": "2022-10-21T10:29:58-05:00",
      "updated_at": "2022-10-21T10:29:58-05:00"
    },
    {
      "id": 3,
      "code": "102",
      "business_name": "Hotel Palermo",
      "district": "San Borja",
      "category": "Hoteles",
      "ruc": "20365265851",
      "created_at": "2022-10-21T10:29:58-05:00",
      "updated_at": "2022-10-21T10:29:58-05:00"
    },
    {
      "id": 4,
      "code": "103",
      "business_name": "Mini Market San Blas",
      "district": "Surquillo",
      "category": "Tiendas",
      "ruc": "10426545201",
      "created_at": "2022-10-21T10:29:58-05:00",
      "updated_at": "2022-10-21T10:29:58-05:00"
    },
    {
      "id": 5,
      "code": "105",
      "business_name": "Supermarket Las Vegas",
      "district": "San Borja",
      "category": "Tiendas",
      "ruc": "20115245110",
      "created_at": "2022-10-21T10:29:58-05:00",
      "updated_at": "2022-10-21T10:29:58-05:00"
    }
  ]
}
```

<a name="endpointCustomerListRuc"></a>

### Endpoint: Customer List by RUC

```
GET / api/sales/customers/?ruc=20664585121
```

Example Response:

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 2,
      "code": "101",
      "business_name": "Okashi Restaurant",
      "district": "Miraflores",
      "category": "Restaurantes",
      "ruc": "20664585121",
      "created_at": "2022-10-21T10:29:58-05:00",
      "updated_at": "2022-10-21T10:29:58-05:00"
    }
  ]
}
```

<a name="endpointCustomerListCategory"></a>

### Endpoint: Customer List by Category

```
GET / api/sales/customers/?category=Tiendas
```

Example Response:

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 4,
      "code": "103",
      "business_name": "Mini Market San Blas",
      "district": "Surquillo",
      "category": "Tiendas",
      "ruc": "10426545201",
      "created_at": "2022-10-21T10:29:58-05:00",
      "updated_at": "2022-10-21T10:29:58-05:00"
    },
    {
      "id": 5,
      "code": "105",
      "business_name": "Supermarket Las Vegas",
      "district": "San Borja",
      "category": "Tiendas",
      "ruc": "20115245110",
      "created_at": "2022-10-21T10:29:58-05:00",
      "updated_at": "2022-10-21T10:29:58-05:00"
    }
  ]
}
```

<a name="install_run"></a>

## Install and Run 🚀

### Create virtual environment

- We create the virtual environment for our project.

  ```bash
  python -m venv venv
  ```

- We activate our virtual environment.

  ```bash
  source venv/bin/activate
  ```

### Install requirements

- We install requirements using requirements.txt file.

  ```bash
  pip install -r requirements.txt
  ```

### Connect to database

- We change the file my.cnf for the connection to the database.

  ```bash
  # my.cnf
  [client]
  database = <database-name>
  user = <username>
  password = <password>
  host = 127.0.0.1
  port = 3306
  default-character-set = utf8
  ```

### Migrate

- Inside the `sales_admin/` folder, we create migration files.

  ```bash
  python manage.py makemigrations
  ```

- We execute the changes detected in the models.

  ```bash
  python manage.py migrate
  ```

### Create super user

- We create a super user account to access the Django Admin.

  ```bash
  python manage.py createsuperuser
  ```

- We can validate by querying the auth_user table in the database.

  ```sql
  select * from auth_user;
  ```

### Run

- We raise the development server. Default port 8000.

  ```bash
  python manage.py runserver 0.0.0.0:8080
  ```
