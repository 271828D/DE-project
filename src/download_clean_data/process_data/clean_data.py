"""Script to clean data from the .csv file"""

import pandas as pd
from datetime import datetime
from pathlib import Path
from ..utils.paths import get_data_directory


class ReadCsv:
    """
    Class to read .csv file and return it
    as a pandas dataframe.
    """

    def read(self, path_file: Path) -> pd.DataFrame:
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
        """Get all the discarded rows to a DataFrame"""
        if not self.discarded_rows:
            return pd.DataFrame()  # Return empty DF if nothing discarded

        return pd.concat(
            self.discarded_rows, ignore_index=True
        )  # Concat all the elements on the list discarded_rows

    def save_discarded_rows(
        self, output_path: Path | str | None = None
    ) -> None:
        """Save discarded rows in a .csv file"""
        discarded = self.get_discarded_rows()

        if output_path is None:
            output_path = get_data_directory() / "discarded_rows.csv"
        else:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)

        if not discarded.empty:  # check if discarded.empty is false
            discarded.to_csv(output_path, index=False)
            print(f"{len(discarded)} Discarded rows saved to {output_path}")
        else:
            print("No rows were discarded")

    def save_clean_data(self, output_path: Path | str | None = None) -> None:
        """Save clean rows in a .csv file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"clean_data_{timestamp}.csv"

        if output_path is None:
            output_path = get_data_directory() / filename
        else:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)

        # Save logic
        if not self.df.empty:
            self.df.to_csv(output_path, index=False)
            print(f"{len(self.df)} clean rows saved to {output_path}")
        else:
            print("No clean data to save (dataframe is empty)")
