# Event Management System

## Features
- Event management (Create, Read, Update, Delete).
- User authentication using Tokens.
- Access control (Only admins can manage events).
- PostgreSQL database.
- Deployment on Heroku.

## Technologies Used
- Django and Django REST Framework.
- PostgreSQL.
- Heroku for deployment.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ahmed194724496/Capstone-Project.git
   cd Capstone-Project
Install dependencies:

bash
Copy
pip install -r requirements.txt
Set up the database and run the server:

bash
Copy
python manage.py migrate
python manage.py runserver
API Endpoints
List all events: GET /events/

Create a new event: POST /events/

Update an event: PUT /events/{id}/

Delete an event: DELETE /events/{id}/

Authentication
Obtain a Token: POST /api-token-auth/

Use the Token in the Header: Authorization: Token {your-token}

Deployment to Heroku
Install Heroku CLI and log in.

Create a Heroku app and deploy the project:

bash
Copy
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
Contributing
Fork the repository, create a new branch, make your changes, and then create a Pull Request.

License
This project is licensed under the MIT License.

Copy

---

You can copy and paste this text into your `README.md` file. Let me know if you need further adjustments! 😊
