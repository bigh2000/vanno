License info
========

This repository is cloned from `tzutalin/LabelImg <https://github.com/tzutalin/labelImg>` and edited.

Ubuntu Linux
^^^^^^^^^^^^
Python 3 + Qt5
.. code::
    #!/bin/bash
    sudo apt-get install pyqt5-dev-tools
    sudo pip3 install lmdb
    sudo pip3 install lxml


Explanation
^^^^^^^^^^^
1. You have to put [YOUR_DATASET] inside ``../vanno_data``.

2. If you execute ``distribute_dir.py``, you get ``../vanno_results/[YOUR_DATASET]_env/job_assign.json``.

3. Annotators should execute ``vanno.py`` and verifiers should execute ``vanno_ver.py``. (Below are the shell scripts.)

4. Your annotation results will be stored in ``../vanno_results/[YOUR_DATASET]`` and procedures and statistics will be store as txt files in ``../vanno_results/[YOUR_DATASET]_env``.


user.sh for users
^^^^^^^^^^^^^^^^^
.. code::
    #!/bin/bash
    sudo umount -f ~/Desktop/server
    sudo sshfs -o allow_other vdo-server@192.168.0.142:/home/vdo-server/Annotation ~/Desktop/server
    cd ~/Desktop/server/vanno
    python3 vanno.py


ver.sh for verifiers
^^^^^^^^^^^^^^^^^^^^
.. code::
    #!/bin/bash
    sudo umount -f ~/Desktop/server
    sudo sshfs -o allow_other vdo-server@192.168.0.142:/home/vdo-server/Annotation ~/Desktop/server
    cd ~/Desktop/server/vanno
    python3 vanno_ver.py