"""
Author: Muhammet Ali Güldalı
"""


from operator import index
from unittest import skip
import pandas as pd
import numpy as np
import os



def read_coords(directory):
    foil_list = []
    name_list = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            foil_list.append(f)
            name_list.append(filename)
    all_upper_coords = []
    all_lower_coords = []
    for i in range(len(foil_list)):
        coord_list = []
        for j in range(2):
            coords_temp = pd.read_csv(foil_list[i],index_col=False,delim_whitespace=True,on_bad_lines='skip',usecols=[j])
            if coords_temp.iloc[0].any()>1.5:
                coords_temp = coords_temp.drop([0])
            if int(len(coords_temp))%2 != 0:
                coords_temp = coords_temp.drop([0])
            coord_list.append(coords_temp)
        coords = pd.concat([coord_list[0],coord_list[1]],axis=1,join='inner')
        coords = coords.set_axis(['X', 'Y'], axis=1)
        upper_idx = int(len(coords)/2)
        upper_coords = coords[0:upper_idx]
        lower_coords = coords[upper_idx:]
        upper_coords = upper_coords.sort_values(by=['X'])
        lower_coords = lower_coords.sort_values(by=['X'])
        upper_np = np.array(upper_coords)
        lower_np = np.array(lower_coords)
        upper = upper_np.reshape(-1,2)
        lower = lower_np.reshape(-1,2)
        x = np.vstack((upper[:,0],lower[:,0]))
        y = np.vstack((upper[:,1],lower[:,1]))
        all_upper_coords.append(x)
        all_lower_coords.append(y)
    return (all_upper_coords,all_lower_coords,name_list)
