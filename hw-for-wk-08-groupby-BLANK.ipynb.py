#!/usr/bin/env python
# coding: utf-8

# ### Paycheck Protection Program
# 
# Let's analyze **an excerpt** from  <a href="https://www.sba.gov/funding-programs/loans/covid-19-relief-options/paycheck-protection-program">SBA's PPP loan data</a>.
# 
# The file we're working on is an excerpt (ingested via a link below) so we can't draw any hypothesis from our findings in this homework.

# In[1]:


## import library
import pandas as pd


# In[2]:


## Ingest remote data
df = pd.read_csv("https://raw.githubusercontent.com/sandeepmj/datasets/main/ppp_excerpt.csv")
df


# In[5]:


## get info about data types
df.info()


# ### ```.agg()```
# 
# - Use the ```.agg()``` that allows you call specific summary statistics at one time.

# In[7]:


## get the count, mean and median for CurrentApprovalAmount
result = df['CurrentApprovalAmount'].agg(['count', 'mean', 'median'])
result


# In[26]:


## What summary statistics for the CurrentApprovalAmount by Race?
## if you get scientific notation, round it by running the display option that changes the default display
## run the display code here

do=df["CurrentApprovalAmount"].agg("sum")
do


# In[ ]:





# ## ```groupby```

# In[10]:


## What is the sum, mean and count for the current 
## approval amount for owners by race 

dp=df["CurrentApprovalAmount"].agg(["sum","count", "mean"])
dp


# In[19]:


gb=df.groupby("Race")
gb

## What question(s) might you ask based on this result?

List answer(s):

# ================================

# In[22]:


## What is the sum and mean for the ForgivenessAmount amount for owners by gender

de=df["ForgivenessAmount"].agg(["sum","mean"])
de


# In[24]:


gw=df.groupby("Gender")
gw


# In[ ]:





# In[29]:


## What is the sum, mean and count for the current 
## approval amount for owners by race and gender

dq=df["CurrentApprovalAmount"].agg(["sum","mean","count"])
dq


# In[31]:


gp=df.groupby("Gender")
gp


# In[32]:


gi=df.groupby("Race")
gi


# ## What question(s) might you ask about the unanswered categories?:
# List answer(s) here:

# In[ ]:




