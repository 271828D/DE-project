"""Test commit for the main.py"""

import argparse
from src.download_clean_data.utils.check_url_get_data import GetDataFromURL


def main():
    """Main file to run the program"""

    parser = argparse.ArgumentParser(description="ag desc")

    parser.add_argument(
        "--url", help="url to use for downloading the .csv file"
    )

    args = parser.parse_args()

    print(f"url to get the .csv file: {args.url}")

    # Usando la clase
    downloader = GetDataFromURL()

    data_content = downloader.check_request(args.url)

    downloader.download_file(data_content)


if __name__ == "__main__":

    main()
