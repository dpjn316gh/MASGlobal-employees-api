# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


import logging

import requests


class JsonRestClient:
    """
    Json rest client
    """

    def __init__(self, base_url: str, timeout: str):
        """
        Initialize the client
        Args:
            base_url:
            timeout:
        """
        self.base_url = base_url
        self.timeout = timeout

    def make_get(self, resource: str, timeout="0"):
        """
        Make get requests
        Args:
            resource: specific resource
            timeout:

        Returns: a json response or an error

        """
        try:
            if timeout == "0":
                timeout = self.timeout

            response = requests.get(f"{self.base_url}/{resource}", timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            logging.error(errh)
        except requests.exceptions.ConnectionError as errc:
            logging.error(errc)
        except requests.exceptions.Timeout as errt:
            logging.error(errt)
        except requests.exceptions.RequestException as err:
            logging.error(err)
