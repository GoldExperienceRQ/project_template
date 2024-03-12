import pandas as pd


def get_console_input():
    """ 
    Gets input from console, then returns it
    Parameters: none
    Returns:
        my_input (string): Inputed string
    """
    return input("Write something: ")


def read_file(file_path):
    """ 
    Reads given file and return its text
    Parameters: 
        file_path (string): path to the file
    Returns:
        value (string): Text in the file
    """
    with open(file_path) as my_file:
        return my_file.read()


def read_file_with_pandas(file_path):
    """ 
    Reads given file with pandas library severating it by spaces and returns dataframe
    Parameters: 
        file_path (string): path to the file
    Returns:
        value (array): Stringified dataframe
    """
    with open(file_path) as my_file:
        return pd.read_csv(my_file, sep=" ").to_string()