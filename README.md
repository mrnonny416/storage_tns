# storage_tns

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

A web-based inventory management system for materials and equipment, built with Django.

## Features

-   User authentication (custom user model)
-   Add, edit, and view storage items with images
-   Search and filter by type and category
-   Track borrowing and returning history
-   Admin interface for managing data

## Demo

See the project on GitHub: [mrnonny416/storage_tns](https://github.com/mrnonny416/storage_tns)

## Project Structure

```
storage_tns/
├── manage.py
├── requirements.txt
├── README.md
├── storage_tns/              # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── storage_tns_app/          # Main application (models, views, templates)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── templates/
│   └── static/
├── Templates/                # Project-level HTML templates
├── static/                   # Project-level static files (images, CSS, JS)
└── db.sqlite3                # SQLite database (default)

## Getting Started

### Prerequisites

-   Python 3.9+
-   pip

### Installation

1. **Clone the repository**

    ```sh
    git clone https://github.com/mrnonny416/storage_tns.git
    cd storage_tns
    ```

2. **Create and activate a virtual environment (recommended)**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (for admin access)**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**

    ```sh
    python manage.py runserver
    ```

7. **Access the app**
    - Main site: [http://localhost:8000/](http://localhost:8000/)
    - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Project Structure

-   `storage_tns/` - Django project settings
-   `storage_tns_app/` - Main application (models, views, templates)
-   `Templates/` - HTML templates
-   `static/` - Static files (images, CSS, JS)
-   `db.sqlite3` - SQLite database (default)

### Media & Static Files

Uploaded images are stored in `storage_tns_app/static/media/`.  
You may need to create this directory if it does not exist.

## Requirements

See [requirements.txt](requirements.txt).

## License

This project is licensed under the MIT License.

---

## requirements.txt

```text
Django>=3.2,<4.0
pytz
sqlparse
asgiref
```
