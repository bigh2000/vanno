License info
========

This repository is cloned from [tzutalin/LabelImg](https://github.com/tzutalin/labelImg) and edited.

Ubuntu Linux
^^^^^^^^^^^^
Python 2 + Qt4

.. code::

    sudo apt-get install pyqt4-dev-tools
    sudo pip install lmdb
    sudo pip install lxml
    make qt4py2

Python 3 + Qt5

.. code::

    sudo apt-get install pyqt5-dev-tools
    sudo pip3 install lmdb
    sudo pip3 install lxml
    make qt5py3


connect_server.sh for vdo_data*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code::

    #!/bin/sh
    sudo umount -f ~/Desktop/server
    sudo sshfs -o allow_other vdo-server@192.168.0.142:/home/vdo-server/Annotation ~/Desktop/server
    cd ~/Desktop/server/vanno
    python3 vanno.py


connect_server.sh for vdo_ver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code::

    #!/bin/sh
    sudo umount -f ~/Desktop/server
    sudo sshfs -o allow_other vdo-server@192.168.0.142:/home/vdo-server/Annotation ~/Desktop/server
    cd ~/Desktop/server/vanno
    python3 vanno_ver.py
