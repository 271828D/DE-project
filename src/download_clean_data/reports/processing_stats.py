"""File with the Class to generate the first artifact"""

import json
import pandas as pd


class DataStats:
    """Class that generate the stats
    for the first artefact
    """

    def __init__(
        self,
        df_original: pd.DataFrame,
        df_clean: pd.DataFrame,
        df_discarded: pd.DataFrame,
    ):
        self.df_original = df_original
        self.df_clean = df_clean
        self.df_discarded = df_discarded

    def get_total_rows(self) -> int:
        """Calculate total rows before clean process"""
        return len(self.df_original)

    def get_empty_rows(self) -> int:
        """Calculate total empty rows"""
        empty_rows_df = self.df_original[self.df_original.isna().all(axis=1)]
        return len(empty_rows_df)

    def get_total_invalid_discarded_rows(self) -> int:
        """
        Calculate total invalid discarded rows.
        Assumption:
        total invalid discarded = empty + duplicate
        """
        return len(self.df_discarded)

    def get_total_duplicate_rows(self) -> int:
        """Calculate total of duplicate rows"""
        duplicates_df = self.df_original[
            self.df_original.duplicated(keep="first")
        ]
        return len(duplicates_df)

    def get_usable_rows(self) -> int:
        """Calculate the total rows in the clean
        dataset"""
        return len(self.df_clean)

    def build_stats_dict(self) -> dict[str:int]:
        """Build dictionary with stats"""
        return {
            "total_rows": self.get_total_rows(),
            "total_empty_rows_removed": self.get_empty_rows(),
            "total_invalid_rows_discarded": self.get_total_invalid_discarded_rows(),
            "total_duplicate_rows_removed": self.get_total_duplicate_rows(),
            "total_usable_rows": self.get_usable_rows(),
        }

    def save_stats_to_json(
        self, output_path: str = "../data/processing_statts.json"
    ) -> None:
        """Save stats on json file"""
        stats_dict = self.build_stats_dict()

        with open(output_path, "w") as f:  # open and write the file
            json.dump(stats_dict, f, indent=4)

        print(f"Stats saved in: {output_path}")
