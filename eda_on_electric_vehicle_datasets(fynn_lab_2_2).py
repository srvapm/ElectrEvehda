# -*- coding: utf-8 -*-
"""EDA on Electric_Vehicle_Datasets(fynn lab 2.2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JMtwuC5dUcqre3Ih96_yvev_7sk3EOSP
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm

df= pd.read_csv('ElectricCarData_regular.csv')

df.head()

df.isnull().sum() #null values

df.describe()

df.info() #information of type of data
plt.show()

a=np.arange(1,104)
sb.pairplot(df,hue='RapidCharge') #pairplot for rapid charger

ax= plt.figure(figsize=(20,10))
sb.barplot(x='Brand',y=a,data=df)
plt.grid(axis='y')
plt.title('Brands Available')
plt.xlabel('Brand')
plt.ylabel('Numbers')
plt.xticks(rotation=45)
plt.show() #Numbers of the brands

ax= plt.figure(figsize=(15,8))
sb.heatmap(df.corr(),linewidths=1,linecolor='white',annot=True) #heatmap to show co-relation between the features
plt.show()

df['PlugType'].value_counts().plot.pie(figsize=(5,10),autopct='%.0f%%',explode=(.1,.1,.1,.1))
plt.title('Plug Type')
plt.show() #type of plug charing

ax= plt.figure(figsize=(20,10))
sb.barplot(x='Brand',y='PriceEuro',data=df,palette='Set2')
plt.title('Price of a Car')
plt.xlabel('Price in Euro')
plt.grid(axis='y')
plt.ylabel('Numbers')
plt.xticks(rotation=45)
plt.show()

df['BodyStyle'].value_counts().plot.pie(figsize=(6,10),autopct='%.0f%%',explode=(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1))
plt.title('Body Style')
plt.show #body style of the cars

ax= plt.figure(figsize=(20,5))
sb.barplot(x='Brand',y='PriceEuro',data=df,palette='Set2')
plt.title('Price of a Car')
plt.xlabel('Price in Euro')
plt.grid(axis='y')
plt.ylabel('Numbers')
plt.xticks(rotation=45)
plt.show()#price of the cars