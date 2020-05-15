.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _customize-html-report:

========================================
Grafana, InfluxDB report customization
========================================

.. :contents:: Table of Contents

Intro
-----
InfluxDB is a time series database built specifically for storing time series data, and Grafana is a visualization tool for this kind of data. Below are some basics on how to set up your Grafana dashboard with InfluxDB and how to use the Grafana InfluxDB solution to display the output of Scipion monitors. We will show here how to configure the system in order to allow you to visualize what you want, the way that you want. In Summary the general idea is, 
Scipion **summary monitor** is the agent responsible for gathering and aggregating data, like the defocus of each of the collected Movies. InfluxDB will store the data, and expose it to Grafana, which will display it to the final users..



Setting UP Grafana and Influxdb
-------------------------------

For starters, download InfluxDB and Grafana. In our facilities we have used version 1.6 and 1.7 for grafana and 1.8 for influxdb but we are using the basic funtionality of these software so very likely other versions will also work.

The basic setup is to have InfluxDB and Grafana connected together. InfluxDB has an API that defaults to port 8086 while Grafana’s API is on port 3000. And Grafana will call the InfluxDB API whenever it wants to query data. When you set up the InfluxData time series platform, you will need a collection agent collecting your metrics this collection agent wil the Scipion **summary monitor** (select the option *use grafana/influx*).

InfluxDB is essentially a time series database process that runs on a server. That process can also run on the same box that Grafana runs on. Grafana has a very lightweight server-side application, and most of Grafana monitoring runs in the browser.

It’s easiest to set up Grafana and InfluxDB on the same instance, although it may also be interesting to set influxdb in the same machine in which you are running Scipion. In our facility Scipion is installed in three different machines and reports to a single InfluxDb database installed in the same machine than Grafana.

InfluxDb is more memory-intensive and CPU-intensive application than Grafana, because a lot of Grafana’s work happens in the browser. Although with a standard use, report each magnitude once per minute, any computer may handle both applications.

As for security settings, every Grafana instance and Influx Database has a default admin user and default password. If you are setting your system in a public network you should consider creating user with restricted privileges.


Installing and setting up InfluxDb
----------------------------------
We will not discuss here how to install or do the basic configuration of InfluxDb since it is discussed elsewhere (see for example <https://devconnected.com/how-to-install-influxdb-on-ubuntu-debian-in-2019/>). 

You may check that the database is running using the command line cliente *influx*

 .. code-block:: bash

      $ influx
      > show databases
      name: databases
      name
      ----
      _internal

At this point you may create an admin user. Type inside the client **influx**

 .. code-block:: sql
    CREATE USER admin WITH PASSWORD 'password1' WITH ALL PRIVILEGES
    CREATE USER "scipion_writer" WITH PASSWORD 'password2'

Enable secure transmission
__________________________
In our setup we have secured our instances with HTTPS via secure certificates.
You may find a description of the process in the `URL <https://devconnected.com/how-to-setup-telegraf-influxdb-and-grafana-on-linux/>`_
 
  532  sudo certtool --generate-privkey --outfile server-key.pem --bits 2048
  533  sudo certtool --generate-self-signed --load-privkey server-key.prm --outfile server-cert.pem
chown influxdb.influxdb influxdb*

Edit file sudo vi /etc/influxdb/influxdb.conf
     [http]
  # Determines whether HTTP endpoint is enabled.
  enabled = true

  # Determines whether the Flux query endpoint is enabled.
  flux-enabled = true

  # Determines whether the Flux query logging is enabled.
  # flux-log-enabled = false

  # The bind address used by the HTTP service.
  bind-address = ":8086"

  # Determines whether user authentication is enabled over HTTP/HTTPS.
  auth-enabled = true
https-enabled = true

# The SSL certificate to use when HTTPS is enabled.
https-certificate = "/etc/ssl/influxdb/server-cert.pem"
# https-certificate = "/etc/ssl/certs/influxdb.crt"


# Use a separate private key location.
https-private-key = "/etc/ssl/influxdb/server-key.pem"
# https-private-key = "/etc/ssl/certs/influxdb.key"


Restart6 service: sudo systemctl restart influxdb.service
influx -ssl  -unsafeSsl -host nolan.cnb.csic.es
auth
use scipion





Setting up graphs for Grafana Metrics
-------------------------------------

InfluxData’s “How to use Grafana with InfluxDB” webinar explains how to use Grafana UI to set up graphs and use InfluxDB Query Builder.


