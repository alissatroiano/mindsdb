import pandas as pd
from typing import Dict
# import env.py
import os
from env import api_key, api_secret
print(api_key)

# from mindsdb.integrations.libs.api_handler import APIHandler
# from mindsdb.integrations.libs.response import HandlerStatusResponse 


# class CoinglassHandler(APIHandler):
#     """
#     A class for handling connections and calls to the Coinglass API
#     """
#     def __init__(self, name: str):
#         super().__init__(name)
#         """ constructor
#         Args:
#             name(str): the handler's name
#         """
#         self._tables = {}


#     def register_table(self, table_name: str, table_class: Any):
#         """
#         Register coinglass data table(s) here (example, 'coins');
#         """
#         self._tables[table_name] = table_class


#     def connect(self) -> HandlerStatusResponse:
#         """
#         Creates a new Coinglass client if needed and sets Coinglass as the client to use for requests.

#         Returns newly created or existing Coinglass client
#         """
#         if self.is_connected():
#             return HandlerStatusResponse(status=False, message='Already connected to Coinglass')
        
#         if self.api_key and self.api_secret:

