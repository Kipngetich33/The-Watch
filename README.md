# App Name
The Watch

## Description
This is a web app that allows users to sign up as part of a neighborhood  stay updated on the different things and information about the neigborhood on all factors including finding handymen, meetings etc.

## User Stories
* A user can sign in to the application
* A user can create a profile and set profile with general information and location
* A user can view a list of different businesses in my neighborhood.
* A user can Rate the different Businesses.
* A user can Find the contact Information of different handymen such Electricians
* A user can leave a review for the different handymen.
* A user can find contact Information public services such as health department and the police department.
* A user can post to as well as view posts on their neighborhood tutorials
* A user can move out of a neighborhood
* A user can only view information concerning their neighborhood

## Set Up and Installation

#### Prerequisites

* Python 3.6.2
* Virtual environment
* Postgres Database
* Reliable Internet Connection

## Installation Process

* Copy repolink

in your terminal run the following commands

* $ git clone REPO-URL in your terminal
* $ cd watch
* $ python3.6 -m venv virtual
* $ touch .env ( to the file add :
        SECRET_KEY=<your secret key>
        DEBUG=True)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt
* $ psql ; CREATE DATABASE instagram ;

In the settings.py module of the project make the following changes

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'watch',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}

* $ python3.6 manage.py runserver (this command runs the application of port http://127.0.0.1/8000 )
 
## Known Bugs

No known bugs

## CREDITS

Moringa School,Python Documentation, StackOverflow.com and W3 schools

## Technologies Used

This project uses major technologies which are :

* HTML5/CSS
* Bootstrap
* Python3.6
* Django Frane Work
* Postgress Database

## Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through khalifngeno@gmail.com or leave a comment here on github.

## License 

Copyright MIT [LiCENSE](./LICENSE) (c) 2017 [Kipngetich Ngeno](https://github.com/Kipngetich33)

