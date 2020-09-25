Hello world
===========

The first venture into kubeflow can be accessed from the local repository. If you're on the cloud,
you have to upload that first (or sync the repository remotely on the VM that you created using the
github link). Otherwise, you can start jupyter lab from the "tutorials" directory. When the UI spins up,
you can then access each notebook by browsing the directories on the left.

Further instructions and explanations are in each notebook. These notebooks are rendered and also
accessible on github:

`Notebooks directory <https://github.com/gtoonstra/ml-with-kubeflow/tree/master/tutorials>`_

**Important takeaways from the tutorial:**

* There is a python SDK for interacting with Kubeflow, called "kfp".
* For creating Kubeflow pipelines, there is a module in the SDK called "dsl" (kfp.dsl)
* Every task in kubeflow is always something running inside a docker container on kubernetes.
* You can run python functions that you define locally as part of the pipeline.
* You can specify a pipeline using the SDK and trigger it on kubeflow with one line of code.
* You can also compile the pipeline into a YAML file and upload that to kubeflow manually.
* There are other things the kfp package can do, like managing experiments, pipelines through the
  API that I didn't show in the tutorial.
