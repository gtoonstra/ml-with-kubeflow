#!/bin/sh

# This is the way to name the image tag when on GCP/ GCR
# image_name=gcr.io/$PROJECT_ID/$TEAM_NAME/datasource
# The following is the image_name when deploying to a local GCR:
image_name=localhost:5000/datasource
# In a real pipeline you'd probably take this from a "version" file or attribute somewhere
# (As well as applying "latest" for the tag?)
image_tag=latest

full_image_name=${image_name}:${image_tag}

cd "$(dirname "$0")"

# This builds the image
docker build -t "${full_image_name}" .

# For GCP, you probably want to push this to the GCR.
# Before you can do that, you must authenticate the "docker" command line util to
# allow it to push there.
# more info: https://cloud.google.com/container-registry/docs/advanced-authentication#gcloud-helper
# > gcloud auth configure-docker
#
docker push "$full_image_name"
