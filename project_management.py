# -*- coding: utf-8 -*-
"""project Management

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cwXsF_Tgasb4X8OEIEbfNSmHnTVBkvw0
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
uploaded = files.upload()

df=pd.read_csv('/content/sample_data/Project Management Dataset.csv')
df.head()

print(df.isnull().sum())

print(df.describe())

sns.histplot(data=df,x=' Project Cost ',kde=True)
plt.title('Distribution Of Project Cost')
plt.show()

sns.countplot(data=df,x='Project Type')
plt.xticks(rotation=45)
plt.title(' Project Count by Type ')
plt.show()

sns.barplot(data=df,x='Department',y=' Project Cost ',estimator=np.mean)
plt.xticks(rotation=45)
plt.title(' Average Cost by Department ')
plt.show()

plt.pie(df['Status'].value_counts(),labels=df['Status'].value_counts().index,
        autopct='%1.1f%%')
plt.title('Project Status Distribution')
plt.show()

corr=df.corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

sns.boxplot(data=df,x='Complexity',y='Completion%',showfliers=False)
plt.title(' Project Complection % by Complexity ')
plt.show()

df[' Project Cost ']=df[' Project Cost '].str.replace(',','').astype(float)
df['Year-Month']=df['Year'].astype(str)+'-'+df['Month'].astype(str)
df.groupby('Year-Month')[' Project Cost '].sum().plot()
plt.title('Monthly Project Costs Over Time')
plt.xticks(rotation=45)
plt.show()

sns.scatterplot(data=df,x=' Project Cost ',y=' Project Benefit ')
plt.title('Project Cost vs.Benefit')
plt.show()

import plotly.express as px

fig = px.scatter_3d(df, x=' Project Cost ', y=' Project Benefit ', z='Complexity',
                  color='Project Type')
fig.update_layout(scene = dict(
                    xaxis = dict(title  = 'Project Cost'),
                    yaxis = dict(title  = 'Project Benefit'),
                    zaxis = dict(title  = 'Complexity')))
fig.show()