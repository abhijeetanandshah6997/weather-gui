# [Weather App](http://3.18.101.48:8080/)

A Django(Python Web Framework) Application that allows user to create and conduct program.

The application has following features :
* Weather Report for Current Date
* Weather Report for Past Date
* Weather Report optional Download as Text File
* Assist feature to convert weather data to other units
* Calculator provides Unit Conversion for several scales

---
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Things required to get the web application up and running.
* Python 3
* pip3
* Django 3.0.5
* PyCharm CE 2020

### Installation
A step by step series of examples that tell you how to get a development environment running.

Run the below commands :-

# WebApp
* Open the Project Directory in PyCharm CE
* In Terminal > Goto Project Directory manage.py
* Create and Activate a Virtual Environment named .env
* Refer to the .example.env to configure the environment variables
* To Run Server :
```
    pip3 install -r requirements.txt
    python3 manage.py runserver <Port>
```

---
### Project Structure
```

wfh160420
├── application
│   └── weather
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   ├── __init__.py
│       ├── models.py
│       ├── static
│       │   ├── css
│       │   │   └── home.css
│       │   └── images
│       │       ├── background.png
│       │       └── favicon.ico
│       ├── templates
│       │   └── weather
│       │       ├── base.html
│       │       ├── error.html
│       │       └── home.html
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── db.sqlite3
+── env
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
└── weather_gui
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```
---
### License
This project is licensed under Nineleaps Technology Solutions Pvt Ltd. © 2020.