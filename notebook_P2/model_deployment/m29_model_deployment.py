#!/usr/bin/python

import pandas as pd
from sklearn.externals import joblib
import sys
import os
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import r2_score, roc_auc_score
from sklearn.model_selection import train_test_split

def predict_movie_genre(year,title,plot):
    
    clf = joblib.load(os.path.dirname(__file__) + '/movie_pred.pkl') 
    vect= joblib.load(os.path.dirname(__file__) + '/vect.pkl') 
    
    x_text=[{"Year": year, "title": title, "plot": plot}]
    input_ = pd.DataFrame.from_dict(x_text)
    
    X_test_dtm = vect.transform(input_['plot'])
    
    cols = ['p_Action', 'p_Adventure', 'p_Animation', 'p_Biography', 'p_Comedy', 'p_Crime', 'p_Documentary', 'p_Drama', 'p_Family',
        'p_Fantasy', 'p_Film-Noir', 'p_History', 'p_Horror', 'p_Music', 'p_Musical', 'p_Mystery', 'p_News', 'p_Romance',
        'p_Sci-Fi', 'p_Short', 'p_Sport', 'p_Thriller', 'p_War', 'p_Western']


    # Make prediction
#    Prediccion = tree.predict(input_encode)

    y_pred_test_genres = clf.predict_proba(X_test_dtm)
    
    res = pd.DataFrame(y_pred_test_genres, index=input_.index, columns=cols)   
    
    return res

if __name__ == "__main__":
    
#    if len(sys.argv) == 1:
#        print('Please add an input')
        
#    else:

#        url = sys.argv[1]

    res = predict_movie_genre(year,title,plot)
    print(res)