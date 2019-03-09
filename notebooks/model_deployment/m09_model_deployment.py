#!/usr/bin/python

import pandas as pd
from sklearn.externals import joblib
import category_encoders as ce
import sys
import os

def predict_price(year,Mileage,State,Make,Model):
    
    tree = joblib.load(os.path.dirname(__file__) + '/price_pred.pkl') 
    encoder = joblib.load(os.path.dirname(__file__) + '/encode.pkl')
    
    x_text=[{"Year": year, "Mileage": Mileage, "State": State, "Make":Make, "Model":Model}]
    input_ = pd.DataFrame.from_dict(x_text)
    input_encode = encoder.transform(input_)

    # Make prediction
#    Prediccion = tree.predict(input_encode)

    Prediccion = tree.predict(input_encode)
    
    return Prediccion[0]

if __name__ == "__main__":
    
#    if len(sys.argv) == 1:
#        print('Please add an input')
        
#    else:

#        url = sys.argv[1]

    Prediccion = predict_price(year,Mileage,State,Make,Model)
    print(Prediccion[0])