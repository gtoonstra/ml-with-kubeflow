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

You need an experimental environment at your disposal, which is capable of running kubeflow pipelines.
This is either a beefy desktop / laptop (minimum 16G) or an experimental cluster in the cloud.


Study Guide
-----------

1. Quick install of the "Pipelines" component
2. Hello world examples
3. More examples up to "componentizing" parts of your pipeline
4. More advanced features that not everyone needs
5. Conclusions on what we learned so far
6. Diving deeper: Relevant kubernetes design
7. Diving deeper: Kubeflow design
8. Extracting principles from Kubeflow's design
9. Why those principles matter


Content
-------
.. toctree::
    :maxdepth: 4

    quickdeploy
