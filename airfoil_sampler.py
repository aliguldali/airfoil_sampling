"""
Author: Muhammet Ali Güldalı
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import coord_reader as cread
from cosine_dist import get_cosine_distribution
import pandas as pd

directory = './Airfoil_profiles'
 
x,y,name_list = cread.read_coords(directory)

#upper = np.array(upper)
#lower = np.array(lower)
#upper = upper.reshape(-1,2)
#lower = lower.reshape(-1,2)
plt.figure(figsize = (5.15,5.15))
plt.subplot(111)
samples = get_cosine_distribution()
for j in range(len(name_list)):
    filename = str(name_list[j])[:-4]
    y_values = pd.DataFrame() 
    for i in range(2):
        x_val = np.linspace(x[i][0], x[i][-1], 100)
        sampled_y = np.interp(samples, x[j][i], y[j][i])
        tck = interpolate.splrep(x[j][i], y[j][i], k = 5, s = 4)
        y_int = interpolate.splev(x_val, tck, der = 0)
        print(sampled_y)
        y_values[i] = sampled_y
        plt.plot(samples, sampled_y, linestyle = '', marker = 'o')
        plt.plot(x_val, y_int, linestyle = ':', linewidth = 0.25, color =  'black',)
        plt.axis('equal')
        filename
        plt.title(filename)
    plt.savefig("output/graphs/"+filename+".png")
    plt.clf()
    y_values.to_csv("output/values/"+filename+".csv",index=False)
    