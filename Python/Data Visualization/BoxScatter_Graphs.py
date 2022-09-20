def pandas_3():
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

    # clean up the dataset to remove unnecessary columns (eg. REG)
    df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

    # let's rename the columns so that they make sense
    df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)

    # for sake of consistency, let's also make all column labels of type string
    df_can.columns = list(map(str, df_can.columns))

    # set the country name as index - useful for quickly looking up countries using .loc method
    df_can.set_index('Country', inplace=True)

    # add total column
    df_can['Total'] = df_can.sum(axis=1)

    # years that we will be using in this lesson - useful for plotting later on
    years = list(map(str, range(1980, 2014)))

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # group countries by continents and apply sum() function
    df_continents = df_can.groupby('Continent', axis=0).sum()

    # data frame for Box plots
    df_japan = df_can.loc[['Japan'], years].transpose()

    # prints statistics
    df_japan.describe()

    # horizontal box plots
    # for box plots python automatically identifies outliers
    df_CI.plot(kind='box', figsize=(10, 7), color='blue', vert=False)

    plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
    plt.xlabel('Number of Immigrants')

    plt.show()

    # to create subplots
    fig = plt.figure()  # create figure

    ax0 = fig.add_subplot(1, 2, 1)  # add subplot 1 (1 row, 2 columns, first plot)
    ax1 = fig.add_subplot(1, 2, 2)  # add subplot 2 (1 row, 2 columns, second plot). See tip below**

    # Subplot 1: Box plot
    df_CI.plot(kind='box', color='blue', vert=False, figsize=(20, 6), ax=ax0)  # add to subplot 1
    ax0.set_title('Box Plots of Immigrants from China and India (1980 - 2013)')
    ax0.set_xlabel('Number of Immigrants')
    ax0.set_ylabel('Countries')

    # Subplot 2: Line plot
    df_CI.plot(kind='line', figsize=(20, 6), ax=ax1)  # add to subplot 2
    ax1.set_title('Line Plots of Immigrants from China and India (1980 - 2013)')
    ax1.set_ylabel('Number of Immigrants')
    ax1.set_xlabel('Years')

    plt.show()

    # get data from top 15 countries for immigrants to canada
    df_top15 = df_can.sort_values(['Total'], ascending=False, axis=0).head(15)

    # create a list of all years in decades 80's, 90's, and 00's
    years_80s = list(map(str, range(1980, 1990)))
    years_90s = list(map(str, range(1990, 2000)))
    years_00s = list(map(str, range(2000, 2010)))

    # slice the original dataframe df_can to create a series for each decade
    df_80s = df_top15.loc[:, years_80s].sum(axis=1)
    df_90s = df_top15.loc[:, years_90s].sum(axis=1)
    df_00s = df_top15.loc[:, years_00s].sum(axis=1)

    # merge the three series into a new data frame
    new_df = pd.DataFrame({'1980s': df_80s, '1990s': df_90s, '2000s': df_00s})

    # check how many points in data set fall above outlier threshold (> Q3 by 1.5x IQR)
    new_df = new_df.reset_index()
    new_df[new_df['2000s'] > 209611.5]


    ##### SCATTER PLOTS #####
    # get data for immigrants to Canada from ALL countries broken out per year
    # we can use the sum() method to get the total population per year
    df_tot = pd.DataFrame(df_can[years].sum(axis=0))

    # change the years to type int (useful for regression later on)
    df_tot.index = map(int, df_tot.index)

    # reset the index to put in back in as a column in the df_tot dataframe
    df_tot.reset_index(inplace=True)

    # rename columns
    df_tot.columns = ['year', 'total']

    # create a line of best fit to the dataset
    x = df_tot['year']  # year on x-axis
    y = df_tot['total']  # total on y-axis
    fit = np.polyfit(x, y, deg=1)

    # plot data and line
    df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

    plt.title('Total Immigration to Canada from 1980 - 2013')
    plt.xlabel('Year')
    plt.ylabel('Number of Immigrants')

    # plot line of best fit
    plt.plot(x, fit[0] * x + fit[1], color='red')  # recall that x is the Years
    plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

    plt.show()

    # print out the line of best fit
    'No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1])

    # Display data for 3 countries for each year
    # create df_countries dataframe
    df_countries = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()

    # create df_total by summing across three countries for each year
    df_total = pd.DataFrame(df_countries.sum(axis=1))

    # reset index in place
    df_total.reset_index(inplace=True)

    # rename columns
    df_total.columns = ['year', 'total']

    # change column year from string to int to create scatter plot
    df_total['year'] = df_total['year'].astype(int)

    ### Bubble Plots ###

    # transposed dataframe
    df_can_t = df_can[years].transpose()

    # cast the Years (the index) to type int
    df_can_t.index = map(int, df_can_t.index)

    # let's label the index. This will automatically be the column name when we reset the index
    df_can_t.index.name = 'Year'

    # reset index to bring the Year in as a column
    df_can_t.reset_index(inplace=True)

    # Normalize data set using feature scaling (scales full data set between 0-1)
    norm_brazil = (df_can_t['Brazil'] - df_can_t['Brazil'].min()) / (
                df_can_t['Brazil'].max() - df_can_t['Brazil'].min())

    norm_argentina = (df_can_t['Argentina'] - df_can_t['Argentina'].min()) / (
                df_can_t['Argentina'].max() - df_can_t['Argentina'].min())

    # Plot and overlay 2 scatter plots
    # Brazil
    ax0 = df_can_t.plot(kind='scatter',
                        x='Year',
                        y='Brazil',
                        figsize=(14, 8),
                        alpha=0.5,  # transparency
                        color='green',
                        s=norm_brazil * 2000 + 10,  # pass in weights
                        xlim=(1975, 2015)
                        )

    # Argentina
    ax1 = df_can_t.plot(kind='scatter',
                        x='Year',
                        y='Argentina',
                        alpha=0.5,
                        color="blue",
                        s=norm_argentina * 2000 + 10,
                        ax=ax0
                        )

    ax0.set_ylabel('Number of Immigrants')
    ax0.set_title('Immigration from Brazil and Argentina from 1980 to 2013')
    ax0.legend(['Brazil', 'Argentina'], loc='upper left', fontsize='x-large')