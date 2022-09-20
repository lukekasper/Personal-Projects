def maps():

    #install folium (python map generation libraries)
    import piplite
    # await piplite.install(['openpyxl==3.0.9', 'folium'])

    import pandas as pd  # primary data structure library
    import numpy as np  # useful for many scientific computing in Python

    # pip3 install folium==0.5.0
    import folium

    # define the world map (Stamen Toner maps are high contrast B+W maps)
    # other map styles: Stamen Terrain
    world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Toner')

    # make map of san francisco crime data from csv
    from js import fetch
    import io

    URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Police_Department_Incidents_-_Previous_Year__2016_.csv'
    resp = await fetch(URL)
    text = io.BytesIO((await resp.arrayBuffer()).to_py())

    df_incidents = pd.read_csv(text)

    # get the first 100 crimes in the df_incidents dataframe
    limit = 100
    df_incidents = df_incidents.iloc[0:limit, :]

    # San Francisco latitude and longitude values
    latitude = 37.77
    longitude = -122.42

    # create map and display it
    sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

    # superimpose crime locations
    # instantiate a feature group for the incidents in the dataframe
    incidents = folium.map.FeatureGroup()

    # loop through the 100 crimes and add each to the incidents feature group
    for lat, lng, in zip(df_incidents.Y, df_incidents.X):       # zip pairs each item in each array together as a tuple
        incidents.add_child(
            folium.features.CircleMarker(
                [lat, lng],
                radius=5,  # define how big you want the circle markers to be
                color='yellow',
                fill=True,
                fill_color='blue',
                fill_opacity=0.6
            )
        )

    # add pop-up text to each marker on the map
    latitudes = list(df_incidents.Y)
    longitudes = list(df_incidents.X)
    labels = list(df_incidents.Category)

    for lat, lng, label in zip(latitudes, longitudes, labels):
        folium.Marker([lat, lng], popup=label).add_to(sanfran_map)

    # add incidents to map
    sanfran_map.add_child(incidents)

    # to reduce congestion, add labels directly to markers on map
    # loop through the 100 crimes and add each to the map
    for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
        folium.features.CircleMarker(
            [lat, lng],
            radius=5,  # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            popup=label,
            fill_color='blue',
            fill_opacity=0.6
        ).add_to(sanfran_map)

    ## can also group them together in clusters ##
    from folium import plugins

    # let's start again with a clean copy of the map of San Francisco
    sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

    # instantiate a mark cluster object for the incidents in the dataframe
    incidents = plugins.MarkerCluster().add_to(sanfran_map)

    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
        folium.Marker(
            location=[lat, lng],
            icon=None,
            popup=label,
        ).add_to(incidents)

    ####  Choropleth Maps  ####
    # download canadian dataframe
    from js import fetch
    import io

    URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx'
    resp = await fetch(URL)
    text = io.BytesIO((await resp.arrayBuffer()).to_py())

    df_can = pd.read_excel(
        text,
        sheet_name='Canada by Citizenship',
        skiprows=range(20),
        skipfooter=2)

    # clean up the dataset
    df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
    df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
    df_can.columns = list(map(str, df_can.columns))
    df_can['Total'] = df_can.sum(axis=1)
    years = list(map(str, range(1980, 2014)))

    # download countries geojson file
    from js import fetch
    import io
    import json

    URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/world_countries.json'
    resp = await fetch(URL)
    data = io.BytesIO((await resp.arrayBuffer()).to_py())
    world_geo = json.load(data)

    # create a map from geoJSON data
    world_map = folium.Map(location=[0, 0], zoom_start=2)

    # generate choropleth map using the total immigration of each country to Canada from 1980 to 2013
    # key_on: key or variable in json file that contains the variable of intrest; must open json file to determine;
    #         in this case it is the variable that contains the name of the countries (variable of intrest)
    #         note that the key is case sensitive

    # create a numpy array of length 6 and has linear spacing from the minimum total immigration to the maximum total immigration
    threshold_scale = np.linspace(df_can['Total'].min(),
                                  df_can['Total'].max(),
                                  6, dtype=int)
    threshold_scale = threshold_scale.tolist()  # change the numpy array to a list
    threshold_scale[-1] = threshold_scale[
                              -1] + 1  # make sure that the last value of the list is greater than the maximum immigration

    # let Folium determine the scale.
    world_map = folium.Map(location=[0, 0], zoom_start=2)
    world_map.choropleth(
        geo_data=world_geo,
        data=df_can,
        columns=['Country', 'Total'],
        key_on='feature.properties.name',
        threshold_scale=threshold_scale,
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Immigration to Canada',
        reset=True
    )