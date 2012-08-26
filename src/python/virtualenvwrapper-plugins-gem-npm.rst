Virtualenvwrapper plugins for gems and npm's
############################################

:date: 2012-08-25 
:tags: virtualenvwrapper, virtualenv, ruby , nodejs
:category: python
:author: Rach Belaid

I love virtualenv and when I have to install some libs globably, it makes me mad. 

In a previous `post </keep-your-gems-and-npms-inside-your-virtualenv.html>`_, I explained how to modify your activate script for being able
to encapsulate node and ruby packages which are called gems and npm's.

After realizing that virtualwrapper was offering a way to extend it via plugins.
I decided to wrote 2 tiny plugins for it for handling the hack automaticaly in a nicer way. 

.. note::  

        This post assume that you are using `virtualenvwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_,
        otherwise I advice you to check it first.

virtualenvwrapper gem plugin   
============================

It happen more and more often that I'm trying some ruby packages.
Ruby has some very good apps like : `chef <http://www.opscode.com/chef/>`_, `sass <http://sass-lang.com/>`_,
`localtunnel <http://progrium.com/localtunnel/>`_, ... 


Download and install
--------------------

I encourage you to install it via ``pip`` ::

        pip install virtualenvwrapper.gem

Otherwise you can download `virtualenvwrapper.gem <http://pypi.python.org/pypi/virtualenvwrapper.gem>`_ on pypi 
and installing by running ::

        python setup.py install 


.. warning:: Where to install it

        This package cannot be installed inside a virtualenv but as to be globaly like virtualenvwrapper

How to use it
-------------

::

        mkvirtualenv test
        workon test #if not already inside
        gem install sass
        which sass #> $VIRTUAL_ENV/lib/gems/bin/sass

 
virtualenvwrapper npm plugin 
============================  

Even if I'm not a fan of nodejs, I have to admit that the node's app
for frontend processing and testing are awesome, eg : `less <http://lesscss.org/>`_,
`r.js <http://requirejs.org/docs/optimization.html>`_, `buster.js <http://busterjs.org/>`_


Download and install:
---------------------

I encourage you to install it via ``pip`` ::

        pip install virtualenvwrapper.npm

Otherwise you can download `virtualenvwrapper.npm <http://pypi.python.org/pypi/virtualenvwrapper.npm>`_ on pypi 
and installing by running ::

        python setup.py install 


.. warning:: 

        This package cannot be installed inside a virtualenv but as to be installed globaly like virtualenvwrapper
        

How to use it
-------------

::

        mkvirtualenv test
        workon test #if not already inside
        npm install less
        which lessc #> $VIRTUAL_ENV/bin/lessc

