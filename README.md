# my-first-blog
Create a local virtual environment with `virtualenv` and install the dependencies with `pip`.

### Ensure you are using Python version 3
python3 --version  
 I have running in venv Python 3.8.2
### Once you're in that virtualenv run 
pip install -r requirements.txt
### Migrate database by running
python manage.py migrate
### Run the server by running
python manage.py runserver
  #### Starting development server:
   http://127.0.0.1:8000/

For the language guide tutorial, see https://circleci.com/docs/2.0/language-python/

# Configuring a Python Application on CircleCI

[This document](https://circleci.com/docs/2.0/language-python/) describes how to configure CircleCI using a sample application written in Python.
## Overview

This guide uses this sample Django application to describe configuration best practices for Python applications building on CircleCI. The application is hosted on GitHub and is building on CircleCI.

Consider forking the repository and rewriting the configuration file as you follow this guide.
