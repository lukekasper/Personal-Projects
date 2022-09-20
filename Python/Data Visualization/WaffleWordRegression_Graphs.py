def pandas_4():

    # Import Libraries
    import piplite
    await piplite.install(['openpyxl==3.0.9', 'seaborn'])

    import numpy as np
    import pandas as pd  # primary data structure library
    from PIL import Image  # converting images into arrays

    from js import fetch
    import io

    # Data Setup
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
    import matplotlib.patches as mpatches  # needed for waffle Charts

    mpl.style.use('ggplot')  # optional: for ggplot-like style

    ### Waffle Charts ###
    # useful for displaying progress towards a goal
    # see new library PyWaffle for latest version of tool being developed
    # create dataframe for Scandanavian Countries
    df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]

    # determine proportion of each category with respect to the total
    total_values = df_dsn['Total'].sum()
    category_proportions = df_dsn['Total'] / total_values

    # define waffle chart dimensions
    idth = 40  # width of chart
    height = 10  # height of chart
    total_num_tiles = width * height  # total number of tiles

    # compute the number of tiles for each category
    tiles_per_category = (category_proportions * total_num_tiles).round().astype(int)

    # initialize the waffle chart as an empty matrix
    waffle_chart = np.zeros((height, width), dtype=np.uint)

    # define indices to loop through waffle chart
    category_index = 0
    tile_index = 0

    # populate the waffle chart
    for col in range(width):
        for row in range(height):
            tile_index += 1

            # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...
            if tile_index > sum(tiles_per_category[0:category_index]):
                # ...proceed to the next category
                category_index += 1

            # set the class value to an integer, which increases with class
            waffle_chart[row, col] = category_index

    # map the chart to a visual
    width = 40  # width of chart
    height = 10  # height of chart

    categories = df_dsn.index.values  # categories
    values = df_dsn['Total']  # corresponding values of categories

    colormap = plt.cm.coolwarm  # color map class

    # call waffle chart function
    create_waffle_chart(categories, values, height, width, colormap)

    #### Regression Plots ####
    # install seaborn
    # !pip3 install seaborn

    # import library
    import seaborn as sns

    # create new DF of total immigrants to Canada from all countries per year
    # we can use the sum() method to get the total population per year
    df_tot = pd.DataFrame(df_can[years].sum(axis=0))

    # change the years to type float (useful for regression later on)
    df_tot.index = map(float, df_tot.index)

    # reset the index to put in back in as a column in the df_tot dataframe
    df_tot.reset_index(inplace=True)

    # rename columns
    df_tot.columns = ['year', 'total']

    # call seaborn to make regression plots in one line!
    # automatically plots 95% confidence interval
    # confidence is the mean +/- variation in that measurement
    plt.figure(figsize=(15, 10))
    sns.set_style('whitegrid')  # change background to white background with ticks
    sns.set(font_scale=1.5)
    ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})

    ax.set(xlabel='Year', ylabel='Total Immigration')  # add x- and y-labels
    ax.set_title('Total Immigration to Canada from 1980 - 2013')  # add title
    plt.show()

    #### Word Clouds ####
    await piplite.install(['wordcloud==1.8.1'])
    from wordcloud import WordCloud, STOPWORDS

    # open txt file and read it into a variable
    alice_novel = urllib.request.urlopen('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/alice_novel.txt').read().decode("utf-8")
    stopwords = set(STOPWORDS)
    stopwords.add('said')  # add the words said to stopwords

    alice_wc = WordCloud(
        background_color='white',
        max_words=2000,
        stopwords=stopwords
    )

    # generate the word cloud
    alice_wc.generate(alice_novel)

    fig = plt.figure(figsize=(14, 18))

    # display the word cloud
    plt.imshow(alice_wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # save mask to alice_mask
    alice_mask = np.array(Image.open(urllib.request.urlopen('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%204/images/alice_mask.png')))

    # show mask
    fig = plt.figure(figsize=(14, 18))

    plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # can pass mask as a parameter into word cloud function
    # create a wordcloud based on proportion of immigrants from each country that contributed to total
    total_immigration = df_can['Total'].sum()
    max_words = 90

    # duplicate each countries name based on how many immigrants they contributed to Canada's total
    word_string = ''
    for country in df_can.index.values:
         # check if country's name is a single-word name
        if country.count(" ") == 0:
            repeat_num_times = int(df_can.loc[country, 'Total'] / total_immigration * max_words)
            word_string = word_string + ((country + ' ') * repeat_num_times)



# Function to create a waffle chart
def create_waffle_chart(categories, values, height, width, colormap, value_sign=''):
    # compute the proportion of each category with respect to the total
    total_values = sum(values)
    category_proportions = [(float(value) / total_values) for value in values]

    # compute the total number of tiles
    total_num_tiles = width * height  # total number of tiles
    print('Total number of tiles is', total_num_tiles)

    # compute the number of tiles for each catagory
    tiles_per_category = [round(proportion * total_num_tiles) for proportion in category_proportions]

    # print out number of tiles per category
    for i, tiles in enumerate(tiles_per_category):
        print(df_dsn.index.values[i] + ': ' + str(tiles))

    # initialize the waffle chart as an empty matrix
    waffle_chart = np.zeros((height, width))

    # define indices to loop through waffle chart
    category_index = 0
    tile_index = 0

    # populate the waffle chart
    for col in range(width):
        for row in range(height):
            tile_index += 1

            # if the number of tiles populated for the current category
            # is equal to its corresponding allocated tiles...
            if tile_index > sum(tiles_per_category[0:category_index]):
                # ...proceed to the next category
                category_index += 1

                # set the class value to an integer, which increases with class
            waffle_chart[row, col] = category_index

    # instantiate a new figure object
    fig = plt.figure()

    # use matshow to display the waffle chart
    colormap = plt.cm.coolwarm
    plt.matshow(waffle_chart, cmap=colormap)
    plt.colorbar()

    # get the axis
    ax = plt.gca()

    # set minor ticks
    ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
    ax.set_yticks(np.arange(-.5, (height), 1), minor=True)

    # add dridlines based on minor ticks
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

    plt.xticks([])
    plt.yticks([])

    # compute cumulative sum of individual categories to match color schemes between chart and legend
    values_cumsum = np.cumsum(values)
    total_values = values_cumsum[len(values_cumsum) - 1]

    # create legend
    legend_handles = []
    for i, category in enumerate(categories):
        if value_sign == '%':
            label_str = category + ' (' + str(values[i]) + value_sign + ')'
        else:
            label_str = category + ' (' + value_sign + str(values[i]) + ')'

        color_val = colormap(float(values_cumsum[i]) / total_values)
        legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

    # add legend to chart
    plt.legend(
        handles=legend_handles,
        loc='lower center',
        ncol=len(categories),
        bbox_to_anchor=(0., -0.2, 0.95, .1)
    )
    plt.show()