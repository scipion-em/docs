=====================
IDE Eclipse Standard
=====================

Eclipse is the integrated development environment (IDE) recommended for
Scipion. The features include: support for project creation and managed
build, standard make build, source navigation, various source knowledge
tools, such as type hierarchy, call graph, include browser, macro
definition browser, code editor with syntax highlighting, folding and
hyperlink navigation, source code refactoring and code generation.

.. contents:: Table of Contents

How to Install
==============

The Eclipse installation process has four main steps:

1.  Install the Java runtime environment (JRE 7.0 recommended)
2.  Install the Eclipse software (It does not includes JRE).
3.  Launch Eclipse.
4.  Install a set of plugins for extend functionality.

If you have the Java software installed, you only need to download the
Eclipse package from `[Eclipse download
page] <http://www.eclipse.org/downloads/>`_ be sure of select *Eclipse IDE
Standard* and for the platform you want( e.g.: Windows, Linux, 32 or 64 bits).
After that, you only need to untar the package and launch Eclipse. Is also
useful add a shortcut to the Desktop or Panel for launching.


Installing plugins
------------------

The process of installing plugins has become simpler in Eclipse. There
is an installation dialog under **Help -> Install New Software**. There
are some Software Sites installed from Eclipse Standard by default. You
can add your own for installing new plugins, test the connection,
disable Sites and using Export… / Import… its easy to share sets of
Software Sites between different installations or with others. After
the new site is added some Features will appear and can be checked for
install. There are some Options you can check to get only the latest
versions, hide already installed software and so on. If you don’t find
what you’re looking for, try to uncheck **Group items by category**, not
all available Plug-ins are categorized.


Python
------

There is a useful plugin for eclipse development, PyDev, which can be
installed from `[here] <http://pydev.org/updates/>`_

* How to add mi python code to a PYTHONPATH?: project -> properties -> pydevPYTHONPATH

Git
---

With most of Eclipse distributions, a git client will be built-in but,
otherwise, you can also install it using eclipse interface. The most
used plugin that give git functionalities to eclipse is called *EGit*
(which can be installed from the eclipse marketplace, using the eclipse
interface - menu "help" - or downloaded from `[here] <http://wiki.eclipse.org/EGit/User_Guide>`_).

Scipion Development
=====================

To start developing Scipion with Eclipse we need to create an Eclipse
project with the Scipion source. If we already have a working copy we
can import files into a new project or having the EGit plugin we can
create the project just checking out directly from the Scipion
repository.


Creating project from Git working copy
---------------------------------------

If we have a working copy of Scipion project in development from Git, we
should import it and establish as PyDev project.

Go to **File -> Import**, in Git section select **Projects from Git**.
Now, as we have already cloned git repository, we have to select
**Local**, then *Add* and browse to Scipion folder and click on **Ok**.
Now select the repository placed in scipion folder/.git, and finally
select that repository in the Select a Git repository window.

Next step is *Select a wizard to use for importing projects* window,
where we select *Use the New Project wizard* and click on **Finish**.
Now select PyDev Project and click on **Next**. Type a name for the
project, unmark *Use default location* and select the folder you placed
scipion. In *Project type* select *Empty Project* and click on
**Finish**.

Creating project from Git repository
--------------------------------------

In this case the process is the same as above, but you have to select
*URI* instead of **Local**, being all this process equivalent to
download from **command line**. You have to use the "Clone URI" link according to
your permission as seen on **How to Git**, for example type directly
https://github.com/I2PC/scipion.git in the URI field. The different
fields should be fulfilled automatically. Click on Next. In Branch
Selection window mark the branches you want to download (by default, as for now,
master, stable and v1.0 should be enough). Click on
**Next**. Type the folder where the scipion code is going to be
downloaded, choose the initial branch in case you marked more than one
and click on Next. After that, code is being downloaded and it may take
a while. The next step is the second step described in above section.