#!/usr/bin/env python
# coding: utf-8

# #                  
#  A1: Analytics Report
# **********************************************************************************************************************
#                                             February 2023
#                                           Priscilla Chacur
#                                  Computational Data Analytics with Python
#                                      Hult International Business School
# **********************************************************************************************************************

# # Problem
# 
# - _Who we are: European sports clothes company_
# 
# - _Goal: Expand internationally_
# 
# __Question: Where should we expand to and why?__
# 

# ## Problem 1: Economic

# ### Problem statement
# 
# International market chosen has to be positioned in the world with a strong economic view. The economic viewpoint provides the overall strength of the nation per person, but its also important to look into the potential of market growth.
# 
# When thinking about expanding, ensuring that the economic activity of a country is high and that the nation is growing is crucial since when businesses thinks about expanding its a long term plan.

# ### Understanding
# In order to approach this problem, GDP (per capita) and net migration are good measures that will determine the economic position of the country.
# 
# __Variables Used__
# 
# _1. Net migration:_
# 
# - The net migration is measured in percentage. It is an indicator of the number of people that are moving into the country compared to moving out. This is important because if a significant number people are leaving the country, the market opportunity for business is decreasing in the long run. 
# 
# - If the net migration is below the 25% quantile if means that its part of 1/4 of the countries with highest number of people leaving the country. For that reason, if it's below that threshold, it is not interesting to open business there.
# 
# _2. GDP ($ per capita):_
# 
# - The GDP stands for Gross Domestic Product (USD $ per capita). It is a measure of how much each person in the country provides values, it is used as an indicator for economic growth.
# 
# - If the countries falls below the median (50% quantile) in comparison to the rest of the world, it is considered an unattractive economically speaking for business expansion. 
# 

# ## Problem 2: Quality of Life

# ### Problem statement 2
# 
# In order to expand internationally, it's important to take info consideration the quality of life of the population. This is important because we are a sport clothing company and we need to ensure that the country is affordable and that the population has capital to invest in non- essential goods like our market. Furthermore, its important to have a country where people have easy access to cities and ability to move around to get to where they want to go, especially as international companies like us typically expands to other large cities.
# 
# Ensuring that the country chosen has a high quality of life is making sure that the population becomes a real market opportunity for the business as they will have the chance to have access and purchasing the goods.

# ### Understanding 2
# 
# In order to approach this problem Local Purchasing Power, Affordability Index and Accessbilities to cities are indicators that determine the quality of life of the country.
# 
# __Variables Used__
# 
# _1. Local Purchasing Power Index:_
# 
# - The Local Purchasing Power Index is a measure of how much the population can buy goods and services locally in comparision with the average local wage. This is important because it's a tools can be used to compare the local currency with the other currencies and how much people can buy with that value.
# 
# - Since this variable can be used as a comparison with other countries' currency, the mean becomes a useful measure, and therefore if the country falls below the worldwide mean, it's not strategic to expand there as the relative purchasing power is low and sport clothing is not considered an essential item so will not be priority for the population.
# 
# _2. Affordability Index:_
# 
# - The Affordability index is used as a measure of the individual's  average person's capacity to buy things. It can also be a good indicator of the cost of living in the country.
# 
# - If the countries falls below 1/4 (25% quantile) it demonstrates that the affordability index is low and therefore the country is too expensive compared to the average wage. Similarly to the Local Purchasing Power Index, if the country is too expensive, the population will prioritize costs related to essential things like housing and food and not sports clothing, and therefore would not be strategic to expand there.
# 
# 
# _3. Accessibilities to Cities:_
# 
# - Accessibilities to cities provides a measure of how easy it is for people to transport themselves throughout the country to the cities (regardless of the method of transportation). This is important because international companies move into larger cities and with a higher access, it allows people from different regions in that country to access the larger cities and become a market opportunity.
# 
# - It's important to sort the accessibilities to cities value in order from larger to smaller. This gives the opportunity of the market to see not only the larger city market but also other regions.

# ## Problem 3: Market Size

# ### Problem statement 3
# 
# When expanding internationally, the market size is extremelly important to understand the market size and therefore the business opportunity. Furthemore, we are a sports clothing company, and therefore the higher the median age, its a relationship with quality of life. 
# 
# If the population in general is healthy, they tend to practice more exercise, and therefore key market opportunity for business. Furthermore, ideally the world share should be siginificant enough to contribute for the brand awareness and recognition of the European brand.

# ### Understanding 3
# 
# In order to approach this problem Median Age and Population World Share (%) are indicators that determine the market size.
# 
# __Variables Used__
# 
# _1. Median Age:_
# 
# - The median age is an indicator of the population age distribution. This measure relates to high life expectancy and that means that the country likely has a high quality or that the population values a healthy lifestyle. A healthy population has the relationship with the practice of exercises and therefore a key market opportunity for the business.
# 
# - The highest the median age, the higher the life expectancy of the country. Filtering the countries in the lower half of the quantile provides the countries that tend to value exercise more.
# 
# _2. World Share (%):_
# 
# - The population world share (%) is a variable for the how much of the world population is concentrated in a certain country. This is important because countries with an insignificant population percentage is unattractive for business because of, both, business market opportunity, and brand recognition in the area.
# 
# - If the countries falls below 3/4 (75% quantile) it demonstrates that the world share is low and therefore would not be interesting to expand to.

# # Results

# ### Problem 1: Economic (Net Migration and GDP ($ per capita))
# 

# When observing the economic perspective, the difference by continent doesn't seem that much but because its averaged it out with all countries by continent. However, when looking at individual countries, there are major countries that a positive net migration meaning the population has a tendency to grow in the upcoming years due to the population movement. Furthermore, selecting a country with a strong GDP per capita is usually, but not necessarily,  related to a developed country and a country from a high income group. Economic strong nations are usually known, overall, to be better options to expand to due to their overall infrastructure.

# #### Net Migration by Continent

# ![Screenshot 2023-02-21 at 8.51.51 PM.png](attachment:60bf24a8-ce7d-422a-a3ef-244edd81c98f.png)
# 

# ### Problem 2: Quality of Life (Local Purchasing Power, Affordability Index & Accessibility to Cities)

# As a clothing company, we position ourselves as a non - essential business, and for that reason by filtering the countries with high purchasing power and affordability index, we guarantee that there is a significant part of the population that will spend money on the sports clothes. 
# 
# While looking at the overall population is important, it's not the main measure, because many countries, such as India, has a significant high population but main economic activities are only in a few cities. Countries like Canada, that while the population is not as high compared to other countries, the demographic of the countries and the high level cities infrastructure is located in a few cities where the population densitiy is concentrated. Therefore the accessibility to the cities for the population is one of the highest.
# 

# #### Local Purchasing Power Index Map

# ![Screenshot 2023-02-21 at 10.02.46 PM.png](attachment:a9536734-5d7b-49c7-b459-84c8c28c9de2.png)
# 

# ### Problem 3: Market Size (Median Age & World Share)

# Positioning ourselves to focus on countries that has a relatively a healthy lifestyle has a higher chance of becoming customers as they will be more focusing on being active and going to the gym, which ultimately is our targetted market. This is why countries with high median age means that the life expectancy is higher and therefore, it also means that the country has a culture that values a healthier lifestyle more.
# 
# While it might be easier to go for population as mentioned previously, the percentage of the world share plays a significant role not only for brand recognition, but also for a higher market opportunity. A combination of higher net migration and world share means that it contributes for an opportunity to select a growing potential market.

# #### Median Age by Continent

# ![Screenshot 2023-02-21 at 10.11.21 PM.png](attachment:ef83c5bc-84f3-4bd1-9234-ccc503ecf996.png)

# ### Conclusion
# 

# A combination of economic factors, market size and quality of life describes a perfect market potential for international expansion. This covers not only population behavior (healthy lifestyle with median age), but also the quality of life the country offers to their population (included in affordability index and local purchasing power). However, opening a business overseas needs to be looked at long term strategies including the potential for market growth with net migration, as well as having a well established economy with a high GDP per capita.
# 
# For that reason, the country that we should be expanding internationally to is Canada.

# ![Screenshot 2023-02-21 at 10.15.57 PM.png](attachment:eda9177c-b165-4f79-9e60-def7f0862f69.png)
# 
# _Source: https://www.bbc.com/news/world-us-canada-16841111 _

# # Assumptions

# __Assumptions__
# 
# 1. Countries with null values/missing values in more than 9 of the selected variables has been removed due to the lack of information for analysis.
# 2. The sports clothing company is in all of Europe, with a solid brand recognization in the region, and wanting to expand internationally already removes a total of 36 European countries from the analysis. 
#     - These countries are:  Albania, Austria, Belarus, Belgium, Bulgaria, Croatia, Curaçao, Cyprus, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Moldova, Montenegro, Netherlands, Norway, Poland, Portugal, Russia, Slovakia, Slovenia, Spain, Sweden, Switzerland, United Kingdom, Ukraine.
# 3. The age structure with the population between  15- 64 years old is equally distributed with urban population of the country 
# 4. The European sport clothing company does not only include sport specific clothes, but also any kind of activewear and it includes options for both woman and men
# 5. The three main categories (market size, quality of life and market size) and the variables chosen within them are the most important factors when expanding an sports clothing company in a new market
# 6. Canada is a strong market not only for exercises in general that improve sales for activewear but is also a seasonal sports country that contributes to the brand establishment.

# # Limitations

# __Limitations__
# 
# 1. The analysis is with data from 2020 and therefore it's assumed that the data remained the same
# 2. This analysis does not provide qualitative analysis, for instance it does not take into consideration cultural differences
# 3. Canada is a market with local activewear competitors already, and the current local market analysis for strategic penentration is not taken into consideration.
# 4. This analysis does not take historic data from the company in question (European sports clothes) which could be a factor for determining amount to be invested or partnerships for example
# 5. The analysis is taken into consideration only a few variables, and when prioritizing other variables (both, in the databases available and outside data) the result can differ.

# # Data

# ## Importing Libraries and Setting up the files

# In[1]:


#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#Specifying file name and reading the file to import into Python
#Using this file for Local Purchasing Power data
cost_of_living_2020 = pd.read_csv('World Bank/2020-cost-of-living/cost of living 2020.csv')

#Using the file to get the age group structure for all countries  -- target market
#This file provides me with the percentage of the population in between the ages of 15- 64 years old
#Which is the audience
countries_age_structure = pd.read_csv('World Bank/countries-dataset-2020/coutries age structure.csv')

#using the file to get the crime index/ safety index for all countries
#Using the file to get the safety index for each country- used to explore data
crime_index_countries_2020 = pd.read_csv('World Bank/countries-dataset-2020/crime index by countries 2020.csv')

#using the file to get the properties price index information (including rent) for all countries
#Used this file to get the affordability index for each country (one of the main chosen variables)
properties_price_countries_2020 = pd.read_csv('World Bank/countries-dataset-2020/Properties price index by countries 2020.csv')

#using the file for information for all countries and continents
#Used to get country name and country code
countries_and_continents = pd.read_csv('World Bank/world-countries-and-continents-details/countries and continents.csv')

#using the file to get the information for the population of each country
#Used this file to get data on Population (2020), Median Age, Urban Pop %, World Share %
population_countries_2020 = pd.read_csv('World Bank/population-by-country-2020/population_by_country_2020.csv')

#using the file to get the information of country regions
#Used the file to get info on CountryCode, Short name, Region,Income Group
country_details = pd.read_csv('World Bank/world-development-indicators/Country.csv')

#using the file to get information of the contries and continents of the world
#Used this file to get info on country name, Net Migration, Accessibilities to cities, Continent,
#Development Status and Human Development Index
countries_continents_world = pd.read_csv('World Bank/Countries_and_continents_of_the_world.csv')


#Ensuring all data can be visible for EDA
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)


# In[ ]:





# ## Merging datasets

# In[2]:


##Getting the details of each country together -- using country name and code to merge the datasets

#Understanding the countries_and_continents dataframe
countries_and_continents.head()

#Selecting only the desired info from that dataset
countries_and_continents[['name',"ISO3166-1-Alpha-3", "Continent"]]

#Finding out if there are any null values
countries_and_continents[['name',"ISO3166-1-Alpha-3", "Continent"]].isna().sum()

#list of desired columns
selec_columns_w_null_countries = countries_and_continents[['name',"ISO3166-1-Alpha-3", "Continent"]]

#Rows with the null values and drop the first columns which are NaN country names
null_in_selected = selec_columns_w_null_countries.isna()
countries_and_continents[['name',"ISO3166-1-Alpha-3", "Continent"]][null_in_selected.any(axis=1)]

#new table with name, code, and continent-- dropped first 2 columns with no country name
selec_columns_table = countries_and_continents[['name',"ISO3166-1-Alpha-3", "Continent"]].drop([0,1])

#Another dataset to cross reference country names and codes
country_details[['CountryCode','ShortName','Region','IncomeGroup']]

#merge country_details and countries_and_continents through CountryCode
merged_country_details = pd.merge(selec_columns_table, country_details, left_on='ISO3166-1-Alpha-3', right_on='CountryCode', how='inner').drop_duplicates()
country_details_table = merged_country_details[["name",'CountryCode', "Continent",'Region','IncomeGroup']]

#renaming column names
country_details_table = country_details_table.rename(columns
                                                     ={"name": "Country Name", 'CountryCode': 'Code', 'IncomeGroup': 'Income Group'})

#Selecting only desired columns
filtered_countries_continents_world = countries_continents_world[["Country Name","Continent","Development Status","Country Code","Region",
                            "Net migration","accessibility_to_cities","Human Asset Index", "Human Development Index",
                           "GDP ($ per capita)","GNI per capita"]]

#Merging another dataset
merged_countries_continents = pd.merge(country_details_table, filtered_countries_continents_world, left_on='Code', right_on='Country Code', how='inner')

#Dropping repeated countries info
columns_to_drop = ['Code','Country Name_x','Region_y']
merged_countries_continents = merged_countries_continents.drop(columns_to_drop, axis=1)

#After merging datasets, there are 2 continents columns [['Continent_x','Continent_y']].info()
    #Continent_x  182 non-null   
    #Continent_y  215 non-null 
#Therefore, dropping the column with more null values
merged_countries_continents.drop('Continent_x', axis=1, inplace=True)
merged_countries_continents.head()


# In[3]:


#Merging merged_countries_continents dataset for world bank info:
    #- safety index
    #- price to income ratio
    #- Affordability index
    #- Population
    #- Yearly Change
    #- Migrants
    #- Median Age
    #- Urban pop%
    #- World Share
    
livinginfo_country = pd.merge(merged_countries_continents,crime_index_countries_2020, left_on='Country Name_y', right_on='Country', how='outer').drop_duplicates() 
livinginfo2_country = pd.merge(livinginfo_country,population_countries_2020, left_on='Country Name_y', right_on='Country (or dependency)', how='outer').drop_duplicates()
livinginfo3_country = pd.merge(livinginfo2_country,properties_price_countries_2020, left_on='Country Name_y', right_on='Country', how='outer').drop_duplicates()
livinginfo4_country = pd.merge(livinginfo3_country,countries_age_structure, left_on='Country Name_y', right_on='Country', how='outer').drop_duplicates()
livinginfo5_country = pd.merge(livinginfo4_country,cost_of_living_2020, left_on='Country Name_y', right_on='Country', how='outer').drop_duplicates()

#Complete dataset with all variables
livinginfo5_country.info ()


# ## Choosing variables for main dataset

# In[4]:


#Selecting the variables to be used
df = livinginfo5_country[['Country (or dependency)','Region_x', 'Income Group',
                         'Continent_y','Development Status','Country Code',
                         'Net migration','accessibility_to_cities',
                         'Human Development Index','GDP ($ per capita)',
                         'Safety Index','Population (2020)',
                         'Med. Age','Urban Pop %',
                         'World Share',
                         'Affordability Index','Age 15 to 64 Years',
                         'Local Purchasing Power Index']]

#Renaming columns
df.rename(columns = {'Country (or dependency)':'Country','Region_x':'Region', 
                     'Continent_y':'Continent', 'accessibility_to_cities':'Accessibilities to Cities', 
                     'Med. Age': 'Median Age'}, inplace = True)

#Understanding datatypes
df.info()


# ### Changing Datatypes

# In[5]:


#Columns with datatype as objects to be changed for float
df[['Net migration','Median Age','Urban Pop %','World Share','Age 15 to 64 Years']]


# In[6]:


## Cleaning the data

# split the "Urban Pop %" column into two columns
df['Urban Pop %'] = df['Urban Pop %'].str.rstrip('%')

# split the "World Share" column into two columns
df['World Share'] = df['World Share'].str.rstrip('%')

# split the "Age 15 to 64 Years" column into two columns
df['Age 15 to 64 Years'] = df['Age 15 to 64 Years'].str.rstrip('%')

#Changing commas to period
df['Net migration'] = df['Net migration'].str.replace(',', '.')


# In[4]:


# Removing non numeric values and changing datatypes


df['Net migration']= df['Net migration'].astype(float)
df[['World Share','Age 15 to 64 Years']]= df[['World Share','Age 15 to 64 Years']].astype(float)

#Changing the string values to null and then converting the datatype

#Median Age
df['Median Age'] = df['Median Age'].replace('N.A.',np.nan)
df['Median Age'] = df['Median Age'].replace('',np.nan)
df['Median Age'] = df['Median Age'].astype(float)

#Urban Pop %
df['Urban Pop %'] = df['Urban Pop %'].replace('N.A.',np.nan)
df['Urban Pop %'] = df['Urban Pop %'].astype(float)


# In[8]:


#Double checking to ensure datatype has been changed
df[['Net migration','Median Age','Urban Pop %','World Share','Age 15 to 64 Years']]

df.info()


# ## Visualizing the Countries Distribution

# In[9]:


# create pivot table to group by continent and development status
pivot_data = pd.pivot_table(df, index=['Continent', 'Development Status'], values='Country', aggfunc='count')

# unstack the pivot table to create separate columns for each development status
pivot_data = pivot_data.unstack()

# plot the data as a stacked bar chart
ax = pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6))

# set the axis labels and chart title
ax.set_xlabel('Continent')
ax.set_ylabel('Number of Countries')
ax.set_title('Countries per Development Status by Continent Before Filtering')
plt.show()


# In[10]:


#Understanding the Development status by each continent

dev_stat_countries = df.groupby(['Continent','Development Status'])['Country'].nunique()

pd.DataFrame(dev_stat_countries)


# ### Removing Null Values

# In[11]:


#Finding which data has null values as country names

null_country_name = df['Country'].isnull()
null_country_name


# In[12]:


#Info with countries not linked to it is being removed

#dropping those rows country as null values
df = df.drop(df[null_country_name].index)

df.info()


# In[13]:


#Exploring data with significant null values
df.tail(50)

#finding which columns have null values and what they are
null_counts = df.isnull().sum(axis=1)
null_filter = null_counts > 9

#Seeing which rows have more than 9 features/info missing
df[null_filter].head()


# In[14]:


#Mostly null values (so removing them)

#dropping those rows with null values
df = df.drop(df[null_filter].index)

df.info()


# ## Creating variable for Target Market

# In[15]:


df[['Population (2020)','Urban Pop %','Age 15 to 64 Years']].head()


# In[16]:


#Creating a new variable that focused on the target market

#Target market = Urban pop between 15- 64 years old
#Converting Urban pop and age 15-64 years to % and then deciding on target market
df['Target Market (millions)'] = ((df['Population (2020)'] * (df['Urban Pop %']/100) * (df['Age 15 to 64 Years']/100))/1000000).round(2)

df[['Country','Target Market (millions)']].sort_values(by='Target Market (millions)', ascending = False).head()


# In[17]:


#Dropping columns that are no longer needed: Population, Urban Pop, Age Structure between 15-64

df = df.drop(df[['Urban Pop %','Age 15 to 64 Years']], axis =1)

df.head()


# In[18]:


#Dropping countries with no population/target market information

df = df.dropna(subset=['Target Market (millions)'])
df.info()


# ## EDA

# In[19]:


df.describe().round(2)


# ### Correlation between variables

# In[20]:


#Understanding the correlation between the variables (creating matrix)

#setting correlation variable
data_corr = df.corr()

#creating the matrix
corr_matrix = plt.figure(figsize=(20, 15))
plt.matshow(data_corr, fignum=corr_matrix.number, cmap = 'coolwarm')
plt.xticks(range(data_corr.shape[1]),
           data_corr.columns, fontsize=14, rotation=45)
plt.yticks(range(data_corr.shape[1]), 
           data_corr.columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16);


# ### Understanding Development Status

# In[21]:


# create pivot table to group by continent and development status
pivot_data = pd.pivot_table(df, index=['Continent', 'Development Status'], values='Country', aggfunc='count')

# unstack the pivot table to create separate columns for each development status
pivot_data = pivot_data.unstack()

# plot the data as a stacked bar chart
ax = pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6))

# set the axis labels and chart title
ax.set_xlabel('Continent')
ax.set_ylabel('Number of Countries')
ax.set_title('Countries per Development Status by Continent After the Filtrer')
plt.show()

#All underdeveloped countries have been dropped due to missing information


# ### Removing Current Market: Europe

# In[22]:


#Getting all countries part of the European continent (current organization market)

european_countries = df[df['Continent'] == 'Europe']['Country']

#There are 35 European countries
european_countries.count()


# In[23]:


#Dropping European countries since the company wants to expand outside of Europe

df = df.drop(df[df['Country'].isin(european_countries)].index)

df.info()


# ### Exploring market - Net Migration (Economic)

# In[24]:


#For market opportunity, the market has to have a relative growing population
#compared to the rest of the world meaning the market is growing (people moving to the country and not from)


df['Net migration'].describe().round(2)


# In[25]:


#Finding net migration info by continent
net_migration_continent = df.groupby('Continent')['Net migration'].describe().round(2)


net_migration_continent.head()


# In[26]:


#Getting Net migration
netmigration_sorted = df.sort_values('Net migration', ascending=False)

#Selecting 1 country per continent
top_1_continent = netmigration_sorted.groupby('Continent').head(1)

#Group top 1 by continent + descriptive stats for Net migration info
net_migration_continent = top_1_continent.groupby('Continent')['Net migration'].describe().round(2)

#Only for top country
net_migration_continent['mean']


# ### Exploring Market- Economically - GDP ($ per capita) (Economic)

# In[27]:


#In order to consider for business opportunity, ideally the market should be positioned strongly in the world
#economically, for that reason, its important to look at GDP ($ per capita)

df['GDP ($ per capita)'].describe().round(2)


# In[28]:


#Finding out what is the high end outlier for GDP
max_gdp = df[df['GDP ($ per capita)'] == 37800.00]["Country"]
max_gdp
#Max GDP is USA


# ### Exploring Market - Local Purcharsing Power (Quality of Life)

# In[29]:


#To understand the market, its important to see how much the population can buy considering their local wage

df['Local Purchasing Power Index'].describe().round(2)


# In[30]:


#Finding net migration info by continent

lpp_index_continent = df.groupby('Continent')['Local Purchasing Power Index'].describe().round(2)
lpp_index_continent.head()


# ### Exploring Market - Affortability Index (Quality of Life)

# In[31]:


#To understand the market, its important to see how affordable the country is for people
#This determine how much the population is able to spend on living costs/clothes and others

df['Affordability Index'].describe().round(2)


# ### Exploring Market - Median Age (Market Size)
# 

# In[32]:


#As a clothing sports company, quality of life is an important factor
#Therefore having a higher quality of life is usually related to having a high median age of population
#meaning the population has a tendency to live longer

df['Median Age'].describe().round(2)


# In[33]:


#Finding Median age by continent
median_age_continent = df.groupby('Continent')['Median Age'].describe().round(2)


median_age_continent.head()


# ## Exploring Data - World Map

# In[34]:


df.head()


# ### Visualizing the Map

# #### Safety Index

# In[35]:


import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame

#simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the world_map GeoDataFrame with the world GeoDataFrame
merged = pd.merge(world, df, left_on = 'iso_a3',right_on = 'Country Code', how = 'outer')

#Safety Index
merged['Safety Index'].fillna(0, inplace=True)

#Formating the map
fig,ax = plt.subplots(figsize = (15,8))
cmap = plt.cm.get_cmap("Blues").copy()
cmap.set_over(alpha = 0)
merged.plot(column = 'Safety Index', cmap = cmap, legend = True, ax=ax, edgecolor='black')
plt.show()

#safety index is just another variable that contributes to the overall quality of life


# #### Target Market (millions)

# In[36]:


#simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the world_map GeoDataFrame with the world GeoDataFrame
merged = pd.merge(world, df, left_on = 'iso_a3',right_on = 'Country Code', how = 'outer')

#Safety Index
merged['Target Market (millions)'].fillna(0, inplace=True)

#Formating the map
fig,ax = plt.subplots(figsize = (15,8))
cmap = plt.cm.get_cmap("YlGnBu").copy()
cmap.set_over(alpha = 0)
merged.plot(column = 'Target Market (millions)', cmap = cmap, legend = True, ax=ax, edgecolor='black')
plt.show()

#Target Market in millions (Country Pop * Urban Pop * Age Structure between 15-64 years old)


# #### Local Purchasing Power Index

# In[37]:


#Local Purchasing Power Index

merged = pd.merge(world, df, left_on = 'iso_a3',right_on = 'Country Code', how = 'outer')

merged['Local Purchasing Power Index'].fillna(0, inplace=True)

#Formating the map
fig,ax = plt.subplots(figsize = (15,8))
cmap = plt.cm.get_cmap("Reds").copy()
cmap.set_over(alpha = 0)
merged.plot(column = 'Local Purchasing Power Index', cmap = cmap, legend = True, ax=ax, edgecolor='black')
plt.show()


# ### Exploring Market - World Share (Market Size) 

# In[38]:


#There should have a significant world share %
#This contributes for the brand awareness and recognition,

df['World Share'].describe().round(2)


# ### Exploring Market - Accessibility to Cities (Quality of Life)

# In[39]:


df.loc[:, ["Country", "Accessibilities to Cities"]].sort_values("Accessibilities to Cities", ascending=False).head()


# In[40]:


#Showing Canada before filtering 

merged = pd.merge(world, df, left_on = 'iso_a3',right_on = 'Country Code', how = 'outer')

merged['Accessibilities to Cities'].fillna(0, inplace=True)

#Formating the map
fig,ax = plt.subplots(figsize = (15,8))
cmap = plt.cm.get_cmap("Reds").copy()
cmap.set_over(alpha = 0)
merged.plot(column = 'Accessibilities to Cities', cmap = cmap, legend = True, ax=ax, edgecolor='black')
plt.show()


# # Problem Solving

# ## Net Migration (Problem 1: Economic)

# In[41]:


#Boxplot graph to visualize the net migration by continent

#Setting the box to plot the graph
fig, ax = plt.subplots(figsize=(11, 5))

#This helps understand and compare each continent and outliers
sns.boxplot(y='Continent', x='Net migration', data=df, orient='h')

#Labeling graphs
plt.title('Net migration by Continent')
plt.xlabel('Net migration')
plt.ylabel('Continent')
plt.show()


#Bottom 25% of overall seems to remove the bottom outliers as well as lower end of the migration spectrum


# In[42]:


#Finding the countries that are below the 25% quantile

low_net_migration = df[df['Net migration'] < -1.13]

low_net_migration.info()


# In[43]:


#Dropping low migration markets
df = df.drop(low_net_migration.index)

#Resetting the index
df = df.reset_index()

df.info()


# ## GDP ($ per capita) - (Problem 1: Economic)

# In[44]:


# Plotting a histogram of the GDP per capita values
plt.hist(df['GDP ($ per capita)'], facecolor='pink', edgecolor='black', bins=50)

#Histogram formatting
plt.xlabel('GDP ($ per capita)')
plt.ylabel('Frequency')
plt.title('Distribution of GDP per capita')

plt.show()


# In[45]:


#Removing lower GDP ($ per capita) countries based on the 50% quantile (2900.00)
#Not using mean because of the USA having a high end outlier that's pushing the mean up

low_gdp_countries = df[df['GDP ($ per capita)'] < 2900]

low_gdp_countries.info()


# In[46]:


#Dropping low GDP economic markets
df = df.drop(low_gdp_countries.index)

df.info()


# In[47]:


#Resetting the index
df = df.reset_index(drop=True)

df.info()


# ## Local Purchasing Power (Problem 2: Quality of Life)

# In[48]:


#Boxplot graph for different local purchasing power index
#x-axis shows the different continents (it's easier to visualize based on each continent to compare)

#This helps understand and compare each continent and outliers
sns.boxplot(x='Continent', y='Local Purchasing Power Index', data=df)

#Formatting the graph
plt.title('Local Purchasing Power Index by Continent')
plt.xlabel('Continent')
plt.ylabel('Local Purchasing Power Index')
plt.show()


#seems like there are a few countries with LPP Index below 20


# In[49]:


#Removing low local purchasing power based on the overall mean (60.40)
#With low purchasing power, sports clothing is not basic need and therefore low opportunity for market exploration

low_lpp_index = df[df['Local Purchasing Power Index'] < 60.40]

low_lpp_index.info()


# In[50]:


#Dropping lower Local purchasing power index countries
df = df.drop(low_lpp_index.index)

df.info()


# ## Affordability Index (Problem 2: Quality of Life)

# In[51]:


#Plot a histogram for the distribution of the affordability

plt.hist(df['Affordability Index'], facecolor='green', edgecolor='black', bins=40)

#Histogram editing
plt.xlabel('Fequency')
plt.ylabel('Affordability Index')
plt.title('Distribution of Affordability Index')

plt.show()


# In[52]:


#Removing lower affordability countries based on the 25% quantile (1.43)
#If the country is not affordable, people are not spending in sports clothes

low_affordability_index = df[df['Affordability Index'] < 1.43]

low_affordability_index.info()


# In[53]:


#Dropping low affordability index countries
df = df.drop(low_affordability_index.index)

df.info()


# In[54]:


#Reseting index
df = df.reset_index(drop=True)

df.info()


# ## Median Age (Problem 3: Market Size)

# In[55]:


# Plotting a histogram of the distribution of median age of the population
plt.hist(df['Median Age'], facecolor='purple', edgecolor='black', bins=10)

#Histogram formatting
plt.xlabel('Frequency')
plt.ylabel('Median Age')
plt.title('Distribution of Median Age')

plt.show()


# In[56]:


df.head(8)


# In[57]:


#Removing lower median age based on the 50% quantile (30.00)
#Very similar to the mean

low_median_age = df[df['Median Age'] < 30.00]

low_median_age.info()


# In[58]:


#Dropping low median age
df = df.drop(low_median_age.index)

df.info()


# ## World Share (Problem 3: Market Size) 
# 

# In[59]:


# Plotting a histogram for world share
plt.hist(df['World Share'], facecolor='Orange', edgecolor='black', bins=50)

#Histogram formatting
plt.xlabel('Frequency')
plt.ylabel('World Share')
plt.title('Distribution of World Share (%)')

plt.show()


# In[60]:


#Boxplot graph for world share (%)

#This helps understand and compare each continent and outliers
sns.boxplot(x='World Share', data=df)

#Formatting the graph
plt.title('World Share by Continent')
plt.ylabel('World Share')
plt.show()

#Concentration on the lower end --> Using 75% quantile (0.37)


# In[61]:


#Removing lower world share (%) based on the 75% quantile (0.37)
#Very similar to the mean

low_world_share = df[df['World Share'] < 0.37]

low_world_share.info()


# In[62]:


#Dropping low world share
df = df.drop(low_world_share.index)

df.info()


# ## Selected Country: Canada 

# In[63]:


#Accessibilities to Cities in Canada is significantly greater than the US
df.head().round(2)


# ## Accessibility to Cities (Problem 2: Quality of Life)

# Signifcantly higher Score in Accessibilites to City - Canada is the new choosen market

# In[64]:


#Showing Canada after filtering

merged = pd.merge(world, df, left_on = 'iso_a3',right_on = 'Country Code', how = 'outer')

merged['Accessibilities to Cities'].fillna(0, inplace=True)

#Formating the map
fig,ax = plt.subplots(figsize = (15,8))
cmap = plt.cm.get_cmap("Reds").copy()
cmap.set_over(alpha = 0)
merged.plot(column = 'Accessibilities to Cities', cmap = cmap, legend = True, ax=ax, edgecolor='black')
plt.show()


# # __We should expand to Canada!__
