# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:11:59 2023

@author: rouab
"""
print("test with branch")


# -*- coding: utf-8 -*-
"""
RISK MAPS
@author: Miia Chabot
"""
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#HEATMAP, Exercise 1.-------------------------------------------------------------
# Create a dataset
df = pd.DataFrame(np.random.random((5,5)), columns=["a","b","c","d","e"])
# numpy.random.random() is one of the function for doing random sampling in numpy. 
#It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0).


# Default heatmap            ------- plot first heatmap
p1 = sns.heatmap(df)


#Exercise2-----------------------------------Measuring Correlations-------------------
# Create a dataset
df = pd.DataFrame(np.random.random((100,5)), columns=["a","b","c","d","e"])
 
# Calculate correlation between each pair of variable
corr_matrix=df.corr()            # gives me matrix 5/5
 
# plot it
sns.heatmap(corr_matrix, cmap='PuOr')
# cmap='PuOr' : for color option
#Change it 
# https://matplotlib.org/stable/gallery/color/colormap_reference.html
sns.heatmap(corr_matrix, cmap='seismic')


#Exercise 3.----------------------------------------------------------------------
#HALF CORRELATION MATRIX
import seaborn as sns
import pandas as pd
import numpy as np
np.random.seed(0)
 
# Create a dataset
df = pd.DataFrame(np.random.random((100,5)), columns=["a","b","c","d","e"])

# Calculate correlation between each pair of variable
corr_matrix=df.corr()
 
# Can be great to plot only a half matrix
# Generate a mask for the upper triangle
mask = np.zeros_like(corr_matrix)
mask[np.triu_indices_from(mask)] = True

# Draw the heatmap with the mask
sns.heatmap(corr_matrix, mask=mask, square=True, cmap='rainbow')


#Exercise 4.---------------------------------------------------------------------
 
# Create a dataset
df = pd.DataFrame(np.random.random((10,10)), columns=["a","b","c","d","e","f","g","h","i","j"])

# plot a heatmap with annotation
sns.heatmap(df, cmap='rainbow', annot=True, annot_kws={"size": 7})

#Exercise 5--------------------------------------------------------------------------

import matplotlib.pyplot as plt

column_labels = list('ABC')
row_labels = list('WXYZ')
data = np.array([[1, 2, 3], [0, 3, 2], [1, 2, 3], [4, 3, 2]]) 
fig, axis = plt.subplots() 
heatmap = axis.pcolor(data, cmap=plt.cm.Greens)
plt.savefig('test.png')
plt.show() 

#Exercise 6 -------------------------------------------real case study------------
column_labels = list('ABC') 
row_labels = list('WXYZ')
data = np.array([[1, 2, 3], [0, 3, 2], [1, 2, 3], [4, 3, 2]])
fig, axis = plt.subplots() 
heatmap = axis.pcolor(data, cmap='rainbow') 
plt.savefig('test.png')
plt.show() 

#Real-case Study: your first RISK MAP------------------------------------------
#Step 1--------------
#Using Diverging colormaps and selecting red, yellow, green
column_labels = list('ABC') 
row_labels = list('WXY')
data = np.array([[4, 4, 3], [4, 3, 2], [3, 2, 2]])
fig, axis = plt.subplots() 
#axis.axis("off")
heatmap = axis.pcolor(data, cmap='RdYlGn') 
plt.savefig('test.png')
plt.show() 

#Making it bigger
data = np.array([[4, 4, 2,1], [4, 2, 1,2], [2,1, 2,0], [1, 2, 0,0]])
fig, axis = plt.subplots()
#axis.axis("off")
heatmap = axis.pcolor(data, cmap='RdYlGn') 
plt.savefig('test.png')
plt.show() 

#choosing different colormaps
data = np.array([[4, 4, 2,1], [4, 2, 1,2], [2,1, 2,0], [1, 2, 0,0]])
fig, axis = plt.subplots()
axis.axis("off")
heatmap = axis.pcolor(data, cmap='coolwarm') 
plt.savefig('test.png')
plt.show() 

#Purple_Green
data = np.array([[4, 4, 2,1], [4, 2, 1,2], [2,1, 2,0], [1, 2, 0,0]])
fig, axis = plt.subplots()
axis.axis("off")
heatmap = axis.pcolor(data, cmap='PRGn') 
plt.savefig('test.png')
plt.show() 

#STep 2, the scatterplot--------------------------------

y = [0.2, 0.4,0.4,2.5,1.5,1.4,1.9,0.95,1,1.3,1.6,1.92,2.7,0.5,1.6,1.8,2.2,2.7,2.5,2.3]
x = [0.9, 0.9,2.7,0.2,0.1,0.3,0.85,1.3,1.8,1.82,1.5,1.82,1.98,2.3,2.6,2.3,2.7,2.1,0.7,0.9]
n = [12,8,14,20,11,19,7,13,17,5,4,15,6,18,10,3,16,2,1,9]

fig, ax = plt.subplots()
ax.scatter(x, y)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i], y[i]))
    
# 3x3 RISK MAP: FINAL STEP------------------------------------------------------------  
# Insert your scatterplot in your map

#The map
data = np.array([[4, 4, 3], [4, 3, 2], [3, 2, 2]])
axis.hlines([1, 2, 3], *axis.get_xlim())
axis.vlines([1, 2, 3], *axis.get_xlim())

# The scatterplot (do not place your dots on the grid)
y = [0.2, 0.4,0.4,2.5,1.5,1.4,1.8,0.8,1.1,1.4,1.6,1.8,2.7,0.5,1.6,1.8,2.2,2.7,2.5,2.3]
x = [0.9, 0.9,2.7,0.2,0.1,0.3,0.8,1.3,1.8,1.82,1.5,1.82,1.9,2.3,2.6,2.3,2.7,2.1,0.7,0.85]
n = [12,8,14,20,11,19,7,13,17,5,4,15,6,18,10,3,16,2,1,9]

fig, axis = plt.subplots()
#axis.axis("off")
heatmap = axis.pcolor(data, cmap='RdYlGn') 
axis.scatter(x, y, c="grey", alpha=0.5 )
axis.hlines([1, 2, 3], *axis.get_xlim(), linestyles ='dotted',lw=1.5, color='grey')
axis.vlines([1, 2, 3], *axis.get_xlim(),linestyles ='dotted',lw=1.5, color='grey')

plt.title("Risk Map",size=12, fontname="Calibri")
plt.xlabel("Severity", size=10, fontname="Calibri")
plt.ylabel("Frequency", size=10, fontname="Calibri")

for i, txt in enumerate(n):
      axis.annotate(txt, (x[i], y[i]),xytext=(x[i]+0.03, y[i]+0.04))

plt.savefig('test.png')
plt.show() 

#Using Your own Excel-----------------------------------------------------------------

df = pd.read_excel("C:/Users/Miia CHABOT/Desktop/Data/Data_Heatmap.xlsx")
data = np.array([[4, 4, 3], [4, 3, 2], [3, 2, 2]])
n = df['N'].to_list()
x = df['X'].to_list()
y = df['Y'].to_list()

fig, axis = plt.subplots()
axis.axis("off")
heatmap = axis.pcolor(data, cmap='RdYlGn')
axis.vlines([1, 2, 3], *axis.get_xlim(), linestyles ='dotted', lw=1.5, color ='grey')
axis.hlines([1, 2, 3], *axis.get_xlim(), linestyles ='dotted', lw=1.5, color ='grey')
axis.scatter(x, y, c='grey',alpha=0.5)

for i, txt in enumerate(n):
    axis.annotate(txt, (x[i], y[i]),xytext =(x[i]+0.03, y[i]+0.04))

plt.savefig('test.png')
plt.show() 
    
# end file
# end end
