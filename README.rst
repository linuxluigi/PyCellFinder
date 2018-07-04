============
PyCellFinder
============

.. image:: https://travis-ci.org/linuxluigi/PyCellFinder.svg?branch=master
    :target: https://travis-ci.org/linuxluigi/PyCellFinder

.. image:: https://coveralls.io/repos/github/linuxluigi/PyCellFinder/badge.svg?branch=master
    :target: https://coveralls.io/github/linuxluigi/PyCellFinder?branch=master

.. image:: https://readthedocs.org/projects/pycellfinder/badge/?version=latest
    :target: https://pycellfinder.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

It's mostly an interface for `OpenCV <https://opencv.org/>`_ special make for counting cells on a picture.


Quickinstall
------------

To install this from the internet use pip or follow the
`install instructions <https://pycellfinder.readthedocs.io/en/latest/install.html>`_::

    $ python3 -m pip install git+git://github.com/linuxluigi/PyCellFinder.git

Usage
-----

Minimal Params
^^^^^^^^^^^^^^

Use it with the default parameters::

    $ pycellfinder -i path_to_your_image

The output presents the count of found objects in the image.

Optional Params
^^^^^^^^^^^^^^^

===========================================  ===============  ======================================================
usage                                        default value    description
===========================================  ===============  ======================================================
-h, --help                                                    show a help message and exit
--version, -v                                                 show program's version number and exit
--input INPUT, -i INPUT                                       path to input file
--output OUTPUT, -o OUTPUT                                    path to output file
--plot PLOT, -p PLOT                                          set True for plot output image
--threshold THRESHOLD, -t THRESHOLD          16               threshold level
--min_size MIN                                                min object size
--max_size MAX                                                max object size
--color COLOR                                                 filter by color 0=Black 255=White
--circularity CIRCULARITY                                     filter by circularity, float value between 0.0 & 1.0
--convexity CONVEXITY                                         filter by convexity, float value between 0.0 & 1.0
--inertia INERTIA                                             filter by inertia
===========================================  ===============  ======================================================