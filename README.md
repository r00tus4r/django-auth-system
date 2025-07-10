# Django Auth System

A full-featured user authentication system built with Django. It includes registration, login/logout, password change/reset, profile update, and account deletion with a responsive Bootstrap UI.

## 🌟 Features

- User registration and login
- Password hashing and validation
- Profile management
- Password change and reset
- Account deletion
- Custom Django forms and templates
- Flash messages and error handling
- 404 / 500 custom error pages
- Deployed with PythonAnywhere

## 📦 Deployment

This project is deployed using [PythonAnywhere](https://www.pythonanywhere.com/) with static files served via `whitenoise`.

**Live Demo:** [http://djangoauthsys.pythonanywhere.com/](http://djangoauthsys.pythonanywhere.com/)

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-success?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-DB-lightgrey?logo=sqlite&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-blueviolet?logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)

## 📁 Project Structure

```
django-auth-system/
├── accounts/                # User management app
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── config/                  # Django settings and core configuration
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3               # SQLite DB (for dev)
├── LICENSE
├── manage.py
├── README.md
├── requirements.txt         # Dependencies
├── TODO.md                  # Remaining tasks & ideas
├── static/                  # Static files (logo, favicon, etc.)
│   ├── favicon.ico
│   └── logo.png
├── templates/               # HTML templates
│   ├── 404.html
│   ├── 500.html
│   ├── base.html
│   ├── change\_password.html
│   ├── dashboard.html
│   ├── delete\_account.html
│   ├── login.html
│   ├── navbar.html
│   ├── profile.html
│   ├── register.html
│   └── update\_profile.html

````

## 🚀 Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/r00tus4r/django-auth-system.git
   cd django-auth-system
   ```

2. **Create virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations and start server**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Then open your browser: `http://127.0.0.1:8000/`

## 👤 Author

* GitHub: [r00tus4r](https://github.com/r00tus4r)
* Telegram: [@wcyb4r](https://t.me/wcyb4r)

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🔗 Icon Attribution

<a href="https://www.flaticon.com/free-icons/authenticity" title="authenticity icons">Authenticity icons created by meaicon - Flaticon</a>
