# Stenn's Site

Проєкт створено на основі Django.

## Встановлення та запуск

### 1. Клонування репозиторію

```bash
git clone https://github.com/stenn0/mysite.git stenns-site
cd stenns-site
```

### 2. Створення та активація віртуального середовища

```bash
python -m venv venv
venv/Scripts/activate  # Для Windows
# або
source venv/bin/activate  # Для Linux/MacOS
```

### 3. Встановлення залежностей

```bash
pip install -r requirements.txt
```

### 4. Міграції бази даних

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Створення адміністратора

```bash
python manage.py createsuperuser
```

### 6. Збір статичних файлів (для production або за потреби)

```bash
python manage.py collectstatic
```

### 7. Запуск сервера

```bash
python manage.py runserver
```

Сервер буде доступний за адресою: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---
