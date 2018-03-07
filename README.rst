License info
========

This repository is cloned from [tzutalin/LabelImg](https://github.com/tzutalin/labelImg) and edited.

Ubuntu Linux
^^^^^^^^^^^^
Python 2 + Qt4

.. code::

    sudo apt-get install pyqt4-dev-tools
    sudo pip install lxml
    make qt4py2
    python labelImg.py
    python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

Python 3 + Qt5

.. code::

    sudo apt-get install pyqt5-dev-tools
    sudo pip3 install lxml
    make qt5py3
    python3 labelImg.py
    python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]


connect_server.sh for vdo_data*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#!/bin/sh
sudo umount -f ~/Desktop/server
sudo sshfs -o allow_other vdo-server@192.168.0.142:/home/vdo-server/Annotation ~/Desktop/server
cd ~/Desktop/server/vanno
python3 vanno.py


connect_server.sh for vdo_ver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#!/bin/sh
sudo umount -f ~/Desktop/server
sudo sshfs -o allow_other vdo-server@192.168.0.142:/home/vdo-server/Annotation ~/Desktop/server
cd ~/Desktop/server/vanno
python3 vanno_ver.py