The infrastructure is accesible from a web browser at the URL provided by the I2PC team, where you should enter the password that was given to you.

Once you login you will see a remote desktop like this:

.. figure:: /docs/images/cloud/EOSC-noVNC-desktop.png
   :width: 500
   :alt: VNC remote desktop


Scipion is installed in the scipionuser home folder, where the following plugins are also installed and fully working:

.. figure:: /docs/images/cloud/EOSC-Scipion-plugins.png
   :width: 500
   :alt: Scipion plugins

If you want to use Chimera you should install it through the Plugin Manager.

To copy your data in the virtual server you can use rsync but the destination folder should be located inside the ScipionUserData directory which is the mounting point of the bigger storage disk.

As an example you should launch a similar command from the server where your data and project is located:

rsync -av Instruct_project_1234 scipionuser@IP.OF.THE.SERVICE:ScipionUserData/projects/

Depending on your data size data will take some time to copy but you can login and start working on it.

.. figure:: /docs/images/cloud/EOSC-Scipionproject.png
   :width: 500
   :alt: Scipion project

You might then continue working on the project until you reach your results.


The infrastructure setup has a limited time but in case you need more time you could request it sending an email to i2pc and an extension might be granted depending on the pending requests.

In any case you will have some time to download project and results.

And please do not forget to acknowledge the use of this infrastructure by adding the following paragraph to your publication:

“This work used the EGI infrastructure with the dedicated support of CSIC, IISAS, CESNET-MCC and EGI Foundation”
