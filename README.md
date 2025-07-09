# Django Auth System

A simple and customizable **Django Authentication System** with features like registration, login, logout, profile update, and account deletion. Designed for learning purposes and quick integration into any Django-based web project.

## 🌟 Features

* User registration with validation
* Login and logout system
* Profile update & deletion
* Clean Bootstrap-based UI
* Custom forms & views
* Secure password handling

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
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/                  # Static files (logo, favicon, css/js if any)
│   ├── favicon.ico
│   └── logo.png
├── templates/               # HTML templates
│   ├── base.html
│   ├── navbar.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── profile.html
│   ├── update_profile.html
│   └── delete_account.html
├── db.sqlite3               # SQLite DB (for dev)
├── manage.py                # Django CLI
├── requirements.txt         # Dependencies
├── LICENSE
└── README.md
```

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

4. **Run the project**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Then open your browser: `http://127.0.0.1:8000/`

---

## 👤 Author

* GitHub: [r00tus4r](https://github.com/r00tus4r)
* Telegram: [@wcyb4r](https://t.me/wcyb4r)

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🔗 Icon Attribution

<a href="https://www.flaticon.com/free-icons/authenticity" title="authenticity icons">Authenticity icons created by meaicon - Flaticon</a>
