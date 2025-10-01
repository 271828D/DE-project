# from urllib.request import urlretrieve
# import requests


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

    def dowload_file(self, output_path: str | None = None):
        """
        Dowload the respective .csv file from the url
        and save it into the output path if this is
        not None
        """
        pass
