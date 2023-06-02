# My Todo list

Django Todo List is a simple web application that allows users to create and manage their daily tasks. This project is built using the Django web framework and Bootstrap for styling.

### Features:
- Tag and Task page
- Create, update, and delete tasks, tag
- Mark tasks as completed or not completed
- Tasks auto filter by completed status or date added

### Installation
Create .env file and populate it with necessary env variables which are listed in .env_sample
And then run following commands:
```shell
git clone https://github.com/bythewaters/todo-list.git
cd Todo_lsit
python3 -m venv venv 
source venv/bin/activate 
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
