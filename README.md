# 🚀 Web Scrapper (Django + BeautifulSoup)

A simple web scraping application built using **Django**, **BeautifulSoup**, and **Requests**.

This project allows users to enter a website URL, scrape all anchor (`<a>` tags) from the page, and display them in a clean Bootstrap-styled table interface.

---

## 📌 Features

- Scrape all links (`<a>` tags) from any public website
- Automatically adds `https://` if missing
- Stores scraped links in SQLite database
- Displays results in a responsive Bootstrap table
- Shows total record count
- Clear/Delete all scraped results
- Clean UI with Bootstrap 5

---

## 🛠️ Tech Stack

- Python 3.x
- Django 5.x
- BeautifulSoup4
- Requests
- SQLite (default Django DB)
- Bootstrap 5

---

## 📂 Project Structure

```
mysite/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .gitignore
│
├── mysite/                # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── scrapper/              # Django App
    ├── migrations/
    ├── templates/
    │   └── scrapper/
    │       └── result.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/web-scrapper.git
cd web-scrapper
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present:

```bash
pip install django beautifulsoup4 requests
```

Then generate it:

```bash
pip freeze > requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Start Development Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🧠 How It Works

1. User enters a website URL.
2. If URL does not start with `http`, `https://` is automatically added.
3. `requests` fetches page content.
4. `BeautifulSoup` parses HTML.
5. All `<a>` tags are extracted.
6. Link text and href are stored in the database.
7. Results are displayed in a styled table.

---

## ⚠️ Notes

- Some websites block scraping (e.g., Google, Amazon).
- Works best with public/static websites.
- Database used: SQLite (default Django).

---
## 📁 Important Directory Note

This repository has the following structure:

```
Project 4/
    mysite/
        manage.py
        mysite/
        scrapper/
```

To run the Django development server, you must navigate into the directory that contains `manage.py`.

### Run Server Correctly

```bash
cd mysite
python manage.py runserver
```

If you try to run the server from the outer project folder, it will not work because `manage.py` is inside the `mysite/` directory.


## 🔒 .gitignore Includes

- `venv/`
- `db.sqlite3`
- `__pycache__/`
- `.env`
- `.vscode/`
- OS-specific files

---

## 📌 Future Improvements

- Add User-Agent headers
- Prevent duplicate links
- Add pagination
- Add search/filter functionality
- Deploy to cloud (Render / Railway / etc.)

---

## 👩‍💻 Author

Built as a Django learning project.

