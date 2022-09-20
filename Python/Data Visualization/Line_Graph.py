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
    print('Data downloaded and read into a dataframe!')

    # get info about dataframe
    df_can.info(verbose=False)

    # get column names
    df_can.columns

    # get list of indices
    df_can.index

    # get columns and indices as actual lists
    df_can.columns.tolist()
    df_can.index.tolist()

    # size of dataframe (rows, columns)
    df_can.shape

    # clean dataset to remove unecessary columns
    # in pandas axis=0 represents rows (default) and axis=1 represents columns.
    df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
    df.drop_duplicates() # remove duplicates
    df_can.head(2)

    # rename columns to make sense
    df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
    df_can.columns

    # Add column 'Total' that sums up the total immigrants by country over the entire period 1980 - 2013
    df_can['Total'] = df_can.sum(axis=1)

    # Check how many null columns are in dataset
    df_can.isnull().sum()

    # stat summary of each column in dataset
    df_can.describe()

    df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]  # returns a dataframe
    # notice that 'Country' is string, and the years are integers.

    # set index to be based on country column and not numeric
    # can go back to original using reset_index
    df_can.set_index('Country', inplace=True)

    # optional: to remove the name of the index
    df_can.index.name = None

    # 1. the full row data (all columns)
    df_can.loc['Japan']

    # as a row vector
    df_can[df_can.index == 'Japan']

    # 3. for years 1980 to 1985
    df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]

    # convert year column names to strings
    df_can.columns = list(map(str, df_can.columns))

    # create a variable for calling all years as a list of strings
    # useful for plotting later on
    years = list(map(str, range(1980, 2014)))

    # 1. create the condition boolean series for countries in the continent of asia
    condition = df_can['Continent'] == 'Asia'

    # 2. pass this condition into the dataFrame
    df_can[condition]

    # we can pass multiple criteria in the same line.
    # let's filter for AreaNAme = Asia and RegName = Southern Asia
    # Use | for OR
    df_can[(df_can['Continent'] == 'Asia') & (df_can['Region'] == 'Southern Asia')]

    #########  Visualize Data Using Matplotlib ###############
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # Plot a line graph of immigration from Haiti using df.plot().
    # first extract data series for Haiti
    haiti = df_can.loc['Haiti', years]  # passing in years 1980 - 2013 to exclude the 'total' column
    haiti.plot()

    haiti.index = haiti.index.map(int)  # let's change the index values of Haiti to type integer for plotting
    haiti.plot(kind='line')

    plt.title('Immigration from Haiti')
    plt.ylabel('Number of immigrants')
    plt.xlabel('Years')
    # annotate the 2010 Earthquake.
    # syntax: plt.text(x, y, label)
    plt.text(2000, 6000, '2010 Earthquake')  # see note below

    plt.show()  # need this line to show the updates made to the figure

    # get dataset for China and Inida
    df_CI = df_can.loc[['China', 'India'], years]

    # make a line plot of the data
    df_CI.plot(kind='line')

    # pandas plots the indices of the df on the x-axis and the columns as individual lines on the y-axis.
    # Since df_CI is a dataframe with the country as the index and years as the columns,
    # we must first transpose the dataframe using transpose() method to swap the row and columns
    df_CI = df_CI.transpose()
    df_CI.plot(kind='line')
    plt.title('Immigrant from China & India')
    plt.ylabel('Num Immigrants')
    plt.xlabel('Year')

    # plot top 5 countries that contribute immigrants to canada
    inplace = True  # paramemter saves the changes to the original df_can dataframe

    # re-sort data set by column 'Total' in descending order
    df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
    df_top5 = df_can.head(5) # get the top 5

    # transpose the dataframe
    df_top5 = df_top5[years].transpose()

    df_top5.index = df_top5.index.map(int)  # let's change the index values of df_top5 to type integer for plotting
    df_top5.plot(kind='line', figsize=(14, 8))  # pass a tuple (x, y) size

    plt.title('Immigration Trend of Top 5 Countries')
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')
    plt.show()

    # bar for vertical bar plots
    # barh for horizontal bar plots
    # hist for histogram
    # box for boxplot
    # kde or density for density plots
    # area for area plots
    # pie for pie plots
    # scatter for scatter plots
    # hexbin for hexbin plot