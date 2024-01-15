# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:08:02 2024

@author: Bmbofwana
"""

import pandas as pd 
from datetime import datetime as dt 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

###Load Data 
data = pd.read_csv(r'C:\Users\bmbof\Desktop\Model\TestData.csv')

###Check Data types 
data.dtypes

###Check missing data
data.isnull().sum()

###Drop missing values
data = data.dropna(subset = ['name'])
data = data.drop('Unnamed: 0',axis=1)

######DATA PROCESSING

###Main category data 
print(data['main_category'].unique())

###Reduce the number of Main Categories 
Categories = {'Arts': ['Crafts, Arts, Photography'],
              'News': ['Journalism','Publishing'],
              'Movies': ['Film & Video', 'Video'],
              'Music': ['Music'],
              'Food': ['Food'],
              'Design': ['Design','Fashion'],
              'Games': ['Games','Comic'],
              'Theatre': ['Theatre'],
              'Tech': ['Technology'],
              'Dance': ['Dance']}


##New Main category 
data['New_Category'] = ''

##Recode Main category
for i in data.itertuples():    
    for j in Categories.items():
        if i[4] in j[1]:
            data['New_Category'][i[0]] = j[0]
        else:
            data['New_Category'][i[0]] = 'Unknown Category'




###Date processing
data['date'] = pd.to_datetime(data['launched'], format="%Y-%m-%d",errors='coerce')
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['day_of_week'] = data['date'].dt.dayofweek
data['qrt_year'] = data['date'].dt.quarter
data['week_month'] = data['date'].dt.week


###Sub Category data 
###View Sub category data points & drop data points having counts < 50
music_data = data[data['main_category'] == 'Music']
print(music_data['sub_category'].unique())
counts = music_data['sub_category'].value_counts()
valid_subcategories = counts[counts >= 50].index
music_data = music_data[music_data['sub_category'].isin(valid_subcategories)]


###Goal processing
##Compute summary statistics || Log transformation goal || Trim 15% of outliers 
music_data['goal'] = music_data['goal'].astype('float')
music_data['log_goal'].describe()
music_data['log_goal'] = np.log(music_data['goal'])
sns.boxplot(x = music_data['log_goal'])
sns.distplot(music_data['log_goal'])

###Feature Engineering - Length of the title 
data['name_length'] = data['name'].str.count(' ')

###Movie name processing
for i in ui.itertuples():    
    for j in Categories.items():
        print(j[0])
        if i[4] in j[1]:
                ui['New_Category'][i[0]] = j[0]
        else:
            continue
        
    