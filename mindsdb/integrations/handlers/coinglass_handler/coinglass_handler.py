import pandas as pd
from typing import Dict
import os

from mindsdb.integrations.libs.api_handler import APIHandler
# from mindsdb.integrations.handlers.coinglass_handler.coinglass_tables import CoinglassDataTable
from mindsdb.integrations.libs.response import (
    HandlerStatusResponse as StatusResponse,
    HandlerResponse as Response
    )
api_key = os.environ.get("API_KEY") 
# print(api_key)

BASE_COINGLASS_URL = 'https://open-api.coinglass.com/'
# print(BASE_COINGLASS_URL)
class CoinglassHandler(APIHandler):
    """
    A class for handling connections and calls to the Coinglass API

    Attributes:
    client ()
    """
    def __init__(self, name: str = None, **kwargs):
            """
            Register API tables and prepare handler for an API connection
            """
            super().__init__(name)
            self.api_key = None

            args = kwargs.get('connection_args', {})
            if 'api_key' in args:
                self.api_key = args['api_key']

            self.client = None
            self.is_connected = False

            return 

    def connect(self):
        """
        Creates a new Coinglass client if needed and sets Coinglass as the client to use for requests.

        Returns newly created or existing Coinglass client
        """
        if self.is_connected is True and self.client:
            return self.client
        
        if self.api_key:
            self.client = api_key, BASE_COINGLASS_URL
            self.is_connected = True
            return self.client
        else:
             self.client = BASE_COINGLASS_URL

        self.is_connected = True
        return self.client
    

    def check_connection(self) -> StatusResponse:
        """
        Checks the connection to Coinglass API by sending a ping request to the API.
        Returns a StatusResponse object indicating the success of the connection from mindsdb to the Coinglass Handler.
        """
         
        response = StatusResponse(False)
         
        try:
            client = self.connect()
            client.ping()
            response.success = True

        except Exception as e:
            response.message = str(e)
            response.success = False
        
        return response

    # def connect(url: str = None, headers: str = None, response: str = None):
    #     """
    #     Connects to Coinglass using an API Key
    #     param url: url provided by Coinglass
    #     param headers: headers provided by Coinglass
    #     param response: response provided by Coinglass
    #     return: Server response
    #     """
    #     if self.is_connected is True and self.client:
    #         return self.client
        
    #     if self.api_key:
    #         self.client = self.api_key
    #         self.is_connected = True
    #         return self.client
            
    #     else:
    #         self.is_connected = False
    #         return self.client


    # def check_connection(self) -> StatusResponse:
    #     """
    #     Checks if the connection to the Coinglass API is working.
    #     """
    #     response = StatusResponse(False)

    #     try:
    #         api_key = self.connect()

    #         # raise error if authentication fails
    #         api_key.get_user(id=1)
    #         response.success = True

    #     except Exception as e:
    #         response.message = f'Error connecting to Coinglass: {e}'
    #         print(response.message)
        

    #     if self.is_connected is False:
    #         return StatusResponse(status=False, message='Not connected to Coinglass')

    #     else:
    #         return StatusResponse(status=True, message='Connected to Coinglass')


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