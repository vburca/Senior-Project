Senior-Project
==============
Computer Science Senior Project (2013-2014)

Project Paper: http://digitalrepository.trincoll.edu/theses/393/

Expander Graphs - generating "good" expander graphs using a variation of Margulis' approach.

## Install Git
Install the latest version of git from git clone [https://github.com/git/git.git](https://github.com/git/git.git)
If you have git installed already, update to the latest version:
    
    git clone https://github.com/git/git.git 


## Install PIP (Python package installer)

    curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    [sudo] python get-pip.py

[http://www.pip-installer.org/en/latest/installing.html](http://www.pip-installer.org/en/latest/installing.html)


## Install Virtual Environment (virtualenv)
Virtual environment is an environment for python that will help you create different package configurations for different projects (similar to Ruby's gemsets).

    [sudo] pip install virtualenv

[https://pypi.python.org/pypi/virtualenv](https://pypi.python.org/pypi/virtualenv)


## Clone the repo

    git@github.com:vburca/Senior-Project.git


## Activate Environment
In order to activate the VirtualEnvironment (that contains the libraries needed for the project, including [NumPy](http://docs.scipy.org/doc/numpy/reference/index.html)), run

    source activate_environment
*to disable the environment, run `deactivate`*
