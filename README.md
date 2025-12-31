### A RESTful API for a library Management System using Django Rest Framework and sqlite3.

## Techstack: 
Python,Django,DjangoRestFramework, sqlite3

## Getting Started:
__Step 1:__ Clone the repository: 
```
git clone https://github.com/PratikG345/Library_api.git
```

__Step 2:__ Create virtual environment by using 
```
py -m venv env
```

__Step 3:__ Activate the virtual environment by 
```
env/Scripts/activate
```
__Step 4:__ navigate to project 
```
cd library
```
__Step 5:__ run on local server 
```
python3 manage.py runserver
```
## API Endpoints: 
1. __GET books/__ - list all books
2. __POST books/create/__ - create a book
3. __GET books/{id}/__ - Retrive details of single book
4. __PUT books/{id}/__ - Update a book
5. __DELETE books/{id}/__ - Delete a book

## Project Scope
This project was intentionally kept simple to strengthen backend fundamentals:
1. Clean model definition
2. Basic CRUD APIs
3. Proper request/response handling
4. Understanding DRF serializers and views

No authentication or advanced features were added by design.
