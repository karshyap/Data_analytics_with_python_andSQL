#Libraries
import numpy
import matplotlib
import os
import sys
import pandas as pd


#Lessons 1 and 2



#Python Basics and List Dictionary and Boolean
string_1 = 'Statistics is good'
print( (string_1)

#Working on Lists
cities = ['New_york', 'Chicago', 'Dallas', 'Houston','Los_Angeles']
print( (cities))
print( cities[:3])
print( cities[1:])
print( len(cities))

#Working on Dictionary
Percentage = {'Math':90,'Science':85,'Economics':80,'History':75,'English':90,'Geography':80}
print( Percentage['Math'])

print( Percentage)

Percentage['Science'] = 90
Percentage['Math'] = 80
print( Percentage)

sorted(Percentage)
print( Percentage)



#Dictionary Containing List
municipalities = {
    'New York City': [
        'Manhattan',
        'The Bronx',
        'Brooklyn',
        'Queens',
        'Staten Island'
    ],
    'Tokyo': [
        'Akihabara', 
        'Harajuku', 
        'Shimokitazawa']
        }
print( municipalities['New York City'])
print( municipalities['New York City'][1:3])

#Boolean Objects and Type
bool_obj = True
print( bool_obj)
print( type(bool_obj))





###Learning about keys
city_population = {
  'Tokyo': 13350000, # a key-value pair
  'Los Angeles': 18550000,
  'New York City': 8400000,
  'San Francisco': 1837442,
}
city_population.keys()
type(city_population.keys())

print( city_population.keys())


print( type(city_population.values()))

type(city_population.values())


municipalities = {
    'New York City': [
        'Manhattan',
        'The Bronx',
        'Brooklyn',
        'Queens',
        'Staten Island'
    ],
    'Tokyo': [
        'Akihabara', 
        'Harajuku', 
        'Shimokitazawa', 
        'Nakameguro', 
        'Shibuya']
        }
type(municipalities)
type(municipalities['Tokyo'])
type(municipalities['Tokyo'][0])


print( type(municipalities['Tokyo'])))
print( type(municipalities['Tokyo'][0])))

print( municipalities['Tokyo'][0]))
print( len(municipalities['Tokyo'][0])))




x = city_population.values()
print( numpy.mean(x)

print( numpy.max(x))
print( numpy.min(x))


# Python Notebook - Clone of Python Tutorial - Lessons 3, 4, 5, & 6

datasets[0].head(n=5)

#Working with Pandas and Dataframe in Python
datasets[0].head()

#Using Head we print the first 5 Lines of any DataFrame
print( type(datasets))




data = pd.DataFrame()
data = datasets[0]





#Fill NA value with Empty String
data = data.fillna('')
print( data['website_section'][1:10])


type(data['website_section'])

#Selecting the First 3 Row
print( data[:3])

print( data[2:3])

data.ix[1]


data['title'][:3]



#Converting in to List
x = []
x = data['user_agent'][0:5]
print( x)

type(x)

x = []
x = list(data['user_agent'][0:5])
type(x)


#Using value_counts()
print( data['title'].value_counts())





data = datasets[0]
print( type(data['title'].value_counts()))

data['title'].value_counts()[0]

data['title'].value_counts()[:20].plot()

data['title'].value_counts()[:20].plot(kind='bar')


data.head()


data['platform'].value_counts()[:20]
data['platform'].value_counts()[:20].plot(kind='bar')




data['title'] == 'Watsi | Fund medical treatments for people around the world'

selected_data = (data['title'] == 'Watsi | Fund medical treatments for people around the world')
print( len(data[selected_data])

#Selecting a Specific Title and print(ing the Referral Count in that(top 15)
data = datasets[0]
selected_data = (data['title'] == 'Watsi | Fund medical treatments for people around the world')
print( (type(selected_data)))
sel_data = data[selected_data]
print( (type(sel_data)))



print( (data['referrer'].str.contains('medical')))

print( (data['referrer'].str))


data = data.fillna('')
medical_referrer_index = data['referrer'].str.contains('medical')
print( medical_referrer_index)

medical_referrals = data[medical_referrer_index]
medical_referrals = data[medical_referrer_index]
print( (medical_referrals))

medical_fund_index = data['referrer'].str.contains('crowdfund')
fund_data = data[medical_fund_index]
print( fund_data)




#Lessons 3,4,5,6

datasets[0].head(n=5)

#Pandas
import pandas as pd
data = pd.DataFrame()
data = datasets[0]
data = data.fillna('')
data.head()

#Prinitng the Device and the Maximum used Device
print( data['platform'].value_counts())
print( data['platform'].value_counts()[0])

type(data['platform'].value_counts())

#Trying to print( the Collumn which has the Highest Number as the Platform Used(UnSucessfully!!)
type1,value = data['platform'].value_counts()[0]
print( type1)
print( value)


#Creating a new Collumn in the DataFrame
#Assigning it a value
data['new'] = 2
#Value would be reflected across all the rows
print( data[:3])

#Overwriting the 'new' collumn with a Different Value
#Voila! The Value is reflected in all the rows
data['new'] = 'over-written'
print( data[:3])

#Testing the in Operator
mobile = ['iPhone', 'Android', 'iPad', 'Opera Mini', 'IEMobile', 'BlackBerry']
for mob in mobile:
  print( mob)

print( 'iPad' in mobile)


#Checking with If and ElseIf
if 'iPad' in mobile:
  print( 'In Mobile Section')
else:
  print( 'Found No Where!!')

#Working with Function
def in_group(platform):
  if platform in mobile:
    print( "We found it!!")
  
in_group('iPad')

#Working with Data Frame using the User-Built Function
def filter_desktop_mobile(platform):
    if platform in mobile:
        return 'Mobile'
    elif platform == 'Desktop':
        return 'Desktop'
    else:
        return 'Not Known'

data = datasets[0]
data =  data.fillna('')
data['platform'].apply(filter_desktop_mobile)

# Python Notebook - Clone of Python Tutorial - Lessons 7 & 8

datasets[0].head(n=5)

data = datasets[0]
data = data.fillna('')
print( data.head())

import pandas as pd
import numpy as np

data = datasets[0]
data = data.fillna(np.nan)


data.head()

data.sample(4)


data.sort_values(by='arr_delay',ascending = False)[:10]

#Working with Lambda Function
data['delayed'] = data['arr_delay'].apply(lambda x: x > 0)
print( data['delayed'][:10])



print( data['unique_carrier'][:5])
print( data['delayed'][:5])

group_by_carrier = data.groupby(['unique_carrier','delayed'])
type(group_by_carrier)

import numpy as np
data = datasets[0]
data = data.fillna(np.nan)
data['delayed'] = data['arr_delay'].apply(lambda x: x > 0)
group_by_carrier = data.groupby(['unique_carrier','delayed'])

type(group_by_carrier)

group_by_carrier.head()

group_by_carrier.size()

import numpy as np
data = datasets[0]
data = data.fillna(np.nan)
data['delayed'] = data['arr_delay'].apply(lambda x: x > 0)
group_by_carrier = data.groupby(['unique_carrier','delayed'])
count_delays_by_carrier = group_by_carrier.size().unstack()
count_delays_by_carrier

#Plotting the Data to COmpare Visually
count_delays_by_carrier.plot(kind='barh', stacked=True, figsize=[16,6], colormap='winter')

#Working on Pivot table

import numpy as np
data = datasets[0]
data = data.fillna(np.nan)
data['delayed'] = data['arr_delay'].apply(lambda x: x > 0)
group_by_carrier = data.groupby(['unique_carrier','delayed'])
count_delays_by_carrier = group_by_carrier.size().unstack()
flights_by_carrier = data.pivot_table(index='flight_date', columns='unique_carrier', values='flight_num', aggfunc='count')
flights_by_carrier.head()

data.head(1)

delays_list = ['carrier_delay','weather_delay','late_aircraft_delay','nas_delay','security_delay']
flight_delays_by_day = data.pivot_table(index='flight_date', values=delays_list, aggfunc='sum')
flight_delays_by_day

flight_delays_by_day.plot(kind='area', figsize=[16,6], stacked=True, colormap='autumn')

#Operations on Pivot Table
data.pivot_table(columns='unique_carrier', values='arr_delay').sort_values(ascending=False)
    

southwest = data[data['unique_carrier'] == 'WN']['arr_delay']
southwest


southwest.describe()


#Plotting Histogram
pd.Series([1, 2, 5, 9, 12, 20]).plot(kind='hist', bins=[0,10,20],color='r')

bin_values = np.arange(start=-50, stop=200, step=10)
us_mq_airlines_index = data['unique_carrier'].isin(['US','MQ']) # create index of flights from those airlines
us_mq_airlines = data[us_mq_airlines_index] # select rows
group_carriers = us_mq_airlines.groupby('unique_carrier')['arr_delay'] # group values by carrier, select minutes delayed
group_carriers.plot(kind='hist', bins=bin_values, figsize=[12,6], alpha=.4, legend=True) # alpha for transparency

group_carriers.describe()


hi_volume = data['origin'].value_counts()[:20]
hi_volume_airports_names = hi_volume.index.tolist()
hi_volume_airports = data[data['origin'].isin(hi_volume_airports_names)]
hi_volume_airports_pivots = hi_volume_airports.pivot_table(index='flight_date', columns='origin', values='arr_delay')
hi_volume_airports_pivots
airport_bins = numpy.arange(-10,100,3)
hi_volume_airports_pivots.plot(kind='hist', bins=airport_bins, figsize=[12,6], alpha=.4, legend=True)

hi_volume_airports_pivots = hi_volume_airports.pivot_table(index='flight_date', columns='origin', values='arr_delay')
hi_volume_airports_pivots.plot(kind='box', figsize=[16,8])


