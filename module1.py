from math import exp
from operator import index
from aeropy import xfoil_module
import pandas as pd
import os
import numpy as np
velocities = [100000,500000,1000000,10000000]
directory = "C:/Users/Administrator/Desktop/WinForm/PythonApplication3/foil_data/model_1/"
export_data = pd.DataFrame()
coef_data = pd.DataFrame()
for filename in os.listdir(directory):
    if filename.endswith('.dat'):
        coords = pd.read_csv("./"+filename,header=None,index_col=None).transpose()
        coords = coords.drop(index=0)
        coords.index = ["0"]
        for i in range(4):
            a = np.arange(0,15,0.5)
            Reynolds = velocities[i]
            for d in range(len(a)):
                export_data = pd.concat([export_data,coords])
                alpha = a[d]
                x = xfoil_module.find_coefficients(str(filename),alpha=alpha,NACA=False,PANE=True,Reynolds=Reynolds,iteration=2000)
                x = pd.DataFrame(x, index= [0])
                coef_data = pd.concat([coef_data,x])
                print(coef_data)
export_data = export_data.reset_index()
export_data.pop("index")
print("______",export_data,"______")
coef_data = coef_data.reset_index()
coef_data.pop("index")
print("______",coef_data,"______")
export_data = pd.concat([export_data,coef_data],axis=1)
export_data.to_csv("model1")
