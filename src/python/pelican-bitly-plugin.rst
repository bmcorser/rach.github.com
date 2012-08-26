bit.ly plugin for pelican
#########################

:date: 2012-08-26
:tags: analytics, pelican
:category: python
:author: Rach Belaid
:twitter_msg: Bit.ly plugin for Pelican from @rachbelaid #python #bitly #pelican  

I started writing this blog using `Pelican <http://pelican.notmyidea.org/en/3.0/>`_ which is static blog generator 
build by `Alexis Metaireau <http://blog.notmyidea.org/>`_ and based on technologies that I know and mainly that I don't hate : Python, Rst, Jinja2 ...

During the customization of this blog, I wanted to be able to know how the posts will be shared by using a url shortener like `bit.ly <http://bit.ly/>`. 
Since Pelican support plugin from the version 3.0 and I hate doing repeating tasks, why not to write a plugin for it?

I'have been amazed how easy it has been to wrote this plugin.
Pelican provide a easy way to register signals which is documented `here <http://pelican.notmyidea.org/en/3.0/plugins.html>`_

The only issues met was that the signal required for me was not existing yet. But it has been just fine with a bit of monkey patching.

If you have a need for it, feel free to use this plugin and report any bugs or feedback on the `pelican.bitly github project <https://github.com/rach/pelican.bitly>`_. 


Download and install
--------------------

I encourage you to install the plugin via ``pip`` ::

        pip install pelican.bitly

Otherwise you can download `pelican.npm <http://pypi.python.org/pypi/pelican.bitly>`_ on pypi 
and installing it by running ::

        python setup.py install 

How to use it
-------------

To load the plugin, you have to add it in your settings file. 

.. code:: python

        PLUGINS = ['pelican-bitly',]


.. note:: you can setup the plugin by specifying a string with the path to with the path to it or import it and add the module in the list
        

For being able to use this pluging you need to have SITEURL defined in your settings file, otherwise the plugin has no way to guess the absolute url. 

.. code-block:: python

        SITEURL = 'http://example.com' 

The last step is adding  your bit.ly username and api key in your settings file

.. code-block:: python

        BITLY_USERNAME = 'username'
        BITLY_API_KEY = 'api_key'

.. warning:: 
        
        If you are using a public repository as Github for the keeping the source code of your pelican site then think about keeping the settings 
        ``BITLY_USERNAME`` and  ``BITLY_API_KEY`` in a separated settings file (eg: ``local_settings.py``) and added this one to your ``.gitignore``
        

Now that the plugin is configured, you can rebuilt your site and you should see  the short url being created in the ``pelican`` output :: 

        -> generate short url http://example.com/post_example.html -> http://bit.ly/XXXXXX


From your templates,you can now access the bitly url of the ``article`` and ``page`` object from the ``bitly_url`` attribute ::

        {{ article.bitly_url }}
        {{ page.bitly_url }}



