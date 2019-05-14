.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _enable-gpu-in-scipion:

==========
GPU
==========

Introduction to GPU
===================

Vector processing units in graphic cards (GPU) allow for very fast processing,
provided the program makes the most of its parallel features. The most popular
platform for GPU computing is Nvidia CUDA.

Enable GPU in Scipion
~~~~~~~~~~~~~~~~~~~~~~

If you foresee that the end user will have access to a GPU when using the image,
then you should prepare all the GPU-related stuff.

First, NVidia driver:

.. code-block:: bash
    # Download the latest stable driver.
    # Disable nouveau:
    echo "blacklist nouveau" > /etc/modprobe.d/disable-nouveau.conf
    # Update init disk
    update-initramfs -u
    # reboot
    # install dependencies
    apt-get install linux-headers-$(uname -r) build-essential
    # run the binary installer
    chmod u+x NVIDIA-Linux-x86_64-361.42.run
    ./NVIDIA-Linux-x86_64-361.42.run

Then, install CUDA. We recommend `CUDA 5.5 <https://developer.nvidia.com/cuda-toolkit-55-archive>`_
(which requires `gcc 4.6 <http://www.tranquilinho.com/informatica/linux/compilar-gcc/>`_)

.. code-block:: bash
    ./cuda_5.5.22_linux_64.run -toolkit -silent

The last requisite is OpenCV, which can be installed with scipion install
script (you may need to specify gcc/g++ 4.6 in CMakeCache.txt).

The CUDA switch will be enabled later in scipion.conf.

.. code-block:: bash

    # GPU features require manual change in config/scipion.conf:
    CUDA = True

(see `How to install <https://scipion-em.github.io/docs/docs/scipion-modes/install-from-sources.html>`_)

EM packages that benefit from GPU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Motioncorr

.. code-block:: bash

    ./scipion installp -p scipion-em-motioncorr -j 4

GPU purchase guide
~~~~~~~~~~~~~~~~~~

Most popular GPU card brand is NVidia. It has 3 main product lines:

* Tesla: optimized for scientific computing and reliavility. "Expensive", but you get direct long-term Nvidia support, better drivers, ECC memory. Very good double-precission performance (though your algorithm may work well with just simple-precission).
* Quadro: also high-quality components, but more focused on CAD applications
* GeForce: marketed for gaming, they can also be used as GPU, like Quadro and Tesla. "Cheap" models available. Usually they are bulky and power hungry, since they are intended for consumer desktop PC. Therefore, they may be a pain to install in a standard 1U server. Additionally, most servers vendors do not support this kind of cards.

In terms of performance per euro, usually it is best to go with top consumer cards, like GTX 1080. If money is not a problem, Tesla is the safe investment. Quadro stand in the middle ground: cheaper than Tesla, they offer good performance and are supported by most server vendors.
