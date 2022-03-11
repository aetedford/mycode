#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Exploring using pandas to create dataframes, and output graphs"""

import pandas as pd

def main():
    # define the name of our xls file
    excel_file = 'movies.xls'

    # create a DataFrame (DF) object. EASY!
    # because we did not specify a sheet
    # only the first sheet was read into the DF
    movies = pd.read_excel(excel_file)

    # Choose the first column "Title" as
    # index (index=0)
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    

    print(movies_sheet1.loc[movies_sheet1["Year"]>1950])
    print(movies_sheet1.loc[(movies_sheet1["Year"]>1950)&(movies_sheet1["IMDB Score"]>6.0)])




if __name__ == "__main__":
    main()

