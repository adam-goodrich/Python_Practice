#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


# In[2]:


plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14


# ### Choose the OCC portal CSV File

# In[3]:


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
file_name = file_path
df = pd.read_csv(file_name)


# In[4]:


df.head()


# ### Chose the Google Sheets Invoicing Spreadsheet CSV File

# In[5]:


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
file_name = file_path
df_1 = pd.read_csv(file_name)


# In[6]:


df_1.head()


# ## Extract information needed from OCC portal CSV File

# In[7]:


df["File Number Data"]
new_File_Number_Data = []
for i in df["File Number Data"]:
    list = i.split ("\n")
    new_File_Number_Data.append(list[1])


# In[8]:


new_File_Number_Data


# In[9]:


df["Invoice Total"]
new_invoice_total = []
for i in df["Invoice Total"]:
    i = i.replace("$", "")
    new_invoice_total.append(i)


# In[10]:


new_invoice_total


# In[11]:


occ_df_1 = pd.DataFrame(data={'file': new_File_Number_Data})
occ_df_2 = pd.DataFrame(data={"occ_bill": new_invoice_total})


# In[12]:


occ_df_1


# In[13]:


occ_df_2


# In[14]:


occ_df = pd.concat([occ_df_1, occ_df_2], axis=1)


# In[15]:


occ_df


# ## Extract information needed from Google Sheets CSV File

# In[16]:


df_1["file"]
new_df_1 = []
for i in df_1["file"]:
    new_df_1.append(i)


# In[17]:


new_df_1


# In[18]:


df_1["bill"]
bill_df_1 = []
for i in df_1["bill"]:
    bill_df_1.append(i)


# In[19]:


bill_df_1


# In[20]:


gs_df = pd.DataFrame(data={"file": new_df_1, "our_bill": bill_df_1})


# In[21]:


gs_df


# ## Combine the information from both extracted Dataframes

# In[22]:


gs_occ_df = gs_df.merge(occ_df, how='left')
gs_occ_df = gs_occ_df.fillna("missing")


# In[23]:


# gs_occ_df = pd.concat([gs_df, occ_df], axis=1) 
# gs_occ_df = gs_occ_df.fillna("missing")


# In[33]:


gs_occ_df


# In[34]:


# gs_occ_df[gs_occ_df.new_invoice_total != "missing"]


# ### for loop to get mileage true-ups

# In[38]:


for i in gs_occ_df.iterrows():
    num_1 = (i[1][2])
    num_2 = (i[1][1])
    try:
        answer = (float(num_1)-float(num_2))/1.5
        if answer > 10 or answer < -10:
            print("Needs Further Review (WT or FR Override)")
        else:
            print(answer)
    except:
        print("Missing From Billing Portal")


# In[142]:


gs_occ_df["bill_df_1"].plot(kind="pie")


# In[ ]:




