"""Test commit for the main.py"""

import argparse
from src.download_clean_data.utils.check_url_get_data import GetDataFromUrl
from src.download_clean_data.process_data.clean_data import ReadCsv, CleanData
from src.download_clean_data.reports.processing_stats import DataStats
from src.download_clean_data.reports.monthly_metrics import (
    data_preparation,
    calculate_monthly_metrics,
    save_monthly_metrics_to_csv,
)


def main():
    """Main file to run the program"""

    parser = argparse.ArgumentParser(description="ag desc")

    parser.add_argument(
        "--url", help="url to use for downloading the .csv file"
    )

    args = parser.parse_args()

    print(f"url to get the .csv file: {args.url}")

    # Get the data
    downloader = GetDataFromUrl()
    data_content = downloader.check_request(args.url)
    output_path = downloader.download_file(data_content)  #

    # Read the data from CSV
    reader = ReadCsv()
    dataframe = reader.read(output_path)
    original_dataframe = dataframe.copy()

    # Clean data
    cleaner = CleanData(dataframe)
    cleaner.remove_duplicate_rows()
    cleaner.clean_empty_rows()
    cleaner.save_discarded_rows()
    cleaner.save_clean_data()  # Add. save step for the clean data
    discarded_dataframe = cleaner.get_discarded_rows()

    # Reports
    # data stats JSON
    data_stats = DataStats(
        df_original=original_dataframe,
        df_clean=cleaner.df,
        df_discarded=discarded_dataframe,
    )

    data_stats.save_stats_to_json()

    clean_df = data_preparation(cleaner.df)  # Second cleaning process
    metrics = calculate_monthly_metrics(clean_df)

    save_monthly_metrics_to_csv(metrics)


if __name__ == "__main__":

    main()
