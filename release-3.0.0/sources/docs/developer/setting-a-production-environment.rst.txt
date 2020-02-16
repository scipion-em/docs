.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _setting-a-production-environment:

============================
Scipion web production setup
============================


Production environment
^^^^^^^^^^^^^^^^^^^^^^

This setup uses tools that are production-ready and support the
requirements of a web service in the Internet (which are quite different
from a small local service for testing)

All the service needs are self-contained in the service directory. For
simplicity, this directory is called "scipion", so the typical path to
the service would be /services/scipion

While everything is nicely organized, you can find the mandatory
introductory documentation in the `scipion/README.md` file.

The current frontend is an apache server, and the current application
server is Gunicorn. You can manage (start, restart...) both services
with the `scipion/scripts/apache-service` and
`scipion/etc/scipion-manager` scripts.

The service as a whole is managed with `scipion/etc/service-manager`. It
is the perfect *starting point* to learn the latest state of things
regarding configuration and how everything works (what it is needed and
when).

All the relevant configuration is in `scipion/etc`. For example, apache
configuration, backup configuration, roles, permissions...

One key setting is which scipion software installation to use. Set it in
the `${scipion}` variable (in `scipion.env`, through the `$PW_HOME`
variable).

Other more general service settings are in `scipion/etc/service.cfg`

---- Movies upload

This feature is currently supported by `/services/scipion-mws`

In upcoming releases, it may be integrated into Scipion service.

Again, all config is in `scipion-mws/etc`, and you can dive into the
details from `scipion-mws/etc/service-manager`


Cloning the production environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clone the service an ps-scripts repos (there are snapshots of them `[here] <http://scipion.cnb.csic.es/git/scipion-ps.tar.gz>`_ vand `[here] <http://scipion.cnb.csic.es/git/ps-scripts.tar.gz>`_). First clone the
scipion (web) service repository, then inside it, the ps-scripts repository. We recomend to use /services as base directory, hence after
the 2 clones, you should find `/services/scipion/scripts`, `/services/scipion/scripts/etc`, ...

Edit `etc/service.cfg` and update the service and service_root
parameters.

Run the `service-create` script using its absolute path, and follow its
instructions. For example,

`/services/scipion/service-create`

(If needed, use sudo to run the command.)

Run

`/services/scipion/scripts/config/apache2/mkhttpd_conf > /services/scipion/etc/apache/httpd.conf`
`/services/scipion/scripts/config/apache2/mkservice_conf > /services/scipion/etc/apache/service.conf`

and check `service.conf` to ensure all paths are correct.

Currently, scipion-specific config is split across 3 different
places:

* `etc/scipion-config/*.conf`: global configuration (in theory)
* `usr/scipion/config/*.conf`: global configuration (of the scipion
  instance in use)
* `data/scipionweb/.config/scipion`: configuration of each of the web
  tools.

Check/edit all these scipion config files above.

Regarding the projects data, you need to clone the directories
`data/scipionweb/ScipionUserData/(movies,myfirstmap,myresmap)`

For the tests data, you need to run (as scipionweb user):

`/services/scipion/usr/scipion/scipion  testdata --download riboMovies`

Run

`/services/scipion/etc/service-manager start`

This script will check if all the software dependencies for the services
are installed (and install the missing ones)

If there are any issues during the installation, you can check the logs at
`/services/scipion/log`

Restart (Bounce)

`/services/scipion/etc/service-manager restart`


Scipion deployments

For single-user ("private") use, Scipion can be deployed anywhere; for example, in the user's home directory.
On multi-user machines, the prefered location is /usr/local/scipion.
In cluster environments, Scipion should be installed in the shared filesystem, so all nodes have access to it. In crunchy, for example, the preferred path is /gpfs/fs1/apps/scipion

