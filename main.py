"""Test commit for the main.py"""

import argparse
from src.download_clean_data.utils.check_url_get_data import GetDataFromUrl
from src.download_clean_data.process_data.clean_data import ReadCsv, CleanData


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

    # Clean data
    cleaner = CleanData(dataframe)
    cleaner.remove_duplicate_rows()
    cleaner.clean_empty_rows()
    cleaner.save_discarded_rows()

    # Reports


# python main.py
# --url "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
# Testing funcionalities

if __name__ == "__main__":

    main()
