"""Script to clean data from the .csv file"""

import pandas as pd


class ReadCsv:
    """
    Class to read .csv file and return it
    as a pandas dataframe.
    """

    def __init__(self):
        pass

    def read(self, path_file: str) -> pd.DataFrame:
        return pd.read_csv(path_file, sep=",")


class CleanData:
    """
    Class to clean the dataframe.
    """

    def __init__(self):
        pass

    def remove_duplicate_rows() -> pd.DataFrame:
        pass

    def clean_empty_rows() -> pd.DataFrame:
        pass

    def get_discarded_rows() -> pd.DataFrame:
        pass
