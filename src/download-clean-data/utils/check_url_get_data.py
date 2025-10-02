# from urllib.request import urlretrieve
import requests
from pathlib import Path
from datetime import datetime


class GetDataFromURL:
    """
    Class to verify URL and dowload the file
    """

    def __init__(self, path: str):
        self.path = path
        pass

    def check_url(self, timeout=15) -> bool:
        """Verify if the URL exist and can
        be applied a GET request.

        Args:
            timeout: time

        """
        pass

    def check_request(self, url: str, timeout: int = 15) -> bytes:
        """This function do the request (GET)
        to the url and raise an exception if
        is not capable to get the data.

        Args:
            url: must be an string but not None
                str.
            timeout (optional): time in seconds for
                the GET method.
        """
        # Try/catch to check url
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  # Check for error codes (classic 404 lol)
            return response.content

        except requests.Timeout:
            print(f"response took more than {timeout} seconds")
            return None

        except requests.HTTPError as e:
            print(f"HTTP Error {e.response.status_code}: {e}")
            return None

        except requests.RequestException as e:
            print(f"Download failed: {e}")
            return None

    def download_file(self, url_data: bytes, output_path: str | None = None):
        """
        Download the data file to a .csv file,
        creates the /data folder and saves
        the downloaded data in the /data folder
        with the name:
        order_items_<timestamp>.csv

        Arg:
            url_data:
            output_path (optional):
        """
        # Name generation for the file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"order_items_{timestamp}.csv"

        # Create data folder if doesn't exist
        data_folder = Path("data")
        data_folder.mkdir(parents=True, exist_ok=True)

        # Falta agregar check: exist ?
        output_file = data_folder / filename
        print(f"File path: {output_file}")

        # Open the file and saves the data
        with output_file.open("wb") as f:
            f.write(url_data.content)

        return print(f"Data stored in: {output_file}")
