#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd


# In[13]:


# importing data points - 06/05/23_vp
df = pd.read_csv(r'C:\Users\ASUS\Desktop\US_Accidents_Dec21_updated.csv')


# In[19]:


df.head(2)


# In[21]:


#importing entire databse
df


# In[22]:


#viewing entire columns of databse
df.columns


# In[23]:


#viewing the features of databse
len(df)


# In[25]:


#viewing all the columns swith their data types
   df.info()


# In[24]:


#viewing all the important numeric functions 
df.describe()


# In[27]:


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

newdf=df.select_dtypes(include=numerics)


# In[28]:


newdf
len(newdf.columns)


# In[48]:


#viewing missing percentages
missing_percentages=df.isna().sum().sort_values(ascending=False)/len(df)
missing_percentages


# In[54]:


type(missing_percentages)


# In[55]:


missing_percentages


# In[59]:


#importing matplotlib as library
from matplotlib import pyplot as plt


# In[196]:


#plotting a graph where missing percentage is not equal to zero
missing_percentages[missing_percentages != 0].plot(kind='barh') 
"""plt.xlabel('test')
plt.ylabel('')
plt.ta"""


# In[68]:


df.columns


# In[69]:


comment =  """columns we'll analyze
    1.city
    2.startr time
    3.start lat,start lng
    4.temperature
    5.weather condition
    """
    


# # CITIES

# In[79]:


#defining cities based on uniqueness and finding their total number
cities=df.City.unique()
len(cities)


# In[84]:


#defining cities by accidents
cities_by_accident=df.City.value_counts()
cities_by_accident


# In[89]:


cities_by_accident.plot(kind='barh')
plt.show()


# In[90]:


cities_by_accident[:20].plot(kind='barh')
plt.show()


# In[86]:


#finding out why new york doesnt show in the list for accidents when it has the highest population in usa
'New York' in df.State
#'new york' in df.State


# In[95]:


#importing seaborn library
import seaborn as sns
sns.set_style("darkgrid")


# In[98]:


#using distplot to show the different variables density in our plot
sns.distplot(cities_by_accident)


# In[102]:


#defining high accident cities and low accident cities using our previosuly created function "cities _by _accident"high_accident_cities=cities_by_accident[cities_by_accident>= 1000]
low_accident_cities=cities_by_accident[cities_by_accident<=1000]


# In[103]:


#no. of high accident cities
len(high_accident_cities)


# In[104]:


#percentage of high accident cities
len(high_accident_cities)/len(cities)


# # summary
# 
# no data for New York 
# 
# Less than 4% of cities have more than 1000 yearly accidents

# In[105]:


sns.distplot(high_accident_cities)


# In[107]:


sns.distplot(low_accident_cities)


# #USING LOG SCALE TO REDUCE THE EXPONENTIAL DUSTRIBUTION OF DATA
# sns.histplot(cities_by_accident,log_scale=True)

# In[117]:


cities_by_accident[cities_by_accident==1]


# over 800 cities have reported just 1 accident, we should probbaly investigate more
# 
# the number of accidents in cities decreases exponentially
# 

# # START TIME

# In[123]:


df.Start_Time


# In[124]:


df.Start_Time[0]


# In[127]:


#defining start time in a date time format
df.Start_Time=pd.to_datetime(df.Start_Time)


# In[128]:


df.Start_Time[0]


# In[130]:


#determining the starting point by hour
df.Start_Time.dt.hour


# In[140]:


sns.histplot(df.Start_Time.dt.hour,bins=24)


# a high % of accidents occur between 4-5pm. probably people in a hurry to go out for evening meetups or returning from work

# next highest % is between 7-8 am probably because of people leaving for woerk

# In[135]:


sns.distplot(df.Start_Time.dt.dayofweek,bins=7,kde=False,norm_hist=True)


# In[144]:


#defining sundays start time for accidents by using start time by days of the week
sundays_Start_Time=df.Start_Time[df.Start_Time.dt.dayofweek==6]
sundays_Start_Time


# In[146]:


sns.distplot(sundays_Start_Time.dt.hour,bins=245,kde=False,norm_hist=True)


# In[147]:


#defining mondays start time for accidents by using start time by days of the week
mondays_Start_Time=df.Start_Time[df.Start_Time.dt.dayofweek==0]
mondays_Start_Time


# In[148]:


sns.distplot(mondays_Start_Time.dt.hour,bins=245,kde=False,norm_hist=True)


# on both sundays and mondays the peak occurs between 2-4pm

# In[152]:


#plotting based on accidenst by months
sns.distplot(df.Start_Time.dt.month,bins=12,kde=False,norm_hist=True)


# In[153]:


#defining accidenst for the year 2019 and plotting them on distplot
df_2019=df[df.Start_Time.dt.year==2019]
sns.distplot(df_2019.Start_Time.dt.month,bins=12,kde=False,norm_hist=True)


# In[154]:


#defining accidenst for the year 2018 and plotting them on distplot
df_2019=df[df.Start_Time.dt.year==2018]
sns.distplot(df_2019.Start_Time.dt.month,bins=12,kde=False,norm_hist=True)


# In[155]:


#defining accidenst for the year 2017 and plotting them on distplot
df_2019=df[df.Start_Time.dt.year==2017]
sns.distplot(df_2019.Start_Time.dt.month,bins=12,kde=False,norm_hist=True)


# In[156]:


#defining accidenst for the year 2016 and plotting them on distplot
df_2019=df[df.Start_Time.dt.year==2016]
sns.distplot(df_2019.Start_Time.dt.month,bins=12,kde=False,norm_hist=True)


# some data is probably missing for jan and feb for year 2016

# In[159]:


#USING PIE CHART TO DETERMINE THE SEVERITY OF THE ACCIDENTS I.E. HOW MUCH THEY IMPACTED THE TRAFFIC. ON THIS SCALE, THE HIGHEST IMPACT WAS "2" WHICH IS THE MOST FREQUENT SEVERITY
df.Severity.value_counts().plot(kind='pie')


# In[160]:


#finding the initial latitide during accidents
df.Start_Lat


# In[162]:


#finding the initial longitude during accidents
df.Start_Lng


# In[164]:


sns.scatterplot(x=df.Start_Lng, y=df.Start_Lat)


# In[167]:


sample_df=df.sample(int(0.1 * len(df)))


# In[168]:


#making a scatterplot for a sample siz e of 0.001 of the entire dataframe
sns.scatterplot(x=df.Start_Lng, y=df.Start_Lat, size=0.001)


# In[172]:


#importing folium to use maps for data visualization
import folium


# In[173]:


#creating marker values
lat,lon = df.Start_Lat[0],df.Start_Lng[0]
     
 lat,lon


# In[178]:


#creating a map for our desired latitude and longitude valueds, the marker determines the position where our latitude and longitude intersect and give us a specific location
map=folium.Map()
marker= folium.Marker ((lat, lon))
marker.add_to(map)
map
 


# In[179]:


#using iter items for repeated result of different values of the same defined column. once i ue index 1 the same function is repeated for subsequent indexes
for x in df[['Start_Lng']].sample(100).iteritems():
    print(x[1])


# In[180]:


list(df.Start_Lat)


# In[182]:


list(df.Start_Lng)


# In[186]:


#to create a list with longitude and latitude combined as pairs we use the zip function
list(zip (list(df.Start_Lat),list(df.Start_Lng)))


# In[188]:


from folium.plugins import HeatMap


# In[191]:


map=folium.Map()
HeatMap(zip(list(df.Start_Lat),list(df.Start_Lng))).add_to(map)
map


# In[194]:


sample_df=df.sample(int(0.001*len(df)))
lat_lon_pairs=list(zip(list(sample_df.Start_Lat),list(sample_df.Start_Lng)))


# In[195]:


#after determining sample sizes for long and lat pairs we make a heatmap
map=folium.Map()
HeatMap(lat_lon_pairs).add_to(map)
map


# SUMMARY OF THE DATABASE
# 
# .no data from new york
# 
# .the number of accidenst per city decreases exponentially
# 
# .less than 4% of cities have more than 1000 yearly accidents
# 
# .over 800 cities have reported just one accident 
# 
# for now we have analyzed these columns and aspects of our database but we can look into more columns for future EDA analysis for a much more detailed picture.
# 

# In[ ]:




