
A simple but functional invoicing system built with Django.  
Designed for small business use, personal billing, or as a base for future extensions.

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
- English-first with Lithuanian formatting (e.g. dates, "Suma žodžiais")

---

## Status

⚠️ **Still in development.**  
The app works, but the frontend is basic, and more features and tweaks are planned for the future.
This is my first Django project after academy, and i'm still working on it!

---

## Tech Stack

- Python 3.x
- Django
- SQLite (for dev)
- Bootstrap (minimal use)
- Crispy forms
- WeasyPrint (for PDF generation)
- num2words (for amount in words)

---

## Setup Instructions

1. **Clone the project**

```bash
git clone https://github.com/tadas-jnl/Invoicing.git
cd Invoice
```

3. **Create .env file inside project folder (next to settings.py file!) with your secret key**

```env
DEBUG = True
SECRET_KEY = 'your-secret-key-here'
DB_PATH = db.sqlite3
```

4. **Create virtual environment and install dependencies**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. **Run migrations and create superuser**

```bash
cd invoice
python manage.py migrate
python manage.py createsuperuser
```

4. **Run server**

```bash
python manage.py runserver
```
