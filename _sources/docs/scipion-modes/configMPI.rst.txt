


One known change for **Ubuntu 18** and **CentOS** are the MPI paths in
``<your_scipion_home>/config/scipion.conf``:

For **Ubuntu 18**:

::

   MPI_LIBDIR = /usr/lib/x86_64-linux-gnu/openmpi/lib
   MPI_INCLUDE = /usr/lib/x86_64-linux-gnu/openmpi/include/

For **CentOS**:

::

    MPI_BINDIR = /usr/lib64/openmpi/bin
    MPI_LIBDIR = /usr/lib64/openmpi/lib
    MPI_INCLUDE = /usr/include/openmpi-x86_64