How to github page with git subtree merge 
#########################################

:date: 2012-08-19 
:tags: github, git, pelican
:category: git
:author: Rach Belaid

This post is about using ``git subtree merge`` to have a branch a subset of an other branch. 
The Github will be a use case and a way to illustrate this feature, there is probably others
way to accomplish the same result.

Github have a way for hosting and serve static web page,
which is very pratical if you need to create a page for your opensource project
or create a blog like this one that you are reading now!

If you never hear about Github Page then the first place to start is 
on the official doc about `Github page <http://pages.github.com/>`_.
But if are interrest to build a custom page that I personnaly found most of my answer
on their `help page <https://help.github.com/categories/20/articles>`_.

Let's do a quick summarize..

There is 3 type of Github page : **User**, **Organisation** and **Project page**

- The User and Organisation page share the same behavior :

        The static page is read from the ``master`` branch and from the repo called ``username.github.com`` 
        and for organisation ``organisation.github.com``.

        Which means you should have some something like that for the repo url for a User Page:

        ::

                [SSH]     git@github.com:username/username.github.com.git 
                [HTTPS]   https://github.com/username/username.github.com.git

        or for organisation :

        ::

                [SSH]     git@github.com:organisation/organisation.github.com.git 
                [HTTPS]   https://github.com/organisation/organisation.github.com.git

        The website will be accesible via ``username.github.com`` or ``organisation.github.com`` and
        it will read the index.html inside the root folder.

        eg: You can found the repo of this blog on  https://github.com/rach/rach.github.com and access to it via http://rach.github.com/

- Project Page are slightly different :

        The static page is read from the ``gh-pages`` branch and access the website via ``username.github.com/projectname``.
        And the repo stay the same as the project one.


Now it's there that the problem arrive, maybe for any reason you don't want to have
your static website in the root folder. In my concern, I m'using pelican which is 
a static blog generator and I want to have static output in a specific directory.
I won't be Pelican specific but that could be your case if you are using anything to generate your page that you don't want to expose directly : Mardown, Less, Rst, Template ... 

Let's assume for the following that we are building a User Github Page and
you have a source and output folder as below :

::

        (root)
           |-> output
           |-> source
        

That mean that we want to have the master branch centered on the output folder which a perfect use case for subtree merg.Like say the doc on git subtree merge :

| *"There are situations where you want to include contents in your project
  from an independently developed project. 
 You can just pull from the other project as long as there are no conflicting paths.*
| ...
| *What you want is the subtree merge strategy, which helps you in such a situation."*
| `reference <http://www.kernel.org/pub/software/scm/git/docs/howto/using-merge-subtree.html>`_

In our case we are not going to pull for an other project but the idea is the same.

In other words, we want to have the root of ``master`` branch pointing the ``output`` 
of the ``source`` branch and being easy to update.
We are going to merge the ``output`` folder of the ``source`` branch of same repository into the ``master`` (your current branch).

Here is the command sequence you need: 

.. code-block:: none

        (source)$ git checkout --orphan master
        (master)$ git rm -rf .
        (master)$ git merge -s ours --no-commit origin/source
        (master)$ git read-tree -m -u source:output
        (master)$ git commit -m "Merge folder output of branch source"

1. Create an orphan branch, which is a branch without parent
2. Remove any previously tracked element
3. Prepare for the later step to record the result as a merge.
4. Read folder ``output`` of ``source`` branch into the current directory.
5. commit the merge .

.. note:: For maintaining the result,  merges using "subtree" 
      
        git pull -s subtree origin source

.. note::  Alternative to create an empty branch
        true | git mktree | xargs git commit-tree | xargs git branch master
