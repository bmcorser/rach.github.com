How to use the subtree merge strategy
#####################################

:date: 2010-10-03 10:20
:tags: thats, awesome
:category: yeah
:author: Rach Belaid

There are situations where you want to include contents in your project from an independently developed project. You can just pull from the other project as long as there are no conflicting paths.

The problematic case is when there are conflicting files. Potential candidates are Makefiles and other standard filenames. You could merge these files but probably you do not want to. A better solution for this problem can be to merge the project as its own subdirectory. This is not supported by the recursive merge strategy, so just pulling won’t work.

What you want is the subtree merge strategy, which helps you in such a situation.

In this example, let’s say you have the repository at /path/to/B (but it can be an URL as well, if you want). You want to merge the master branch of that repository to the dir-B subdirectory in your current branch.

Here is the command sequence you need: 

.. code-block:: none
   :linenos:

   $ git remote add -f Bproject /path/to/B
   $ git merge -s ours --no-commit Bproject/master
   $ git read-tree --prefix=dir-B/ -u Bproject/master #3
   $ git commit -m "Merge B project as our subdirectory" #4
   $ git pull -s subtree Bproject master #5


1. name the other project "Bproject", and fetch.

2. prepare for the later step to record the result as a merge.

3. read "master" branch of Bproject to the subdirectory "dir-B".

4. record the merge result.

5.  maintain the result with subsequent merges using "subtree"

The first four commands are used for the initial merge, while the last one is to merge updates from B project.
