#!/usr/bin/env python
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">
# 
# ## Homework: Plotting With Pandas
# 
# _Authors: Kevin Coyle (L.A.)_
# 
# ---
# 
# 

# Welcome!

# #### Pandas: Plotting Practice Problems
# 
# In this homework, you're going to write code for a few problems. 
# 
# You'll practice the following programming concepts we've covered in class:
# * Plotting with Pandas.
# * Determining best plot given a data set.

# #### #1. Import Pandas, `Matplotlib.pyplot`, and NumPy. Don't forget the line that makes `matplotlib` render in a Jupyter Notebook!

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix
get_ipython().run_line_magic('matplotlib', 'inline')


# #### #2. Read in the NBA players `csv` into a variable called `nba_df`.

# This is a data set of NBA players from 2015. The filename is `NBA_players_2015.csv`.

# In[2]:


nba_df = pd.read_csv('NBA_players_2015.csv')


# #### #3. Look at the first five rows of the data set.

# In[3]:


nba_df.head()


# In[ ]:





# #### #4. Create a histogram of the `age` column.

# In[4]:


nba_df["age"].plot(kind="hist")


# #### #5. Create a histogram of the `age` column, but change the number of bins to `20`.

# In[5]:


nba_df["age"].plot(kind="hist", bins=20)


# #### #6. Discuss the difference in the two plots and the implications.

# While skewed, the plot with fewer bins leads one to believe that the bin to the right of the highest-numbered age bin is the second largest. The second-largest bin occurs right after 22 and before 25.

# #### #7. Rename the `position` column `'pos'` with the following `C:5`, `G:1`, and `F:3`. Then create a scatter matrix plot with the `'pos'`, `'pts'`, `'age'`, and `'fg'` columns.

# In[6]:


nba_df


# In[7]:


nba_df = nba_df.replace(to_replace="C", value=5)
nba_df


# In[8]:


nba_df = nba_df.replace(to_replace="G", value=1)
nba_df


# In[9]:


nba_df = nba_df.replace(to_replace="F", value=3)
nba_df


# In[10]:


nba_df


# In[11]:


nba_df_scatter = nba_df


# In[12]:


nba_df_scatter = pd.DataFrame(np.random.randn(1000, 4), columns=["pos", "pts", "age", "fg"])
pd.plotting.scatter_matrix(nba_df_scatter, alpha=0.2, figsize=(15, 15))


# #### #8. Plot the number of guards, centers, and forwards in this data set.

# In[13]:


nba_df["pos"].value_counts()


# In[14]:


nba_df["pos"].value_counts().plot(kind="bar")
plt.xticks(np.arange(3), ("Guards", "Forwards", "Centers"))


# The end!

# #### Great job!
