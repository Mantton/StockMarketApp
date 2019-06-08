# Back End Stock Analysis Environemnt

from yahoo_fin.stock_info import *


value = get_live_price('FLWS')

price = round(value,2)

data = get_data('AAPL', start_date='06/01/2019')

print(price)
print(data)
