
# Ecommerce API Capstone

A production-ready **Inventory & Product Management REST API** built with **Django** and **Django REST Framework**.

This system provides secure authentication, product & stock management, and order handling for small to medium-sized businesses. Designed as a **capstone backend project**, it focuses on clean architecture, real-world business logic, and scalability.

---

## 🌐 Live Demo

Test the live API here: [Inventory Management API Live](https://ecommerce-api-rb25.onrender.com)

---

## ✨ Motivation

This project simulates a real-world inventory and sales management system to:

* Track products and stock levels
* Manage orders and transactions
* Organize categories and product details
* Provide a solid backend for future full-stack development

The goal was to **go beyond CRUD** and implement meaningful business logic for production-ready APIs.

---

## 🛠 Features

### 🔐 Authentication & Authorization

* User signup, login, and token-based authentication (DRF Token)
* Role-based permissions (admin/staff)
* Secure endpoint access

### 📦 Product & Inventory Management

* Product management: name, description, price, category, stock, image
* Category management
* Automatic stock handling on orders (optional feature)

### 🔍 Filtering, Search & Ordering

* Search by product name
* Filter by category
* Ordering by price, creation date, stock quantity
* Paginated API responses

---

## ⚙️ Tech Stack

* Python 3.x
* Django 5.x
* Django REST Framework
* DRF Token Authentication
* SQLite (development) / MySQL or PostgreSQL (production)
* Git & GitHub for version control

---

## 🧩 Project Structure

```
Ecommerce-api-capstone/
├── core/                       # Main app: products, orders, categories
├── ecommerce_api_capstone/     # Django project folder (settings, wsgi)
├── manage.py
├── requirements.txt
├── staticfiles/
├── db.sqlite3
```

---

## 📮 API Endpoints

| Endpoint                | Method         | Description                            |
| ----------------------- | -------------- | -------------------------------------- |
| `/api/products/`        | GET/POST       | List or create products                |
| `/api/products/<id>/`   | GET/PUT/DELETE | Retrieve, update, or delete a product  |
| `/api/categories/`      | GET/POST       | List or create categories              |
| `/api/categories/<id>/` | GET/PUT/DELETE | Retrieve, update, or delete a category |
| `/api/orders/`          | GET/POST       | List or create orders                  |


---

## ▶️ Run Locally

Clone the repo:

```bash
git clone https://github.com/soylu22/Ecommerce-api-capstone.git
cd Ecommerce-api-capstone
```

Create a virtual environment and activate:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

 API is available at `http://127.0.0.1:8000/`

---

## 🎯 Learning Outcomes

* Designing production-ready REST APIs
* Implementing authentication & role-based permissions
* Writing efficient Django ORM queries
* Building an inventory management system
* Structuring a clean, maintainable Django project

---

## 🔮 Future Improvements

* Add full reporting & analytics dashboards
* Implement low-stock email notifications
* Asynchronous order handling with Celery
* Swagger / OpenAPI documentation
* Frontend dashboard with React
* Multi-warehouse support

---

## 👨‍💻 About the Developer

Hi! I’m **Leul Misganaw** — a Junior Backend Developer building real-world Django applications.

* GitHub: [soylu22](https://github.com/soylu22)
* Email: [leulmisganaw222@gmail.com](leulmisganaw222@gmail.com)

