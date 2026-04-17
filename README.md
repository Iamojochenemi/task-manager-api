# Django REST Backend System

A modular backend system built with Django REST Framework featuring two independent applications: a Task Management API and an E-commerce Order Management API.

This project demonstrates backend engineering skills including authentication, permissions, relational database design, and RESTful API architecture.

---

## Project Structure

This project contains two independent Django apps:

### 1. Tasks App
A task management system where users can:
- Create tasks
- Update tasks
- Delete tasks
- Mark tasks as completed or pending
- Filter and search tasks

Each user can only access their own tasks.

---

### 2. Ecommerce (Orders) App
A simplified e-commerce order management system where users can:
- Create orders with multiple items
- View their orders
- Track order status (pending, shipped, delivered, etc.)
- Calculate total order price automatically

Admins can:
- Update order status
- Manage order lifecycle

---

## Features

### Authentication & Security
- User registration and login
- JWT authentication (SimpleJWT)
- Session authentication for browsable API
- Role-based permissions (Admin vs Regular Users)

### API Design
- RESTful architecture using Django REST Framework
- Nested serializers for order items
- Consistent API response structure
- Permission-based access control

---

## Tech Stack

- Python 3
- Django
- Django REST Framework
- Simple JWT
- postgreSQL (ecommerce module)
- SQlite (task_manager_api)
- Django Filters

---

## API Endpoints

### Authentication
- POST /api/token/ → Obtain JWT token
- POST /api/token/refresh/ → Refresh token
- POST /api/register/ → Register new user

---

### Tasks API
- GET /api/tasks/ → List user tasks
- POST /api/tasks/ → Create task
- GET /api/tasks/{id}/ → Retrieve task
- PATCH /api/tasks/{id}/ → Update task
- DELETE /api/tasks/{id}/ → Delete task

---

### Orders API
- GET /api/orders/ → List user orders
- POST /api/orders/ → Create order with items
- GET /api/orders/{id}/ → Retrieve order
- PATCH /api/orders/{id}/ → Update order (admin only)
- DELETE /api/orders/{id}/ → Delete order (admin only)
- PATCH /api/orders/{id}/update_status/ → Update order status (admin only)

---

## Setup Instructions

```bash
git clone https://github.com/Iamojochenemi/task-manager-api.git
cd task-manager-api

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
# Task Manager API

A secure, multi-user Task Management API built with Django REST Framework and JWT authentication.

## Features

- User authentication with JWT
- Each user manages only their own tasks
- Create, update, delete tasks
- Mark tasks as completed or uncompleted
- Filtering, searching, and ordering

## Tech Stack

- Django
- Django REST Framework
- Simple JWT
- SQLite

## Setup

git clone https://github.com/Iamojochenemi/task-manager-api.git
cd task-manager-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## API Endpoints

- /api/token/  (POST)
- /api/token/refresh/  (POST)
- /api/tasks/  (GET, POST)
- /api/tasks/<id>/  (GET, PATCH, DELETE)
