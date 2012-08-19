Monitor and aggregate your logs with Sentry
###########################################

:date: 2012-08-19 
:tags: monitoring, logs, python
:category: python
:author: Rach Belaid
:status: draft


Setting up Sentry server
========================

Dependencies
------------

- Python dev packages :: 

   apt-get install python-setuptools python-dev

- PostgreSQL ::  

   sudo apt-get install postgresql

Create a place to keep the venv

sudo mkdir -p /usr/local/venv/
sudo chmod og+w /usr/local/venv

Install and create a virtualenv
-------------------------------

Keep you package clean, use a virtualenv.

- Install::  
    
    sudo apt-get install python-pip
    sudo pip install virtualenv

- Create venv::

    virtualenv /usr/local/venv/sentry/
    

Setting up the database
-----------------------

Install Mysql :: 

    sudo apt-get install mysql-server libmysqlclient-dev
    
- Create a database for sentry  ::

    sudo mysql -p -e "CREATE DATABASE sentry;"
     
- Create a sentry user and grant him  privilege :: 

       sudo mysql -p -e "GRANT ALL ON sentry.* TO sentry@localhost IDENTIFIED BY 'PASSWORD';"

.. note::

    If you need to send a password via command line then think about adding some space
    at the start of the line. This will guarantee that the command is not kept in history.
  


Install Sentry
--------------

Activate the venv and install sentry ::
   
    source /usr/local/venv/sentry/bin/activate
    pip install sentry

Install other dependencies inside the venv ::

    pip install MySQL-python

Init the configuration ::

    sentry init /etc/sentry.conf.py


Configure Sentry
---------------- 

You need to configure the database access for the sentry user ::

    DATABASES = {
        'default': {
            # You can swap out the engine for MySQL easily by changing this value
            # to ``django.db.backends.mysql`` or to PostgreSQL with
            # ``django.db.backends.postgresql_psycopg2``
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'sentry',
            'USER': 'sentry',
            'PASSWORD': 'SENTRY_PASSWORD',
            'HOST': '',
            'PORT': '',
        }
    }


You need to select what will be your web host and port but the default could be enough ::

    SENTRY_WEB_HOST = '0.0.0.0'
    SENTRY_WEB_PORT = 8080

.. DANGER:: make the access private ::

        ENTRY_PUBLIC = False

.. note:: You should configure the URI to Sentry

It will attempt to guess it if you don't but proxies may interfere with this.::


    SENTRY_URL_PREFIX = 'http://sentry.example.com'  # No trailing slash!



Setup db
--------

If you changed from the default SQLite database, make sure you start by creating the database Sentry is expecting. Once done, you can create the initial database using the upgrade command: ::
  
        sentry --config=/etc/sentry.conf.py upgrade

It’s very important that you create the default superuser through the upgrade process. If you do not, there is a good chance you’ll see issues in your initial install.

If you did not create the user on the first run, you can correct this by doing the following: ::

    # create a new user
    sentry --config=/etc/sentry.conf.py createsuperuser

    # run the automated repair script
    sentry --config=/etc/sentry.conf.py repair --owner=<username>

All schema changes and database upgrades are handled via the upgrade command, and this is the first thing you’ll want to run when upgrading to future versions of Sentry.

Setting up an Apache Proxy for port 80 -> 8080
----------------------------------------------

This configuration will setup Apache2 to proxy port 80 to 8080 so that you can keep Sentry running on 8080. ::

    sudo apt-get install apache2
    sudo a2enmod proxy
    sudo a2enmod proxy_http
    sudo a2enmod vhost_alias

You can remove the default vhost but I encourage to keep it allow access only via the right domain ::

    #do not do this next command if you already have virtual hosting setup that depends on the default site.
    sudo a2dissite default

Create a file called ``sentry`` in /etc/apache2/sites-available ::

    <VirtualHost *:80>
        ServerName sentry.rockaboxmedia.com
        ProxyRequests Off
        <Proxy *>
            Order deny,allow
            Allow from all
        </Proxy>
        ProxyPreserveHost on
        ProxyPass / http://localhost:4080/
    </VirtualHost>

Add the new vhost and restart apache2 :: 
    
    sudo a2ensite sentry
    sudo apache2ctl restart


Running Sentry as service
-------------------------

You need to install supervisor as a daemon  ::

    apt-get install supervisor

You need to update the configuration of supervisor in your install to be sure that  ::

    [program:sentry-web]
    directory=/usr/local/venv/sentry/
    command=/usr/local/venv/sentry/bin/sentry --config=/etc/sentry.conf.py start http
    autostart=true
    autorestart=true
    redirect_stderr=true

Configure a project in Sentry
=============================

Go to your sentry project url and log with the login and pwd of the superuser that you created previously

Create a project with a team ( it seem that the team is mandatory )
 
Now you can use the DSN in you project and follow the instruction matter of the technology:
 Django, Flask.

For Django :

Start by installing raven-python: ::
    pip install raven

Then simply modify your Django configuration:

::
    # Set your DSN value
    SENTRY_DSN = 'http://<PUBLIC_KEY>:<PRIVATE_KEY>@host:port/<PROJECT_ID>'

    # Add raven to the list of installed apps
    INSTALLED_APPS = INSTALLED_APPS + (
    # ...
    'raven.contrib.django',
    )

That's it! Raven automatically installs an error handling hook to pipe all uncaught exceptions to Sentry.

For Flask:

Start by installing raven-python and Blinker:

:: 
    pip install raven blinker

Blinker is required for signals to work within Flask.

Add the required configuration in your application setup: ::


    from raven.contrib.flask import Sentry

    app.config['SENTRY_DSN'] = 'http://<PUBLIC_KEY>:<PRIVATE_KEY>@host:port/<PROJECT_ID>'
    sentry = Sentry(app)

That's it! Raven automatically installs an error handling hook to pipe all uncaught exceptions to Sentry.


Extra Doc links:


- Raven : http://raven.readthedocs.org/en/latest/index.html
- Django : http://raven.readthedocs.org/en/latest/config/django.html
- Flask : http://raven.readthedocs.org/en/latest/config/flask.html
- Javascript : https://github.com/lincolnloop/raven-js
- PHP : https://github.com/getsentry/raven-phpi


Setting up outbound email
=========================

TODO


Setting up https 
================

TODO

Setting up SSO
==============

TODO

Upgrade Sentry
==============

TODO
