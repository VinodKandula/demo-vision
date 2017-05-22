#!/bin/bash

TUTORIALDIR=~/demo-vision
cd $TUTORIALDIR
gcloud config set project skotwani-helloworld
gcloud iam service-accounts create vision-quickstart --no-user-output-enabled
gcloud iam service-accounts keys create key.json --iam-account \
     vision-quickstart@skotwani-helloworld.iam.gserviceaccount.com \
  && export GOOGLE_APPLICATION_CREDENTIALS=key.json
python label.py resources/cat.jpg
