import pandas as pd

# Functions
def make_ratio(dataframe, dividend, divisor, new_colname):
    '''
    Takes in a dataframe, two column names, and a name for the output column,
    It returns a new dataframe, identical to the input, but with a new column,
    made by dividing the dididend column by the divisor colum in the original dataframe.

    Inputs
    ----------
    dataframe (pandas.DataFrame): a pandas dataframe
    dividend (pandas.Series): a column in the dataframe
    divisor (pandas.Series): another column in the dataframe
    new_colname (string): the name to give to the new column

    Returns:
    new_dataframe (pandas.DataFrame): a new dataframe with the ratio column
    '''

    new_dataframe = dataframe.copy()

    new_dataframe[new_colname] = new_dataframe.apply(lambda x: x[dividend] / x[divisor], axis = 1)

    return new_dataframe