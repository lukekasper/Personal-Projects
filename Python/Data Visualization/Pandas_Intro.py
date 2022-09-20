def pandas_intro():
    ### SEE DATA ANALYSIS NOTES FROM CIT 590 FOR MORE TIPS ###

    import numpy as np
    import pandas as pd
    # !pip install openpyxl

    # Read data from Excel File and print the first five rows
    xlsx_path = '/Users/lukekasper/Downloads/TopSellingAlbums.xlsx'
    df = pd.read_excel(xlsx_path)
    df.head()

    # Assign x1 as column of the dataframe
    x1 = df[['Length']]
    print(x1)

    # Assign x as series
    x2 = df['Length']

    # Assign y as multiple columns of dataframe
    y = df[['Artist', 'Length', 'Genre']]

    # Access value of first row/column
    df.iloc[0, 0]

    # Access column using name
    df.loc[1, 'Artist']  # prints row 2 of column "Artist"

    # Slicing the dataframe
    df.iloc[0:2, 0:3]

    # Slicing the dataframe using the name
    df.loc[0:2, 'Artist':'Released']

    # convert the dataframe index df to characters and assign it to df_new
    # find the element corresponding to the row index a and column 'Artist'
    # Then select the rows a through d for the column 'Artist'
    new_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    df_new = df
    df_new.index = new_index
    df_new.loc['a', 'Artist']
    df_new.loc['a':'d', 'Artist']
