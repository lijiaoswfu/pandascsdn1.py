import pandas as pd

pd.options.display.max_columns = 999  # 显示最大999列
orders = pd.read_excel('C:/Temp/Orders.xlsx')

print(orders.Date.dtype)