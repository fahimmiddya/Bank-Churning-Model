import numpy as np
import pandas as pd
import joblib
from guietta import _, Gui , Quit
gui = Gui(
    title = 'Bank GUI'
    ['Enter Values:', "__a__","__b__","__c__","__d__","__e__","__f__","__g__",['Predict']],
    [' Prediction :'     ,'result',  _    ,      _,      _,_      ,      _,      _,         _   ],
    [_               ,_       ,_      ,_      ,   Quit, _     ,      _,      _,_            ]
)
algo = joblib.load(r"C:\Users\fahra\OneDrive\Desktop\Bank\bank.pkl")
encoder = joblib.load(r'C:\Users\fahra\OneDrive\Desktop\Bank\bank_encoder.pkl')
with gui.Predict:
    new=[[float(gui.a),gui.b,float(gui.c),float(gui.d),float(gui.e),float(gui.f),float(gui.g)]]
    n = encoder.transform(new)
    predict = algo.predict(n)
    if predict == [1]:
        gui.result = "High chance of customer exiting."
    else:
        gui.result = "High chance of customer not exiting."
    
gui.run()