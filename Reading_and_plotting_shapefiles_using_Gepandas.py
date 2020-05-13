<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Topic: "Reading_and_plotting_shapefiles_using_Gepandas"

@author: KUSH
"""


# Import necessary libraraies
# Packages Required: Geopandas, Descartes, Numpy, Matplotlib

import geopandas as gpd
import matplotlib.pyplot as plt

file_1 = r"F:/netcdf/GIS/clipped_final/A_P_Puram_East_Coast.shp"
file_2 = r"F:/netcdf/GIS/clipped_final/Ambabal_Godavari.shp"

# Display a file:
catchment_1 = gpd.read_file(file_1)
catchment_1.plot(cmap = "jet", figsize = (10,10))

# Access the attribute table of shape file:

attribute_table = (catchment_1)
print(attribute_table)

# OR

# Access the attribute table of shape file:

Fields = (catchment_1.head(len(catchment_1)))
print(Fields)

no_of_columns = len(catchment_1)

# Displaying both the files together in one image:
catchment_2 = gpd.read_file(file_2)
catchment_2.plot(cmap = "rainbow", figsize = (10,10))


fig, ax = plt.subplots(1)
catchment_1.plot(ax =ax,cmap = "jet")
catchment_2.plot(ax = ax,cmap = "rainbow")
fig.show()

=======
# -*- coding: utf-8 -*-
"""
Topic: "Reading_and_plotting_shapefiles_using_Gepandas"

@author: KUSH
"""


# Import necessary libraraies
# Packages Required: Geopandas, Descartes, Numpy, Matplotlib

import geopandas as gpd
import matplotlib.pyplot as plt

file_1 = r"F:/netcdf/GIS/clipped_final/A_P_Puram_East_Coast.shp"
file_2 = r"F:/netcdf/GIS/clipped_final/Ambabal_Godavari.shp"

# Display a file:
catchment_1 = gpd.read_file(file_1)
catchment_1.plot(cmap = "jet", figsize = (10,10))

# Access the attribute table of shape file:

attribute_table = (catchment_1)
print(attribute_table)

# OR

# Access the attribute table of shape file:

Fields = (catchment_1.head(len(catchment_1)))
print(Fields)

no_of_columns = len(catchment_1)

# Displaying both the files together in one image:
catchment_2 = gpd.read_file(file_2)
catchment_2.plot(cmap = "rainbow", figsize = (10,10))


fig, ax = plt.subplots(1)
catchment_1.plot(ax =ax,cmap = "jet")
catchment_2.plot(ax = ax,cmap = "rainbow")
fig.show()

>>>>>>> be2911ef0b78548e92b475d02667c2ba49481369
#