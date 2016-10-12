# Improve A Django Project
Improving on a Django Project - TeamTreehouse

## Prerequisites
 - Python 3
 
## To Run
  1. Open a command-line or terminal window.
  2. `cd` into the project directory
  3. We must install the project dependencies:
     `pip install -r requirements.txt`
  4. We need to migrate the sql db so:
     `python manage.py makemigrations`
     `python manage.py migrate`
  5. Start the server
    `python manage.py runserver`
    
     or
     
    `python manage.py runserver 0.0.0.0:8000`
  6. Open browser to that address.
