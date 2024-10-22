Task Manager Application
This is a simple task management application built using Django. Users can register, log in, and manage tasks, including creating, updating, deleting, and marking them as completed.

Features
User Authentication: Users can register, log in, and log out using Django's built-in authentication system.
Task Management: Users can create, update, delete, and toggle the completion status of their tasks.
User-Specific Tasks: Each user can view and manage only their tasks.


Sure! Here's a short README file that provides an overview of your Django project:

Task Manager Application
This is a simple task management application built using Django. Users can register, log in, and manage tasks, including creating, updating, deleting, and marking them as completed.

Features
User Authentication: Users can register, log in, and log out using Django's built-in authentication system.
Task Management: Users can create, update, delete, and toggle the completion status of their tasks.
User-Specific Tasks: Each user can view and manage only their tasks.
Installation
Prerequisites
Conda
Docker
Set up the environment

Clone the repository:


git clone https://github.com/yourusername/task-manager.git
cd task-manager
Create the conda environment: Use the provided environment.yml file to create a conda environment:



conda env create -f environment.yml
conda activate django-project

Apply the migrations:

python manage.py migrate
Run the development server:

python manage.py runserver

Using Docker
Build the Docker image:

docker build -t task-manager .

Run the application:

docker run -p 8000:8000 task-manager

Running Tests
To run the tests, use the following command:

pytest
You can also use Docker to run tests:

docker build -t task-manager-test -f Dockerfile.test .
docker run task-manager-test