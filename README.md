# DeteriorationPrediction
## Introduction
This is a repository in which anyone can use our model to predict neurological deterioration after mild traumatic brain injury.

## Setup
We run the code below on Python 3.9 with the packages listed in requiements.txt.

## How to use
First, you need to overwrite the "demo-data" with your data and implement "XGBoost_model.py". You will obtain the probability of your data, and you will also obtain the 1 or 0 result judged from the cutoff value that we set in our article.


Input for each feature 
ASDH: the sickness (mm) of acute subdural hematoma in the initial Computed Tomography(CT), Cerebral Contusion: the diameter (mm) of cerebral contusion in the initial CT,
D-dimer: the value of D-dimer (ug/ml) from the blood sample at admission, Fibrinogen: the value of fibrinogen (mg/dL) from the blood sample at admission, sBP: systolic blood pressure (mmHg) at admission
