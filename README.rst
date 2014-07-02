**********************************************
yopy: Zero characters communication for humans
**********************************************

.. code-block:: python

    from yopy import Yo

    # Send a single yo
    y = Yo('ronaldmcdonald')
    y.yo('hamburglar')

    # 'Yo' all subscribers
    y = Yo(token='<your token here>')
    y.yo_all()


Or, from the command line:

.. code-block:: bash

    $ yopy ronaldmcdonald hamburglar



`MIT Licensed <http://sloria.mit-license.org/>`_
