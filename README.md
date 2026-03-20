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
