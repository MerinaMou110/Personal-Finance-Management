

 Personal Finance Management System

 Objective

Develop a "Personal Finance Management System" using Django, Django REST Framework, and PostgreSQL. This application helps users track their income, expenses, and savings goals.

Features

- User registration with email confirmation
- User authentication and token-based authorization
- CRUD operations for income, expenses, and savings goals
- Filtering transactions based on date ranges
- Profile management including updating user details

 Requirements

- Python 3.x
- Django 3.x
- Django REST Framework
- PostgreSQL
- Node.js (for frontend setup)


Backend Setup

1. Clone the repository

2. Set up a virtual environment


3. Install the required Python packages:

    
    pip install -r requirements.txt
    

4. Configure PostgreSQL database
        

5. Create a `.env` file in the project root directory with the following content:

    env
    SECRET_KEY=your_secret_key
    DB_NAME=financeapp
    DB_USER=financeuser
    DB_PASSWORD=password
    DB_HOST=localhost
    DB_PORT=5432
    EMAIL=your_email@example.com
    EMAIL_PASSWORD=your_email_password
    

7. Run database migrations:

     python manage.py migrate
    

8. Create a superuser:

    
    python manage.py createsuperuser


9. Start the backend server:

    python manage.py runserver
    

Frontend Setup

1. Navigate to the frontend directory :
    cd frontend

 API Documentation


Authentication Endpoints

- https://personal-finance-management-hauf.onrender.com/authenticate/register/: Register a new user.
   

- https://personal-finance-management-hauf.onrender.com/authenticate/login/: Log in a user.
    

- https://personal-finance-management-hauf.onrender.com/authenticate/logout/: Log out a user.
    
 User Endpoints

- https://personal-finance-management-hauf.onrender.com/users/: Get user details.
    
 


Income Endpoints

-https://personal-finance-management-hauf.onrender.com/finance/incomes/: Get all incomes for the authenticated user.
  


Expense Endpoints



-https://personal-finance-management-hauf.onrender.com/finance/expenses/: Add a new expense.
   

Saving Goal Endpoints

-
- https://personal-finance-management-hauf.onrender.com/finance/savings_goals/: Add a new savings goal.
    

This README provides a comprehensive guide to setting up, running, and using your Personal Finance Management System. Adjust the content as necessary to fit the specifics of your project.
