# DCRM - Django Customer Relationship Management

Welcome to DCRM, a Django-based Customer Relationship Management system. This project is designed to help manage customer records efficiently and effectively.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Connecting MySQL with Django](#connecting-mysql-with-django)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Authentication (Register, Login, Logout)
- Add, Update, and Delete Customer Records
- View Customer Details
- Secure and Scalable

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/anujyadav73/DCRM.git
   cd DCRM

2. **Create a virtual environment:**
    ```sh
    python -m venv venv

3. **Activate the virtual environment**
    On Windows
    ```sh
    .\venv\Scripts\activate

    On macOS/Linux
    
    source venv/bin/activate

4. **Install the required packages:**
    ```sh
    pip install -r requirements.txt

5. - [Connecting MySQL with Django](#connecting-mysql-with-django)
    ```sh
    python manage.py migrate

6. **Run the development server:**
    ```sh
    python manage.py runserver

# Connecting MySQL with Django
**To connect your Django project to a MySQL database, follow these steps:**
1. **Install MySQL server and create a database for your project.**
2. **Install the MySQL client library:**
    ```sh
    pip install mysqlclient

3. **Update your Django project's settings to use MySQL. Open settings.py and modify the DATABASES section:**
    # filepath: dcrm/settings.py
    ```sh
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
                'HOST': 'localhost',  # Or your database host
                'PORT': '3306',       # Or your database port
        }
}

4. **Apply the migrations to set up your MySQL database:**
    ```sh
    python manage.py migrate

# Usage
**Navigate to http://127.0.0.1:8000/ in your web browser.**
**Register a new user or log in with an existing account.**
**Add, update, or delete customer records as needed.**
# Contributing
    Contributions are welcome! Please follow these steps:

        1. Fork the repository.
        2. Create a new branch (git checkout -b feature-branch).
        3. Make your changes.
        4. Commit your changes (git commit -m 'Add some feature').
        5. Push to the branch (git push origin feature-branch).
        6. Open a pull request.
# License
    This project is licensed under the MIT License. See the LICENSE file for details.