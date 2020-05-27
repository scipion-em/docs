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
InfluxDB is a time series database built specifically for storing time series data, and Grafana is a visualization tool for this kind of data. Below are some basics on how to set up your Grafana dashboard with InfluxDB and how to use the Grafana InfluxDB solution to display the output of Scipion monitors. In Summary the general idea is, 
Scipion **summary monitor** is the agent responsible for gathering and aggregating data, like the defocus of each of the collected Movies. InfluxDB will store the data, and expose it to Grafana, which will display it to the final users.



Setting UP Grafana and Influxdb
-------------------------------

For starters, download InfluxDB and Grafana. In our facilities we have used version 1.6 and 1.7 for grafana and 1.8 for influxdb but we are using the basic funtionality of these software so very likely other versions will also work.

The basic setup is to have InfluxDB and Grafana connected together and Grafana will call the InfluxDB API whenever it wants to query data. When you set up the InfluxData time series platform, you will need a collection agent collecting your metrics this collection agent wil the Scipion **summary monitor**.

InfluxDB is essentially a time series database process that runs on a server. That process can also run on the same box that Grafana runs on. Grafana has a very lightweight server-side application, and most of Grafana monitoring runs in the browser.

It’s easiest to set up Grafana and InfluxDB on the same instance, although it may also be interesting to set influxdb in the same machine in which you are running Scipion. In our facility Scipion is installed in three different machines and reports to a single InfluxDb database installed in the same machine than Grafana.

InfluxDb is more memory-intensive and CPU-intensive application than Grafana, because a lot of Grafana’s work happens in the browser. Although with a standard use, report each magnitude once per minute, any computer may handle both applications.

As for security settings, every Grafana instance and Influx Database has a default admin user and default password. If you are setting your system in a public network you should consider creating user with restricted privileges.


Installing and setting up InfluxDb
----------------------------------
We will not discuss here how to install or do the basic configuration of InfluxDb since it is discussed elsewhere (see for example https://devconnected.com/how-to-install-influxdb-on-ubuntu-debian-in-2019/). 

You may check that the database is running using the command line cliente *influx*

 .. code-block:: bash

      $ influx
      > show databases
      name: databases
      name
      ----
      _internal

At this point you may create: an admin user, a user that can write and a readonly user. Type inside the client **influx**

 .. code-block:: sql
 
    CREATE USER admin WITH PASSWORD 'password1' WITH ALL PRIVILEGES
    CREATE USER "scipion_writer" WITH PASSWORD 'password2'
    CREATE USER "scipion_reader" WITH PASSWORD 'password3'

Enable secure transmission
__________________________
In our setup we have secured our instances with HTTPS via secure certificates.
You may find a description of the process in https://devconnected.com/how-to-setup-telegraf-influxdb-and-grafana-on-linux/

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
    
Note: The flag **unsafeSsl* is needed if you use a self-signed certificate.

* Create database "scipion" and grant access permision to scipion_writer (as admin user) and to scipion_reader (as readonly user)

 .. code-block:: bash

    influx -ssl -unsafeSsl -host localhost
    Connected to https://localhost:8086 version 1.8.0
    InfluxDB shell version: 1.8.0
    > auth
    username: admin
    password: 
    > CREATE DATABASE scipion
    > GRANT ALL ON scipion TO scipion_writer
    > GRANT READ ON scipion TO scipion_reader


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
* Set the certificate, key file ownership, and permissions so that they are accessible by Grafana.
    * chown grafana.grafana grafana.crt
    * chown grafana.grafana grafana.key
    * chmod 400 grafana.crt
    * chmod 400 grafana.key
* Edit  grafana.ini and modify the following lines
    * protocol = https
    * http_addr = 0.0.0.0
    * cert_file =  /etc/grafana/grafana.crt
    * cert_key = /etc/grafana/grafana.key
    * you may waht to set **viewers_can_edit=true** so that users with view only permission may edit/inspect dashboard settings in the browser, but not save the modifications.
* Reboot grafana and you should be able to connect using https://grafana_host:3000 (default user name and password admin/admin). [If you are working from home and your server is behind a firewall you may open an ssh tunnel using: ssh -L 8888:grafana_host:3000 user@ssh_host.cnb.csic.es, in this case Grafana URL will be https://localhost:8888]
* In addition to the default **admin** user you may create a readonly user (use server admin -> Users)

Grafana create Data Source
________________________

Log into Grafana and  add a data source (see details at https://grafana.com/docs/grafana/latest/features/datasources/add-a-data-source/). Follows a table with the parameters used to create the data source:


+-------+-------------------------+---------+----+
| Name  | InfluxDB-scipion        | Default | on |
+-------+-------------------------+---------+----+
| HTTP                                           |
+-------+----------------------------------------+
| URL   | https://localhost:8086                 |
+-------+----------------------------------------+
|Access | Server (default)                       |
+-------+-------------+--------------------------+
| Whitelisted Cookies |                          |
+---------------------+--------------------------+
| Auth                                           |
+-----------------+-----+------------------+-----+
| Basic auth      | on  | With Credentials | off |
+-----------------+-----+------------------+-----+
|TLS Client Auth  | off | With CA Cert     |     |
+-----------------+-----+------------------+-----+
| Skip TLS Verify | on                           | 
+-----------------+------+-----------------------+
| Forward OAuth Identity | off                   |
+------------------------+-----------------------+
| Basic Auth Details                             |
+-----------------+------------------------------+
| User            | admin                        |
+-----------------+------------------------------+
| Password        | xxxxx                        |
+-----------------+------------------------------+
| InfluxDB Details                               |
+-----------------+------------------------------+
| Database        | scipion                      |
+-----------------+------------------------------+
| User            | admin                        |
+-----------------+------------------------------+
| Password        | xxxxx                        |
+-----------------+------------------------------+
| HTTP Method     | GET                          |
+-----------------+------------------------------+

Grafana create DashBoard
________________________

A dashboard is a set of one or more panels organized and arranged into one or more rows. In our facility we use 5 dashboards. To import a dashboard click the + icon in the side menu, and then click Import. You may import dashboards directly from grafana.com. There we has uploaded the five dashboards used in our facility (just type de dashboard id in the text-window labeled as "Import via grafana.com) and fill the Folder and  Influxdb-scipion parameters ("General" and InfluxDb-scipion are good options). 

* `Summary <https://grafana.com/grafana/dashboards/12351>`_ (ID=12351): general description of the session acquisition 
* `CTF <https://grafana.com/grafana/dashboards/12352>`_ (ID=12352): data related with CTF such as defocus, astigmatism, etc
* `Gain <https://grafana.com/grafana/dashboards/12353>`_ (ID=12353): microcope gain estimation 
* `System <https://grafana.com/grafana/dashboards/12354>`_ (ID=12354): cpu, memory, disk access, etc.
* `Gallery <https://grafana.com/grafana/dashboards/12355>`_ (ID=12355): gallery with micrographs, PSD, CTF, etc



Important The dashboard assume that the images are accesible at /usr/share/grafana/public/img/scipionbox. Please link the directory  remote_path to /usr/share/grafana/public/img/scipionbox. remote_path is defined in next section.



Scipion how to connect it to Influxdb
_____________________________________

The only missing piecce of this puzzle is how to make Scipion to send
data to influxdb so Grafana may display it.  The protocol that perform this task is
**summary monitor** (select the option *use grafana/influx*). This protocol search 
for login information in a file called **secrets.cfg** which should be in the 
directory defined by the variable **EMFACILITIES_HOME** (a template file called **secrest_template.cfg** is 
available in the plugin home directory). The file structure is

 .. code-block:: sql
 
    # using the function enCrypt (see below)
    # this encryption is weak but at least will stop casual users

    # influx: information needed to acces to the "host"
    # running influxdb. If you are not encrypting your
    # communications set ssl = False
    [influx]
    usernameInflux=aW5mbHV4dXNlcm5hbWU=
    passwordInflux=aW5mbHV4cGFzc3dk
    dataBase=scipion
    hostinflux=influx-server.cnb.csic.es
    port=8086
    ssl=True
    verify_ssl=False
    timeZone =Europe/Madrid

    # paramiko,  is a ssh client for python we use it to implement
    # sftp and transfer images from scipion host to grafana host
    # authentication is performed using username and a private key. 
    # The path to the PRIVATE key (keyfilepath) is encrypted and should be similar to
    # '/home/transferusername/.ssh/id_rsa' and the keyfiletype (also encrypted)
    # should be either "RSA" or "DSA"
    # Remember to add the public key to the host paramiko authoris_keys file
    # Important: remote_path should be linked to the image directory with the name
    # scipionbox: ln -s remotepath /usr/share/grafana/public/img/scipionbox
    usernameParamiko=dXNlcm5hbWVQYXJhbWlrbw==
    passwordParamiko=None
    keyfilepath=L2hvbWUvcm9iZXJ0by8uc3NoL2lkX3JzYQ==
    keyfiletype=UlNB
    remote_path=/home/scipionbox/public_html/
    hostparamiko=paramikohost.cnb.csic.es

    # import base64
    # def enCrypt(message):
    #     """Totally naive encription routine that will not
    #     stop a hacker. Use it to encrypt usernames and password.
    #     Ussage: enCrypt("myusername")"""

    #     message_bytes = message.encode('ascii')
    #     base64_bytes = base64.b64encode(message_bytes)
    #     return base64_bytes.decode('ascii')      


Important: you will need to install the following modules in Scipion python:


 .. code-block:: sql
 
    ./scipion3 run pip install paramiko
    ./scipion3 run pip install influxdb
        

Where is my project?
____________________

Last but not least the report sohuld be accesible at the URL  https://grafanahost:8888/d/oYW5BSeWz/scipion_projects?var-project=scipion_project_name and a username and password will be needed to connect to grafana unless you have implemented anonymous authentification (see "https://grafana.com/docs/grafana/latest/auth/overview/#anonymous-authentication")
