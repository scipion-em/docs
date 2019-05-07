.. _how-to-install-drupal-in-sourceforge:

=====================================
How to install drupal in sourceforge
=====================================

Some tips for Drupal installation and configuration on sourceforge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Download Drupal from https://drupal.org/.

You can find the installation guide `[here] <https://drupal.org/documentation/install>`_. However, here we will
provide a brief description of the installation process. This
information is focused on a sourceforge installation; however, it will be
the same or even simpler for any other server. Download Drupal and unzip
it. Connect with sftp or, even better, connect to sourceforge with
Filezilla.

* Data for the connection:

**host**: web.sourceforge.net

**name**: Source forge user

**password**: No password is required

**port**: 22

* Then go to /home/project-web/[project name]/htdocs/

* Once everything is copied, go to the url with a browser, tipically
[project name].sourceforge.net and go on with the configuration process.

* When configuring the db provide the following information:

**host**:mysql-[first letter of the project name]

**user**: it should have admin permissions

* If you lost the login form, you can access by url: /?q=user/login