#!/usr/bin/env python
# coding: utf-8

# # Customer data analysis
# 
#     - data link: https://archive.ics.uci.edu/ml/datasets/bank+marketing

# # < Data Introduction >
#  - Marketing data conducted by overseas banks
#  - Conduct marketing campaigns with outbound telemarketing
#  

# In[1]:


import pandas as pd
from pandas import Series
from pandas import DataFrame

import matplotlib.pyplot as plt


# # Retrieve data
# file: bank-additional-full.csv

# In[2]:


df = pd.read_csv("C:/Users/kcw98/Desktop/Part 13~17 Project/bank-additional/bank-additional/bank-additional-full.csv")


# In[23]:


# Print head for test
df.head()


# In[4]:


# Data is separated by ';', so do in the code
df = pd.read_csv("C:/Users/kcw98/Desktop/Part 13~17 Project/bank-additional/bank-additional/bank-additional-full.csv", engine='python', sep=';')

# head()
df.head()


# # missing data

# In[5]:


# missing data
df.isnull()


# In[6]:


# missing data - in column
df.isnull().sum()

# there is no missing data as a result


# In[7]:


# shape - dataframe size  (row, column)
df.shape


# In[8]:


df.describe()


# In[9]:


# columns = print column name
df.columns


# In[10]:


# unique() - Initial values
# eg) education

df['education'].unique()


# In[11]:


# value_counts() - Initial value's frequencies
df['education'].value_counts()


# # Data Visualisation
# - Clean/prepare the data for analysis

# In[12]:


df['age']


# In[13]:


df['age'].plot()
plt.show()


# - age column line graph (ascending)
# 

# In[14]:


# ascending order
# eg) age column
age = df['age'].sort_values()
age


# In[15]:


# reset_index
age = age.reset_index()

age


# In[16]:


# drop(axis=1) - delete column
age = age.drop('index', axis=1)
age


# In[17]:


age.plot()
plt.show()

# Check the data by separating 'age' into 20s, 30s, 40s...


# In[18]:


# Histogram
df['age'].plot.hist()
plt.show()


# In[19]:


# Histogram

df['age'].plot.hist(bins=range(10,101,10), figsize=[15,8])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Histogram of df.age', fontsize=20)
plt.show()


# In[20]:


# duration line graph visualisation
(((df['duration'].sort_values()).reset_index()).drop('index', axis=1)).plot()
plt.show()


# In[21]:


df['duration'].describe()


# In[22]:


# bins = range(0, 5001, 100)
df['duration'].plot.hist(bins=range(0, 5001c, 100))
plt.show()


# In[ ]:


# HIstogram
df['duration'].plot.hist(bins=range(0, 5001, 100), figsize=[15,8])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Histogram of df.duration', fontsize=20)
plt.show()


# In[ ]:


# unique() - age column initial value check
df['age'].unique()


# In[ ]:


# unique() - marital column initial value check
df['marital'].unique()

# The marital column cannot be visualised by plot()


# - Bar graph visualisation
#     1. value_counts
#     2. Bar graph visualisation

# In[ ]:


# 1. value_counts() initial value frequencies
# marital
marital=df['marital'].value_counts()

# 2. marital variable bar graph visualisation
marital.plot.bar()
plt.show()


# In[ ]:


# 2-1. width bar graph
marital.plot.barh()
plt.show()


# In[ ]:


# same with 'education'
education=df['education'].value_counts()
education.plot.barh()
plt.show()


# # Analysis1:
#     
# ### People with loans are unlikely to sign up for bank products.
# 
# - Goal:
#     1. Hypothesis verification process coding practice
#     2. Practice using groupby
#     
# - Diagramming the coding process for analysis
#     1. Depending on membership status, groups are divided into joined groups and non-joined groups.
#     2. Divide the divided data according to whether or not it is a loan.
#     3. Compare the proportion of people with loans among the group that joined with the proportion of people with loans among the group that did not join.

# In[24]:


# 1. Divide into joined groups and non-joined groups depending on membership status.
# Column for membership: 'y'
# unique()
df['y'].unique()
# Use groupby - Divided into yes and no group


# In[26]:


# 1. Based on the membership status, the data is divided into two groups: joined groups and non-joined groups.
# groupby('y')
grouped=df.groupby('y')


# In[27]:


# 1. Depending on membership status, it is divided into groups that have joined and groups that have not joined.
# get_group('yes') - Extract dataframe where y column is 'yes' - Extract only subscription groups
# get_group('no') - Extract dataframe where y column is 'no' - Extract only groups that have not joined
yes_group = grouped.get_group('yes')
no_group = grouped.get_group('no')


# In[28]:


# 1. Divide into joined groups and non-joined groups depending on membership status.
# output yes_group
yes_group.head()


# In[29]:


# Output no_group
no_group.head()


# In[30]:


# Divide the divided data (yes_group, no_group) according to loan status.
# value_counts
yes = yes_group['loan'].value_counts()
yes


# In[39]:


no = no_group['loan'].value_counts()
no


# In[36]:


# The proportion of people with loans in groups that have joined and the proportion of people with loans in groups that have not joined
# Specific gravity: Divide the value of each series variable by the total of the series
# series/series.sum()
yes = yes/yes.sum()
yes


# In[40]:


no = no/no.sum()
no


# In[41]:


# combine yes & no group dataframe
# concat: Series or data frame fault (default = row-wise concatenation)
pd.concat([yes, no], axis=1)


# In[42]:


#Set series name
yes.name = 'y_yes'
no.name = 'y_no'


# In[43]:


pd.concat([yes,no], axis=1)
# The loan proportion of the group that joined is 0.005 less than that of the group that did not join.


# # Analysis2:
# ### We are trying to market the same product to new customers.
# ### Considering age, product subscription, and occupation, which group needs to change its marketing strategy?
# 
# - Goal:
# 1. Hypothesis verification process coding practice
# 2. Practice using pivot_table
# 
# - Analysis conditions: Analyze three columns (age, job, y) together
# - pd.pivot_table('dataframe variable', value=aggregation target column (numerical data), index=column name to be the row index, columns=column name to be the column index, aggfunc=aggregation function-sum,mean,min,max ,std,var)

# In[45]:


pd.pivot_table(df, values='age', index='y', columns='job', aggfunc='mean')


# In[44]:


# Can be executed by entering values, index, and columns in order instead of writing them out individually
pd.pivot_table(df, 'age', 'y', 'job', aggfunc='mean')


# In[47]:


# multi index - keyboard
# ['y', 'marital'
pd.pivot_table(df, 'age', ['y', 'marital'], 'job', aggfunc='mean')


# In[48]:


# multi index - keyboard
# [ 'job', 'contact']
pd.pivot_table(df, 'age', ['y', 'marital'], ['job', 'contact'], aggfunc='mean')


# In[49]:


# missing value replacement
# fill_value =
pd.pivot_table(df, 'age', ['y', 'marital'], ['job', 'contact'], aggfunc='mean', fill_value = 0)


# In[50]:


#pivot_table
pivot = pd.pivot_table(df, values='age', index='y', columns='job', aggfunc='mean')
pivot


# In[51]:


# Calculate the difference between yes and no rows (using loc inexer)
pivot.loc['yes']-pivot.loc['no']


# In[52]:


# Create diff line (difference between yes line and no line)
pivot.loc['diff']=pivot.loc['yes']-pivot.loc['no']
pivot


# In[53]:


# Sort in descending order by diff
# sort_values() - default: Ascending order by column
# axis=1, ascending=False: Descending by row
result = pivot.sort_values('diff', axis=1, ascending=False)
result


# In[55]:


# Visualize diff row bar graph of result
result.loc['diff'].plot.bar()
plt.show()


# In[56]:


# Visualize diff row bar graph of result

result.loc['diff'].plot.bar(figsize=[15,30])
plt.title('Anlaysis 2 Visualisation', fontsize=20)
plt.xticks(fontsize=16, rotation=45)
plt.yticks(fontsize=16)
plt.xlabel('job', fontsize=16)
plt.ylabel('diff', fontsize=16)
plt.show()


# In[ ]:




