# Django Invoicing App

A simple but functional invoicing system built with Django.  
Designed for small business use, personal billing, or as a base for future extensions.  
The invoice format is universal but tailored to Lithuanian invoice standards.

This project is still in development. I created it to gain hands-on experience with a real-world Django application.

Deployed at https://billmaker.eu
---

## Features

- User authentication
- Individual & company profiles
- Invoice creation with:
  - Seller and buyer data
  - Itemized product/service list
  - Automatic total calculation
  - PDF invoice generation (WeasyPrint)
- Basic Bootstrap styling
- Languages: English (more coming soon)

---

## Status

⚠️ **Still in development.**  
The core functionality works, but the frontend is basic. More features, styling, and tweaks are planned.  
This is my first Django project after completing my academy course, and I'm actively improving it.

---

## Tech Stack

- Python 3.x
- Django
- PostgreSQL
- HTML / CSS / Bootstrap

---

## Setup Instructions

1. **Clone the project**

```bash
git clone https://github.com/tadas-jnl/Invoicing.git
cd Invoicing
```

2. **Create .env file inside Invoicing/invoices/**

```env
DEBUG=True
SECRET_KEY=your_secret_key
DB_PATH=invoices.db
DB_NAME=invoicedb
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'localhost', '127.0.0.1']
```

3. **Create virtual environment and install dependencies**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. **Run migrations and create superuser**

```bash
cd invoices
python manage.py migrate
python manage.py createsuperuser
```

5. **Run development server**

```bash
python manage.py runserver
```
