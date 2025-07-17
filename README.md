# 📝 NoteHub - проект удобных заметок

Этот проект позволяет создавать, писать, и удалять заметки. Так же есть возможность задавать им категории, чтобы фильтровать их, тем самым повысить вашу продуктивность и организованность!

---

## 🧱 Стек технологий

- Python 3.11.7
- Django
- Django templates
- Django admin
- Django ORM
- PostgreSQL
- Docker + Docker Compose
- CSS

---

## 🗂 Структура проекта

```
django-notes-orm-W1lden/
├── .github/
│   └── .keep
├── notebook_project/
│   ├── notebook_project/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── notes/
│   │   ├── migrations/
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── constants.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static/
│   │   ├── img/
│   │   │   └── logo.png
│   │   └── style.css
│   ├── templates/
│   │   ├── all_notes.html
│   │   ├── base.html
│   │   ├── note_detail.html
│   │   ├── user.html
│   │   └── users.html
│   ├── .env_example
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── fixtures.json
│   ├── manage.py
│   └── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Запуск проекта

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Solva-technology/django-notes-orm-W1lden.git
cd notebook_project
```

2. Создайте .env файл. Вот пример:
```env_example
POSTGRES_DB=notes_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=django-insecure-y&dh*6$8z4#v#aiml=zg5)&7+yf=w3(keb^8^lb@8x7$5zjkm@
LANGUAGE_CODE=ru
TIME_ZONE=Asia/Almaty
```

3. Соберите и запустите Docker контейнер:
```bash 
docker compose up --build
```

4. В браузере прейдите на сайт приложения notes:
```bash
http://0.0.0.0:8000/
```

---

## 🛠️ Запуск админки

1. Создайте супер пользователя:
```bash
docker exec -it web python manage.py createsuperuser
```

2. Зайдите в админ панель:
```bash
http://0.0.0.0:8000/admin/
```

---

## 🌐 Маршруты
- http://0.0.0.0:8000/ - главная страница, список всех заметок;
- http://0.0.0.0:8000/user/<номер пользователя> - страница пользователя;
- http://0.0.0.0:8000/users/ - страница пользователей;
- http://0.0.0.0:8000/note/<номер заметки> - страница определенной заметки;
- http://0.0.0.0:8000/admin/ - админ панель.

---

## 👤 Автор

[W1lden (GitHub)](https://github.com/W1lden)