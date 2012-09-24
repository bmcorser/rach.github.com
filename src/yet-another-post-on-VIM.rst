Yet another post on VIM
========================

What will be a technical blog without a post on VIM, some people will think.
But this post have been wrote initialy for me as guideline and documention 
for reminding my  the essantial commands and the WHY!
"What my command for doing that?" 
"Why do I have this plugin?" 
"What did I change that in my `.vimrc`."

Introduction
------------


At the start, Vim look like a mysterious ugly black box. So why using it?
Personaly my story, is the one of somebody who probably used the most popular IDE:
Eclipse, Textmate, Sublime, NetBean, Pycharm ...
Mostly desapointed by most of them, one day decided:
-  I want to have one IDE (one to rull them all)
-  The next IDE that I learn  will be the last ... or at least hope so
-  And more important than everything else, it needs to be OPENSOURCE  I hope.

VIM out of the box is a big block of marble, it does take time to get the result 
that you want. You will maybe get quickly the rough line of the result but it
will require polish.

If you are looking about motivation about "Should I use VIM or not".
Here is not the right place, I'm already convinced and wont be objective.
But  more people  use it and more it will becomme awsome.

.. quote::  "Vim Creep" -> http://www.rudism.com/s/vimcreep

	*Your eyes twinkled from the glow of rows upon rows of monitors in the darkened computer
	 lab as you witnessed in awe the impossible patterns of code and text manipulation 
	that flashed across the screen.

	"How did you do that?" you asked, incredulous.

	The pithy, monosyllabic answer uttered in response changed your life forever: "Vim."*

Get Started
-----------

Package
-------

Vundle 
https://github.com/gmarik/vundle

Vundle is short for Vimbundle and is a Vim plugin manager.


File navigation 
--------------- 

Neerdtree

vim-powerline

Search 
------
ack.vim

Buffer/Clipboard
----------------

YankRing

gundo.vim   http://sjl.bitbucket.org/gundo.vim/
"You know that Vim lets you undo changes like any text editor. What you might not know is that it doesn't just keep a list of your changes — it keeps a goddamed tree of them. "

Vesionning controle 
-------------------

Git : fugitive 
Mercurial : 

Check:
-----

Code 

comment : https://github.com/scrooloose/nerdcommenter
syntastic
localrc : http://www.vim.org/scripts/script.php?script_id=1408


python : http://www.vim.org/scripts/script.php?script_id=790




spell check 
-----------

" Set region to British English
set spelllang=fr

"""""""
"Mapping
"
" Toggle spell checking on and off with `,s`
let mapleader = ","

:set spell!
Cannot find spell file for "fr" in utf-8
Do you want me to try downloading it?

Downloading fr.utf-8.spl...
:!curl 'http://ftp.vim.org/pub/vim/runtime/spell/fr.utf-8.spl' -o '/var/folders/yp/30hnj8090yvcq2txj7b9ysf00000gn/T/vrcDgXU/0.
spl'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
"/var/folders/yp/30hnj8090yvcq2txj7b9ysf00000gn/T/vrcDgXU/0.spl" [noeol] 1122L, 571626C
In which directory do you want to write the file:
1. /usr/local/Cellar/macvim/7.3-64/MacVim.app/Contents/Resources/vim/runtime/spell
"/usr/local/Cellar/macvim/7.3-64/MacVim.app/Contents/Resources/vim/runtime/spell/fr.utf-8.spl" [New] 1122L, 571627C written
Do you want me to try getting the .sug file?
This will improve making suggestions for spelling mistakes,
but it uses quite a bit of memory.

Downloading fr.utf-8.sug...
:!curl 'http://ftp.vim.org/pub/vim/runtime/spell/fr.utf-8.sug' -o '/var/folders/yp/30hnj8090yvcq2txj7b9ysf00000gn/T/vrcDgXU/0.
sug'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
"/usr/local/Cellar/macvim/7.3-64/MacVim.app/Contents/Resources/vim/runtime/spell/fr.utf-8.sug
