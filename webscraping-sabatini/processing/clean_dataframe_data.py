import pandas

def clean_dataframe_data(dataframe):
    RIGHT_SIDE_TEXT = ' IVA inc.'
    LEFT_SIDE_TEXT = '$'
    try:
        dataframe['precio'] = dataframe['precio'].str.strip(RIGHT_SIDE_TEXT)

    except Exception as e:
        print("Error while stripping right side of the text: ", e.args)
    
    try:
        dataframe['precio'] = dataframe['precio'].str.strip(LEFT_SIDE_TEXT)

    except Exception as e:
        print("Error while stripping the left side of the text: ", e.args)
    
    try:
        dataframe['precio'] = pandas.to_numeric(dataframe['precio'], downcast='signed')

    except Exception as e:
        print("Error while converting precio column to numeric.", e.args)

    print(dataframe)
    return dataframe
