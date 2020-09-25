ML with Kubeflow documentation site
===================================

.. important::

    **Disclaimer**: This is not the official documentation site for
    Kubeflow. This site is not affiliated, monitored or controlled by
    the official Kubeflow development effort. If you are looking for
    the official documentation site, please follow this link:

    `Official Kubeflow documentation <https://www.kubeflow.org//>`_

    What you will find here is a step-by-step tutorial, incrementally increasing
    the complexity and adding more capabilities from Kubeflow.

::

    You can find this project on github:

    https://github.com/gtoonstra/docker-airflow


.. image:: img/GitHub-Mark-Light-32px.png


Why this documentation site?
----------------------------

As I started learning about Kubeflow, I found it confusing:

    * There have been some versions already and some examples only apply to the older versions
    * The examples are in different repositories, only online or are difficult to execute on your
      deployment of Kubeflow
    * The concepts are sometimes described, but not exemplified, and you need to look for a working
      example to understand how it works in practice.

I am also the author of the successful documentation site "ETL with airflow", which has, I think,
helped numerous engineers in understanding airflow and get up to speed with that. I want to give
people a similar experience with kubeflow, which for me at least is more complex than airflow.


Prerequisites
-------------

**For a quick local deployment**:

* A docker environment
* A laptop/desktop that is beefy enough to run a small cluster, at least 16G of memory and 50G of diskspace.

or

**For a quick cloud deployment**:

* I recommend Google Cloud Platform, which has a very easy method for deploying kubeflow and for which
  you get $300 free credit when you create your project for the first time.


Study flow
----------

1. Quick deploy of the "Kubeflow Pipelines" component
2. Getting jupyter lab going
3. The simplest "Hello world" example
4. Other examples showing more of what's possible
5. Componentization of your code.
6. Visualization components, metrics.
7. Conclusions on what we learned so far
8. Diving deeper: Relevant kubernetes design
9. Diving deeper: Kubeflow design
10. Extracting principles from Kubeflow's design
11. Understanding the principles and Kubeflow "Selling Points"
12. Best practices of data science on kubeflow

Content
-------
.. toctree::
    :maxdepth: 4

    quickdeploy
    jupyter
    helloworld
