# Speech order
It is a Django project, that allows you to make different online orders using your voice.


## Apps
There are two apps:
- Pizza
- Our Pizzeria


#### Pizza
It is an app using which you can order a pizza in supported pizzerias.

The app currently supports only one pizzeria - Our Pizzeria, but it is easy to add new ones.

#### Our Pizzeria
It is an online pizzeria, that may be opened.

## Using
You must have Python 3.5 and PIP installed on your machine.

You have to install requirements using PIP in your command line. The command for it is 'pip3 install -r requirements.txt'. It has to be called from the root folder of the project.

When everything is ready, you should call the command 'python3 manage.py runserver' from the root folder to run a project server.

Finally, the site is ready to use. You should past http://127.0.0.1:8000/ in your browser (Speech Order works fully only in Google Chrome) URL field to see it.


## Tests
The project can be tested if you use the command 'python3 manage.py test'.


## Administration
You can administrate the site using an admin site 'http://127.0.0.1:8000/admin/' (login = admin, password = WebChallenge).
