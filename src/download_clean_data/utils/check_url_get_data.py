# from urllib.request import urlretrieve
import requests
from pathlib import Path
from datetime import datetime


class GetDataFromUrl:
    """
    Class to verify URL and dowload the file
    """

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
        # Check for the url to not be an empty str
        if not url or not isinstance(url, str):
            raise ValueError("URL must be a non-empty string")
        # Timeout can't be 0 or negative value
        if timeout <= 0:
            raise ValueError("Timeout must be positive")

        # Try/catch to check url
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  # Check for error codes (classic 404 lol)
            return response.content

        except requests.Timeout:
            print(f"response took more than {timeout} seconds")
            raise TimeoutError(f"Request exceeded {timeout} seconds")

        except requests.HTTPError as e:
            raise print(f"HTTP Error {e.response.status_code}: {e}")

        except requests.RequestException as e:
            print(f"Download failed: {e}")
            return None

    def download_file(
        self, url_data: bytes, output_path: Path | None = None
    ) -> Path:
        """
        Download the data file to a .csv file,
        creates the /data folder and saves
        the downloaded data in the /data folder
        with the name:
        order_items_<timestamp>.csv. The
        function returns the path for the downoaded file.

        Arg:
            url_data:
            output_path (optional):
        """
        # Name generation for the file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"order_items_{timestamp}.csv"

        # Create data folder if doesn't exist
        project_root = Path(
            __file__
        ).parent.parent.parent.parent  # Take the path of the file (__file__)
        data_folder = project_root / "data"
        data_folder.mkdir(parents=True, exist_ok=True)

        # Falta agregar check: exist ?
        output_file = data_folder / filename
        print(f"File path: {output_file}")

        # Open the file and saves the data
        with output_file.open("wb") as f:
            f.write(url_data)

        print(f"Data stored in: {output_file}")

        return output_file
