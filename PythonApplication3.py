from tkinter import Pack
from aeropy import xfoil_module
import numpy as np


directory = "C:/Users/Administrator/Desktop/WinForm/PythonApplication3/foil_data/model1"
a = np.arange(0,15,0.5)
print(xfoil_module.find_coefficients("0_0.dat",alpha=a,NACA=False,PANE=True,Reynolds=100000,iteration=2000))