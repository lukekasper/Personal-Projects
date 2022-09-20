def pandas_2():
    import piplite
    await piplite.install(['openpyxl==3.0.9'])

    import pandas as pd
    import numpy as np

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

    # rename columns
    df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)

    # see if all columns are type string
    all(isinstance(column, str) for column in df_can.columns)

    # make them all strings
    df_can.columns = list(map(str, df_can.columns))

    # set country name as index
    df_can.set_index('Country', inplace=True)

    # Make a Total column
    df_can['Total'] = df_can.sum(axis=1)

    # Make years list
    years = list(map(str, range(1980, 2014)))

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # sort Total column in descending order
    df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

    df_top5 = df_can.head()

    # change index type to integer and plot
    df_top5.index = df_top5.index.map(int)
    df_top5.plot(kind='area',
                 alpha=0.25,    # transparency of stacked areas
                 stacked=False,
                 figsize=(20, 10))  # pass a tuple (x, y) size

    plt.title('Immigration Trend of Top 5 Countries')
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')

    plt.show()

    # option 2: Object-oriented method; preferred option with more flexibility
    ax = df_top5.plot(kind='area', alpha=0.35, figsize=(20, 10))

    ax.set_title('Immigration Trend of Top 5 Countries')
    ax.set_ylabel('Number of Immigrants')
    ax.set_xlabel('Years')

    # plot the lowest 5 countries for immigration
    # get the top 5 entries
    df_least5 = df_can.tail(5)
    df_least5 = df_least5[years].transpose()

    df_least5.index = df_least5.index.map(int)

    ### HISTOGRAMS ###
    # call numpy's histogram method to split data into 10 equal bins and assign variables for plotting
    count, bin_edges = np.histogram(df_can['2013'])

    # plot histogram
    df_can['2013'].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)  # xticks ensures bins align with tic marks

    # add a title to the histogram
    plt.title('Histogram of Immigration from 195 Countries in 2013')
    # add y-label
    plt.ylabel('Number of Countries')
    # add x-label
    plt.xlabel('Number of Immigrants')

    plt.show()

    # can equivalently plot by passing the plot type as a method
    df_can.loc[['Denmark', 'Norway', 'Sweden'], years].plot.hist()      # does not look right without transposing data

    # transpose
    df_t = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()

    # let's get the x-tick values
    count, bin_edges = np.histogram(df_t, 15)

    # un-stacked histogram
    df_t.plot(kind='hist',
              figsize=(10, 6),
              bins=15,
              alpha=0.6,
              xticks=bin_edges,
              color=['coral', 'darkslateblue', 'mediumseagreen']
              )

    plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
    plt.ylabel('Number of Years')
    plt.xlabel('Number of Immigrants')

    # to see full list of color options
    for name, hex in matplotlib.colors.cnames.items():
        print(name, hex)

    ### BAR Chart ###
    df_iceland = df_can.loc['Iceland', years]
    df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)  # rotate the xticks(labelled points on x-axis) by 90 degrees

    plt.xlabel('Year')
    plt.ylabel('Number of Immigrants')
    plt.title('Icelandic Immigrants to Canada from 1980 to 2013')

    # Annotate arrow
    plt.annotate('',  # s: str. Will leave it blank for no text
                 xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
                 xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
                 xycoords='data',  # will use the coordinate system of the object being annotated
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
                 )

    # Annotate Text
    plt.annotate('2008 - 2011 Financial Crisis',  # text to display
                 xy=(28, 30),  # start the text at at point (year 2008 , pop 30)
                 rotation=72.5,  # based on trial and error to match the arrow
                 va='bottom',  # want the text to be vertically 'bottom' aligned
                 ha='left',  # want the text to be horizontally 'left' algned.
                 )

    # get immigrants to Canada from top 15 countries
    df_can.sort_values(by='Total', ascending=True, inplace=True)

    # get top 15 countries
    df_top15 = df_can['Total'].tail(15)

    # generate plot
    df_top15.plot(kind='barh', figsize=(12, 12), color='steelblue')
    plt.xlabel('Number of Immigrants')
    plt.title('Top 15 Conuntries Contributing to the Immigration to Canada between 1980 - 2013')

    # annotate value labels to each country
    for index, value in enumerate(df_top15):
        label = format(int(value), ',')  # format int with commas

        # place text at the end of bar (subtracting 47000 from x, and 0.1 from y to make it fit within the bar)
        plt.annotate(label, xy=(value - 47000, index - 0.10), color='white')

    plt.show()



    # stacked Histogram
    count, bin_edges = np.histogram(df_t, 15)
    xmin = bin_edges[0] - 10  # first bin value is 31.0, adding buffer of 10 for aesthetic purposes
    xmax = bin_edges[-1] + 10  # last bin value is 308.0, adding buffer of 10 for aesthetic purposes
    df_t.plot(kind='hist',
              figsize=(10, 6),
              bins=15,
              xticks=bin_edges,
              color=['coral', 'darkslateblue', 'mediumseagreen'],
              stacked=True,
              xlim=(xmin, xmax)
              )

    plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
    plt.ylabel('Number of Years')
    plt.xlabel('Number of Immigrants')

    plt.show()