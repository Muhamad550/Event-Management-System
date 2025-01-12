# Event Management API

This project is a backend solution for managing events using Django and Django REST Framework (DRF). It allows users to perform CRUD operations (Create, Read, Update, Delete) on events, while also handling user authentication and ensuring data security.

## Features
- **CRUD Operations**: Create, read, update, and delete events.
- **Authentication**: Secure login with Django's built-in authentication system.
- **Access Control**: Admin users can manage events, while regular users can only view them.
- **Database**: PostgreSQL for storing event and user data.
- **Deployment**: Deployed on Heroku for easy access.

## Technologies Used
- **Backend**: Django and Django REST Framework
- **Database**: PostgreSQL
- **Deployment**: Heroku
- **Version Control**: Git and GitHub

## Installation
1. Clone the repository:  
   ```bash  
   git clone https://github.com/Muhamad550/Event-Management-System.git  
   cd Event-Management-System  
Install dependencies:
bash
نسخ الكود
pip install -r requirements.txt  
Configure the database in settings.py with your PostgreSQL credentials.
Apply migrations:
bash
نسخ الكود
python manage.py migrate  
Run the server:
bash
نسخ الكود
python manage.py runserver 
