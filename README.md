This Project is using django version 2.0 with python3.

Install virtual environment using virtualenv -p python3 $ virtualenv -p python3 env

Enable virtualenv $ source env/bin/activate

goto inside project folder location and start the server and run following commands <br />
  `python manage.py makemigrations` <br />
  `python manage.py migrate` <br />
  `python manage.py runserver` <br />
  
You will need to install RabbitMQ and Celery in order to send asynchronous email after sign-up.
Currently this app sends only console E-mail. 
So, you will be able to see email printed in your console window.

To install Celery:  `pip install Celery`
To install rabbitmq-server on Ubuntu: 
    `apt-get install -y erlang` <br/>
    `apt-get install rabbitmq-server` <br/>

Then enable and start the RabbitMQ service:
    `systemctl enable rabbitmq-server` <br/>
    `systemctl start rabbitmq-server` <br/>
    
Now you can start the RabbitMQ server using the following command:
    `rabbitmq-server`
    
Starting The Worker Process
    Open a new terminal tab, and run the following command:
        `celery -A hidden_brains worker -l info` <br/>
    Change hidden_brains to the name of your project.

User can access index view pages at root url.
For rest API please find following paths:
  1. login: 'api/login'
  2. register: 'api/register'
  3. change password:  'api/change_password'  This api requires user to be authenticated (Token Based).
