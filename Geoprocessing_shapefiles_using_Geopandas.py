# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:26:53 2020

@author: KUSH
"""
# Import necessary libraraies
# Packages Required: Geopandas, Descartes, Numpy, Matplotlib

import geopandas as gpd
import matplotlib.pyplot as plt

file_1 = r"F:\IND_adm_shp/IND_adm0.shp"
file_2 = r"F:\IND_adm_shp/Uttarakhand.shp"
file_3 = r"F:\IND_adm_shp/Himanchal.shp"

India = gpd.read_file(file_1)
Uttarakhand = gpd.read_file(file_2)
Himanchal = gpd.read_file(file_3)

India.plot(cmap = "rainbow",edgecolor='k')
Uttarakhand.plot(cmap = "jet",edgecolor='k')
Himanchal.plot(cmap = "rainbow",edgecolor='k')

# Intersecting

Intersection=gpd.overlay(India,Uttarakhand,how = "intersection")
Intersection.plot()

# Union

Union=gpd.overlay(Himanchal,Uttarakhand,how = "union")
Union.plot(cmap = "tab10",edgecolor='k',facecolor='none')


# Difference

Difference=gpd.overlay(India,Uttarakhand,how = "difference")
Difference.plot(cmap = "tab10",edgecolor='k',facecolor='none')

# symmetrical difference

symmetrical_Difference = gpd.overlay(India,Uttarakhand,how = "symmetric_difference")
symmetrical_Difference.plot(cmap = "tab10",edgecolor='k',facecolor='none')



