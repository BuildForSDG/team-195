[![Build Status](https://travis-ci.org/BuildForSDG/team-195.svg?branch=develop)](https://travis-ci.org/BuildForSDG/team-195)

# GRADE SCHOOL API

This is a web API that users can register as tutors and students. The users first have to sign up then they'll have to complete their profile to access it's services.

## Tutors
- Can create courses
- Can create chapters for each course

## Students
- Subscribe to a course

### Langauge

```
Python
```

#### Framework
```
- django==3.0.5
- djangorestframework==3.11.0
```

## How to run the API

### Clone the repository

```
git clone git@github.com:BuildForSDG/team-195.git
```

### Change the directory to api's folder

```
path\to\folder\team-195> cd tutor
```

### Install dependancies

```
- pip install -r requirements/local.txt 
- pip install -r requirements/base.txt 
```

### Database configurations

#### For postgreSQL and prefered realational databases set enviroment variables as
```
- DATABASE_URL = psql://USER:PASSWORD@HOST:PORT/your-database
- TEST_DATABASE = psql://USER:PASSWORD@HOST:PORT/test-database
```

#### Make migrations and run migrations

```
- python manage.py makemigrations
- python manage.py migrate
```

### Run the API

```
python manage.py runserver
```

## API views

### Users sign up
```
POST /users/add/
```

### Tutor's registration
```
POST /users/tutors/register/
```

### Student's registration
```
POST /users/students/register
```

#### Update student's record
```
PUT /users/students/<int: student_id>
```

#### Gets all students' records
```
GET /users/students/all/
```

#### Gets a student's record
```
GET /users/students/all/<int:student_id>
```

#### Delete a student's record
```
DELETE /users/students/delete/<int:student_id>/
```

### Sign in
```
POST /api-token-auth/
```

#### Set authorization header for each request to access the resources
```
Authorization: Token "theToken"
```
### Course

#### Creates a grade level
```
POST /courses/grades/
```

#### Creates a course record
```
POST /courses/
```

#### Creates a chapter for a particular course
```
POST /courses/chapters/
```

#### View all courses and their chapters
```
GET /courses/
```

#### View a tutor and all courses he/she created
```
GET /users/tutors/<int:tutor_id>
```

### Makes a student to take a course
```
POST /users/students/<int:student_id>/courses/<int:course_id>/take_course
```

## Collaborators
- [Benard Wambua](https://github.com/BernardWambua)
- [Andrew Njaya](https://github.com/Njaya2019)
- [Peter Kuria](https://github.com/peterkuria)

## References
- [Django documentation](https://docs.djangoproject.com/en/3.0/)
- [Django rest framework](https://www.django-rest-framework.org/)
- [PostgreSQL docs](https://www.postgresql.org/)
