import pandas as pd


def write_to_console(value):
    """ 
    Outputs given value to the console
    Parameters: 
        value (any): given value
    Returns:
        my_input (string): Inputed string
    """
    print(value)


def write_to_file(file_path, value):
    """ 
    Converts given value to the string and writes it to the given file
    Parameters: 
        file_path (string): path to the file
        value (any): given value
    Returns: None    
    """
    with open(file_path, "w") as my_file:
        my_file.write(value)
