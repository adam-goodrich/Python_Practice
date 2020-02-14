#!/usr/bin/env python
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">
# 
# ## Homework: Intro to Pandas
# 
# _Author: Kevin Coyle (L.A.)_
# 
# ---
# 
# 

# Welcome!

# #### Pandas: Intro Practice Problems
# 
# In this homework, you're going to write code for a few problems. 
# 
# You'll be practicing these programming concepts we've covered in class:
# * Reading data sets into Pandas.
# * Filtering, manipulating, and sorting data sets.
# * Basic exploratory data analysis with Pandas.

# #### #1. Import Pandas with an alias of `pd`.

# In[1]:


import pandas as pd


# #### #2. Read in the NBA players `csv` into a variable called `nba_df`.

# This is a data set of NBA players from 2015. The filename is `NBA_players_2015.csv`.

# In[2]:


nba_df = pd.read_csv('NBA_players_2015.csv')


# #### #3. Look at the first five rows of the data set.

# In[3]:


nba_df.head()


# #### #4. Check out the shape of the data set.

# In[4]:


nba_df.shape


# #### #5. Run some summary stats on the data set with the `describe()` function.

# In[5]:


nba_df.describe()


# #### #6. Sort the data set in on the `players` column in alphabetical order.

# In[6]:


nba_df["player"].sort_values()


# #### #7. Filter the data set. Create three sub DataFrames from the `position` column for `G`, `F`, and `C`.

# In[7]:


mask_g = (nba_df["pos"] == "G")
nba_df[mask_g]


# In[8]:


mask_f = (nba_df["pos"] == "F")
nba_df[mask_f]


# In[9]:


mask_c = (nba_df["pos"] == "C")
nba_df[mask_c]


# #### #8.  Run `describe()` on these new DataFrames. Compare the mean field goals (the `fg` column) between positions.

# In[10]:


nba_df[mask_g].describe()


# In[11]:


nba_df[mask_f].describe()


# In[12]:


nba_df[mask_c].describe()


# The end!

# #### Great job!
