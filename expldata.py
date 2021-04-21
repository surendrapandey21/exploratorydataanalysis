# Importing all the libraries needed in this notebook 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sample = pd.read_csv(r'/Users/surendra/Downloads/SampleSuperstore (2).csv')
sample.head()

sample.tail()

#Checking the data type
sample.dtypes

#Checking the missing values/outliers if any
sample.shape

sample.describe() # Give statistics data

sample.describe(include='all')

#Analysing Segment of people buying from the supermart
sample['Segment'].value_counts()

sample['Segment'].value_counts()/len(sample['Segment'])*100

s=(sample['Segment'].value_counts()/len(sample['Segment'])*100).plot(kind='bar',color='g')

#Analysing ship mode for the supermart
sample['Ship Mode'].value_counts()

M=(sample['Ship Mode'].value_counts())/len(sample['Ship Mode'])*100
M

M.plot(kind='bar')

#Analysing Category of items in supermart
sample['Category'].value_counts()

C=(sample['Category'].value_counts())/len(sample['Category'])*100
C.plot(kind='bar',color='r')

#Analysing Sub-category of items in the supermart
((sample['Sub-Category'].value_counts())/len(sample['Sub-Category'])*100).plot(kind='bar')

fig, ax = plt.subplots()
colors = {'Consumer':'red', 'Corporate':'blue', 'Home Office':'green'}
ax.scatter(sample['Sales'], sample['Profit'], c=sample['Segment'].apply(lambda x: colors[x]))
plt.show()

sample.pivot_table(values='Sales', index='Segment', columns='Discount', aggfunc='median')

sample.pivot_table(values='Profit', index='Segment', columns='Discount', aggfunc='median')

temp_sample = sample.loc[(sample['Segment']=='Consumer')&(sample['Discount']==0.1)]
temp_sample['Profit'].plot.hist(bins=50)

temp_sample = sample.loc[(sample['Segment']=='Consumer')&(sample['Discount']==0.2)]
temp_sample['Profit'].plot.hist(bins=50)

temp_sample = sample.loc[(sample['Segment']=='Corporate')&(sample['Discount']==0.8)]
temp_sample['Profit'].plot.hist(bins=50)

temp_sample = sample.loc[(sample['Segment']=='Consumer')&(sample['Discount']==0.8)]
temp_sample['Profit'].plot.hist(bins=50)

temp_sample = sample.loc[(sample['Category']=='Furniture')&(sample['Discount']==0.2)]
temp_sample['Profit'].plot.hist(bins=50)

temp_sample = sample.loc[(sample['Category']=='Technology')&(sample['Discount']<=0.3)]
temp_sample['Profit'].plot.hist(bins=50)

temp_sample = sample.loc[(sample['Category']=='Technology')&(sample['Discount']>=0.3)]
temp_sample['Profit'].plot.hist(bins=50)

temp_sample = sample.loc[(sample['Category']=='Office Supplies')&(sample['Discount']<=0.3)]
temp_sample['Profit'].plot.hist(bins=50)

temp_sample = sample.loc[(sample['Category']=='Office Supplies')&(sample['Discount']>=0.3)]
temp_sample['Profit'].plot.hist(bins=50)

temp = sample.groupby(['Segment', 'Discount']).Profit.median()
temp.plot(kind = 'bar', stacked = True)

