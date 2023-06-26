import os
import pandas as pd
import time

from mindsdb.integrations.libs.api_handler import APIHandler
from mindsdb.integrations.libs.response import (
    HandlerStatusResponse as Response)
from mindsdb.integrations.utilities.date_utils import interval_str_to_duration_ms, utc_date_str_to_timestamp_ms
from mindsdb.integrations.utilities.sql_utils import extract_comparison_conditions
from mindsdb_sql.parser import ast

from typing import Dict, List, Any

from mindsdb.integrations.libs.coinglass.coinglass import Coinglass

class CoinglassDataTable(APIHandler):

    # Default 1m intervals in aggregate data
    DEFAULT_AGGREGATE_INTERVAL = '1m'
    DEFAULT_AGGREGATE_TARDE_LIMIT = 1000
    