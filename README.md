Simple registration App

Install virtual environment using virtualenv -p python3 $ virtualenv -p python3 env

Enable virtualenv $ source env/bin/activate

goto inside project folder location and start the server and run following commands
  `python manage.py makemigrations`
  `python manage.py migrate`
  `python manage.py runserver`

User can access index view pages at root url.
For rest API please find following paths:
  1. login: 'api/login'
  2. register: 'api/register'
  3. change password:  'api/change_password'  This api requires user to be authenticated (Token Based).
