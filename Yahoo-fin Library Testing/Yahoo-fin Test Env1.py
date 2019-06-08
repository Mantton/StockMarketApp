# Back End Stock Analysis Environemnt

from yahoo_fin.stock_info import *


value = get_live_price('AAPL')

price = round(value,2)

print(price)
