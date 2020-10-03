Componentization
================

This tutorial shows how componentization works in Kubeflow.

You can run the code on your cluster, or inspect the notebook from the tutorials directory
on github:

`Notebooks directory <https://github.com/gtoonstra/ml-with-kubeflow/tree/master/tutorials>`_

**Important takeaways from the tutorial**

* It allows you to run heterogeneous code (mixing python, R, C++ etc.), as long as each component can read from a local file.
* It helps to avoid "version hell" in which package X is not compatible with the version Y that package Z requires. In monolith applications
  this can be a difficult thing to figure out (and lose a lot of time there).
* The pipeline overall is easier to unit test and system test. Each part of the pipeline that used to be embedded in the design
  is now testable using simple input and output files.
* Many components have less dependencies on outside services (BigQuery, GCS), which improves testability further.
* You can decide when to componentize and this is part of the vision/mission of Kubeflow: start with an experiment and then first schedule
  the experiment that does everything, componentize its parts, improve monitoring as you go.
