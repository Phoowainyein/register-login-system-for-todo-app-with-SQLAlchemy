# register-login-system-for-todo-app-with-SQLAlchemy
Implementing todo app with SQLAlchemy,Python

## To Run ##

* Run `main.py`
```php
python3 main.py
```

## Task Description ##

Implementing user  register/login functionality for todo-app users. Associated each todo item for each user will be added created in the database .

After launching `main.py ` ,the application will ask you if the user wants to Register or Login .

* If user wants to REGISTER, the application  will ask the user for the username and password combination
	  * If user with this username already exists in the table users, app will notify about that and not create the new user
    *	If this username did not exist, it will  create account for the user in the table users

* If user wants to LOGIN, the application will  ask user the username and password
  *	If the given username and password combination does not exist in the table users, then it will inform user about this and do not allow user into the system
  *	If this username and password combination exists in the table users, then allow the user in the system and store the user that logged in


* User will be able to add new to-do item and remove each item that is associated with the user.

## Here is UML diagram

![tododb](todo_db.png?raw=true "To-Do app Database")
