# RNG-WebApp


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/ltlx4/RNG-WebApp.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install django
    $ pip install django-crispy-forms
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
