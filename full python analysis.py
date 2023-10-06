#full python script

# In[2]:


import pandas as pd 
import numpy as np


# In[3]:


# data import
balance_data = pd.read_csv('balance_data.csv')
nsfr_haircut = pd.read_csv('nsfr_haircut.csv')


# In[4]:


# changing the type to float
pd.options.display.float_format = '{:,.2f}'.format


# In[5]:


balance_data.head()


# In[6]:


nsfr_haircut.head()


# In[7]:


def task_4(balance_data, nsfr_haircut):
    balance_data = balance_data.copy()
    nsfr_haircut = nsfr_haircut.copy()


# In[8]:


# merging the data
merged_data = pd.merge(balance_data, nsfr_haircut, how='inner', on=['NSFR_GROUP', 'BALANCE_GROUP', 'BALANCE_CATEGORY', 'BALANCE_SUB_CATEGORY', 'GAP'])


# In[9]:


merged_data.head()


# In[10]:


# calculating the NSFR ratio and dividing into groups

merged_data['product'] = merged_data['TOTAL_BALANCE_EUR'] * merged_data['NSFR_HAIRCUT']
RSF_sum = merged_data.query("NSFR_GROUP == 'RSF' | NSFR_GROUP == 'RSF_OBS'")['product'].sum()
ASF_sum = merged_data.query("NSFR_GROUP == 'ASF'")['product'].sum()
NSFR_dec = ASF_sum/RSF_sum


# In[11]:


# formating for NSFR ratio
print('\n4. Task solution')
print('\nCurrent NSFR is {:.2%}'.format(NSFR_dec))
print('NSFR is greater than 100%, the bank has enough available stable funding to meet the required stable funding\n')


# In[12]:


# pivot table for daily balance by balance groups and time gaps
column_order = ['<6m', '6 - 12m', '>12m'] #to order the pivot columns
balance_by_gap = merged_data.pivot_table(index=['NSFR_GROUP', 'BALANCE_GROUP'],
                                         columns='GAP',
                                         values='TOTAL_BALANCE_EUR',
                                         aggfunc='sum',
                                         fill_value=0)
balance_by_gap1 = balance_by_gap.reindex(column_order, axis=1)


# In[13]:


# weighted average NSFR haircuts by balance groups
weighted_haircuts = merged_data.pivot_table(index=['NSFR_GROUP', 'BALANCE_GROUP'],
                                            values='NSFR_HAIRCUT',
                                            # using numpy to aggregate with weighted average
                                            aggfunc=lambda rows: np.average(rows, weights=merged_data.loc[rows.index, 'TOTAL_BALANCE_EUR']))


# In[74]:


print('\nDaily balance by balance groups and time gaps:')
display(balance_by_gap1)


# In[15]:


print('\nWeighted NSFR haircuts by balance groups:')
display(weighted_haircuts)


# In[ ]:




