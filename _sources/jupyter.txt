Jupyter lab
===========

When you deployed on Google Cloud
---------------------------------

The next step is to get the jupyter notebooks going. If you deployed on the Google Cloud Platform,
the easiest way is to use the "Notebooks" section on "AI Platform". That will spin up a VM that is
ready to use with jupyter preinstalled. As a matter of fact, you'll jump straight into the UI
when the link becomes available.

You can not use Google Cloud notebooks when you deployed your cluster locally.

When you deployed locally
-------------------------

Locally you should create your own jupyter environment. This can be anywhere, but I suggest to do
this in the "tutorials" directory of the repository of this site, which is where you'll find an easy
requirements.txt file that will pre-deploy all the necessary packages.

First, create the venv in that directory and activate it:

::

    python3 -m venv venv
    source venv/bin/activate

Then we first upgrade pip to the latest version:

::

    pip install --upgrade pip setuptools wheel

And then install the packages in the requirements:

::

    pip install -r requirements.txt

If everything installed fine, you can now access the jupyter lab environment:

::

    jupyter lab

Great, so by now we should have a cluster running and a jupyter lab environment that allows us to
interact with the cluster.
