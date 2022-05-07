import xlwings as xw
import pandas as pd


wb = xw.Book()
sht = wb.sheets['Sheet1']
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
sht.range('A1').color = (34,139,34)
sht.range('A6').formula='=SUM(B2:B3)'
sht.range('A1').value = df
sht.range('A1').options(pd.DataFrame, expand='table').value

