# FrostyDelights 🍦

A Django web app to manage ice cream inventory for a local shop. This project was developed as part of the Django lab assignment and fulfills Tasks 1 through 5, including setup, model creation, form handling, view integration, and custom theming.

## Features
- View a list of all ice cream items
- Add new ice cream entries (name, flavor, and price)
- Form validation to ensure valid inputs
- Ice cream-themed user interface using simple HTML and inline CSS
- Admin panel enabled for managing inventory

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/philingus/frostydelights.git
cd frostydelights
```

### 2. Set up a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 3. Install dependencies
```bash
pip install django
```

### 4. Apply migrations
```bash
python manage.py makemigrations inventory
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to use the app.

## Project Structure
```
frostydelights/
│
├── inventory/
│   ├── models.py         # IceCream model
│   ├── forms.py          # ModelForm for adding ice cream
│   ├── views.py          # Home and Add views
│   ├── urls.py           # App routing
│   ├── admin.py          # Admin registration
│   └── templates/
│       └── inventory/
│           ├── home.html # Homepage with item list
│           └── add.html  # Form to add items
│
├── frostydelights/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── db.sqlite3
└── manage.py
```

## Requirements Met
✅ Task 1: Django project and app created  
✅ Task 2: Model (`IceCream`) defined with name, flavor, and price  
✅ Task 3: Form created using `ModelForm`  
✅ Task 4: Views implemented with routing and form handling  
✅ Task 5: Custom HTML template with styling and full functionality

## License
For educational use only.
