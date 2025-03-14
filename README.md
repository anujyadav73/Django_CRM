# DCRM - Django Customer Relationship Management

Welcome to DCRM, a Django-based Customer Relationship Management system. This project is designed to help manage customer records efficiently and effectively.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
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

    python -m venv venv

3. **Activate the virtual environment**
    On Windows
    .\venv\Scripts\activate

    On macOS/Linux
    source venv/bin/activate

4. **Install the required packages:**
    pip install -r requirements.txt

5. **Set up the database:**
    python manage.py migrate

6. **Run the development server:**
    python manage.py runserver

## Usage
    Navigate to http://127.0.0.1:8000/ in your web browser.
    Register a new user or log in with an existing account.
    Add, update, or delete customer records as needed.
## Contributing
    Contributions are welcome! Please follow these steps:

        Fork the repository.
        Create a new branch (git checkout -b feature-branch).
        Make your changes.
        Commit your changes (git commit -m 'Add some feature').
        Push to the branch (git push origin feature-branch).
        Open a pull request.
## License
    This project is licensed under the MIT License. See the LICENSE file for details.