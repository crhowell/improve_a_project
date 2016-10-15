# Improve A Django Project
Improving on a Django Project - TeamTreehouse

## Prerequisites
 - Python 3

## To Test
  1. Open a command-line or terminal window.
  2. `cd` into the project directory
  3. To test menu app
   `python manage.py test menu`
    
     or
    
     With coverage
     `coverage run ./manage.py test menu`
     `coverage report`
    
  
## To Run
  1. Open a command-line or terminal window.
  2. `cd` into the project directory
  3. We must install the project dependencies:
     `pip install -r requirements.txt`
     
  4. Start the server
    `python manage.py runserver`
    
     or
     
    `python manage.py runserver 0.0.0.0:8000`
  5. Open browser to that address.
