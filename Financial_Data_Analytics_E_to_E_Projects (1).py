#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ## Datasets import from csv file(Collection)

# In[2]:


df = pd.read_csv(r"C:\Users\Hp\Downloads\financial_analytics_data.csv")


# In[3]:


df


# ### 1) Problem Statement (Objective) : - 
# 
# ##### 1) Without analyzing the competition, it is difficult for a business to survive. You are
# ##### 2) tasked to analyse the competition for the management to provide better results. This
# ##### 3) data set has information on the market capitalization of the top 500 companies in India.
# ##### 4) Serial NumberNameName of CompanyMar Cap – CroreMarket Capitalization in
# ##### 5) CroresSales Qtr – CroreQuarterly Sale in crores. Find key metrics and factors and
# ##### 6) show the meaningful relationships between attributes.
# ##### 7) Do your own research and come up with your findings

# ## 2) Understanding the data :- 

# In[4]:


# Top 5 data show

df.head()


# In[5]:


# Bottom 5 data show

df.tail()


# In[6]:


df.columns


# In[7]:


# How many Row's and Calumn in this data show

print('Number of Rows :- ', df.shape[0])

print('Number of Columns : - ', df.shape[1])


# In[8]:


# Data information

df.info()


# In[9]:


# All Numerical data show in percentile 

round(df.describe(),2).T


# ## 2) Data Cleaning and Preprocessing : - 

# In[10]:


df.isnull()


# In[11]:


df.isnull().sum()


# In[12]:


# Droped the unnecessary column from data : - 

df.drop(['Unnamed: 4'], axis = 1, inplace = True)


# In[13]:


df


# In[14]:


df.isnull().sum()


# In[15]:


df['Mar Cap - Crore'].value_counts()


# In[16]:


# Droped the duplicates values from the data

print(df.duplicated('Mar Cap - Crore'))


# In[17]:


df.drop_duplicates('Mar Cap - Crore', inplace = True)


# In[18]:


df


# In[19]:


df.isnull().sum()


# In[20]:


df['Mar Cap - Crore'].fillna(df['Mar Cap - Crore'].mean(), inplace = True)


# In[21]:


df.isnull().sum()


# In[22]:


df['Sales Qtr - Crore'].value_counts()
print(df)
df['Sales Qtr - Crore'].nunique()


# In[23]:


for column in df.columns:
    if df[column].dtype != 'object':
        mean = df[column].mean()
        df[column] = df[column].fillna(mean)


# In[24]:


df.isnull().sum()


# ## Exploratory Data Analysis (EDA) 

# In[25]:


df.columns


# In[26]:


df.info()


# ## Used by Histogram graph for Market Capitalization
# 
# 
# ### 1. Distribution of Market Capitalization

# In[27]:


plt.figure(figsize=(10, 6))
plt.hist(df['Mar Cap - Crore'], bins=25, color='blue', edgecolor='black')
plt.xlabel('Market Capitalization (Crore)')
plt.ylabel('Frequency')
plt.title('Distribution of Market Capitalization')
plt.show()


# ## Used by Histogram Graph for Quarterly Sales
# 
# ### 2. Distribution of Quarterly Sales

# In[28]:


plt.figure(figsize=(10, 6))
plt.hist(df['Sales Qtr - Crore'], bins=30, color='salmon', edgecolor='black')
plt.xlabel('Quarterly Sales (Crore)')
plt.ylabel('Frequency')
plt.title('Distribution of Quarterly Sales')
plt.show()


# ## Used by Scatter plot for Market Cap vs. Quarterly Sales
# 
# 
# ### 3. Market Capitalization vs. Quarterly Sales

# In[29]:


plt.figure(figsize=(10, 6))
plt.scatter(df['Mar Cap - Crore'], df['Sales Qtr - Crore'], color='purple')
plt.xlabel('Market Capitalization (Crore)')
plt.ylabel('Quarterly Sales (Crore)')
plt.title('Market Cap vs. Quarterly Sales')
plt.show()


# ## Used by Bar plot for Top 10 Companies by Market Capitalization
# 
# 
# ### 4. Top 10 Companies by Market Capitalization

# In[30]:


top_10_mar_cap = df.nlargest(10, 'Mar Cap - Crore')

plt.figure(figsize=(12, 8))
plt.bar(top_10_mar_cap['Name'], top_10_mar_cap['Mar Cap - Crore'], color='teal')
plt.xlabel('Company Name')
plt.ylabel('Market Capitalization (Crore)')
plt.title('Top 10 Companies by Market Capitalization')
plt.xticks(rotation=45)
plt.show()


# ## Used by Bar plot for Top 10 Companies by Quarterly Sales
# 
# 
# ### 5. Top 10 Companies by Quarterly Sales

# In[31]:


top_10_sales = df.nlargest(10, 'Sales Qtr - Crore')

plt.figure(figsize=(12, 8))
plt.bar(top_10_sales['Name'], top_10_sales['Sales Qtr - Crore'], color='orange')
plt.xlabel('Company Name')
plt.ylabel('Quarterly Sales (Crore)')
plt.title('Top 10 Companies by Quarterly Sales')
plt.xticks(rotation=45)
plt.show()


# ## Top 5 companies by market capitalization
# 
# ### 6. Key Metrics and Findings

# In[34]:


top_5_mar_cap = df.nlargest(5, 'Mar Cap - Crore')
print("Top 5 Companies by Market Capitalization:")
print(top_5_mar_cap[['Name', 'Mar Cap - Crore']])


# ## Top 5 companies by quarterly sales
# 
# ### 6.1 Key Metrics and Findings

# In[35]:


top_5_sales = df.nlargest(5, 'Sales Qtr - Crore')
print("Top 5 Companies by Quarterly Sales:")
print(top_5_sales[['Name', 'Sales Qtr - Crore']])


# ## Summary statistics for numerical columns
# 
# ### 7. Market Capitalization and Quarterly Sales Summary Statistics

# In[36]:


summary_stats = df[['Mar Cap - Crore', 'Sales Qtr - Crore']].describe()
print(summary_stats)


# ## Summary of Findings :-
# 
# ### a) Distribution Insights:-
# 
# #### Market capitalization and quarterly sales follow a certain distribution, with a few companies having very high values compared to others.
# 
# ### b) Relationship Between Attributes:-
# 
# #### The scatter plot and correlation heatmap help in understanding the relationship between market capitalization and quarterly sales.
# 
# ### c) Top Companies:-
# 
# #### Identifying the top companies by market capitalization and quarterly sales provides insights into the market leaders.

# ## Conclusion
# #### These analyses and visualizations provide a comprehensive understanding of the market landscape 
# #### for the top 500 companies in India. 
# #### The management can use these insights to better understand the competition and make informed decisions.

# In[ ]:




