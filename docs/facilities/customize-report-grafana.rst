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
You may find a description of the process in the https://devconnected.com/how-to-setup-telegraf-influxdb-and-grafana-on-linux/

 * Enable HTTP point in your InfluxDB server (set "enabled = true" in /etc/influxdb/influxdb.conf, section [http])
 * Enable HTTP authentication on your InfluxDB server (set "auth-enabled = true" in /etc/influxdb/influxdb.conf)
 * Create a private key for your InfluxDB server (cd /etc/ssl; mkdir influxdb && cd influxdb; certtool --generate-privkey --outfile server-key.pem --bits 2048)
 * Create a public key for your InfluxDB server (certtool --generate-self-signed --load-privkey server-key.pem --outfile server-cert.pem)
 * Set new files owner (chown influxdb:influxdb server-key.pem server-cert.pem)
 * Enable HTTPS on your InfluxDB server. Edit  file and set: /etc/influxdb/influxdb.conf:
     * https-enabled = true
     * https-certificate = "/etc/ssl/influxdb/server-cert.pem"
     * https-private-key = "/etc/ssl/influxdb/server-key.pem"
* reboot Influx (systemctl restart influxdb)
* test secure conection works

 .. code-block:: bash

    $ influx -ssl -unsafeSsl -host localhost
    Connected to https://localhost:8086 version 1.8.0
    InfluxDB shell version: 1.8.0
    > auth
    username: scipion_writer
    password: 
    > show databases
    name: databases
    name

* Create database "scipion" and grant access permision to scipion_writer (as admin user)

 .. code-block:: bash

    influx -ssl -unsafeSsl -host localhost
    Connected to https://localhost:8086 version 1.8.0
    InfluxDB shell version: 1.8.0
    > auth
    username: admin
    password: 
    > CREATE DATABASE scipion
    > GRANT ALL ON scipion TO scipion_writer


* Check you can access influx service from the computer that will run scipion 
    * you may need to open port 8086 in your influxdb server
    * log in remote compute and execute: influx -ssl -unsafeSsl -host host_withInflux.xxx.yy.zz

Installing and setting up Grafana
-------------------------------------

Follow instruction available at  https://grafana.com/docs/grafana/latest/installation/

Set up secure conection:
First create certificate 

* cd /etc/grafana
* Create certificate: 
    * openssl genrsa -out grafana.key 2048
    * openssl req -new -key grafana.key -out grafana.csr
    * openssl x509 -req -days 365 -in grafana.csr -signkey grafana.key -out grafana.crt
* Set the certificate, key file ownership, and permissions so that they are accessible to Grafana.
    * chown ams:hadoop grafana.crt
    * chown ams:hadoop grafana.key
    * chmod 400 grafana.crt
    * chmod 400 grafana.key
* Edit  grafana.ini




InfluxData’s “How to use Grafana with InfluxDB” webinar explains how to use Grafana UI to set up graphs and use InfluxDB Query Builder.


