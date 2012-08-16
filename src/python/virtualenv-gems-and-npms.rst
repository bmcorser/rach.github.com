How to have a virtualenv full of gems and npms
##############################################

:date: 2012-08-15 
:tags: virtualenv, ruby , nodejs
:category: python
:author: Rach Belaid


Alas the python community doesn’t have yet some of the great tools that the Ruby/Node community have like Compass , Chef , lessc

And when you are used to work with virtual environment the last thing that you want to do it’s starting to install lib globaly.

So stick the few lines below at the bottom of virtualenv’s ‘postactivate’ or at the enf of the ‘activate’ script.

.. code-block:: none
    export GEM_HOME="$VIRTUAL_ENV/gems"
    export GEM_PATH=""
    PATH="$GEM_HOME/bin:$PATH"
    export PATH
    export npm_config_prefix=$VIRTUAL_ENV

And now inside your virtualenv, you can do :

.. code-block:: none
    gem install <package>
    npm -g install  <package>

All yours gems/npms won’t be installed globaly but inside the vitualenv and will be deleted with it.
