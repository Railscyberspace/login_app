# login_app

We’ll assume you have Django installed already. You can tell Django is installed and which version by running the following command in a shell prompt (indicated by the $ prefix):

$ python -m django --version

Creating a project: $ django-admin startproject mysite This will create a mysite directory in your current directory. If it didn’t work, see Problems running django-admin.

Let’s look at what startproject created:

Register/ manage.py Register/ init.py settings.py urls.py asgi.py wsgi.py

These files are:

The outer mysite/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like. manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py. The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls). mysite/init.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs. mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work. mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher. mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details. mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

Let’s verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands:

$ python manage.py runserver

You’ll see the following output on the command line:

Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied. Run 'python manage.py migrate' to apply them.

February 19, 2021 - 15:50:53 Django version 3.1, using settings 'mysite.settings' Starting development server at http://127.0.0.1:8000/ Quit the server with CONTROL-C.

Changing the port

By default, the runserver command starts the development server on the internal IP at port 8000.

If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:

$ python manage.py runserver 8080

your apps can live anywhere on your Python path. In this tutorial, we’ll create our poll app in the same directory as your manage.py file so that it can be imported as its own top-level module, rather than a submodule of mysite.

To create your app, make sure you’re in the same directory as manage.py and type this command:
python manage.py startapp polls
