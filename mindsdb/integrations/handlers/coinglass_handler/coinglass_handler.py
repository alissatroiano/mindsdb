import pandas as pd
from typing import Dict
import os
from mindsdb.integrations.libs.api_handler import APIHandler
from mindsdb.integrations.libs.response import (
    HandlerStatusResponse as StatusResponse,
    HandlerResponse as Response,
)
api_key = os.environ.get("API_KEY") 


class CoinglassHandler(APIHandler):
    """
    A class for handling connections and calls to the Coinglass API

    Attributes:
    client ()
    """
    def __init__(self, name: str):
        super().__init__(name)
        """ constructor
        Args:
            name(str): the handler's name
        """
        self._tables = {}


    def register_table(self, table_name: str, table_class: Any):
        """
        Register coinglass data table(s) here (example, 'coins');
        """
        self._tables[table_name] = table_class
        

    def connect(self):
        """
        Sends a GET request to the Coinglass API to get the list of coins and their data.
        """
        if self.is_connected is True and self.client:
            return self.client
        
        if self.api_key:
            self.client = self.api_key
            self.is_connected = True
            return self.client
            
        else:
            self.is_connected = False
            return self.client


    def check_connection(self) -> StatusResponse:
        """
        Checks if the connection to the Coinglass API is working.
        """
        if self.is_connected is False:
            return StatusResponse(status=False, message='Not connected to Coinglass')

        else:
            return StatusResponse(status=True, message='Connected to Coinglass')


    # def get_future_coins_market(url, headers, response, print):
    #     """
    #     Uses request parameters from Coinglass API docs to (url, headers, response and, print) to fetch future coins market data
    #     """
    #     url = 'https://open-api.coinglass.com/public/v2/futures_coins_markets'
    #     headers = {
    #         "accept": "application/json",
    #         "content-type": "application/json"}
    #     response = requests.get(url, headers=headers)

    #     print(response.text)
    #     return response.text