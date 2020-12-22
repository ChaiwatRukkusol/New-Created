import pandas as pd
import numpy as np

df  = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')[0]
df = df[df['Borough'] != 'Not assigned'].reset_index(drop=True)
df.head(15)

x = df['Neighbourhood'] == "Not assigned"
df.loc[x, 'Neighbourhood'] = df.loc[x, 'Borough']

df.shape


print('the shape of the dataframe is', df.shape)

df1 = pd.read_csv('https://cocl.us/Geospatial_data')
df1

df = df.sort_values(by='Postal Code')
df1 = df1.sort_values(by='Postal Code')

latitude = df1['Latitude'].values
longitude = df1['Longitude'].values

df['latitude']  = latitude
df['longitude'] = longitude
df


from geopy.geocoders import Nominatim

address =  'Toronto'
geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude

import folium

map_toronto = folium.Map(location=[latitude, longitude], zoom_start=10)

for lat, lng, borough,  in zip(df['latitude'], df['longitude'], df['Borough']):
    label = borough
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='red',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)

map_toronto
