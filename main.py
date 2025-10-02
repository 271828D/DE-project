"""Test commit for the main.py"""

import argparse


def main():
    """Main file to run the program"""

    parser = argparse.ArgumentParser(description="ag desc")

    parser.add_argument("url", help="url to use for downloading the .csv file")

    args = parser.parse_args()

    print(f"url to get the .csv file: {args.url}")

    if __name__ == "__main__":

        main()
