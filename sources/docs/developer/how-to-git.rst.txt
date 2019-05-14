.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _how-to-git:

==========
How to GIT
==========

We manage our development through issues tracking in Scipion GitHub project. +
A nicer view of the Scipion issues is provided by `Waffle.io <https://waffle.io/I2PC/scipion>`_

.. contents:: Table of Contents

Basic GIT documentation
=======================

General
-------
`[A visual reference to GIT] <http://marklodato.github.com/visual-git-guide/index-en.html>`_

`[Git Book] <http://git-scm.com/book>`_: Read chapters 2 and 3

Specific
--------
`[Git for SVN users] <https://git.wiki.kernel.org/index.php/GitSvnCrashCourse>`_

`[Services] <https://services.github.com/>`_

Configuration
=============

Setup your name and email
-------------------------

.. code-block:: bash

    git config --global user.name "Your Name"
    git config --global user.email "your@email.domain"

Setup some aliases
------------------

.. code-block:: bash

    git config --global alias.co checkout
    git config --global alias.br branch
    git config --global alias.ci commit
    git config --global alias.st status

Some others handful aliases for using the *git-flow* methodology.

.. code-block:: bash

    # To create a new feature branch and publish to origin
    git config --global alias.new-feature '!git checkout -b $1 master \
    && git push -u origin $1 #'
    # To create a hotfix branch (now from v1.0)
    git config --global alias.new-hotfix '!git checkout -b $1 v1.0 \
    && git push -u origin $1 #'

Branches
========

List all branches
-----------------

.. code-block:: bash

    git branch -a

Create a new branch and move to it:
-----------------------------------

.. code-block:: bash

    git checkout -b NEW_BRANCH

Then you can publish it to origin:

.. code-block:: bash

    git push -u origin NEW_BRANCH

Deleting a branch
-----------------

Locally delete a branch

.. code-block:: bash

    git branch -d OLD_BRANCH

    This must be done in a different branch than OLD_BRANCH

The previous command does not allow to locally remove unless the
OLD_BRANCH has been merged to another branch. If you want, anyway to
locally remove the branch do

.. code-block:: bash

    git branch -D oldBranch

To delete the branch remotely (after delete it locally):

.. code-block:: bash

    git push origin :OLD_BRANCH

Everybody else has to "update" the list of branches in the origin, so
that they also get it deleted:

.. code-block:: bash
    git remote prune origin

Remote branch
-------------

To create a local branch at the status of a remote branch:

.. code-block:: bash

    git pull
    git checkout -b newlocalbranchname origin/remotebranchname

To create a branch and also set to track the remote branch:

.. code-block:: bash

    git pull
    git checkout -t origin/branch-name [-b newlocalbranch]


Submit a bugfix (with branch creation)
--------------------------------------

.. code-block:: bash

    git checkout -b newBranchWithBugFix
    git commit -m "Your comment" yourFiles
    git push -u origin newBranchWithBugFix

Compare differences
-------------------

To see differences between branch A and B:

.. code-block:: bash

    git diff --name-status A..B

To see differences in a particular file between branch A and B:

.. code-block:: bash

    git diff A B myFile

List the files that are changed between the local and the official repository
-----------------------------------------------------------------------------
.. code-block:: bash

    git diff origin/branch --name-only

List the files that are changed between two branches
----------------------------------------------------

.. code-block:: bash

    git diff branch1 branch2  --name-only

Apply the differences from one branch into another
--------------------------------------------------

Let's say that there is a file in branch2 with some differences with respect to
branch 1. Then you want to take these differences and put them in branch 1.
From branch 1, you must do

.. code-block:: bash

    git diff branch1..branch2 yourFile > patchFile
    git apply patchFile

If you run the git diff without file, then all changes between the two branches
are dumped into the patchFile.

Tags
----

To create a tag:

.. code-block:: bash

    git tag -a TAG_NAME -m "TAG MESSAGE"

You can submit to a shared server in the same way as a branch:

.. code-block:: bash

    git push origin TAG_NAME

To delete a tag:

.. code-block:: bash

    git tag -d TAG_NAME
    git push origin :TAG_NAME

Stashing
========

Often, when you’ve been working on a part of your project, things end in
a messy state. You want to switch branches for a while in order to work
on something else. The problem is, you don’t want to do a commit of
half-done work (just to be able to get back to this point later). The
answer to this issue is the git stash command:

.. code-block:: bash

    $ git stash

Now you can easily switch branches and do work elsewhere: your changes
are stored on your stack. To see which stashes you’ve stored, you can
use:

.. code-block:: bash

    git stash list:

You can reapply the one you just stashed by using the command shown in
the help output of the original stash command:

.. code-block:: bash

    git stash pop

more: http://git-scm.com/book/en/Git-Tools-Stashing

Merging
=======

Undo a merge in the middle of it
--------------------------------

Let's say you are in the middle of a merging, and you regret from the
changes you have already been introducing. Files that are not related to
the merging conflicts are unaffected by this command.

.. code-block:: bash

    git merge --abort


Avoid merge commits
--------------------

If you want to avoid merge commits follow
this `[link] <http://kernowsoul.com/blog/2012/06/20/4-ways-to-avoid-merge-commits-in-git>`_

In summary use:

.. code-block:: bash

    git pull --rebase

or make it the default behavior in the config.


Commits
=======

Checkout a commit by date
--------------------------

In case of looking for a commit by date, the repository can be moved by:

.. code-block:: bash

    git co `git rev-list -n 1 --before="2011-06-21 13:37" master`

Check which commits have not been pushed yet
--------------------------------------------

.. code-block:: bash

    git log origin/master..master


Revert the changes introduced by a commit
-----------------------------------------

If you have committed and pushed some changes, you may undo them by

.. code-block:: bash

    git revert [commitHash]

Other useful commands
---------------------

.. code-block:: bash

    git grep

* Look for specified patterns in the tracked files in the work tree.

.. code-block:: bash

    git blame

* Show what revision and author last modified each line of a file.

Git-Flow
========

Since January-2016, we started to follow the *git-flow* development methodology
using git.

Summarizing, there are two main branches: *master* and *devel*. New branches
should be opened from devel for each new feature that will be included in the
next release. Feature-branches should be merged back through Pull Requests in
GitHub to allow peer-review and discussions. Master branch should always contain
a released status. When we are ready for a new release, we should create a
release-branch from devel and only commit bug-fixes to it. When this
release-branch is merged (also through Pull Request) to master, it means a new
release that should be tagged in master.

The following image illustrates very well this workflow and a very nice explanation
can be found `[here] <http://nvie.com/posts/a-successful-git-branching-model>`_.

.. figure:: http://nvie.com/img/git-model@2x.png
   :align: center
   :width: 500
   :alt: Table mode.


Gitting in Scipion
==================

Fork I2PC/scipion
-----------------

Look for the fork icon (top-right) and make a Fork on your account o institutional account.
image::https://help.github.com/assets/images/help/repository/fork_button.jpg[ForkIcon]

Clone your fork
---------------

.. code-block:: bash

    git clone git@github.com:YourUserNameHere/scipion.git --origin privatescipion

This should bring your repo to your machine with the remote name
"privatescipion". Feel free to use a different name. It's yours!

Delete all branches, except master
-----------------------------------

You can keep them, but to avoid confusions, you might want to start with a
branchless repo. Well, I guess you need to keep one: Keep master.

Add a I2PC/scipion remote
-------------------------

.. code-block:: bash

    git remote add I2PC https://github.com/I2PC/scipion.git

This adds a second remote name I2PC. Again, feel free to name it your way.

In order to catch the branches list from the new repo,

.. code-block:: bash

    git pull --all

Checkout I2PC/devel branch
---------------------------

Once you have 2 remotes you have to be more specific when checking out branches
from a remote.

To checkout devel, from I2PC type:

.. code-block:: bash

    git checkout -b devel I2PC/devel

TIP: To check the upstreams (where your local branch will push to) of your
branches type:

.. code-block:: bash

    git branch -vv

Start your branch from I2PC/devel
----------------------------------

Now, when you need a branch to work on something new, that branch should go to
your "privatescipion" but start from, usually, I2PC/devel.


.. code-block:: bash

    git checkout -b mynewfeature devel

now you can work locally as usual with your commits, etc.

Pushing your branch to your own repo
------------------------------------

Whenever you want to send changes, you must send them to your remote:
+git push --set-upstream privatescipion mynewfeature+

Sending changes back to I2PC
-----------------------------

Let's update your "mynewfeature" branch with possible devel changes.

.. code-block:: bash

    git checkout devel
    git pull
    git checkout -
    git merge devel

Resolve conflicts if any. And push the branch again to your privatescipion with:
+git push+

Finally, just create a PR across forks using as base I2PC/devel


= Other useful resources

`[gitflow: A successful Git branching model] <http://nvie.com/posts/a-successful-git-branching-model/>`_

`[Use SSH keys in Github and forget about passwords] <http://help.github.com/articles/generating-ssh-keys/>`_

`[Changing a remote's URL] <http://help.github.com/articles/changing-a-remote-s-url/>`_

`[Online git tutorial] <http://try.github.io/levels/1/challenges/1>`_
