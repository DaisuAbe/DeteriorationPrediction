import pandas as pd
import pickle

# Load the XGBoost model
filename = 'XGBoost_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Load the demo data
X_data = pd.read_csv('demo-data.csv')

# Make predictions and output the probability of the case
y_predicted = loaded_model.predict_proba(X_data)[:, 1]
probability = y_predicted * 100
print("Probability:", probability)

# Set a cut-off value and 
# In this demo, we set 49.98738 as the cut-off value, because we adopted this value in our article.

for i in probability:
    if i >= 49.98738:
        result=1
    else:
        result=0
print("Prediction result:", result)