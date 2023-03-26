# The S&P500 is one of the most popular indexes for tracking the market. One of the most important characteritics of the fund 
# is that it is market cap weighted. This means larger companys get a larger weight. This project builds an alternative version 
# where all companies are weighted equally.

import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

stocks = pd.read_csv('sp500_stocks.csv')

from secrets_1 import IEX_CLOUD_API_TOKEN

symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
print(data)