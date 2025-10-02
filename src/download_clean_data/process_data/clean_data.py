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

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()  # keep copia del original
        self.discarded_rows = []  # discarded rows log

    def remove_duplicate_rows(self) -> pd.DataFrame:
        """Remove and track duplicated rows"""
        duplicates = self.df[
            self.df.duplicated(keep="first")
        ]  # get duplicates rows; keep="first" to keep the 1st inst
        self.discarded_rows.append(
            duplicates
        )  # save duplicated rows in a list
        self.df = self.df.drop_duplicates(
            keep="first"
        )  # throw away duplicated values
        return self.df

    def clean_empty_rows(self) -> pd.DataFrame:
        """Remove rows where all cols. are empty"""
        empty_rows = self.df[self.df.isna().all(axis=1)]  # get empty rows
        self.discarded_rows.append(
            empty_rows
        )  # add the empty rows to discarded tracking
        self.df = self.df.dropna(
            how="all"
        )  # throw away instances with null/empty in all columns
        return self.df

    def get_discarded_rows(self) -> pd.DataFrame:
        pass
