# PetCareExchange API

PetCareExchange API is a RESTful web API that allows you to manage pet sitters and pets, including creating, editing, getting, and deleting them. It is built using the Django Rest Framework and uses PostgreSQL as a powerful and open-source relational database management system. Additionally, it leverages AWS S3, a web-based cloud storage service, for storing pet images. To access the front-end for this API, visit [front-end-pet-care-exchange](https://github.com/viktoriiazolotova/front-end-pet-care-exchange).

## Technologies Used:

1. Django: a high-level Python web framework for the backend
2. PostgreSQL: A powerful, open-source relational database management system.
3. AWS S3: A web-based cloud storage service for storing images.
4. React.js - for building front end.
5. Heroku: a platform for deploying and running applications.

## Basic Features:

1. Custom petsitter model with CRUD endpoints
2. Custom pet model with CRUD endpoints
3. One-to-many relationship between petsitters and pets
4. Amazon S3 storage for storing pet images


## Getting Started

1. Clone the repository to your local machine:
``` 
$ git clone https://github.com/viktoriiazolotova/django-react-pet-care-exchange.git
```

2. Create and activate a Python virtual environment:
```   
python3 -m venv env
source env/bin/activate
```

3. Install the required packages:
```    
$ pip install -r requirements.txt
```

4. Set up a Postgres database for the project.
    
5. Create .env file and update the environment variables accordingly:
```       
SECRET_KEY=
#Database settings
DATABASE_URL='postgres://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName'
#AWS S3 settings
AWS_S3_ACCESS_KEY_ID=
AWS_S3_SECRET_ACCESS_KEY=
```

6.  Note: For local development, comment AWS settings under settings.py, 
the pictures will be stored to the local storade under /media directory.
    
7. Run the following commands to setup the database tables and create a super user.
```   
$ python manage.py migrate
$ python manage.py createsuperuser
```

8. Run the development server using:
```  
$ python manage.py runserver
```

9.  Open a browser and go to http://localhost:8000/ to access the API.

