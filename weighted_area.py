# -*- coding: utf-8 -*-
import ogr
import gdal
import geopandas as gpd
import matplotlib.pyplot as plt
import csv
import numpy as np

data = np.genfromtxt(r'F:\netcdf\GIS\India_85_2006-2100_ams_series.csv', delimiter=',')
avg_prec = []
for i in range(75):
    avg_prec.append([])
    
for index in range(95):
    weighted_area = []
    area = []
    latitude = []
    longitude = []
    precipitation = []
    for i in range(75):
        weighted_area.append([])
        area.append([])
        latitude.append([])
        longitude.append([])
        precipitation.append([])
        avg_prec.append([])
    file2 = open(r"F:\netcdf\stations.csv", "r+")
    stations_name = []
    for row in csv.reader(file2):
        stations_name.append(row[0])
        #print(stations_name)
    count = 0

    for name in stations_name:
        sum = 0
        daShapefile = r"F:\netcdf\GIS\clipped_final\{}.shp".format(name)
        driver = ogr.GetDriverByName('ESRI Shapefile')
        dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.
        layer = dataSource.GetLayer()
        featureCount = layer.GetFeatureCount()
        layerDefinition = layer.GetLayerDefn()
    
        weighted_area[count].append(name)
        area[count].append(name)
        latitude[count].append(name)
        longitude[count].append(name)
        precipitation[count].append(name)
        if index == 0:
            avg_prec[count].append(name)
        
        
 #   print ("Number of features is {}" .format(featureCount))

 #   for i in range(layerDefinition.GetFieldCount()):
 #       print(layerDefinition.GetFieldDefn(i).GetName())
    
        for feature in layer:
#            print (feature.GetField("AREA_GEO"))
            sum = sum + feature.GetField("AREA_GEO")
            area[count].append(feature.GetField("AREA_GEO"))
            latitude[count].append('%.2f'%feature.GetField("Latitude"))
            longitude[count].append('%.2f'%feature.GetField("Longitude"))
      #     print(sum)
            for i in range(data.shape[0]):
  #             print(data[i,2])
                if '%.2f'%feature.GetField("Latitude") == '%.2f'%data[i,0] and '%.2f'%feature.GetField("Longitude") == '%.2f'%data[i,1] :
                    # print(data[i,2])
                    precipitation[count].append(data[i,2+index])
            
        
        for feature in layer:
#           print (feature.GetField("AREA_GEO")/sum)
            weighted_area[count].append(feature.GetField("AREA_GEO")/sum)
        
        count+=1   
    

    for length in range(75):
        x = precipitation[length][1:]
        y = weighted_area[length][1:]
        z  = np.multiply(x,y)
        #   for i in range(z.shape[0]):
        #      avg_prec[length].append(z[i])
        auto_sum = np.sum(z)
        avg_prec[length].append(auto_sum)
    
        
        
import csv
data = [[10,'a1', 1], [12,'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
with open("temp.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerows(data)
with open('temp.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ')
 for row in data:
   print(', '.join(row))
    

with open("weighted_area.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerows(weighted_area)
    
    
    
    
    