===========
Description
===========
Detect package carrier from tracking number and generate tracking url.

============
Requirements
============
* python >= 3.2

============
Installation
============
.. code-block:: bash

    $ pip install tracking_url

=====
Usage
=====

.. code-block:: python

    import tracking_url

    match = tracking_url.guess_carrier('0123456789')
    if match is None:
        print('No matching carrier found')
    else:
        print('Number:', match.number)
        print('Carrier:', match.carrier)
        print('Url:', match.url)

======
Thanks
======
This code is a simple python port of the identically named node module.

Big thanks to https://github.com/wankdanker for the original code and
research.

======
Issues
======
If you have any suggestions, bug reports or annoyances please report them
to the issue tracker at https://github.com/sereema/tracking-url/issues .
