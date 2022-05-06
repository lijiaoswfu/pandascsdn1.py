import xlwings as xw
import matplotlib.pyplot as plt

wb = xw.Book('QM.xlsx')
sht = wb.sheets['Sheet1']
sht.range('A12').value = 'Foo 1'
sht.range('A1').value