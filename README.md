[![Build Status](https://travis-ci.org/Ogollah/Questioner.svg?branch=develop)](https://travis-ci.org/Ogollah/Questioner)  [![Coverage Status](https://coveralls.io/repos/github/Ogollah/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/Ogollah/Questioner?branch=develop)  [![Maintainability](https://api.codeclimate.com/v1/badges/eab2d4d71fc565021f7e/maintainability)](https://codeclimate.com/github/Ogollah/Questioner/maintainability)

# Questioner
```
Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize
questions to be answered. Other users can vote on asked questions and they bubble to the top
or bottom of the log.
```

# Questioner API Endpoints
|Endpoint                                 | Functionality                    |HTTP method 
|-----------------------------------------|----------------------------------|-------------
|/api/v1/user/signup                      |Signup account                    |POST        
|/api/v1/user/auth/signin                 |Signin in user                    |POST
|/api/v1/user/auth/signout                |Signout in user                   |POST
|/api/v1/meetups/create                   |Create a meetup record            |POST
|/api/v1/meetups/upcoming                 |Get upcoming meetups              |GET
|/api/v1/meetups/<meetup-id>              |Fetch specific upcoming meetup    |GET
|/api/v1/questions/questions              |Fetch all question                |GET
|/api/v1/questions/<meetup-id>/create     |Create a question                 |POST
|/api/v1/questions/<question-id>          |Access a question                 |GET
|/api/v1/questions/<question-id>/upvote   |upvote specific question          |PATCH
|/api/v1/questions/<question-id>/downvote |downvote specific question        |PATCH
|/api/v1/questions/<meetup-id>/rsvp       |Rsvp a specific meetup            |POST
|/api/v1/meetups/<meetup-id>/update       |Update specific upcoming meetup   |PATCH

### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/Ogollah/Questioner.git
  $ cd Questioner
  ```

2. Initialize and activate a virtualenv:
  ```
  $ python3 -venv env
  $ source env/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ manage.py run/test
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)

## GitHub pages

Go to [Questioner](https://ogollah.github.io/Questioner/UI/templates/index.html)

## Heroku

Go to [Heroku](https://metup-quiz-api-heroku.herokuapp.com/)

# Project Owner
   [Andela Kenya](https://andela.com/?gclid=Cj0KCQiA1NbhBRCBARIsAKOTmUu9zzKI7k5uTm4K6kn6Wyv5Uk9S_JgBZCJia4FM98S8nMVuQ2DJePEaAlF9EALw_wcB)

# Developer
   [Stephen Ogolla](https://github.com/Ogollah/)

