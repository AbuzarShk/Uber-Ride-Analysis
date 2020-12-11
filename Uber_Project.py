#!/usr/bin/env python
# coding: utf-8

# In[104]:



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[73]:


uber = pd.read_csv("D:\\Uber-Ride-Analysis\\uber-raw-data-apr14.csv")


# In[74]:


uber.head()


# In[75]:


uber.info()


# In[76]:


def num_missing(x):
    return sum(x.isnull())
print('Number of Missing Columns or a null value:')
print(uber.apply(num_missing, axis=0))


# In[77]:


uber.isna().sum()


# In[106]:


uber['Date/Time'] = pd.to_datetime(uber['Date/Time'], format="%m/%d/%Y %H:%M:%S")
uber['DayofWeekNum'] = uber['Date/Time'].dt.dayofweek
uber['Weekday'] = uber['Date/Time'].dt.day_name()
uber['DayNum'] = uber['Date/Time'].dt.day
uber['HourofDay'] = uber['Date/Time'].dt.hour


# In[107]:


uber.head()


# In[108]:


uber.shape


# In[109]:


uber['Base'].unique()


# In[110]:


sns.catplot(x='Base', data=uber, kind='count')


# In[111]:


uber_week_data = uber.pivot_table(index=['DayofWeekNum','Weekday'], values='Base' ,aggfunc='count')
uber_week_data


# In[112]:


uber_week_data.plot(kind='bar',figsize=(8,6))


# In[118]:


uber_hourly_data = uber.pivot_table(index=['HourofDay'], values='Base' ,aggfunc='count')
uber_hourly_data.plot(kind='line',figsize=(10,5),title='Hour Journeys')


# In[120]:


uber_hourly_data = uber.pivot_table(index=['DayNum'], values='Base' ,aggfunc='count')
uber_hourly_data.plot(kind='bar',figsize=(10,5),title='Journeys by DayNum')


# In[124]:


def count_rows(rows):
    return len(rows)

by_date = uber.groupby('DayNum').apply(count_rows)
by_date


# In[131]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[143]:


uber_hourly_data = uber.pivot_table(index=['HourofDay'], values='Base' ,aggfunc='count')
uber_hourly_data.plot(kind='hist',title='Hour of Day')


# In[160]:


uber_hourly_data = uber.pivot_table(index=['HourofDay'], values='Base' ,aggfunc='count')
uber_hourly_data.plot(kind='hist',figsize=(10,5),title='Hour Journeys')


# In[166]:


count_rows(uber)
by_hour_weekday = uber.groupby('HourofDay DayofWeekNum'.split()).apply(count_rows).unstack()
by_hour_weekday


# In[167]:


plt.figure(figsize=(15,10))
sns.heatmap(by_hour_weekday)

