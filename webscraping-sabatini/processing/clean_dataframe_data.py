import pandas

def clean_dataframe_data(dataframe):
    RIGHT_SIDE_TEXT = ' IVA inc.'
    LEFT_SIDE_TEXT = '$'
    dataframe['precio'] = dataframe['precio'].str.strip(RIGHT_SIDE_TEXT)
    dataframe['precio'] = dataframe['precio'].str.strip(LEFT_SIDE_TEXT)
    dataframe['precio'] = pandas.to_numeric(dataframe['precio'], downcast='signed')
    print(dataframe)
    return dataframe
